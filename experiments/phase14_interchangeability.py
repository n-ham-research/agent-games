"""Exact finite stochastic aggregation and private-memory realization examples.

The four-state model has distinct hidden-state transitions in each two-state
fibre. Only its observed interface aggregates. No software-agent experiment or
general equivalence solver is implemented.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product

ACTIONS=tuple(product(range(2),repeat=2))
PLANS=tuple(product(range(2),repeat=3))  # first action, then action at obs0/1


def pure_policy(plan):
    def policy(observations,own_actions):
        a=plan[0] if not own_actions else plan[1+observations[-1]]
        return {a:Q(1)}
    return policy


def posterior_policy(weights):
    """Kuhn realization using only own-action compatibility, not opponents."""
    def policy(observations,own_actions):
        live=[(p,w) for p,w in weights.items()
              if not own_actions or p[0]==own_actions[0]]
        z=sum((w for p,w in live),Q(0))
        if not z:return {0:Q(1)}
        result=defaultdict(Q)
        for p,w in live:
            a=p[0] if not own_actions else p[1+observations[-1]]
            result[a]+=w/z
        return dict(result)
    return policy


def kernel(fine,state,actions,context_input):
    c,m=state if fine else (state,0)
    q=Q(1+c+actions[0]+2*actions[1]+context_input,7)
    reward=int(actions[0]==(actions[1]^c))
    for cp,p in ((0,1-q),(1,q)):
        if fine:
            preferred=m^actions[0]^actions[1]
            for mp,pm in ((preferred,Q(2,3)),(1-preferred,Q(1,3))):
                yield (cp,mp),cp,(reward,reward),actions,p*pm
        else:
            yield cp,cp,(reward,reward),actions,p


def adaptive_context(t,observations):
    return (t+observations[-1])%2


def zero_context(t,observations):return 0


def outcome_law(fine,policies,context=zero_context,horizon=2):
    # Key includes only public observation history, own past actions and state;
    # hidden memory is not available to a policy.
    initial={(0,0):Q(1,2),(0,1):Q(1,2)} if fine else {0:Q(1)}
    frontier={(s,(0,),((),()),()):p for s,p in initial.items()}
    for t in range(horizon):
        new=defaultdict(Q)
        for (s,obs,own,trace),mass in frontier.items():
            e=context(t,obs)
            p0=policies[0](obs,own[0]);p1=policies[1](obs,own[1])
            for a0,pa0 in p0.items():
                for a1,pa1 in p1.items():
                    acts=(a0,a1)
                    for nxt,y,rewards,resources,p in kernel(fine,s,acts,e):
                        step=(e,acts,y,rewards,resources)
                        key=(nxt,obs+(y,),
                             (own[0]+(a0,),own[1]+(a1,)),trace+(step,))
                        new[key]+=mass*pa0*pa1*p
        frontier=new
    out=defaultdict(Q)
    for (s,obs,own,trace),mass in frontier.items():out[trace]+=mass
    return dict(out)


def mixed_plan_law(fine,weights,context=zero_context):
    result=defaultdict(Q)
    for p,w in weights[0].items():
        for q,v in weights[1].items():
            for trace,mass in outcome_law(fine,(pure_policy(p),pure_policy(q)),context).items():
                result[trace]+=w*v*mass
    return dict(result)


def expected_utility(law,player=0):
    return sum((mass*sum(Q(step[3][player],len(trace)) for step in trace)
                for trace,mass in law.items()),Q(0))


def pure_regrets(fine,plans,context=zero_context):
    policies=tuple(map(pure_policy,plans))
    base=outcome_law(fine,policies,context)
    vals=[expected_utility(base,i) for i in range(2)]
    regrets=[]
    for i in range(2):
        best=vals[i]
        for deviation in PLANS:
            changed=list(policies);changed[i]=pure_policy(deviation)
            best=max(best,expected_utility(outcome_law(fine,changed,context),i))
        regrets.append(best-vals[i])
    return tuple(regrets)


def signal_copy_game(common_signal):
    """Own signal marginal is fair; copying has very different regret."""
    signals={(0,0):Q(1,2),(1,1):Q(1,2)} if common_signal else {
        pair:Q(1,4) for pair in ACTIONS}
    baseline=sum((p*(s0!=s1) for (s0,s1),p in signals.items()),Q(0))
    best=baseline
    for mapping in product(range(2),repeat=2):
        value=sum((p*(mapping[s0]!=s1) for (s0,s1),p in signals.items()),Q(0))
        best=max(best,value)
    return baseline,best-baseline


def tv(left,right):
    return sum((abs(left.get(k,Q(0))-right.get(k,Q(0)))
                for k in set(left)|set(right)),Q(0))/2


if __name__=='__main__':
    checked=0
    for context in (zero_context,adaptive_context):
        for plans in product(PLANS,repeat=2):
            profiles=tuple(map(pure_policy,plans))
            assert outcome_law(True,profiles,context)==outcome_law(False,profiles,context)
            checked+=1
    print({'pure_profile_context_pairs':checked,
           'fine_states':4,'quotient_states':2,
           'independent_signals':signal_copy_game(False),
           'common_signal':signal_copy_game(True)})
