"""Exact small-instance checks for Phase 11 orbit reductions.

Enumerates finite profiles/group closures for tests, not a succinct-game solver.
The local polynomial compiler does not enumerate full joint profiles.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product


def profiles(sizes):
    return list(product(*(range(k) for k in sizes)))


# A typed map is (player permutation p, action maps alpha[i] at source i).
def apply(g, s):
    p, alpha = g
    out = [None] * len(p)
    for i, a in enumerate(s):
        out[p[i]] = alpha[i][a]
    return tuple(out)


def pointed(g, item):
    p, alpha = g
    i, *actions = item
    return (p[i], *(alpha[i][a] for a in actions))


def partition(items, generators, action):
    unseen = set(items)
    answer = []
    while unseen:
        seed = min(unseen)
        seen, todo = {seed}, [seed]
        while todo:
            item = todo.pop()
            for g in generators:
                other = action(g, item)
                if other not in seen:
                    seen.add(other)
                    todo.append(other)
        unseen.difference_update(seen)
        answer.append(tuple(sorted(seen)))
    return answer


def action_orbits(sizes, generators):
    return partition([(i, a) for i, k in enumerate(sizes) for a in range(k)],
                     generators, pointed)


def orbit_index(orbits):
    return {item: w for w, orbit in enumerate(orbits) for item in orbit}


def deviation_orbits(sizes, generators):
    return partition([(i, a, b) for i, k in enumerate(sizes)
                      for a in range(k) for b in range(k) if a != b],
                     generators, pointed)


def regret(payoff, s, deviation):
    i, a, b = deviation
    if s[i] != a:
        return Q(0)
    other = list(s)
    other[i] = b
    return Q(payoff(i, s)) - Q(payoff(i, tuple(other)))


def orbit_regret_matrix(sizes, generators, payoff):
    cols = partition(profiles(sizes), generators, apply)
    rows = deviation_orbits(sizes, generators)
    matrix = [[sum((regret(payoff, s, row[0]) for s in orbit), Q(0))
               / len(orbit) for orbit in cols] for row in rows]
    return rows, cols, matrix


def lift(cols, masses):
    return {s: Q(mass) / len(orbit)
            for orbit, mass in zip(cols, masses) for s in orbit}


def all_regrets(sizes, payoff, distribution):
    return {(i, a, b): sum((prob * regret(payoff, s, (i, a, b))
                            for s, prob in distribution.items()), Q(0))
            for i, k in enumerate(sizes) for a in range(k)
            for b in range(k) if a != b}


def compile_conditional(i, a, factors, sizes, index):
    """Return polynomial {sorted tuple of orbit indices: rational coefficient}.

    factors[i] is a list of (scope, table); scope must include i, and table
    maps scope-ordered pure-action tuples to rational payoffs.
    """
    poly = defaultdict(Q)
    for scope, table in factors[i]:
        if i not in scope or len(scope) != len(set(scope)):
            raise ValueError('Factor scope must contain the focal player once')
        others = [j for j in scope if j != i]
        for t in product(*(range(sizes[j]) for j in others)):
            assignment = dict(zip(others, t))
            assignment[i] = a
            coefficient = Q(table[tuple(assignment[j] for j in scope)])
            monomial = tuple(sorted(index[j, assignment[j]] for j in others))
            poly[monomial] += coefficient
    return {monomial: coefficient for monomial, coefficient in poly.items()
            if coefficient}


def evaluate(poly, x):
    total = Q(0)
    for monomial, coefficient in poly.items():
        term = coefficient
        for w in monomial:
            term *= x[w]
        total += term
    return total


def factor_payoff(factors, i, s):
    return sum((Q(table[tuple(s[j] for j in scope)])
                for scope, table in factors[i]), Q(0))


def direct_conditional(i, a, sizes, payoff, marginals):
    others = [j for j in range(len(sizes)) if j != i]
    value = Q(0)
    for t in product(*(range(sizes[j]) for j in others)):
        s, prob = [None] * len(sizes), Q(1)
        s[i] = a
        for j, b in zip(others, t):
            s[j] = b
            prob *= marginals[j][b]
        value += prob * payoff(i, tuple(s))
    return value


def cycle_instance(n):
    sizes = [2] * n
    rotation = (tuple((i + 1) % n for i in range(n)), ((0, 1),) * n)
    complement = (tuple(range(n)), ((1, 0),) * n)
    factors = {i: [((i, (i + 1) % n),
                    {(a, b): int(a == b) for a, b in product(range(2), repeat=2)})]
               for i in range(n)}
    return sizes, rotation, complement, factors
