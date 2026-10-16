"""Exact capped-coverage path encoding; constructs coefficients, not an LP solver."""
from fractions import Fraction as F
from itertools import product


def states(d):
    return tuple(product(range(3), repeat=d))


def step(state, covered, action):
    return tuple(min(2, x + int(action and e in covered))
                 for e, x in enumerate(state))


def path(sets, active, d):
    state = (0,)*d
    result = []
    for i, covered in enumerate(sets):
        action = int(i in active)
        nxt = step(state, covered, action)
        result.append((i, state, action, nxt))
        state = nxt
    return state, tuple(result)


def coefficients(final, covered, action, cost, benefit, delta=F(0)):
    """Utility and unconditional conditional-margin coefficient on an i-edge."""
    success = all(x > 0 for x in final)
    if action:
        pivotal = success and any(final[e] == 1 for e in covered)
        gain = benefit*int(pivotal)-cost
    else:
        repair = (not success and all(x > 0 or e in covered
                                    for e, x in enumerate(final)))
        gain = cost-benefit*int(repair)
    return benefit*int(success)-cost*action, gain-delta


def encode_law(sets, law, d):
    flows, mass = {}, {}
    for active, probability in law.items():
        final, edges = path(sets, active, d)
        mass[final] = mass.get(final, F(0))+probability
        for edge in edges:
            key = (final,)+edge
            flows[key] = flows.get(key, F(0))+probability
    return mass, flows


def evaluate_flow(sets, costs, benefit, mass, flows, delta=F(0)):
    utilities = [F(0)]*len(sets)
    rows = {(i, a): F(0) for i in range(len(sets)) for a in (0, 1)}
    success = sum(p for z, p in mass.items() if all(x > 0 for x in z))
    for (z, i, _state, a, _nxt), value in flows.items():
        utility, margin = coefficients(z, sets[i], a, costs[i], benefit, delta)
        utilities[i] += value*utility
        rows[i, a] += value*margin
    return success, tuple(utilities), rows


def decompose(sets, mass, flows, d):
    """Greedy exact acyclic-flow decomposition, rejecting residual invalid flow."""
    remaining = {edge: F(value) for edge, value in flows.items() if value}
    law = {}
    for final, amount in mass.items():
        left = F(amount)
        while left:
            state, selected, edges = (0,)*d, set(), []
            for i, covered in enumerate(sets):
                choices = [(final, i, state, a, step(state, covered, a))
                           for a in (0, 1)]
                key = next((key for key in choices if remaining.get(key, 0)>0), None)
                if key is None:
                    raise ValueError('flow lacks a source-to-terminal path')
                if key[3]:
                    selected.add(i)
                edges.append(key)
                state = key[4]
            if state != final:
                raise ValueError('wrong terminal')
            weight = min([left]+[remaining[key] for key in edges])
            active = frozenset(selected)
            law[active] = law.get(active, F(0))+weight
            for key in edges:
                remaining[key] -= weight
            left -= weight
    if any(remaining.values()):
        raise ValueError('residual flow')
    return law
