"""Exact moment reduction, rational tilt witnesses and certified root brackets.

This does not round a binding irrational optimum into an exactly obedient law.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb, lcm
from experiments.phase18_endogenous_information import add_log, clean


def parameters(n, benefit, cost, delta):
    if n < 2 or not 0 < cost < benefit or not 0 <= delta <= min(cost, benefit-cost):
        raise ValueError('outside the stated model domain')
    return (cost+delta)/benefit, (cost-delta)/benefit


def minimum_success(n, tau, sigma):
    return max(F(0), (1-n*sigma)/(1-sigma))


def optimal_mean(n, tau, sigma, success):
    if not minimum_success(n,tau,sigma) <= success <= 1:
        raise ValueError('infeasible exact success')
    abstention_bound = n-(1-success)/sigma if sigma else F(n)
    return min(success/tau, abstention_bound)


def preferred_success(n, tau, sigma):
    if sigma >= F(1,n):
        return F(0)
    if tau <= F(1,n):
        return F(1)
    return tau*(1-n*sigma)/(tau-sigma)


def sizes(mean):
    k = mean.numerator//mean.denominator
    weight = mean-k
    return {k: F(1)} if not weight else {k: 1-weight, k+1: weight}


def q_t(n, t, tilt):
    if t == 0:
        return F(0)
    if t == n or tilt is None:
        return F(1)
    return tilt*t/(n-t+tilt*t)


def tilted_success(n, mean, tilt):
    return sum(weight*q_t(n,t,tilt) for t,weight in sizes(mean).items())


def tilt_bracket(n, mean, success, steps=80):
    if not 0 <= mean <= n or not mean/n <= success <= min(F(1), mean):
        raise ValueError('moments require tilt at least one')
    if success == mean/n:
        return F(1),F(1)
    if success == min(F(1),mean):
        return None,None  # exact infinite-tilt endpoint
    lower,upper=F(1),F(2)
    while tilted_success(n,mean,upper) < success:
        upper *= 2
    if tilted_success(n,mean,upper) == success:
        return upper,upper
    for _ in range(steps):
        middle=(lower+upper)/2
        actual=tilted_success(n,mean,middle)
        if actual == success:
            return middle,middle
        if actual < success:
            lower=middle
        else:
            upper=middle
    return lower,upper


def tilt_law(n, mean, tilt):
    joint=defaultdict(F)
    for theta in range(n):
        for t,weight in sizes(mean).items():
            q=q_t(n,t,tilt)
            for a in combinations(range(n),t):
                a=frozenset(a)
                if theta in a:
                    probability=q/F(comb(n-1,t-1)) if t else F(0)
                else:
                    probability=(1-q)/F(comb(n-1,t)) if t < n else F(0)
                joint[theta,a] += weight*probability/n
    return dict(joint)


def binary_kl(q,p):
    out=defaultdict(F)
    if q:
        add_log(out,q/p,q)
    if q != 1:
        add_log(out,(1-q)/(1-p),1-q)
    return clean(out)


def information_formula(n,mean,tilt):
    out=defaultdict(F)
    for t,weight in sizes(mean).items():
        if t in (0,n):
            continue
        for prime,coefficient in binary_kl(q_t(n,t,tilt),F(t,n)).items():
            out[prime] += weight*coefficient
    return clean(out)


def log_nonnegative(expression):
    """Exact sign of a rational linear combination of prime logs."""
    denominator=lcm(*(x.denominator for x in expression.values())) if expression else 1
    numerator,divisor=1,1
    for prime,coefficient in expression.items():
        power=int(coefficient*denominator)
        if power >= 0:
            numerator *= prime**power
        else:
            divisor *= prime**(-power)
    return numerator >= divisor
