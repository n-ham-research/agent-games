# Phase19 — the complete uniform capability–information frontier

16 October2026. Nicholas Ham programme, Codex information branch. Root proposed
symmetrization and the KL-conjugate route; this branch reconstructed the proof,
completed feasibility/endpoints and the optimal mean, and distinguished exact
from at-least reliability. Convexity, rate-distortion and exponential tilting
are established mathematics. Originality of this task-specific completion is
provisional; no generic information-design algorithm is claimed.

## Model and symbols

Retain Phase18's N>=2 named workers, uniform unique capable worker theta,
common benefit B>0, common cost0<c<B. Success occurs iff theta works. Workers
DO NOT know their own capabilities and receive only addressed private work
bits. The trusted coordinator chooses an experiment Z and privately generates
work set A using Z and fresh independent randomness. No free state-correlated
seed, public size announcement, strategic reports, transfers or local tests.
Information cost is I(theta;Z), not message length, physical sensor cost or
implementation memory. Require conditional obedience margin delta with

  0<=delta<=min(c,B-c), tau=(c+delta)/B, sigma=(c-delta)/B.

Thus0<tau<=1 and0<=sigma<=tau<1 except tau may equal1. Write s=Pr(theta in A)
for EXACT success and m=E|A|. At-least success is treated separately below.
All logarithms use the same base; formulas involving exp(alpha) use natural
logs and can be rescaled. Infinite or zero tilt parameters mean limits.

## P19-I1 — exact feasible reliability interval

An obedient mechanism with exact success s exists iff

  s_min<=s<=1, s_min=max(0,(1-N*sigma)/(1-sigma)).               (1)

If sigma=0, this interval contains only s=1. At feasible s define

  U(s)=min(s/tau, N-(1-s)/sigma),                             (2)

with the second entry interpreted as N when sigma=0,s=1. An information-
optimal mechanism can be chosen with mean m=U(s).

**Proof and moment constraints.** Data processing permits replacing any
acquisition by Z=A. Average its channel over all permutations of worker names,
keeping the random permutation private. Mutual information is convex in the
channel for fixed input prior, so this cannot increase cost; success, mean
work and linear obedience are preserved. For the resulting symmetric law,

  work margin = B*s/m-c,
  abstain margin = c-B*(1-s)/(N-m),

where only positive recommendations impose their row. Hence the two exact IC
conditions are s>=tau*m and1-s<=sigma*(N-m). In every law, success and mean
obey s<=m<=N-1+s: a successful set is nonempty, and a failing set has size<=N-1.
Thus m must lie in[s,min(N-1+s,U(s))]. Conversely the symmetric constructions
in I2 realize each such moment pair. The interval is nonempty precisely when
(1) holds: tau<=1 makes s/tau>=s and the abstention bound is >=s exactly at(1).

For later use U(s)<=N*s. Indeed if tau>=1/N the work bound is <=N*s; otherwise
sigma<=tau<1/N and the abstention bound is <=N*s. Also N*s<=N-1+s for s<=1.
So the geometric upper bound is redundant after the IC bounds. It remains
to prove maximizing m within the allowable range minimizes information; I2
provides that proof rather than assuming it.

## P19-I2 — adjacent-cardinality solution and one scalar tilt

For fixed feasible moments(s,m) with m<=N*s, let k=floor m, lambda=m-k. Use cardinalities
k,k+1 with probabilities1-lambda,lambda (omit zero-probability sizes and do not
use N+1 when m=N). For0<t<N define

  q_t(a)=a*t/(N-t+a*t), q_0=0, q_N=1.                        (3)

Choose the unique a>=1 satisfying

  (1-lambda)q_k(a)+lambda q_(k+1)(a)=s.                     (4)

Endpoint/degenerate cases are interpreted as follows: m=0 requires s=0;
m=N requires s=1; if s=m/N use a=1; if s=min(1,m) use a=infinity unless
a lower value already gives the same degenerate law. Otherwise the weighted
function is strictly increasing and(4) has a unique finite solution. Only
moments m<=N*s are needed for the optimal frontier; general moment pairs can
use a<1 instead.

Then the complete exact-success information frontier is

  R(s)=(1-lambda)D_Ber(q_k(a)||k/N)
              +lambda D_Ber(q_(k+1)(a)||(k+1)/N),           (5)

evaluated at m=U(s). At t=0 or N the corresponding divergence is0, since its
q equals the deterministic baseline. Infeasible s has R(s)=+infinity. This
is an explicit adjacent-two-size mechanism plus one monotone scalar equation;
it is not an exponential subset optimization or an unevaluated generic LP.
A rational input may require an algebraic tilt and logarithmic information
value; an exact rational-output claim would be false in general.
For example N=5,B=1,c=3/5,delta=1/10,s=4/5 gives m=8/7 and
weights6/7,1/7 on sizes1,2. Equation(4) reduces to
7a²-89a-168=0, whose positive root is(89+5sqrt505)/14. Thus even a
rationally specified frontier point can have a genuinely irrational optimal
tilt. Finite ideal real-probability channels and exact rational transition
tables are distinct implementation contracts.

