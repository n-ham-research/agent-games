"""Exact private-cost coordination checks; no floating-point LP certificates."""
from fractions import Fraction as F
from itertools import product

POLICIES = ((0, 0), (1, 0), (0, 1), (1, 1))
ACTIONS = tuple(product((0, 1), repeat=2))
TYPES = tuple(product((0, 1), repeat=2))


def payoff(B, costs, actions, i):
    return B * bool(sum(actions)) - costs[i] * actions[i]


def policy_welfare(B, l, h, p, policy0, policy1):
    """Independent local policies; deterministic inputs suffice for team max."""
    out = F(0)
    for t in TYPES:
        costs = tuple((l, h)[z] for z in t)
        mass = (p if t[0] == 0 else 1-p) * (p if t[1] == 0 else 1-p)
        for a in ACTIONS:
            pr = mass
            for i, pol in enumerate((policy0, policy1)):
                pr *= pol[t[i]] if a[i] else 1-pol[t[i]]
            out += pr * sum(payoff(B, costs, a, i) for i in range(2))
    return out


def public_local_max(B, l, h, p):
    return max(policy_welfare(B,l,h,p,a,b) for a,b in product(POLICIES,repeat=2))


def frontier(B, l, h, p):
    cbar = p*l+(1-p)*h
    public = max(2*B-cbar, 2*B*(2*p-p*p)-2*p*l)
    informed = 2*B-l*(2*p-p*p)-h*(1-p)**2
    gap = min(p*(1-p)*(h-l), (2*B-h)*(1-p)**2+l*p*p)
    return public, informed, gap


def cheapest_kernel():
    """Reported type labels; fair ties, NOT generally truthful reports."""
    return {t: ({(1,0):F(1,2),(0,1):F(1,2)} if t[0]==t[1]
                else {(1,0):F(1)} if t[0]<t[1] else {(0,1):F(1)})
            for t in TYPES}


def designated_kernel(i=0):
    a = tuple(int(j==i) for j in range(2))
    return {t:{a:F(1)} for t in TYPES}


def interim(B,l,h,p,kernel,i,true_type,report,action_map=(0,1)):
    out = F(0)
    for other in (0,1):
        t = [0,0]; t[i]=report; t[1-i]=other
        costs = [None,None]; costs[i]=(l,h)[true_type]; costs[1-i]=(l,h)[other]
        mass = p if other==0 else 1-p
        for a, prob in kernel[tuple(t)].items():
            realized=list(a); realized[i]=action_map[a[i]]
            out += mass*prob*payoff(B,costs,realized,i)
    return out


def joint_incentive_gaps(B,l,h,p,kernel):
    """All reports plus every deterministic map recommendation→action."""
    return {(i,t,r,m):interim(B,l,h,p,kernel,i,t,t)-interim(B,l,h,p,kernel,i,t,r,m)
            for i,t,r in product((0,1),repeat=3) for m in ACTIONS}


def kernel_statistics(B,l,h,p,kernel):
    service=F(0); welfare=F(0)
    for t in TYPES:
        mass=(p if t[0]==0 else 1-p)*(p if t[1]==0 else 1-p)
        for a,pr in kernel[t].items():
            service += mass*pr*bool(sum(a))
            welfare += mass*pr*sum(payoff(B,tuple((l,h)[z] for z in t),a,i) for i in (0,1))
    return service,welfare


def deterministic_kernels():
    for actions in product(ACTIONS,repeat=4):
        yield {t:{a:F(1)} for t,a in zip(TYPES,actions)}


def reliability_bound(B,l,h,p,n,service):
    cbar=p*l+(1-p)*h
    return (n*B-cbar)*service + n*p*B*(h-l)/l*(1-service)


def minimum_cost_expectation(costs, probabilities, n):
    return sum(__import__('functools').reduce(lambda x,y:x*y,
               (probabilities[t] for t in ts),F(1))*min(costs[t] for t in ts)
               for ts in product(range(len(costs)),repeat=n))


def procurement_joint_gap(B, actual, i, report, action):
    """Others truthful; fixed least-index tie, paid only on completion."""
    def value(rep,act):
        reports=list(actual); reports[i]=rep
        winner=min(range(len(actual)),key=lambda j:(reports[j],j))
        price=sorted(reports)[1]
        actions=[int(j==winner) for j in range(len(actual))]
        actions[i]=act
        payment=price if winner==i and act else F(0)
        return payoff(B,actual,actions,i)+payment
    truthful_winner=min(range(len(actual)),key=lambda j:(actual[j],j))
    return value(actual[i],int(i==truthful_winner))-value(report,action)


def cheapest_mean_coalition(means, successful):
    return min(successful, key=lambda a:sum(c*x for c,x in zip(means,a)))


def coalition_payoff(B,costs,actions,successful,i):
    return B*int(tuple(actions) in successful)-costs[i]*actions[i]
