"""Exact finite checks for Phase 12 compact representation barriers.

Enumeration here validates reductions, not an asymptotic equilibrium solver.
"""
from fractions import Fraction as Q
from itertools import product


def bits(n):
    return product((0, 1), repeat=n)


def rotate(z):
    """One cyclic pair rotation; z lists A players followed by B players."""
    n = len(z) // 2
    a, b = z[:n], z[n:]
    return tuple(a[-1:] + a[:-1] + b[-1:] + b[:-1])


def quarter_turn(z):
    n = len(z) // 2
    a, b = z[:n], z[n:]
    return tuple(1 - v for v in b) + tuple(a)


def sym_value(z, truth):
    """Average Boolean F over C_n x C_4; truth is its explicit test table."""
    n = len(z) // 2
    total = 0
    current = tuple(z)
    for _ in range(n):
        t = current
        for _ in range(4):
            total += truth[t[:n]]
            t = quarter_turn(t)
        current = rotate(current)
    return Q(total, 4 * n)


def payoff(s, truth, threshold):
    n = (len(s) - 1) // 2
    z, decision = tuple(s[:-1]), s[-1]
    return (tuple(Q(z[j] == z[n+j]) for j in range(n))
            + tuple(Q(z[j] != z[n+j]) for j in range(n))
            + (sym_value(z, truth) if decision else threshold,))


def independent_expectation(function, probabilities):
    ans = Q(0)
    for z in bits(len(probabilities)):
        mass = Q(1)
        for b, p in zip(z, probabilities):
            mass *= p if b else 1-p
        ans += mass * function(z)
    return ans


def mp_regrets(p, q):
    x, y = 2*p-1, 2*q-1
    return (abs(y)-x*y)/2, (abs(x)+x*y)/2


def epsilon_for_counting(n):
    return Q(1, (2 ** (n+1)) * (8*n+8))


def action_orbits(n):
    """Explicit generator traversal on all player-action pairs."""
    universe = {(i, a) for i in range(2*n+1) for a in (0, 1)}
    result = []
    def r(pair):
        i, a = pair
        return ((i+1) % n if i<n else n+(i-n+1) % n, a) if i<2*n else pair
    def t(pair):
        i, a = pair
        return (n+i, a) if i<n else (i-n, 1-a) if i<2*n else pair
    while universe:
        start = min(universe)
        orbit, todo = {start}, [start]
        while todo:
            for nxt in (r(todo[-1]), t(todo[-1])):
                if nxt not in orbit:
                    orbit.add(nxt)
                    todo.append(nxt)
                    break
            else:
                todo.pop()
        universe -= orbit
        result.append(orbit)
    return result


def check_decomposable(node):
    """Return player scope, rejecting overlap at products; tiny tree grammar."""
    tag, *data = node
    if tag == 'const':
        return frozenset()
    if tag == 'leaf':
        return frozenset((data[0],))
    children = data[0]
    scopes = [check_decomposable(c) for c in children]
    if tag == 'product':
        seen = set()
        for scope in scopes:
            if not scope:
                raise ValueError('constant products require explicit folding')
            if seen.intersection(scope):
                raise ValueError('product scopes overlap')
            seen.update(scope)
    elif tag != 'sum':
        raise ValueError('unknown tag')
    return frozenset().union(*scopes)


def sum_product(node, probabilities, evidence=None):
    """Expected payoff by leaf substitution, only after decomposability check."""
    check_decomposable(node)
    evidence = {} if evidence is None else evidence
    def rec(v):
        tag, *data = v
        if tag == 'const':
            return Q(data[0])
        if tag == 'leaf':
            i, values = data
            if i in evidence:
                return Q(values[evidence[i]])
            p = probabilities[i]
            return (1-p)*values[0] + p*values[1]
        values = [rec(c) for c in data[0]]
        if tag == 'sum':
            return sum(values, Q(0))
        ans = Q(1)
        for x in values:
            ans *= x
        return ans
    return rec(node)
