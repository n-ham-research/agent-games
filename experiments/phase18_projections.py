"""Exact protected-edge payoff projection mechanisms, not an LP solver."""
from fractions import Fraction as F
from itertools import combinations


def edges(vertices):
    return tuple(combinations(range(vertices), 2))


def complete_matching(vertices, protected, chosen):
    protected, chosen = set(protected), set(chosen)
    used={v for e in chosen for v in e}
    remaining=[v for v in range(vertices) if v not in used]
    if len(remaining)<4:
        raise ValueError('completion requires at least four remaining vertices')
    matching=set(chosen)|{tuple(remaining[j:j+2]) for j in range(0,len(remaining),2)}
    forbidden=protected-chosen
    while matching & forbidden:
        bad=next(iter(matching & forbidden))
        other=next(e for e in matching if e!=bad and e not in chosen)
        matching.remove(bad);matching.remove(other)
        a,b=bad;c,d=other
        matching.add(tuple(sorted((a,c))));matching.add(tuple(sorted((b,d))))
    if matching & protected != chosen:
        raise ValueError('wrong protected intersection')
    return frozenset(matching)


def threshold_law(probabilities):
    """A common uniform draw realizes arbitrary marginals on <=k+1 subsets."""
    points=sorted({F(0),F(1)}|set(probabilities.values()))
    law={}
    for left,right in zip(points,points[1:]):
        if right==left:continue
        chosen=frozenset(i for i,p in probabilities.items() if p>=right)
        law[chosen]=law.get(chosen,F(0))+right-left
    return law


def projection_mechanism(vertices, protected, success, utilities, cost=F(1,2), delta=F(0)):
    if not F(0)<=success<=1 or not 0<cost<1 or not 0<=delta<=min(cost,1-cost):
        raise ValueError('invalid scalar parameters')
    if len({v for e in protected for v in e})!=2*len(protected):
        raise ValueError('protected edges must be disjoint')
    if vertices%2 or vertices//2 < len(protected)+2:
        raise ValueError('requires m>=k+2')
    x={i:(success-utilities[i])/cost for i in protected}
    if any(not 0<=v<=min(F(1),success/(cost+delta)) for v in x.values()):
        raise ValueError('target outside region')
    law={}
    if success:
        conditional={i:min(v,success)/success for i,v in x.items()}
        for chosen,p in threshold_law(conditional).items():
            active=complete_matching(vertices,protected,chosen)
            law[active]=law.get(active,F(0))+success*p
    if success<1:
        conditional={i:(v-min(v,success))/(1-success) for i,v in x.items()}
        for chosen,p in threshold_law(conditional).items():
            law[chosen]=law.get(chosen,F(0))+(1-success)*p
    return {a:p for a,p in law.items() if p}


def succeeds(vertices, active):
    return len({v for e in active for v in e})==vertices


def statistics(vertices, law, cost=F(1,2), delta=F(0)):
    all_edges=edges(vertices)
    s=sum(p*int(succeeds(vertices,a)) for a,p in law.items())
    u={e:s-cost*sum(p for a,p in law.items() if e in a) for e in all_edges}
    rows={(e,bit):sum(p*(int(succeeds(vertices,a))-int(succeeds(vertices,a^{e}))
                  +cost*(1-2*bit)-delta) for a,p in law.items() if int(e in a)==bit)
          for e in all_edges for bit in (0,1)}
    return s,u,rows
