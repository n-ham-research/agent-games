"""Exact complement-averaging checks; no numerical solver."""
from fractions import Fraction as F
from itertools import product

def profiles(n): return list(product((0, 1), repeat=n))
def complement(a): return tuple(1-x for x in a)
def flip(a, i): return a[:i]+(1-a[i],)+a[i+1:]
def symmetrize(law):
    answer = {}
    for a, p in law.items():
        for b in (a, complement(a)):
            answer[b] = answer.get(b, F(0))+p/2
    return answer

def payoffs(law, u):
    return tuple(sum(p*u(a,i) for a,p in law.items())
                 for i in range(len(next(iter(law)))))

def rows(law, u):
    return {(i,r):sum(p*(u(a,i)-u(flip(a,i),i))
                     for a,p in law.items() if a[i]==r)
            for i in range(len(next(iter(law)))) for r in (0,1)}

def cycle_coordination(a,i): return F(a[i]==a[(i+1)%len(a)])
def xor_utility(masks,biases):
    return lambda a,i:F(sum(a[j] for j in masks[i])%2==biases[i])
