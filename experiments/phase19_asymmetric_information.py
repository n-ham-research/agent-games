"""Two-worker heterogeneous full-success laws; exact rational information."""
from collections import defaultdict
from fractions import Fraction as F
from experiments.phase18_endogenous_information import add_log, clean


def optimum(prior, tau1, tau2, public=False):
    """Masses (theta1,pair), (theta2,pair), prior and thresholds rational."""
    p, t1, t2 = map(F, (prior, tau1, tau2))
    assert 0 < p < 1 and 0 < t1 <= 1 and 0 < t2 <= 1
    if public and t1+t2 > 1:
        return F(0), F(0)
    return min(p, (1-p)*(1-t2)/t2), min(1-p, p*(1-t1)/t1)


def law(prior, a, b):
    p, a, b = map(F, (prior, a, b))
    assert 0 <= a <= p and 0 <= b <= 1-p
    return {(0, (0,)): p-a, (1, (1,)): 1-p-b,
            (0, (0, 1)): a, (1, (0, 1)): b}


def information(joint, prior):
    p = F(prior)
    marg = defaultdict(F)
    for (_, action), mass in joint.items():
        marg[action] += mass
    out = defaultdict(F)
    for (theta, action), mass in joint.items():
        if mass:
            add_log(out, mass/((p if theta == 0 else 1-p)*marg[action]), mass)
    return clean(out)


def entropy_formula(prior, a, b):
    p, a, b = map(F, (prior, a, b))
    out = defaultdict(F)
    add_log(out, p, -p)
    add_log(out, 1-p, -(1-p))
    if a:
        add_log(out, a/(a+b), a)
    if b:
        add_log(out, b/(a+b), b)
    return clean(out)


def margins(joint, costs, benefit=F(1), public=False):
    """Conditional obedience gains; public means size additionally disclosed."""
    masses, gains = defaultdict(F), defaultdict(F)
    for (theta, action), mass in joint.items():
        for i in (0, 1):
            work = i in action
            key = (i, work, len(action) if public else None)
            gain = benefit*(theta == i)-costs[i]
            masses[key] += mass
            gains[key] += mass*(gain if work else -gain)
    return {key: gains[key]/mass for key, mass in masses.items() if mass}
