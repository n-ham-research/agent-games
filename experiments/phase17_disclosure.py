"""Exact channel manipulation and explicit LP export; no LP solver included."""
from fractions import Fraction as F
from collections import defaultdict


def guessing(columns):
    return sum(max(col) for col in columns if col)


def safe(columns, rows):
    return all(all(sum(a*x for a, x in zip(row, col)) >= 0 for row in rows)
               and all(x >= 0 for x in col) for col in columns)


def merge_by_guess(columns):
    grouped = {}
    for col in columns:
        g = max(range(len(col)), key=lambda i: col[i])
        grouped[g] = tuple(a+b for a, b in zip(grouped.get(g, (F(0),)*len(col)), col))
    return grouped


def limited_garble(columns, k):
    grouped = merge_by_guess(columns)
    kept = sorted(grouped, key=lambda g: grouped[g][g], reverse=True)[:k]
    assert kept
    out = {g: grouped[g] for g in kept}
    for g in grouped:
        if g not in out:
            first = kept[0]
            out[first] = tuple(a+b for a, b in zip(out[first], grouped[g]))
    return out


def guessing_lp(prior, rows, labels=None):
    """Return exact sparse LP rows as (coefficients, relation, rhs)."""
    n = len(prior)
    labels = tuple(range(n)) if labels is None else tuple(labels)
    variables = tuple((i, g) for i in range(n) for g in labels)
    constraints = []
    for i, p in enumerate(prior):
        constraints.append(({(i, g): F(1) for g in labels}, '=', p))
    for row in rows:
        for g in labels:
            constraints.append(({(i, g): row[i] for i in range(n)}, '>=', F(0)))
    objective = {(g, g): F(1) for g in labels}
    return variables, objective, constraints


def multirow_law():
    probabilities = ((4, 2, 3), (2, 4, 3), (3, 4, 2), (3, 2, 4))
    joint, costs = {}, {}
    for state, p in enumerate(probabilities):
        costs[state] = (F(1, 2),)*3
        joint[state, frozenset()] = F(1, 4)*F(4, 13)
        for i in range(3):
            joint[state, frozenset({i})] = F(1, 4)*F(p[i], 13)
    rows = ((-F(2, 65), F(2, 65), F(0), F(0)),
            (F(2, 65), -F(2, 65), -F(2, 65), F(2, 65)),
            (F(0), F(0), F(2, 65), -F(2, 65)))
    return joint, costs, rows


def factorized(table):
    """Finite nonnegative two-dimensional probability table has rank at most1."""
    return all(table[i][j]*table[k][l] == table[i][l]*table[k][j]
               for i in range(len(table)) for k in range(len(table))
               for j in range(len(table[0])) for l in range(len(table[0])))
