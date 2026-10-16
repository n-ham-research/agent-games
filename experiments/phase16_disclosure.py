"""Exact small-instance disclosure checks. Exhaustive partitions are not an algorithm claim."""
from fractions import Fraction as F
from experiments.phase15_information import margins


def partitions(values):
    if not values:
        yield ()
        return
    first, *rest = values
    for tail in partitions(rest):
        yield ((first,),) + tail
        for j in range(len(tail)):
            yield tail[:j] + ((first,)+tail[j],) + tail[j+1:]


def volunteer_law(v, prior=None):
    n = len(v)
    prior = tuple(prior) if prior else (F(1, n),)*n
    joint, costs = {}, {}
    for state, value in enumerate(v):
        f = (1-value)/4
        costs[state] = (F(1, 2), F(1, 2))
        joint[state, frozenset()] = prior[state]*f
        for i in (0, 1):
            joint[state, frozenset({i})] = prior[state]*(1-f)/2
    return joint, costs


def release_margins(v, channel, prior=None):
    joint, costs = volunteer_law(v, prior)
    release = {w: channel[w[0]] for w in joint}
    return margins(joint, costs, release,
                   (frozenset({0}), frozenset({1})))


def partition_channel(blocks):
    return {state: {j: F(1)} for j, block in enumerate(blocks) for state in block}


def best_balanced_partition(v):
    return max((p for p in partitions(list(range(len(v))))
                if all(sum(v[i] for i in block) >= 0 for block in p)), key=len)


def greedy_pair_channel(v, prior=None):
    """A feasible transport, not an optimizer for general edge weights."""
    n = len(v)
    prior = tuple(prior) if prior else (F(1, n),)*n
    supply = {i: prior[i]*x for i, x in enumerate(v) if x > 0}
    demand = {i: -prior[i]*x for i, x in enumerate(v) if x < 0}
    assert sum(supply.values()) == sum(demand.values())
    channel = {i: {} for i in range(n)}
    for p in supply:
        for q in demand:
            h = min(supply[p], demand[q])
            if h:
                label = (p, q)
                channel[p][label] = h/v[p]/prior[p]
                channel[q][label] = h/(-v[q])/prior[q]
                supply[p] -= h
                demand[q] -= h
    for i, x in enumerate(v):
        if not x:
            channel[i][('zero', i)] = F(1)
    return channel


def guessing(channel, prior):
    labels = {y for row in channel.values() for y in row}
    return sum(max(prior[i]*channel[i].get(y, 0) for i in channel) for y in labels)
