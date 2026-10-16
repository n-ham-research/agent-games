"""Exact self-test/invitation joint laws; entropy checks via posterior structure."""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def list_joint(n,sizes):
    law={}
    for theta in range(n):
        for k,p in sizes.items():
            for a in combinations(range(n),k):
                if theta in a: law[theta,frozenset(a)]=F(1,n)*p/F(comb(n-1,k-1))
    return law


def singleton_joint(n,tau,t):
    w=t/tau;law={}
    for theta in range(n):
        law[theta,frozenset()]=(1-w)/n
        for j in range(n):law[theta,frozenset((j,))]=w/n*(tau if j==theta else (1-tau)/(n-1))
    return law


def flags(n,alpha,kind):
    if kind=='common':return {tuple([0]*n):1-alpha,tuple([1]*n):alpha}
    if kind=='independent':
        return {v:alpha**sum(v)*(1-alpha)**(n-sum(v)) for v in product((0,1),repeat=n)}
    if kind=='one':
        if alpha!=F(1,n):raise ValueError('one informed requires alpha1/n')
        return {tuple(int(i==j) for i in range(n)):F(1,n) for j in range(n)}
    raise ValueError('unknown flag law')


def expand(law,flaglaw,n):
    out=[]
    for (theta,a),p in law.items():
        for f,q in flaglaw.items():
            real=frozenset(i for i in range(n) if ((i==theta) if f[i] else (i in a)))
            out.append((theta,a,f,real,p*q))
    return out


def success(law):return sum(p for (theta,a),p in law.items() if theta in a)


def rows(expanded,n,B,c,delta):
    result={}
    for theta,a,f,real,p in expanded:
        for i in range(n):
            status=('capable' if theta==i else 'incapable') if f[i] else 'U'
            action=int(i in real);invitation=int(i in a)
            key=i,status,invitation,action
            gain=(B*int(theta==i)-c) if action else (c-B*int(theta==i))
            mass,slack=result.get(key,(F(0),F(0)))
            result[key]=mass+p,slack+p*(gain-delta)
    return {k:v for k,v in result.items() if v[0]}


def posterior(law,a):
    mass=sum(p for (theta,b),p in law.items() if b==a)
    return {theta:p/mass for (theta,b),p in law.items() if b==a and p}
