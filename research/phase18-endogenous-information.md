# Phase18 — information acquisition for an uncertain-capability task

16 October2026. Codex candidate development for Nicholas Ham's Agent Games.
The model has payoff-relevant uncertainty. Entropy/list-decoding methods are
established prior; exact strategic specializations below are provisional in
originality, not a new generic information-design theorem.

## Timing and resources

N>=2 named workers; exactly one is capable, theta uniform on{1,...,N}.
Nobody initially knows theta, INCLUDING their own capability. A task succeeds
iff capable worker theta works. All workers receive common benefit B>0 from
success and each worker pays common cost0<c<B. The coordinator commits to an
experiment Q(Z|theta), pays information cost measured by I(theta;Z), and then
privately recommends work/abstain to every named worker. The complete sampled
work set is A. Fresh coordinator randomness is independent of(theta,Z).
Addressed private channels are supplied resources; their communication length
and privacy cost are not measured by mutual information. Nobody can inspect
another worker's message. No cost reports, transfers, future punishment,
external state-correlated seed, or agent information acquisition are available.

Require conditional obedience advantage at least delta on every positive
recommendation event. Initially allow only private work bits; later compare
public revelation of |A|. All logs use one fixed base. The coordinator optimizes
information acquisition jointly with recommendations, not an additional safe
release of a frozen recommendation law. Data processing gives
I(theta;Z)>=I(theta;A), since A is generated from Z and fresh randomness.
The state cannot be ignored: selecting a worker independently of theta may
fail, and private work incentives depend on posterior capability.

## P18-I1 — exact acquisition cost for certain success

Assume 0<=delta<=min(c,B-c). Write

 r=min(N,B/(c+delta)), k=floor r, lambda=r-k,
 L(r)=(1-lambda)log k+lambda log(k+1),

where at r=N define L(N)=log N without using sizeN+1. Then among all obedient
private-recommendation mechanisms guaranteeing success with probability1,

    minimum I(theta;Z) = log N - L(r).                         (1)

The minimum is attained by an experiment whose output is the work set itself.
If the coordinator must ALSO announce the realized number of workers, the
sharp minimum is instead

    log N - log floor r.                                      (2)

For noninteger r<N the difference lambda log((k+1)/k)>0 is the exact value of
keeping the list size private in this acquisition-cost metric. No claim is
made about the cheapest physical sensor or total communication cost.

**Converse for(1).** Sum unconditional work incentive constraints:

 sum_i [B Pr(theta=i,i in A)-(c+delta)Pr(i in A)] >=0.

Certain success makes the first probability sum1, hence expected work
m=E|A|<=B/(c+delta). Also m<=N, so m<=r. Certain success implies theta in A;
therefore H(theta|A)<=E log|A|. On integer sizes1,...,N, the piecewise-linear
interpolation L of log is concave and increasing, so

 I(theta;Z)>=I(theta;A)>=log N-Elog|A|>=log N-L(m)>=log N-L(r).

This bound does not assume a symmetric mechanism or independent worker
recommendations. Extra private/public messages cannot evade the summed
incentive inequality or data processing.

**Attainment.** Independently choose sizeK=k or k+1 with probabilities1-lambda,
lambda. Conditional on(theta,K), choose uniformly among sizeK subsets
containing theta. Acquire exactly that set Z=A and send each worker its
membership bit, without publishing K. By permutation symmetry,
Pr(i in A)=r/N and Pr(theta=i,i in A)=1/N. Thus each positive work
recommendation gives posterior capability1/r and work advantage B/r-c>=delta.
Under an abstain recommendation theta cannot equal i, so the advantage of
abstaining is c>=delta. The posterior theta given A is uniform on A, giving
H(theta|A)=L(r), exactly attaining(1). At r=N everybody always works, information
cost0, and no abstain recommendation occurs.

