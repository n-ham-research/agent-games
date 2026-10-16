"""Exact histogram coordinates and finite checks for compact task mechanisms.

This constructs coefficient data and exact finite examples, not a general LP
solver or an asymptotic complexity benchmark.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import factorial


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for first in range(n + 1):
            for tail in compositions(n - first, k - 1):
                yield (first,) + tail


def histograms(sizes, type_counts):
    return product(*(tuple(compositions(n, t)) for n, t in zip(sizes, type_counts)))


def histogram_probability(h, probabilities):
    ans = Q(1)
    for row, ps in zip(h, probabilities):
        n = sum(row)
        denom = 1
        for count in row:
            denom *= factorial(count)
        ans *= Q(factorial(n), denom)
        for count, p in zip(row, ps):
            ans *= p ** count
    return ans


def minimal_outcomes(h, success):
    """All cost-cell worker counts with inclusion-minimal successful role totals."""
    bounds = [range(c + 1) for row in h for c in row]
    widths = [len(row) for row in h]
    for flat in product(*bounds):
        offset, y = 0, []
        for width in widths:
            y.append(tuple(flat[offset:offset+width]))
            offset += width
        totals = tuple(map(sum, y))
        if not success(totals):
            continue
        if any(success(tuple(g - (r == j) for j, g in enumerate(totals)))
               for r, value in enumerate(totals) if value):
            continue
        yield tuple(y)


def compressed_interims(sizes, probabilities, masses):
    """masses[(h,y)] is JOINT mass P(H=h)*f_h(y); y=None denotes failure."""
    s = {(r,c): Q(0) for r, ps in enumerate(probabilities) for c in range(len(ps))}
    x = dict(s)
    reliability = Q(0)
    for (h,y), mass in masses.items():
        if y is None:
            continue
        reliability += mass
        for r, ps in enumerate(probabilities):
            for c, p in enumerate(ps):
                s[r,c] += mass * h[r][c] / (sizes[r]*p)
                x[r,c] += mass * y[r][c] / (sizes[r]*p)
    return s, x, reliability


def labeled_profiles(sizes, type_counts):
    labels = tuple(r for r, n in enumerate(sizes) for _ in range(n))
    return labels, product(*(range(type_counts[r]) for r in labels))


def profile_histogram(labels, types, type_counts):
    h = [[0]*t for t in type_counts]
    for r, c in zip(labels, types):
        h[r][c] += 1
    return tuple(map(tuple,h))


def uniform_lifts(labels, types, y):
    """Explicit small-instance uniform coalition lift, not production expansion."""
    if y is None:
        return {frozenset(): Q(1)}
    cells = []
    for r, row in enumerate(y):
        for c, number in enumerate(row):
            eligible = [i for i, pair in enumerate(zip(labels,types)) if pair == (r,c)]
            cells.append(tuple(combinations(eligible,number)))
    outcomes = [frozenset(i for cell in choice for i in cell) for choice in product(*cells)]
    return {coalition: Q(1,len(outcomes)) for coalition in outcomes}


def target_rule_mass(sizes, probabilities, success, chooser):
    result = {}
    ts = tuple(map(len,probabilities))
    for h in histograms(sizes,ts):
        ph = histogram_probability(h,probabilities)
        choices = tuple(minimal_outcomes(h,success))
        conditional = chooser(h,choices)
        if sum(conditional.values(),Q(0)) != 1:
            raise ValueError('not normalized')
        for y, p in conditional.items():
            if y is not None and y not in choices:
                raise ValueError('nonminimal/invalid outcome')
            result[h,y] = ph*p
    return result


def audit_capacity(B, costs, success, work, d):
    U,V = success[d]-work[d],work[d]
    gains = [B*(success[d]-success[c])+costs[c]*(work[c]-work[d])
             for c in range(len(costs))]
    T = max(Q(0),max(g/B for g in gains))
    if T <= U:
        return T,Q(0)
    return U,max(Q(0),max((g-B*U)/(B-c) for g,c in zip(gains,costs)))


def knapsack_expected_cover_cost(weights, quota):
    """Reduction instance: regular iid alpha/2; fallback1; mandatory gatealpha."""
    n = len(weights)
    alpha = Q(1,2**(n+1)*(n+1))
    total = Q(0)
    for low_bits in product((0,1),repeat=n):
        low = [i for i,b in enumerate(low_bits) if b]
        minimum_cardinality = None
        for size in range(len(low)+1):
            if any(sum(weights[i] for i in subset)>=quota for subset in combinations(low,size)):
                minimum_cardinality = size
                break
        cost = Q(1) if minimum_cardinality is None else alpha*minimum_cardinality
        total += alpha+cost
    return total / 2**n, alpha


def decode_failing_subsets(expected_cost, alpha, n):
    scaled = 2**n*(expected_cost-alpha)
    return scaled.numerator//scaled.denominator


def parity_probability(probabilities):
    bias = Q(1)
    for p in probabilities:
        bias *= 1-2*p
    return (1-bias)/2


def xor_width(n):
    # (1/25)^k gives parity bias at most 1/(48n).
    k, power = 1,25
    while power < 24*n:
        k += 1
        power *= 25
    return k


def cyclic_expectation(truth, p):
    n = len(next(iter(truth)))
    result = Q(0)
    for z, value in truth.items():
        k = sum(z)
        result += value * p**k * (1-p)**(n-k)
    return result


def cyclic_difference(truth, p, K):
    n = len(next(iter(truth)))
    alpha = Q(1,2*n)
    theta = Q(2*K+1,2**(n+1))
    return Q(1,2)-p+alpha*(cyclic_expectation(truth,p)-theta)


def cyclic_counting_payoff(profile, truth, K):
    N = len(profile)
    n = N-1
    alpha,theta = Q(1,2*n),Q(2*K+1,2**(n+1))
    answer=[]
    for i,action in enumerate(profile):
        others=tuple(profile[(i+j)%N] for j in range(1,N))
        D=Q(1,2)-Q(sum(others),n)+alpha*(truth[others]-theta)
        answer.append((1+D)/2 if action else Q(1,2))
    return tuple(answer)


def noisy_sign_bisection(advantage, players, epsilon, noise=None):
    """Deterministic bounded-error oracle check, NOT a stochastic implementation.

    The actual sampling theorem supplies errors <=epsilon/4 jointly with high
    probability. Here the exact function and chosen errors expose each bracket.
    """
    if players < 2 or not 0 < epsilon < 1:
        raise ValueError('players>=2 and epsilon in (0,1) required')
    if advantage(Q(0)) <= 0:
        return Q(0),[]
    if advantage(Q(1)) >= 0:
        return Q(1),[]
    T=0
    while (2**T)*epsilon < 4*(players-1):
        T+=1
    lo,hi=Q(0),Q(1)
    trace=[]
    for stage in range(T):
        mid=(lo+hi)/2
        exact=advantage(mid)
        error=Q(0) if noise is None else noise(stage,mid)
        if abs(error)>epsilon/4:
            raise ValueError('oracle error exceeds certified event')
        estimate=exact+error
        trace.append((lo,hi,mid,estimate,exact))
        if abs(estimate)<=epsilon/2:
            return mid,trace
        if estimate>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2,trace