### Lower bound for fixed moments

Let p_t=Pr(|A|=t) and q_t=Pr(theta in A||A|=t) in a symmetric law. Its posterior
is uniform within A and within its complement, and its information is exactly
sum_t p_t D_Ber(q_t||t/N). The same expression is a lower bound before
symmetrizing, by binary KL coarse-graining and conditional convexity.
For alpha=log a>=0, binary KL conjugacy gives

  D_Ber(q||t/N)>=alpha*q-log[1+(exp(alpha)-1)t/N].

Let L_alpha(m) be linear interpolation at integers of
f_alpha(t)=log[1+(exp(alpha)-1)t/N]. This interpolation is concave because f
is concave on[0,N]. Thus E f_alpha(t)<=L_alpha(m), giving

  I(theta;A)>=alpha*s-L_alpha(m).                          (6)

For the two adjacent sizes and probabilities(3), equality holds in both
inequalities. As a varies from1 to infinity the attainable weighted success
runs from m/N to min(1,m); this contains every needed s. Therefore(5) is the
optimal fixed-moment value F(s,m), and

  F(s,m)=sup_(alpha>=0)[alpha*s-L_alpha(m)] for m<=N*s.       (7)

At endpoints this follows by limits; no hidden strict-feasibility assumption
is used. Since L_alpha is increasing for alpha>=0, every expression inside
the supremum is nonincreasing in m. Hence F(s,m) is nonincreasing in m<=N*s.
This proves the optimal choice m=U(s) in I1.

### Explicit attaining experiment

Choose size t with the two stated probabilities, independently of theta.
Conditional on(theta,t), with probability q_t choose a uniformly random size-t
set containing theta; otherwise choose one avoiding theta. For t=0,N use the
only possible set. Set Z=A and privately send its membership bits. The posterior
is the claimed uniform-within-groups distribution, and the global IC moment
inequalities are sufficient by symmetry. Every positive work/abstain event
therefore obeys with the required delta. Cardinality t remains PRIVATE.

Although the complete set alphabet can be exponential, the stochastic sampler
has a compact cardinality/tilt description and sends N addressed bits. Exact
sampling of algebraic probabilities is a different implementation model from
finite rational transition tables. Rational approximation with certified errors
is possible away from binding requirements, but is not silently substituted
for exact IC at a tight boundary. An ideal finite experiment with real
probabilities is permitted for the mathematical infimum/minimum in(5).

### Checks against Phase18 endpoints

At s=1, U=min(N,1/tau), q_t=1 for each positive size: (5) becomes
log N minus the adjacent interpolation of log U, exactly P18-I1.
When sigma>=1/N,0<=s<=tau and U=s/tau<=1, the support is empty/singleton,
q_1=tau, yielding R(s)=(s/tau)D_Ber(tau||1/N), exactly P18-I2.
At tau=1 the work bound forces m=s and all nonempty recommendations identify
the capable worker, giving R(s)=s log N over the feasible interval.

## P19-I3 — exact versus at-least reliability, and the preferred reliability

F(s,m), the unconstrained-IC fixed-moment information minimum, is nonnegative
and jointly convex: mix channels with fixed uniform input prior and use
convexity of mutual information. Its two zero endpoints are F(0,0)=F(1,N)=0,
and complementing A gives F(s,m)=F(1-s,N-m).

If sigma>=1/N, the work bound in(2) binds throughout, R(0)=0, and R(s) is
nondecreasing. If tau<=1/N, the abstention bound binds, R(1)=0, and R(s) is
nonincreasing. In the remaining strict middle regime sigma<1/N<tau, the
bounds cross at

  m_star=(1-N*sigma)/(tau-sigma),
  s_star=tau*m_star.                                      (8)

This point is feasible. Below s_star the abstention bound binds, and R is
nonincreasing; above it the work bound binds, and R is nondecreasing.
Both obedience rows bind at the preferred point. Thus a positive margin
can force a nontrivial information-optimal reliability even when reliability
is not otherwise rewarded.

**Monotonicity proof.** Along the work ray m=s/tau, convex nonnegative F has
value0 at s=0; a convex nonnegative function with a zero left endpoint is
nondecreasing. Along the abstention ray, complementing A gives the same
argument in1-s from the zero endpoint(1,N), hence nonincreasing in s. Comparing
the two affine bounds in(2) gives the crossing and the relevant regime. This
uses global channel convexity, not differentiability across integer sizes.

Consequently, for an AT-LEAST reliability target rho in[0,1], the minimum
information is:

