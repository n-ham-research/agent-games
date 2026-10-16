"""Exact same-coordinate incentive geometry; no LP optimizer."""
from fractions import Fraction as F
from itertools import product, combinations


def profiles(n):
    return tuple(product((0, 1), repeat=n))


def all_graphs(n):
    pairs = tuple(combinations(range(n), 2))
    for bits in range(1 << len(pairs)):
        yield frozenset(e for j, e in enumerate(pairs) if bits >> j & 1)


def adjacent_vertices(edges, i):
    return frozenset(v if u == i else u for u, v in edges if i in (u, v))


def independent(a, edges):
    return all(not (a[i] and a[j]) for i, j in edges)


def maximal_independent(a, edges):
    return independent(a, edges) and all(a[i] or any(a[j] for j in adjacent_vertices(edges, i))
                                        for i in range(len(a)))


def switched(a, i):
    return a[:i]+(1-a[i],)+a[i+1:]


def collision_utility(a, i, edges):
    degree_bound = max(1, max((len(adjacent_vertices(edges, j)) for j in range(len(a))), default=0))
    return 1-F(a[i]*sum(a[j] for j in adjacent_vertices(edges, i)), degree_bound)


def bestshot_utility(a, i, edges, cost=F(3, 4)):
    return F(int(a[i] or any(a[j] for j in adjacent_vertices(edges, i))))-cost*a[i]


def rows(law, edges, utility=collision_utility, delta=F(0)):
    n = len(next(iter(law)))
    return {(i, rec): sum(p*(utility(a, i, edges)-utility(switched(a, i), i, edges)-delta)
                         for a, p in law.items() if a[i] == rec)
            for i in range(n) for rec in (0, 1)}


def marginals(law):
    n = len(next(iter(law)))
    return tuple(sum(p*a[i] for a, p in law.items()) for i in range(n))


def independent_product_law(probabilities):
    result = {}
    for a in profiles(len(probabilities)):
        p = F(1)
        for bit, q in zip(a, probabilities):
            p *= q if bit else 1-q
        if p:
            result[a] = p
    return result


def complete_line_graph(vertices):
    workers = tuple(combinations(range(vertices), 2))
    conflicts = frozenset((i, j) for i, e in enumerate(workers)
                          for j in range(i+1, len(workers)) if set(e) & set(workers[j]))
    return workers, conflicts
