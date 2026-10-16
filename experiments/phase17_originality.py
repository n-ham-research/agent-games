"""Exact perfect-matching face checks; no optimizer or extension-complexity proof."""
from fractions import Fraction
from itertools import combinations


def graph_workers(vertices):
    return tuple(combinations(range(vertices), 2))


def covers(active, edges, vertices):
    touched = set()
    for i in active:
        touched.update(edges[i])
    return len(touched) == vertices


def perfect_matching(active, edges, vertices):
    degrees = [0]*vertices
    for i in active:
        for v in edges[i]:
            degrees[v] += 1
    return all(d == 1 for d in degrees)


def direct_gain(active, i, edges, vertices):
    """Benefit 1, common cost 1/2; own recommendation is membership."""
    changed = active ^ frozenset({i})
    obey = Fraction(int(covers(active, edges, vertices)))-Fraction(i in active, 2)
    deviate = Fraction(int(covers(changed, edges, vertices)))-Fraction(i in changed, 2)
    return obey-deviate


def law_coordinates(law, edges, vertices):
    s = sum(p*int(covers(a, edges, vertices)) for a, p in law.items())
    x = tuple(sum(p*int(i in a) for a, p in law.items()) for i in range(len(edges)))
    u = tuple(s-v/2 for v in x)
    return s, x, u


def all_subsets(n):
    for bits in range(1 << n):
        yield frozenset(i for i in range(n) if bits >> i & 1)


def read_twice_occurrences(vertices):
    """AND over vertex clauses; each clause ORs its incident edge variables."""
    edges = graph_workers(vertices)
    return tuple(tuple(i for i, edge in enumerate(edges) if v in edge)
                 for v in range(vertices))
