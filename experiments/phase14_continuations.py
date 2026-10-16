"""Exact protected CE normal forms and type-blind payoff envelopes."""
from fractions import Fraction as F
from experiments.phase13_coalitions import wins, payoff


def anchored_thinning(law, minimal, protected):
    protected = frozenset(protected)
    result = {}
    for active, prob in law.items():
        reduced = set(active)
        if not wins(active, minimal):
            reduced.intersection_update(protected)
        else:
            for j in sorted(active-protected):
                candidate = frozenset(reduced-{j})
                if wins(candidate, minimal):
                    reduced.remove(j)
        target = frozenset(reduced)
        result[target] = result.get(target, F(0))+prob
    return result


def conditional_margin_slacks(law, minimal, costs, benefit, delta=F(0)):
    result = {}
    for i, cost in enumerate(costs):
        for rec in (0, 1):
            result[i, rec] = sum(prob*(payoff(a, i, minimal, costs, benefit)
                - payoff(a ^ frozenset({i}), i, minimal, costs, benefit)-delta)
                for a, prob in law.items() if int(i in a) == rec)
    return result


def blind_endpoint_slacks(law, minimal, lower, upper, benefit, delta=F(0)):
    # Equivalently check work at the maximum type and abstention at minimum.
    high = conditional_margin_slacks(law, minimal, upper, benefit, delta)
    low = conditional_margin_slacks(law, minimal, lower, benefit, delta)
    return {(i, rec): (high[i, rec] if rec else low[i, rec])
            for i in range(len(lower)) for rec in (0, 1)}


def blind_frontier(minimal, lower, upper, benefit, target, coalition, delta=F(0)):
    singleton = {next(iter(t)) for t in minimal if len(t) == 1}
    assert singleton and target not in singleton and target in coalition
    assert coalition in minimal
    assert delta <= min(lower)
    assert delta <= min(benefit-upper[j] for j in coalition)
    assert not any(wins(frozenset({target, j}), minimal)
                   for j in range(len(lower)) if j not in singleton | {target})
    success = 1-min(lower[j]-delta for j in singleton)/benefit
    work = min(F(1), benefit*success/(upper[target]+delta))
    law = {frozenset(coalition): success,
           frozenset({target}): work-success,
           frozenset(): 1-work}
    return {a: p for a, p in law.items() if p}, success, work


def frontier_payoff(success, work, cost, benefit):
    return benefit*success-cost*work


def bayesian_margin_slacks(kernel, prior, minimal, benefit):
    """Cost-dependent recommendation kernels, conditioning only on own type.

    kernel maps complete cost tuples to laws; prior explicitly supplies masses.
    The mediator can know costs; each agent sees only its own cost/action.
    """
    result = {}
    for costs, weight in prior.items():
        for active, prob in kernel[costs].items():
            for i, cost in enumerate(costs):
                rec = int(i in active)
                key = (i, cost, rec)
                margin = payoff(active, i, minimal, costs, benefit)-payoff(
                    active ^ frozenset({i}), i, minimal, costs, benefit)
                result[key] = result.get(key, F(0))+weight*prob*margin
    return result


def canonical_region_lp(minimal, costs, benefit, protected, delta=F(0)):
    """Construct the exact rational extended formulation, without solving it.

    Rows use >=0 convention; add sum(probabilities)=1 and nonnegativity.
    """
    from experiments.phase13_coalitions import subsets
    protected = frozenset(protected)
    protected_list = sorted(protected)
    protected_parts = [frozenset(protected_list[j] for j in part)
                       for part in subsets(len(protected))]
    columns = set(c for c in protected_parts if not wins(c, minimal))
    for t in minimal:
        for c in protected_parts:
            a = t | c
            if all(not wins(a-{j}, minimal) for j in a-protected):
                columns.add(a)
    columns = sorted(columns, key=lambda a: (len(a), sorted(a)))
    rows = {}
    for i, cost in enumerate(costs):
        for rec in (0, 1):
            rows[i, rec] = tuple((payoff(a, i, minimal, costs, benefit)
                - payoff(a ^ frozenset({i}), i, minimal, costs, benefit)-delta)
                if int(i in a) == rec else F(0) for a in columns)
    return {'columns': tuple(columns), 'obedience_rows': rows,
            'normalization': (F(1),)*len(columns),
            'success': tuple(F(int(wins(a, minimal))) for a in columns),
            'protected_payoffs': {i: tuple(payoff(a, i, minimal, costs, benefit)
                                           for a in columns) for i in protected}}