* R(rho) if sigma>=1/N;
* zero if tau<=1/N;
* R(max(rho,s_star)) in the strict middle regime.

When tau=sigma=1/N (delta=0 at critical cost), R(s)=0 for every s, so either
boundary formula is consistent. At sigma=0 only success1 is feasible and the
middle formula uses s_star=1. A target below s_min is not an impossibility
when stated as AT LEAST: the design may choose a higher feasible reliability.
This distinction is essential at low costs, where inducing failure/abstention
can require information although certain success requires none.

## Provisional significance, prior and verification record

This closes the entire uniform hidden-capability reliability frontier and
explains an abstention-induced lower reliability boundary. The two adjacent
sizes are derived globally from a scalar log-partition concavity argument;
this is stronger than merely enumerating all size probabilities. Its methods
remain classical symmetry, KL tilting and constrained rate-distortion. Exact
priority of this task-specific frontier has not been established. No new
manuscript, companion edits, external contact or author sign-off is implied.


## Primary-source comparison and actual access

* Armenter, Müller-Itten and Stangebye, *Geometric Methods for Finite Rational
  Inattention*, author-hosted working paper dated12August2021,
  https://www.zachstangebye.com/uploads/6/1/8/8/61883065/geometricri.pdf :
  actually read §2,(RI),and §3 exponential conditional rule,printed pp5–6;
  also §5.3 task assignment,pp25–26. This is explicit prior for mutual-
  information acquisition, direct action channels and log-partition convex
  methods. Their assignment example has a manager controlling tasks for
  workers with uncertain skills; it does not impose our workers' separate
  conditional effort-obedience constraints. The2024 published record was
  found, but this comparison uses the actually inspected2021 working body.
  Our candidate increment is the closed uniform multi-worker incentive
  frontier, not RI's optimization principles or exponential tilting.
* Bunte–Lapidoth, *Source Coding, Lists, and Rényi Entropy*, author-hosted
  conference primary PDF,
  https://www.isiweb.ee.ethz.ch/papers/docu/buch-alap-2013-2.pdf : actually
  read §I model,§III LemmaIII.1 and §IV TheoremIV.1,pp1–2. It studies
  asymptotic fixed-description-length coding and list-size moments with
  Rényi-entropy thresholds, rather than this finite single-experiment MI
  objective plus work/abstention IC. It rules out claiming list-size versus
  information tradeoffs as a new general concept; it is not an exact
  theorem-level priority clearance for(1)--(8).
* Sason, arXiv1911.02436v1,§IV-A2 Proposition5,eq220,pp35–36, actually read
  in Phase18, gives the variable-list entropy bound underlying the full-success
  endpoint; see phase18-endogenous-information.md. KL data processing,
  conjugacy, permutation averaging and discrete concavity are established.
* Bergemann–Morris and Dughmi–Xu primary comparisons from Phase15/17 supply
  the established BCE/direct-recommendation framework. No claim is made that
  adding an information objective creates a new general persuasion theory.

Closest exact task-specific priority remains unresolved. The completion has
more content than a generic numerical convex program: it identifies the
complete feasible interval, proves adjacent cardinalities globally optimal,
selects the optimal average work and locates the exact/at-least reliability
minimum. Whether this is a significant original contribution requires a
closer literature audit than these inspected methodological comparisons.

## Exact checks and independent adversarial reconstruction

`python3 -m unittest experiments.test_phase19_information_frontier -v` passes
seven exact tests. The parameter grid covers N2–6, four costs and three margins,
checking the feasibility interval, both IC inequalities and redundant moment
bounds, including sigma0/tau1. Rational common-tilt witnesses test work-binding,
abstention-binding and both-binding preferred reliabilities; all actual private
conditional margins and mutual-information identities are checked. Information
is represented by exact rational coefficients of prime logarithms. Binary-KL
conjugate inequalities are checked by clearing rational exponents and comparing
integers, not floating-point entropy. Root bracketing uses Fraction arithmetic;
one genuinely algebraic-root input is bracketed to width below10^-20.

The implementation constructs rational-tilt witness channels and certified
root brackets. It does NOT silently implement an irrational binding optimum
using a rounded rational law. No general convex solver, asymptotic sampler or
exhaustive continuous-channel search is included; the global optimum follows
from the analytic certificate(6).

Both the separate exploration and geometry branches independently reconstructed
I1–I3, including sigma0, size0/N, integer/limit tilts, conjugate signs, discrete
Jensen direction, optimal-mean monotonicity and the at-least cases. Neither
found a proof defect. This is internal AI adversarial review, not external
peer review, author sign-off or novelty clearance. This branch independently
reviewed the counterfactual hidden-self-test equivalence in phase19-exploration
and ran its nine exact tests; all passed. It also reconstructed the payoff-
complement closure and parity example in phase19-payoff-geometry and ran its
four exact tests; all passed. A minor illustration was clarified by its author.
