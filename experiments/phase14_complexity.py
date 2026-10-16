"""Exact checks for symmetry-constrained pure-payoff oracle lower bounds.

Finite transcripts validate the adversary identities, not the asymptotic theorem.
No random sampling experiment is presented as a confidence-bound proof.
"""
from fractions import Fraction as Q
from itertools import product


def opponent_tuple(profile, i):
    N=len(profile)
    return tuple(profile[(i+j)%N] for j in range(1,N))


def observed_inputs(queries):
    return {opponent_tuple(s,i) for s in queries for i in range(len(s))}


def pointed_payoffs(profile, F, alpha=Q(1,8), theta=Q(1,2)):
    n=len(profile)-1
    answer=[]
    for i in range(n+1):
        z=opponent_tuple(profile,i)
        D=Q(1,2)-Q(sum(z),n)+alpha*(F(z)-theta)
        answer.append((Q(1,2),(1+D)/2))
    return tuple(answer)


def baseline_differences(probabilities, alpha=Q(1,8)):
    n=len(probabilities)-1
    r=Q(1,2)-alpha/2
    total=sum(probabilities,Q(0))
    return tuple(r-(total-p)/n for p in probabilities)


def regrets(probabilities, differences):
    return tuple(max((1-p)*D/2,-p*D/2) for p,D in zip(probabilities,differences))


def hidden_expectations(probabilities, seen):
    """F1=1 outside seen; exact opponent-product expectation for each player."""
    result=[]
    N=len(probabilities)
    for i in range(N):
        ordered=tuple(probabilities[(i+j)%N] for j in range(1,N))
        mass=Q(0)
        for z in seen:
            term=Q(1)
            for bit,p in zip(z,ordered):
                term*=p if bit else 1-p
            mass+=term
        result.append(1-mass)
    return tuple(result)


def hidden_differences(probabilities, seen, alpha=Q(1,8)):
    base=baseline_differences(probabilities,alpha)
    return tuple(D+alpha*e for D,e in zip(base,hidden_expectations(probabilities,seen)))


def constant_query_bound_holds(n, queries, rho=Q(1,64)):
    b=Q(5,8)+rho
    return queries*(n+1)*b**n <= Q(1,8)


def inverse_poly_query_bound_holds(n, queries):
    return queries*(n+1)*8 <= 2**n


def direct_expectation(F, probabilities):
    result=Q(0)
    for z in product((0,1),repeat=len(probabilities)):
        mass=Q(1)
        for bit,p in zip(z,probabilities):mass*=p if bit else 1-p
        result+=mass*F(z)
    return result
