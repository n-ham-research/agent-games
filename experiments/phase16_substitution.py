"""Exact finite support observer and exhaustive tiny bounded-adapter synthesis."""
from itertools import product


def observer(initial, horizon, sparse, rich, successors, actions):
    """successors(t,x,b) unions all unobserved joint actions/context inputs."""
    layer={frozenset(initial)}
    layers=[]
    for t in range(horizon):
        nxt=set(); rows={}
        for support in layer:
            observations={sparse(t,x) for x in support}
            for o in observations:
                c=frozenset(x for x in support if sparse(t,x)==o)
                labels={rich(t,x) for x in c}
                if len(labels)!=1:
                    return None,(t,support,o,c)
                rows[support,o]=next(iter(labels))
                if t+1<horizon:
                    for b in actions:
                        target=frozenset(y for x in c for y in successors(t,x,b))
                        if target: nxt.add(target)
        layers.append(rows); layer=nxt
    return layers,None


def verify_adapter(initial,horizon,sparse,rich,successors,actions,update):
    """Infer output table; reject if same local pair requires two labels."""
    reachable={(0,x) for x in initial}; outputs={}
    for t in range(horizon):
        nxt=set()
        for m,x in reachable:
            o=sparse(t,x); label=rich(t,x); key=t,m,o
            if key in outputs and outputs[key]!=label: return None
            outputs[key]=label
            if t+1<horizon:
                for b in actions:
                    mp=update[t,m,o,b]
                    nxt.update((mp,y) for y in successors(t,x,b))
        reachable=nxt
    return outputs


def synthesize(initial,horizon,sparse,rich,successors,actions,observations,d):
    keys=list(product(range(horizon-1),range(d),observations,actions))
    for choices in product(range(d),repeat=len(keys)):
        update=dict(zip(keys,choices))
        output=verify_adapter(initial,horizon,sparse,rich,successors,actions,update)
        if output is not None: return update,output
    return None


def index_signatures(n):
    """Residual terminal behavior of each word under every possible query."""
    return {w:tuple(w[j] for j in range(n)) for w in product((0,1),repeat=n)}


def index_adapter(word,j):
    mode=0
    for bit in word: mode=2*mode+bit
    return (mode >> (len(word)-j-1)) & 1


def index_model(n):
    """O(n) physical states, n input rounds then query, time external."""
    states=[(j,stored,current) for j in range(n) for stored in (0,1) for current in (0,1)]
    initial=[(j,bit if j==0 else 0,bit) for j in range(n) for bit in (0,1)]
    def sparse(t,x): return x[2] if t<n else x[0]
    def rich(t,x): return x[2] if t<n else (x[0],x[1])
    def successors(t,x,a):
        j,stored,current=x
        if t==n-1: return (x,)
        return tuple((j,bit if j==t+1 else stored,bit) for bit in (0,1))
    return states,(initial,n+1,sparse,rich,successors,(0,))
