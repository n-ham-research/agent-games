"""Exact selective-audit constructions; no external solver or float arithmetic."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb


def profiles(priors):
    for types in product(*(tuple(p) for p in priors)):
        weight = F(1)
        for p, c in zip(priors, types):
            weight *= p[c]
        yield types, weight


def efficient_rule(types, k=1):
    coalitions = list(combinations(range(len(types)), k))
    best = min(sum(types[i] for i in s) for s in coalitions)
    winners = [s for s in coalitions if sum(types[i] for i in s) == best]
    return {s: F(1, len(winners)) for s in winners}


def interim(priors, rule):
    result = [{c: F(0) for c in p} for p in priors]
    for types, weight in profiles(priors):
        for selected, probability in rule(types).items():
            for i in selected:
                result[i][types[i]] += weight * probability / priors[i][types[i]]
    return result


def audit_rates(priors, rule, benefit, k=1):
    x = interim(priors, rule)
    rates = []
    for i, values in enumerate(x):
        if k == 1:
            required = {c: max(values.values()) - v for c, v in values.items()}
        else:
            required = {d: max(c / benefit * (v - values[d])
                               for c, v in values.items()) for d in values}
        rates.append({c: required[c] / (1-v) if v != 1 else F(0)
                      for c, v in values.items()})
    return x, rates


def expected_audits(priors, rule, rates):
    return sum(weight * probability * sum(rates[i][types[i]]
               for i in range(len(types)) if i not in selected)
               for types, weight in profiles(priors)
               for selected, probability in rule(types).items())


def deviating_utility(priors, rule, benefit, rates, agent, true_cost, report, k=1):
    """Best final action after each constructed continuation, others obedient.

    On-path all selected workers are pivotal. A detected liar is sole worker
    for k=1, or faces shutdown with no unilateral recovery for k>=2.
    """
    total = F(0)
    for types, weight in profiles(priors):
        if types[agent] != true_cost:
            continue
        conditional = weight / priors[agent][true_cost]
        reports = list(types)
        reports[agent] = report
        for selected, probability in rule(tuple(reports)).items():
            if agent in selected:
                utility = max(benefit - true_cost, F(0))
            else:
                audit = rates[agent][report] if report != true_cost else F(0)
                punished = max(benefit - true_cost, F(0)) if k == 1 else F(0)
                utility = (1-audit)*benefit + audit*punished
            total += conditional * probability * utility
    return total


def iid_frontier(n, k, p, low, benefit):
    mean_low_workers = sum(min(j, k)*F(comb(n, j))*p**j*(1-p)**(n-j)
                           for j in range(n+1))
    if k == 1:
        return mean_low_workers/p - 1
    return low/benefit*(mean_low_workers-k*p)/p


def success_interim(priors, rule):
    s = [{c: F(0) for c in p} for p in priors]
    for types, weight in profiles(priors):
        success = sum(prob for selected, prob in rule(types).items() if selected)
        for i, c in enumerate(types):
            s[i][c] += weight * success / priors[i][c]
    return s


def reliability_audits(priors, rule, benefit):
    """Closed-form optimum for minimal-coalition-or-failure targets.

    Return interim success/work and (unselected, selected) audit probabilities
    conditional on each reported type. No singleton may complete the task.
    """
    s, x = success_interim(priors, rule), interim(priors, rule)
    audit = []
    for i, prior in enumerate(priors):
        row = {}
        for d in prior:
            capacity_u = s[i][d] - x[i][d]
            gain = {c: benefit*(s[i][d]-s[i][c])
                       + c*(x[i][c]-x[i][d]) for c in prior}
            required_u = max(gain.values()) / benefit
            if required_u <= capacity_u:
                alpha, beta = required_u, F(0)
            else:
                alpha = capacity_u
                beta = max(F(0), max((g-benefit*alpha)/(benefit-c)
                                    for c, g in gain.items()))
            assert 0 <= alpha <= capacity_u
            assert 0 <= beta <= x[i][d]
            row[d] = (alpha, beta)
        audit.append(row)
    return s, x, audit


def reliability_deviation(priors, rule, benefit, s, x, audit,
                          agent, true_cost, report):
    total = F(0)
    for types, weight in profiles(priors):
        if types[agent] != true_cost:
            continue
        reports = list(types)
        reports[agent] = report
        alpha, beta = audit[agent][report]
        unselected_capacity = s[agent][report] - x[agent][report]
        unselected_rate = alpha/unselected_capacity if unselected_capacity else 0
        selected_rate = beta/x[agent][report] if x[agent][report] else 0
        for selected, probability in rule(tuple(reports)).items():
            if not selected:
                value = F(0)
            else:
                baseline = benefit - true_cost if agent in selected else benefit
                rate = selected_rate if agent in selected else unselected_rate
                value = baseline if report == true_cost else baseline*(1-rate)
            total += weight/priors[agent][true_cost]*probability*value
    return total
