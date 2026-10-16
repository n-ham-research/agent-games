"""Independent direct-payoff audit. No previous-phase code is imported."""
from fractions import Fraction
from itertools import product


def bit_profiles(n):
    return tuple(product((0, 1), repeat=n))


def succeeds(profile, weights, quota):
    return sum(a*w for a, w in zip(profile, weights)) >= quota


def utility(profile, weights, quota, costs, player):
    return Fraction(int(succeeds(profile, weights, quota)))-costs[player]*profile[player]


def switch(profile, player):
    result = list(profile)
    result[player] = 1-result[player]
    return tuple(result)


def all_obedience_rows(law, weights, quota, costs, delta=Fraction(0)):
    n = len(weights)
    return {(i, a): sum(prob*(utility(s, weights, quota, costs, i)
                      -utility(switch(s, i), weights, quota, costs, i)-delta)
                  for s, prob in law.items() if s[i] == a)
            for i in range(n) for a in (0, 1)}


def conditional_gains(law, weights, quota, costs):
    rows = all_obedience_rows(law, weights, quota, costs)
    return {(i, a): rows[i, a]/mass
            for i, a in rows
            if (mass := sum(p for s, p in law.items() if s[i] == a))}


def payoff_vector(law, weights, quota, costs):
    return tuple(sum(p*utility(s, weights, quota, costs, i) for s, p in law.items())
                 for i in range(len(weights)))


def preprocess(items, target):
    """Map unrestricted positive SUBSET SUM to 0<item<target, without solving it."""
    if target < 0 or any(a <= 0 for a in items):
        raise ValueError('positive items and nonnegative target required')
    yes, no = ((1, 1), 2), ((2, 2), 3)
    if target == 0 or target in items:
        return yes
    retained = tuple(a for a in items if a < target)
    if not retained or sum(retained) < target:
        return no
    return retained, target


def subset_solutions(items, target):
    return tuple(bits for bits in bit_profiles(len(items))
                 if sum(a*bit for a, bit in zip(items, bits)) == target)


def reduction(items, target, target_cost=Fraction(1, 2), backstop_cost=Fraction(1, 2)):
    if not items or not all(0 < a < target for a in items):
        raise ValueError('restricted subset-sum domain required')
    quota = 2*target+1
    weights = (1,)+tuple(2*a for a in items)+(quota,)
    costs = (target_cost,)+(Fraction(1, 2),)*len(items)+(backstop_cost,)
    return weights, quota, costs


def audit_law(items, target, solution, target_cost=Fraction(1, 2),
              backstop_cost=Fraction(1, 2), delta=Fraction(0)):
    """General weak-obedience law; homogeneous positive-margin specialization."""
    if sum(a*bit for a, bit in zip(items, solution)) != target:
        raise ValueError('invalid witness')
    if delta:
        if target_cost != Fraction(1, 2) or backstop_cost != Fraction(1, 2):
            raise ValueError('positive margins implemented only for homogeneous case')
        success_mass = Fraction(1, 2)+delta
        work_mass = Fraction(1)
    else:
        success_mass = 1-backstop_cost
        work_mass = success_mass/target_cost
    masses = (success_mass, work_mass-success_mass, 1-work_mass)
    if min(masses) < 0:
        raise ValueError('negative mass')
    n = len(items)+2
    profiles = ((1,)+tuple(solution)+(0,), (1,)+(0,)*(n-1), (0,)*n)
    result = {}
    for s, p in zip(profiles, masses):
        if p:
            result[s] = result.get(s, Fraction(0))+p
    return result


def law_statistics(law, weights, quota):
    success = sum(p*int(succeeds(s, weights, quota)) for s, p in law.items())
    marginals = tuple(sum(p*s[i] for s, p in law.items()) for i in range(len(weights)))
    return success, marginals
