"""Exact finite checks for P15-I1--I3; no rank optimization is attempted."""
from fractions import Fraction as F
from collections import defaultdict


def compose(q, d):
    return tuple(tuple(sum(qr[k]*d[k][j] for k in range(len(d)))
                       for j in range(len(d[0]))) for qr in q)


def row_partition(channel):
    cells = defaultdict(list)
    for i, row in enumerate(channel):
        cells[tuple(row)].append(i)
    return tuple(tuple(cell) for cell in cells.values())


def margins(joint, costs, release, minimal, benefit=F(1)):
    """Group by own cost, own literal action and public message.

    joint[(state, frozenset workers)] includes the state prior.
    release[(state, workers)] is a probability dictionary over public messages.
    """
    sums, masses = defaultdict(F), defaultdict(F)
    def wins(a):
        return any(m <= a for m in minimal)
    for (state, a), p in joint.items():
        for y, likelihood in release[(state, a)].items():
            for i, c in enumerate(costs[state]):
                if i in a:
                    advantage = benefit*(int(wins(a))-int(wins(a-{i})))-c
                else:
                    advantage = c-benefit*(int(wins(a|{i}))-int(wins(a)))
                key = (i, c, i in a, y)
                masses[key] += p*likelihood
                sums[key] += p*likelihood*advantage
    return {key: sums[key]/mass for key, mass in masses.items() if mass}


def odds_interval(p, ratio):
    return p/(p+ratio*(1-p)), ratio*p/(1-p+ratio*p)


def worst_margins(c, delta, ratio, benefit=F(1)):
    work, _ = odds_interval((c+delta)/benefit, ratio)
    _, repair = odds_interval((c-delta)/benefit, ratio)
    return benefit*work-c, c-benefit*repair


def safe_ratios(c, delta, benefit=F(1)):
    return ((c+delta)*(benefit-c)/(c*(benefit-c-delta)),
            c*(benefit-c+delta)/((benefit-c)*(c-delta)))


def rr_posterior(p, ratio, favorable=False):
    """One output of randomized response, with both outputs ratio-bounded."""
    event = ratio/(1+ratio) if favorable else 1/(1+ratio)
    other = 1-event
    return p*event/(p*event+(1-p)*other)
