"""Exact read-once formula value/sensitivity lift, not an LP solver."""
from fractions import Fraction as F
from itertools import product

STATES = tuple(product((0, 1), repeat=2))


def nodes(formula):
    if isinstance(formula, int):
        return (formula,)
    return nodes(formula[1])+nodes(formula[2])


def evaluate(formula, active):
    if isinstance(formula, int):
        return int(formula in active)
    op, left, right = formula
    a, b = evaluate(left, active), evaluate(right, active)
    return (a & b) if op == 'and' else (a | b)


def allowed(op, parent, left, right):
    v, p = parent
    a, q = left
    b, r = right
    if op == 'and':
        return v == (a & b) and q == p*b and r == p*a
    if op == 'or':
        return v == (a | b) and q == p*(1-b) and r == p*(1-a)
    raise ValueError('unknown gate')


def lift(formula, active):
    """Maps tree addresses to (value, root-sensitivity)."""
    result = {}
    def visit(tree, address, sensitivity):
        value = evaluate(tree, active)
        result[address] = value, sensitivity
        if isinstance(tree, int):
            return
        op, left, right = tree
        a, b = evaluate(left, active), evaluate(right, active)
        visit(left, address+(0,), sensitivity*(b if op == 'and' else 1-b))
        visit(right, address+(1,), sensitivity*(a if op == 'and' else 1-a))
    visit(formula, (), 1)
    return result


def gate_tables(formula):
    result = {}
    def visit(tree, address):
        if isinstance(tree, int):
            return
        result[address] = tuple(t for t in product(STATES, repeat=3)
                                if allowed(tree[0], *t))
        visit(tree[1], address+(0,))
        visit(tree[2], address+(1,))
    visit(formula, ())
    return result


def marginals(formula, law):
    unary, gates = {}, {}
    for active, mass in law.items():
        lifted = lift(formula, active)
        for address, state in lifted.items():
            key = address, state
            unary[key] = unary.get(key, F(0))+mass
        for address in gate_tables(formula):
            triple = lifted[address], lifted[address+(0,)], lifted[address+(1,)]
            key = address, triple
            gates[key] = gates.get(key, F(0))+mass
    return unary, gates


def reconstruct(formula, unary, gates):
    """Exact junction-tree conditional product from consistent local tables.

    Exponential listing is a finite verification helper; the theorem uses a
    polynomial-size sampler or sparse support extraction, not this enumeration.
    """
    def descend(tree, address, state):
        if isinstance(tree, int):
            return [(frozenset({tree}) if state[0] else frozenset(), F(1))]
        denom = unary.get((address, state), F(0))
        if not denom:
            return []
        result = []
        for triple in gate_tables(tree)[()]:
            if triple[0] != state:
                continue
            mass = gates.get((address, triple), F(0))/denom
            if not mass:
                continue
            for a, pa in descend(tree[1], address+(0,), triple[1]):
                for b, pb in descend(tree[2], address+(1,), triple[2]):
                    result.append((a|b, mass*pa*pb))
        return result
    result = {}
    for state in STATES:
        mass = unary.get(((), state), F(0))
        if not mass:
            continue
        for active, prob in descend(formula, (), state):
            result[active] = result.get(active, F(0))+mass*prob
    return result


def sparse_reconstruct(formula, unary, gates):
    """Greedy exact support extraction, polynomial in the local table encoding."""
    u, g = dict(unary), dict(gates)
    result = {}
    while sum(value for (address, _), value in u.items() if address == ()):
        root = next(state for (address, state), value in u.items() if address == () and value > 0)
        chosen_u, chosen_g, active = [], [], set()
        def descend(tree, address, state):
            chosen_u.append((address, state))
            if isinstance(tree, int):
                if state[0]: active.add(tree)
                return
            triple = next(triple for (place, triple), value in g.items()
                          if place == address and triple[0] == state and value > 0)
            chosen_g.append((address, triple))
            descend(tree[1], address+(0,), triple[1])
            descend(tree[2], address+(1,), triple[2])
        descend(formula, (), root)
        mass = min([u[key] for key in chosen_u]+[g[key] for key in chosen_g])
        for key in chosen_u: u[key] -= mass
        for key in chosen_g: g[key] -= mass
        a = frozenset(active)
        result[a] = result.get(a, F(0))+mass
    if any(u.values()) or any(g.values()):
        raise ValueError('inconsistent local marginals')
    return result
