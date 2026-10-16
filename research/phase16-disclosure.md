# Phase 16 — deterministic disclosure versus fractional balancing

16 October 2026. Agent Games information branch, developed by Codex. All
novelty claims provisional. This investigates a fixed recommendation law,
not designing a new equilibrium or eliciting private information.

## Model and operational objective

Two identical singleton-capable volunteers have benefit B=1, cost c=1/2.
A coordinator observes a finite state theta, draws literal private action
recommendations from a FIXED kernel K, then publishes a state-only channel
L(y|theta). Public randomization is fresh conditional on theta and independent
of recommendation randomness. Agents know their own recommendation and y;
state has no other payoff effect. No transfers or strategic reports occur.
Require conditional obedience margin delta=1/10 on every positive event.

The release's utility is state-guessing success:

    V(L)=sum_y max_theta mu(theta)L(y|theta).

An observer sees y alone, not private recommendations. This is Bayes guessing
probability, not Shannon information, message count, or a complete Blackwell
ordering. For a deterministic partition and UNIFORM prior on N states,
V is exactly the number of nonempty cells divided by N. Arbitrary duplicate
randomized messages cannot improve V.

## P16-D1 — strongly NP-complete deterministic safe guessing

Given an explicit rational fixed K, a uniform prior, and a rational threshold,
deciding whether some deterministic state release preserves delta-obedience
and meets the guessing threshold is NP-complete. Hardness holds already for
the two fixed volunteers above, with at most three action profiles per state,
and with the undisclosed baseline delta-obedient. The reduction is strong in
the explicit sense that one may use the hard 3-PARTITION restriction with
T polynomially bounded in m; then every probability numerator/denominator
and guessing threshold has magnitude polynomial in the number of states.
Thus large binary-encoded numerical magnitudes are unnecessary.

**Proof.** Start with 3-PARTITION: integers a_1,...,a_(3m), T with
T/4<a_j<T/2 and sum a_j=mT. Create N=4m uniform states: item states with
v_j=a_j/T and m anchor states with v=-1. Thus sum_theta v_theta=0.
At state theta put

    f_theta=(1-v_theta)/4,
    K(empty|theta)=f_theta,
    K({0}|theta)=K({1}|theta)=(1-f_theta)/2.

All probabilities are positive rationals. Every work recommendation has
obedience margin 1/2 regardless of the state disclosure. For either agent,
the unnormalized abstention delta-slack contributed by state theta is

    (c-delta)*Pr(abstain|theta)-Pr(empty|theta)
      = (2/5)*(1+f_theta)/2-f_theta = v_theta/5.

Consequently a deterministic cell C is safe iff sum_(theta in C)v_theta>=0.
Since the total sum is zero, every cell of a safe partition actually has sum
zero. Every nonempty cell must contain at least one anchor (all items have
strictly positive v); hence at most m cells are possible. A safe partition
has m cells iff each contains exactly one anchor and item values summing to1.
The strict size bounds force precisely three items per cell, giving exactly
a 3-PARTITION. The guessing threshold is m/N=1/4. Conversely any such triple
partition gives that safe disclosure. The undisclosed single cell is safe,
with abstention margin exactly delta. A partition is a polynomial-size NP
certificate; exact rational cell sums and guessing value are polynomially
checkable. This proves the result using the classical strong NP-completeness
of 3-PARTITION, rather than providing a new proof of that source theorem.

This is exact hardness at a fixed positive REQUIRED obedience margin. It is
not a constant-gap approximation theorem: NO instances may have m-1 cells,
and small perturbations of the required margin can alter the balancing
condition. No hardness is asserted when the safety requirement is only weak
obedience (delta=0) for this same fixed K.

## P16-D2 — scalar tightness gives a transportation normal form

More generally suppose all effective disclosure inequalities reduce to one
signed scalar v(theta), prior mu has full support, and sum mu*v=0. Safety
requires sum mu(theta)L(y|theta)v(theta)>=0 for each y. Summing over y forces
E[v|y]=0 at every positive message. Thus each channel column z_theta=mu L
is a nonnegative zero-v vector.

Let P={theta:v>0}, M={theta:v<0}, Z={theta:v=0}. Every such column splits
into pair-supported balanced columns on P x M and singleton columns on Z.
To see this, match its positive signed masses v_p z_p with negative masses
|v_n|z_n, whose totals agree; each match of size h contributes mass h/v_p
at p and h/|v_n| at n. Zero coordinates split off independently. This
constructive decomposition involves ordinary nonnegative transportation.

Refining a message into these components weakly increases guessing success,
since max_theta sum_r z_(theta,r) <= sum_r max_theta z_(theta,r).
Therefore optimal RANDOMIZED safe state guessing equals

    sum_(z in Z) mu_z + max_h sum_(p,n) h_pn*max(1/v_p,1/|v_n|),

subject to row sums sum_n h_pn=mu_p v_p, column sums
sum_p h_pn=mu_n |v_n|, h>=0. An optimal transportation solution produces
an optimal finite rational channel; conversely any safe channel decomposes
to such a feasible transportation solution with weakly larger objective.
There are at most |P||M|+|Z| nonempty messages, and this is a polynomial-size
rational transportation LP. If v is identically zero, full revelation is
safe and V=1. This is a scalar normal form, not a general efficient algorithm
for arbitrary multiple obedience rows.

For P16-D1 instances, |v_n|=1>v_p, so every edge has objective coefficient
1/v_p. The optimal randomized guessing probability is consequently

    sum_p mu_p = 3/4,

