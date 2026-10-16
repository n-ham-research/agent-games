"""Exact one-cut memory/message certificates; no numerical rank heuristics."""
from fractions import Fraction as F
from itertools import product


def stochastic(a):
    return bool(a) and all(all(x >= 0 for x in r) and sum(r) == 1 for r in a)


def channel(encoder, decoder):
    if not stochastic(encoder) or not stochastic(decoder):
        raise ValueError('stochastic rows required')
    m = len(decoder)
    if any(len(r) != m for r in encoder):
        raise ValueError('cut dimension mismatch')
    y = len(decoder[0])
    if any(len(r) != y for r in decoder):
        raise ValueError('decoder width mismatch')
    return [[sum(encoder[x][j]*decoder[j][z] for j in range(m))
             for z in range(y)] for x in range(len(encoder))]


def normalize(u, v):
    if any(x < 0 for r in u+v for x in r):
        raise ValueError('nonnegative factors required')
    sums = [sum(r) for r in v]
    keep = [j for j,s in enumerate(sums) if s]
    e = [[r[j]*sums[j] for j in keep] for r in u]
    d = [[x/sums[j] for x in v[j]] for j in keep]
    if not stochastic(e):
        raise ValueError('product is not row stochastic')
    return e,d


def rank(a):
    a = [[F(x) for x in r] for r in a]
    k=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(k,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[k],a[pivot]=a[pivot],a[k]
        s=a[k][j]; a[k]=[x/s for x in a[k]]
        for i in range(len(a)):
            if i != k:
                s=a[i][j]; a[i]=[x-s*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a): break
    return k


def optimal_code(n,m,q=1):
    """Pairs of controller mode and retained trusted message, then decode."""
    b=m*q
    enc=[[F(int(j==min(x,b-1))) for j in range(b)] for x in range(n)]
    dec=[[F(int(x==j)) for x in range(n)] for j in range(b)]
    # Unused modes must still have stochastic decoding rows.
    for j in range(n,b): dec[j][0]=F(1)
    return enc,dec


def success(p):
    return sum(p[x][x] for x in range(len(p)))/len(p)


def deterministic_optimum(n,m):
    best=F(0)
    for enc in product(range(m),repeat=n):
        for dec in product(range(n),repeat=m):
            best=max(best,F(sum(dec[enc[x]]==x for x in range(n)),n))
    return best


def replay_adapter(x, blank_rounds):
    """d=N adapter retains x and re-emits it after blank observations."""
    state=x
    return [state for _ in range(blank_rounds)]
