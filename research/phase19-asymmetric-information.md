# Phase 19 — heterogeneous two-worker concealment

Status: proved finite-model extension of P18-I1; novelty provisional. Nicholas
Ham; Codex derivation and exact checks. This is a deliberately small asymmetric
case, not a general nonuniform-prior solution.

## P19-A: exact full-success acquisition with heterogeneous thresholds

There are two workers and exactly one capable worker theta. Let
Pr(theta=1)=p in (0,1). Neither worker knows its own capability. Success means
the capable worker works. Worker i receives B times success minus c_i times
its own work; 0<c_i<B and 0<=delta_i<=min(c_i,B-c_i). A committed coordinator
chooses a finite experiment Z and sends private addressed action bits. Charge
I(theta;Z), not channel construction, addressing or worker information. No
reports or decentralized implementation are assumed. Write

    tau_i=(c_i+delta_i)/B in (0,1].

At certain success only sets {1},{2},{1,2} occur. Data processing lets us take
Z to be that set A. Put a=Pr(theta=1,A={1,2}) and
b=Pr(theta=2,A={1,2}); singleton masses are p-a and 1-p-b. A worker who is told
to abstain is incapable, so its gain c_i meets delta_i automatically. Private
work obedience is exactly

    b <= p(1-tau_1)/tau_1,    a <= (1-p)(1-tau_2)/tau_2.

Together with 0<=a<=p and 0<=b<=1-p these define an independent rectangle.
Let h be binary entropy in nats, with zero terms interpreted continuously.

    I(theta;A)=h(p)-(a+b) h(a/(a+b)).

For positive a,b, the subtracted conditional entropy has partial derivatives
log((a+b)/a) and log((a+b)/b), both positive; continuity gives coordinatewise
monotonicity on the closed rectangle. Hence the exact private minimum is the
displayed information at

    a*=min(p,(1-p)(1-tau_2)/tau_2),
    b*=min(1-p,p(1-tau_1)/tau_1).

This is both a converse for arbitrary private-message mechanisms (coarsen
messages to actions preserving conditional obedience) and an attained finite
experiment: sample the four specified state/action masses. Zero-mass signals
carry no obedience requirement. Degenerate thresholds tau_i=1 are included.

## Public cardinality and an exact concealment criterion

Now disclose |A| publicly in addition to each private bit. Singleton messages
reveal the state and obey. On a pair message both workers are told to work,
so its posterior r=a/(a+b) must satisfy

    tau_1 <= r <= 1-tau_2.

If tau_1+tau_2>1 no positive-probability pair is possible and the minimum
information is h(p). If tau_1+tau_2<=1 the PRIVATE optimizer above already
satisfies these pair inequalities: for p<tau_1 it has a=p,
b=p(1-tau_1)/tau_1; for p>1-tau_2 it has b=1-p,
a=(1-p)(1-tau_2)/tau_2; for intermediate p it has a=p,b=1-p.
Thus it is public-feasible and the two minima coincide. Publishing the entire
set gives the same constraints in this two-worker setting; this equivalence
is not asserted for larger games.

For every full-support prior p, private concealment of cardinality therefore
STRICTLY saves acquisition information iff

    tau_1+tau_2>1 and tau_1<1 and tau_2<1.

Indeed in that case a*,b*>0 and the entropy saving is positive; if either
threshold is one, one pair-state mass vanishes, and no entropy is saved.
This explicitly separates a heterogeneous incentive condition from the prior:
the prior determines the size of the gap but not its strictness.

The additive saving is at most h(p)<=log 2. There is no universal multiplicative
bound on public/private optimal information: take p=1/2 and
tau_1=tau_2=1/2+epsilon. Then a*=b*=(1-tau)/(2tau),
I_private=(2-1/tau)log 2 tends to zero, while I_public=log 2.
These can retain FIXED positive margins, e.g. B=1,delta_i=1/10,
c_i=2/5+epsilon for 0<epsilon<1/10. The gain is in paid acquisition under
supplied private channels; it is not a free physical communication theorem.

## Provenance, checks and novelty limit

The entropy identity, concavity/monotonicity argument and direct-recommendation
reduction are standard information-design tools. This exact heterogeneous
rectangle and private/public criterion are classified as a technically distinct
small extension of P18-I1, not an established major new general principle.
Broader private-over-public persuasion advantages predate this model; see the
primary [Pivotal persuasion](https://www.sciencedirect.com/science/article/pii/S0022053119300018)
abstract and displayed obedience description, accessed 2026-10-17. That model
compares persuasion outcomes, while the present quantity minimizes joint
experiment mutual information subject to certain task success and worker
thresholds. This is a formulation distinction, not evidence of originality.
Full article reconstruction was not performed for that comparison.

experiments/phase19_asymmetric_information.py and its test file check the exact
joint-law/entropy identity in a formal prime-log basis, private/public conditional
margins over 96 rational parameter/architecture cases, binding-cap failures,
threshold-one boundaries and the unbounded-ratio family. Tests supplement the
analytic rectangle optimum; they do not numerically certify entropy ordering.
The formal-log helper is reused with provenance from Phase18.

Independent information and exploration branches reconstructed the rectangle,
public cases, strict-gap criterion and ratio and reran all three tests: no
proof defect found. This is internal AI review, not external validation.