**Converse/attainment for(2).** Condition work incentive constraints on public
K=t and sum workers. Certain success gives

    B Pr(K=t)-(c+delta)t Pr(K=t)>=0.

Every realized t must therefore satisfy t<=B/(c+delta), hence t<=floor r.
The entropy bound gives(2). A fixed uniform containing-theta set of size
floor r attains it; work advantage B/floor r-c>=delta, abstain advantage c.
This concerns revealing cardinality, not revealing the whole recommendation
set. Publicly revealing the set makes any unable recommended worker know
it might be incapable but posterior1/K; the same fixed-size construction
still obeys, and the same cardinality lower bound applies. With common costs
and no own capability information, public fixed-size lists attain(2) too.

Example: N=3,B=1,c=3/5,delta=1/10 gives r=10/7. Private optimal sizes1,2 have
probabilities4/7,3/7; selected work margin1/10, abstain margin3/5, and cost
log3-(3/7)log2. Announcing size2 would leave each selected worker with
capability probability1/2 and work gain -1/10, violating even weak obedience.
Public size disclosure therefore raises optimal acquisition to log3.

## P18-I2 — sharp low-success information slope

A second exact segment quantifies acquisition before certain success. Put
p=1/N, tau=(c+delta)/B, and assume p<tau<=1 and0<=delta<=c-B/N, in particular delta<=B-c. For any desired
success probability0<=s<=tau, the minimum acquisition information among
conditional delta-obedient mechanisms with success exactly s is

    I_min(s)=(s/tau) D_Ber(tau || p).                          (3)

This is a positive linear acquisition cost near zero, caused by incentives:
when c>B/N, zero information cannot induce any work. Without obedience,
everybody could simply work without acquiring information and success would
be certain. Formula(3) is not asserted for s>tau.

**Converse.** For each realized nonempty set A of size t, let q_A=Pr(theta in A|A).
Binary coarse-graining of relative entropy gives

 D(P(theta|A)||uniform)>=D_Ber(q_A || t/N)
                          >=t D_Ber(q_A/t ||1/N).

The second inequality is elementary: for fixed t<N, the difference as a
function of q has its minimum0 at q=t/N; its second derivative is
1/(1-q)-1/(t-q)>=0 (natural-log scale). For t=1 it is equality; t=N forces
q=1 and both sides0. Empty sets contribute nonnegative information and no
success/work. Average and use convexity of binary KL to obtain

    I(theta;A)>=m D_Ber(s/m ||p), m=E|A|.

Summed work obedience gives m<=s/tau. Since D_Ber(a||p)/a increases for a>p
(its derivative has numerator log((1-p)/(1-a))>=0), the claimed lower bound
follows. At s=0 work obedience forces m=0 and the assertion is immediate.

**Attainment.** With probability s/tau generate a singleton{j} using the
N-ary symmetric channel with Pr(j=theta)=tau; otherwise output the empty set.
This choice probability is state independent. Every worker recommendation
gives capability posterior tau, hence work advantage delta. Under abstention,
the capability posterior is(1-s)/(N-s/tau)<=1/N, so abstain advantage is at
least c-B/N>=delta. Empty output carries no state information and each
singleton's posterior gives binary KL D_Ber(tau||p), proving(3).

## What creates the strategic information cost, and what this does not prove

Certain success without incentives needs NO acquisition: instruct everyone
to work. Incentives cap average work at B/(c+delta), turning capability
uncertainty into a list-decoding problem. Private recommendation pooling
converts an integer pointwise worker bound into an average bound; publicly
announcing list size reinstates the integer bound. This is a precise
information/incentive interaction, not the Phase17 payoff-irrelevant redesign
triviality or a generic obedience LP.

If workers know their own capabilities, the unique capable worker can work
without any coordinator information, provided its margin and others' margins
permit it. That changes the model and invalidates the claimed acquisition
necessity. If a state-correlated external seed or side channel is free,
I(theta;Z) alone is not a valid total acquired-information measure. Zero
information is weaker than zero implementation memory/communication, and the
finite experiment assumption is substantive. The optimal set experiment is
an ideal information channel, not a demonstrated physical measurement process.

