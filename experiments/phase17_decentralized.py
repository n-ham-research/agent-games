"""Exact honest tree selection and no-transfer type-imitation checks."""
from fractions import Fraction as F
from itertools import product


def value(tree,active):
    if isinstance(tree,int): return tree in active
    op,l,r=tree
    return (value(l,active) and value(r,active)) if op=='and' else (value(l,active) or value(r,active))


def choose(tree,costs):
    if isinstance(tree,int): return costs[tree],frozenset((tree,))
    op,l,r=tree;cl,al=choose(l,costs);cr,ar=choose(r,costs)
    if op=='and': return cl+cr,al|ar
    return (cl,al) if cl<=cr else (cr,ar)


def all_sets(n):
    return [frozenset(i for i in range(n) if bits[i]) for bits in product((0,1),repeat=n)]


def pure_ne(tree,active,costs,B=F(1)):
    success=value(tree,active)
    for i,c in enumerate(costs):
        switched=active ^ frozenset((i,))
        old=B*success-c*(i in active)
        new=B*value(tree,switched)-c*(i in switched)
        if new>old: return False
    return True


def ic_table(p,types):
    """p[(c1,c2)] is role1 probability; success/exact-one maintained."""
    for c1,c2 in product(types,repeat=2):
        for reported in types:
            if c1*p[c1,c2]>c1*p[reported,c2]: return False
            if c2*(1-p[c1,c2])>c2*(1-p[c1,reported]): return False
    return True


def cost_ratio(p,c1,c2):
    return (p*c1+(1-p)*c2)/min(c1,c2)


def coin_protocol(rounds):
    """Finite truncation: unresolved tie gives no work, no success."""
    unresolved=F(1,2)**rounds
    return {'success':1-unresolved,'work_each':(1-unresolved)/2,
            'expected_rounds':2*(1-unresolved),'bits':4*(1-unresolved)}
