"""Exact binary monotone task CE checks and zero-payoff construction."""
from fractions import Fraction as F
from itertools import combinations


def subsets(n):
    return [frozenset(i for i in range(n) if mask >> i & 1)
            for mask in range(1 << n)]


def wins(active, minimal):
    return any(t <= active for t in minimal)


def payoff(active, i, minimal, costs, benefit):
    return benefit*int(wins(active, minimal))-costs[i]*int(i in active)


def obedience_margins(law, minimal, costs, benefit):
    out = {}
    for i in range(len(costs)):
        for recommendation in (0, 1):
            value = F(0)
            for active, prob in law.items():
                if int(i in active) != recommendation:
                    continue
                other = active ^ frozenset({i})
                value += prob*(payoff(active, i, minimal, costs, benefit)
                               - payoff(other, i, minimal, costs, benefit))
            out[i, recommendation] = value
    return out


def utility(law, i, minimal, costs, benefit):
    return sum(p*payoff(a, i, minimal, costs, benefit) for a, p in law.items())


def purify(law, minimal):
    result = {}
    for active, prob in law.items():
        target = next((t for t in minimal if t <= active), frozenset())
        result[target] = result.get(target, F(0))+prob
    return result


def zero_payoff_witness(minimal, costs, benefit, i):
    """Return exact CE with utility_i=0, or None by the proved criterion."""
    singleton = {next(iter(t)) for t in minimal if len(t) == 1}
    if not singleton:
        return {frozenset(): F(1)}
    if i in singleton:
        return None
    containing = [t for t in minimal if i in t]
    if not containing:
        return None
    t = 1-min(costs[j] for j in singleton)/benefit
    if t > costs[i]/benefit:
        return None
    r = (benefit-costs[i])*t/costs[i]
    partners = {next(iter(a-{i})) for a in containing if len(a) == 2}
    capacity = {j: (1-benefit*r/costs[j])/t for j in partners}
    if any(c < 0 for c in capacity.values()):
        return None
    large = next((a for a in containing if len(a) >= 3), None)
    if large is not None:
        mixture = {large: F(1)}
    else:
        left = F(1)
        mixture = {}
        for j in sorted(partners):
            weight = min(left, capacity[j])
            mixture[frozenset({i, j})] = weight
            left -= weight
        if left:
            return None
    result = {a: t*p for a, p in mixture.items() if p}
    result[frozenset({i})] = r
    result[frozenset()] = 1-t-r
    return {a: p for a, p in result.items() if p}


def antichains(n):
    """Enumerate minimal winning lists: 166 nonconstant nonempty n4 tasks."""
    choices = subsets(n)[1:]
    result = []
    def visit(start, selected):
        if selected:
            result.append(tuple(selected))
        for j in range(start, len(choices)):
            candidate = choices[j]
            if all(not (candidate <= t or t <= candidate) for t in selected):
                visit(j+1, selected+[candidate])
    visit(0, [])
    return result