The two formulas need not characterize the middle success range, nonuniform
priors, heterogeneous costs, or utility from redundant work. Higher cost may
reduce voluntary redundancy and raise required acquisition; better task
performance can require more selective information rather than more disclosure.
These observations are confined to the stated task. No welfare-optimality,
truthful elicitation or independent research novelty is inferred.

## Primary-source comparison and access record

Primary comparisons are being completed. Entropy support bounds, list-decoding
Fano inequalities, binary KL coarse-graining and rational-inattention information
costs are established. This branch must not claim them as new mathematics.
The candidate increment is the exact common-cost obedience-constrained
acquisition curve and private/public cardinality gap for this particular
uncertain-capability task. Originality is provisional pending closer sources.

* Igal Sason, *On Data-Processing and Majorization Inequalities for
  f-Divergences with Applications*, arXiv1911.02436v1,6Nov2019,
  https://arxiv.org/pdf/1911.02436 : actually inspected §IV-A2,Proposition5,
  equation(220),printed pp35–36. Its variable-list Fano bound at zero error
  gives exactly H(theta|A)<=Elog|A|, explicitly attributed there to earlier
  sources. Thus the information-theoretic converse in I1 is established
  list-decoding mathematics. This branch combines it with obedience's average
  work cap and checks an attaining recommendation scheme; it does not claim
  a new Fano inequality, entropy extremizer or adjacent-integer concavity fact.
* Chamsi Hssaine and Siddhartha Banerjee, *Information Signal Design for
  Incentivizing Team Formation*, arXiv1809.00751 primary PDF,
  https://arxiv.org/pdf/1809.00751 : actually read §2 model and information
  structure,Definition1,pp4–6,plus self-awareness discussion. They already
  distinguish agents who know their own abilities from those who do not.
  Their main task is stable team matching with increasing team utilities,
  principal initially knows the abilities, and their stated policy class is
  public signaling. Our task has a unique capable worker, costly binary work,
  and optimizes an acquired-information budget using private recommendations.
  This is a model distinction, not novelty clearance for hidden-ability
  persuasion or the value of concealing information.
* Dughmi–Xu and Bergemann–Morris primary comparisons from Phase17 remain
  relevant established information-design background. A theorem-level search
  specifically for obedience-constrained variable-list acquisition has not
  been exhausted. No externally verified priority claim is made.

## Exact verification and independent attack

`python3 -m unittest experiments.test_phase18_endogenous_information -v` passes
eight exact checks. For N=2,...,7 they check full-success construction masses,
all conditional action margins and mutual-information equality. Low-success
constructions are checked at four success levels for N=2,...,6. The tau=1 endpoint is checked separately. Other checks
verify the explicit10/7 private/public example, the zero-information all-work
regime, the same blind instruction's incentive failure at high cost, and public
fixed-size-list obedience. All probabilities and margins are Fractions. Mutual
information identities are checked EXACTLY as rational linear combinations of
prime logarithms (factor each rational log argument), with no floating-point
entropy tolerance or numerical solver. The tests verify constructions and
identities; global converse inequalities are established analytically above.

The separate sequential branch independently reconstructed I1 and I2. It
identified a missing standalone I2 domain condition tau<=1; this was repaired
explicitly as delta<=B-c before integration. The entropy interpolation,
conditional private/public incentives, binary-KL difference, weighted Jensen
step and increasing KL ratio then passed independent proof attack. This is
internal adversarial AI review, not external peer review or author sign-off.
This branch also reconstructed sequential S1–S3 and ran its eight exact tests;
all passed. Persistent-type imitation, the rational-root obstruction and
finite-random-controller collapse require the recorded autonomous/resource
and pathwise rather than ex-ante interpretation.
