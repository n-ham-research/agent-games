"""Exact rational laws and formal prime-log information expressions."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb


def add_log(out, rational, coefficient):
    """Represent coefficient*log(rational) in the independent prime-log basis."""
    if not coefficient:
        return
    rational = F(rational)
    assert rational > 0
    for number, sign in ((rational.numerator, 1), (rational.denominator, -1)):
        divisor = 2
        while divisor*divisor <= number:
            while number % divisor == 0:
                out[divisor] += sign*coefficient
                number //= divisor
            divisor += 1
        if number > 1:
            out[number] += sign*coefficient


def clean(expression):
    return {p: c for p, c in expression.items() if c}


def information(joint, n):
    marginal = defaultdict(F)
    for (theta, a), prob in joint.items():
        marginal[a] += prob
    result = defaultdict(F)
    for (theta, a), prob in joint.items():
        if prob:
            add_log(result, prob/(F(1, n)*marginal[a]), prob)
    return clean(result)


def full_success_law(n, benefit, cost, delta, public_size=False):
    r = min(F(n), benefit/(cost+delta))
    k = r.numerator//r.denominator
    fraction = r-k
    sizes = {k: F(1)} if public_size or not fraction else {k: 1-fraction, k+1: fraction}
    joint = defaultdict(F)
    for theta in range(n):
        for size, mass in sizes.items():
            for rest in combinations([i for i in range(n) if i != theta], size-1):
                joint[theta, frozenset((theta,)+rest)] += mass/F(n*comb(n-1, size-1))
    return dict(joint), r


def low_success_law(n, tau, success):
    attempt = success/tau
    joint = defaultdict(F)
    for theta in range(n):
        joint[theta, frozenset()] += (1-attempt)/n
        for worker in range(n):
            q = tau if worker == theta else (1-tau)/(n-1)
            joint[theta, frozenset({worker})] += attempt*q/n
    return dict(joint)


def conditional_margins(joint, n, benefit, cost, public_size=False, public_set=False):
    masses, gains = defaultdict(F), defaultdict(F)
    for (theta, a), prob in joint.items():
        for i in range(n):
            label = a if public_set else len(a) if public_size else None
            key = (i, i in a, label)
            masses[key] += prob
            gain = benefit*int(theta == i)-cost if i in a else cost-benefit*int(theta == i)
            gains[key] += prob*gain
    return {key: gains[key]/mass for key, mass in masses.items() if mass}


def statistics(joint):
    return (sum(p for (theta, a), p in joint.items() if theta in a),
            sum(p*len(a) for (theta, a), p in joint.items()))


def full_formula(n, r, public_size=False):
    k = r.numerator//r.denominator
    fraction = F(0) if public_size else r-k
    out = defaultdict(F)
    add_log(out, n, F(1))
    add_log(out, k, -(1-fraction))
    if fraction:
        add_log(out, k+1, -fraction)
    return clean(out)


def low_formula(n, tau, success):
    out = defaultdict(F)
    add_log(out, tau*n, success)
    add_log(out, (1-tau)/(1-F(1,n)), success*(1-tau)/tau)
    return clean(out)
