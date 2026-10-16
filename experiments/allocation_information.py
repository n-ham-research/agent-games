"""Exact finite allocation witnesses; no floating point or inference of novelty."""
from fractions import Fraction as F
from itertools import permutations


def dot(a, b):
    return sum((F(x) * F(y) for x, y in zip(a, b)), F(0))


def rank(rows):
    a = [list(map(F, row)) for row in rows]
    if not a:
        return 0
    pivot = 0
    for col in range(len(a[0])):
        j = next((j for j in range(pivot, len(a)) if a[j][col]), None)
        if j is None:
            continue
        a[pivot], a[j] = a[j], a[pivot]
        q = a[pivot][col]
        a[pivot] = [x / q for x in a[pivot]]
        for j in range(len(a)):
            if j != pivot:
                q = a[j][col]
                a[j] = [x - q*y for x, y in zip(a[j], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def assignment_rows(n):
    return [tuple(int(j == p[i]) for i in range(n) for j in range(n))
            for p in permutations(range(n))]


def contrasts(rows):
    return [tuple(x-y for x, y in zip(row, rows[0])) for row in rows[1:]]


def row_swap_operator(n):
    return [tuple(int(i == 0 and k == j) - int(i == 1 and k == j)
                  for i in range(n) for k in range(n)) for j in range(n)]


def observations(operator, w):
    return tuple(dot(row, w) for row in operator)


def maximizers(rows, w):
    values = [dot(row, w) for row in rows]
    return {i for i, x in enumerate(values) if x == max(values)}


def is_task_sufficient(rows, operator):
    """Row-space criterion, equivalent on the unrestricted real domain."""
    return rank(operator + contrasts(rows)) == rank(operator)


def choose_noisy(scores, y):
    return max(range(len(scores)), key=lambda d: dot(scores[d], y))


def regret(scores, truth, selected):
    values = [dot(row, truth) for row in scores]
    return max(values) - values[selected]
