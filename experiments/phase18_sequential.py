"""Exact repeated-assignment workload identities, no equilibrium solver."""
from fractions import Fraction as F


def prefix_schedule(beta,steps):
    beta=F(beta)
    if not F(1,2)<=beta<1: raise ValueError('discount must lie in [1/2,1)')
    r=F(1,2);bits=[];residuals=[r]
    for _ in range(steps):
        bit=0 if r<=beta else 1
        r=(r-(1-beta)*bit)/beta
        bits.append(bit);residuals.append(r)
    return bits,residuals


def workload_prefix(beta,bits):
    return (1-beta)*sum((beta**t)*a for t,a in enumerate(bits))


def periodic_workload(beta,prefix,period):
    if not period: raise ValueError('nonempty period required')
    return workload_prefix(beta,prefix)+(beta**len(prefix))*workload_prefix(beta,period)/(1-beta**len(period))


def balance_polynomial(prefix,period):
    """Q=2(1-z)[A(1-z^P)+z^L C]-(1-z^P), low-first coefficients."""
    L,P=len(prefix),len(period)
    h=[0]*(L+P+1)
    for t,a in enumerate(prefix): h[t]+=a;h[t+P]-=a
    for t,a in enumerate(period): h[L+t]+=a
    q=[0]*(len(h)+1)
    for t,a in enumerate(h): q[t]+=2*a;q[t+1]-=2*a
    q[0]-=1;q[P]+=1
    while len(q)>1 and q[-1]==0:q.pop()
    return q


def evaluate(coeffs,z):
    return sum(a*z**t for t,a in enumerate(coeffs))


def stage_gain(cost,assigned):
    return 1-cost if assigned else cost
