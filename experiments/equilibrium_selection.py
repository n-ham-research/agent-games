"""Finite selection/Bayesian/log-linear models. Exact Fraction calculations."""
from fractions import Fraction as F
from itertools import product,permutations

TYPES=(F(1,2),F(3,2))
POLICIES=((0,0),(1,0),(0,1),(1,1))

def volunteer_payoff(types,actions,i):
    return 2*bool(sum(actions))-types[i]*actions[i]

def policy_welfare(p0,p1):
    out=F(0)
    for ti,tj in product(range(2),repeat=2):
        types=(TYPES[ti],TYPES[tj])
        for a,b in product((0,1),repeat=2):
            pr=F(1,4)*(p0[ti] if a else 1-p0[ti])*(p1[tj] if b else 1-p1[tj])
            out+=pr*sum(volunteer_payoff(types,(a,b),i) for i in (0,1))
    return out

def interim_value(policies,i,ti,action):
    total=F(0)
    for tj in range(2):
        types=[None,None];types[i]=TYPES[ti];types[1-i]=TYPES[tj]
        for b in (0,1):
            pr=F(1,2)*(policies[1-i][tj] if b else 1-policies[1-i][tj])
            actions=[0,0];actions[i]=action;actions[1-i]=b
            total+=pr*volunteer_payoff(types,actions,i)
    return total

def pure_bne():
    out=[]
    for p0,p1 in product(POLICIES,repeat=2):
        ps=(p0,p1)
        if all(interim_value(ps,i,t,ps[i][t])>=interim_value(ps,i,t,1-ps[i][t])
               for i,t in product(range(2),repeat=2)):
            out.append(ps)
    return out

def mediator(types):
    if types[0]<types[1]:return {(1,0):F(1)}
    if types[1]<types[0]:return {(0,1):F(1)}
    return {(1,0):F(1,2),(0,1):F(1,2)}

def expected_mediator_welfare():
    return sum(F(1,4)*pr*sum(volunteer_payoff(types,a,i) for i in (0,1))
               for types in product(TYPES,repeat=2) for a,pr in mediator(types).items())

def public_good(s,i):
    return 3*int(all(s))-2*s[i]

def potential(s):return 3*int(all(s))-2*sum(s)

def logit_chain(base=F(2)):
    states=list(product((0,1),repeat=3));idx={s:i for i,s in enumerate(states)}
    P=[[F(0) for _ in states] for _ in states]
    for s in states:
        for i in range(3):
            options=[tuple(a if j==i else s[j] for j in range(3)) for a in (0,1)]
            weights=[base**public_good(t,i) for t in options];z=sum(weights)
            for t,w in zip(options,weights):P[idx[s]][idx[t]]+=w/z/3
    raw=[base**potential(s) for s in states];z=sum(raw)
    return states,P,[w/z for w in raw]
