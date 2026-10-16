"""Three-breakpoint optimization of the P18-P retained payoff region."""
from fractions import Fraction as F
from experiments.phase18_projections import projection_mechanism


def optimize(vertices, weights, success_weight, cost=F(1,2), delta=F(0)):
    if not 0 < cost < 1 or not 0 <= delta <= min(cost,1-cost):
        raise ValueError('invalid parameters')
    candidates=[]
    for s in (F(0),cost+delta,F(1)):
        lower=max(s-cost,delta*s/(cost+delta))
        u={i:s if w>=0 else lower for i,w in weights.items()}
        value=success_weight*s+sum(weights[i]*u[i] for i in weights)
        candidates.append((value,s,u))
    value,s,u=max(candidates,key=lambda item:item[0])
    law=projection_mechanism(vertices,tuple(weights),s,u,cost,delta)
    return value,s,u,law