independent of whether the 3-PARTITION instance is YES. Any feasible
transport gives this value, and balanced pair refinement proves it is an
upper bound. Thus on the SAME fixed laws deterministic safe guessing is
at most1/4, while randomized safe guessing is exactly3/4. This is an
operational randomization separation; it is not caused by duplicate labels.

## Relation to perfect privacy and join failure

The scalar equality E[v|y]=0 is exactly a binary perfect-privacy constraint.
Choose a binary latent X with Pr(X=1|theta)=1/2+epsilon*v(theta), for epsilon
small enough to stay in[0,1]. Since E[v]=0, a state channel preserves
X independent of y iff its columns balance v. Therefore the transportation
construction is a rank-two perfect-privacy specialization. It must not be
advertised as a new general information-design or privacy LP method.
The contribution is the explicit fixed-law positive-margin volunteer
embedding and its deterministic/randomized computational boundary; even
that restricted increment requires further novelty investigation.

Pair balancing also explains why there is generally no unique finest safe
partition: balanced pools can cross. It does NOT repair arbitrary join
failure. Tightness of baseline incentive constraints instead changes
inequalities into conservation equalities, exposing an integral partition
problem and its fractional relaxation. Requiring a cell's intersection sums
to be nonnegative is merely the original safety test, not a new structural
join theorem. Private compensation by changing K is outside the fixed-law
claim; allowing it may remove this obstruction and must charge its information
and incentive consequences separately.

## Primary-source access and provisional originality assessment

* Garey and Johnson, *Complexity Results for Multiprocessor Scheduling under
  Resource Constraints*, SIAM J Computing4(4),1975,
  https://epubs.siam.org/doi/10.1137/0204035 : publisher record/abstract inspected,
  source full theorem proof not retrieved in this branch. Classical strong
  3-PARTITION source theorem invoked; do not imply a new proof was checked.
* Rassouli and Gündüz, *On Perfect Privacy*, arXiv1712.08500,
  https://arxiv.org/pdf/1712.08500 : v8,21 January2021 primary PDF inspected,
  SectionIII Theorem1 proof and equations(7)--(9), printed pp6--8. Their
  posterior extreme-point decomposition has support bounded by the conditional
  matrix rank, followed by a mixing LP. At binary rank2 this already gives
  pair-supported columns. P16-D2 is a direct transportation specialization
  for guessing utility, NOT a novel extreme-point algorithm. The restricted
  deterministic volunteer embedding still needs closer prior comparison.
* Babichenko et al., *Algorithms for Persuasion with Limited Communication*,
  https://arxiv.org/pdf/2007.12489 : primary PDF introduction/related-work
  pp2--5 inspected; limited-signal
  persuasion has existing strong hardness. Our fixed-law compliance objective
  differs, but broad signaling-hardness novelty is excluded.
* Bergemann–Morris2016 primary BCE body and McSherry–Talwar2007 were actually
  read in Phase15; see phase15-information.md. Those sources establish the
  information/incentive framework, not the restricted reduction above.

This is a complete candidate proof plus established transportation methods,
not external peer review or author sign-off. It does not outrank the protected
payoff branch without further primary comparison. Exact checks and independent
proof-review status are appended after implementation.

## Exact verification and limits

`python3 -m unittest experiments.test_phase16_disclosure -v` passes six
exact-rational tests. The YES instance has items(4,4,5,5,6,6), the NO instance
has(4,4,4,6,6,6), both T=15,m=2. Exhaustive enumeration of all4140 partitions
of eight states confirms optimal deterministic cells2 and1 respectively;
both attain randomized guessing3/4 with safe pair channels. Further checks
cover all cells of a three-state example, nonuniform priors, zero scalar
coordinates and binary perfect-privacy equivalence. No general LP optimizer
is implemented: the code constructs a feasible greedy transport, which is
optimal for the special reduction but not asserted optimal for arbitrary
edge weights. The separate computation and substitution branches independently
reconstructed D1/D2 without finding a defect; see AG-P16-REVIEW.md.

The separate substitution branch independently reconstructed D1/D2, including
the slack normalization, anchor exhaustion, polynomial numerical restriction,
both directions of the transportation argument and binary privacy equivalence;
no proof defect was found. This is internal adversarial review, not external
peer review or a novelty clearance. This branch also independently reviewed
P16-R1--R3 in phase16-substitution.md and executed its nine exact tests using
`python3 -m unittest discover -s experiments -p test_phase16_substitution.py -v`;
all passed. The trusted-message attainment interface was clarified in response
to review; no mathematical defect was found in the stated scoped results.

## P16-D3 — private refinement cannot repair an unsafe fixed joint law

Root addition after branch review; established conditional-expectation argument.
Fix the complete joint state/action/public-output law J and retain each agent's
original observation event e=(type, recommendation, public output). If its
obedience gain has conditional expectation below delta at e, then no additional
private signal delivered to that agent can make the SAME law delta-obedient
at every refined information event. Indeed if E[Delta|e,z]>=delta on all
positive refinements, averaging over z gives E[Delta|e]>=delta, a contradiction.
The argument allows signals correlated with the full world and recommendation
randomness. It is not limited to the scalar reduction or independent types.

Likewise extra PRIVATE mediator information cannot change incentive validity
if J and receiver observations remain fixed: P15-I1 already separates stochastic
implementation from obedience. Thus information can compensate for public
disclosure only by changing some maintained requirement, such as the joint
recommendation law, available actions/transfers, or the publicly retained
information. No impossibility for redesigned mechanisms is inferred. This
simple consequence answers the fixed-law question without pretending to solve
endogenous joint information/mechanism design. It is BCE/conditioning prior,
not an originality claim or a new theorem needing computational corroboration.
