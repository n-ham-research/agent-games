# Phase17 — multiple incentive rows and the architecture of disclosure

16 October2026. Codex information branch. Proved finite candidates below use
established obedience, decision-rule merging and LP methods. No new general
privacy or persuasion theorem is claimed; novelty remains provisional.

## Model: fixed law, public state channel, explicitly tabulated coefficients

Finite state set Theta has N states and rational full-support prior mu. A
coordinator observes theta and draws literal private recommendations a from
FIXED rational K(a|theta). It separately draws public y from L(y|theta),
conditionally independently of a. Agents observe own type t_i(theta), own
recommendation and y. Utility differences may depend on theta; no reports or
elicitation. For each receiver event e=(i,t_i,a_i) and alternative b_i define

 A_(e,b),theta = sum_(a:e_i(theta,a)=e) K(a|theta)
                   [u_i(theta,a)-u_i(theta,b_i,a_-i)-delta].

Thus there are r explicit obedience rows; conditional delta-obedience means
sum_theta A_(row,theta) mu_theta L(y|theta)>=0 for each row,y. Zero-mass events
are harmless. Assume the undisclosed law is safe, A mu>=0. The objective is
public-only Bayes state guessing V(L)=sum_y max_theta mu_theta L(y|theta).
The observer does NOT see private recommendations. Different statistical
availability constraints or objectives need separate arguments.

## P17-D1 — arbitrary-many-row safe guessing has a polynomial LP

The optimal randomized state-only release has at most N messages and is the
optimum of the following rational LP, regardless of rank or tightness of A:

 variables z_(theta,g)>=0, theta,g in Theta;
 sum_g z_(theta,g)=mu_theta                          for every theta;
 sum_theta A_(row,theta) z_(theta,g)>=0              for every row,g;
 maximize sum_g z_(g,g).

There are N² variables and O(N+rN) principal constraints. Optional dominance
constraints z_(g,g)>=z_(theta,g) make each label its optimal guess; they do not
change the optimum. Recover L(g|theta)=z_(theta,g)/mu_theta. Rational LP theory
gives polynomial bit complexity IN THE EXPLICIT N,r,coefficient input; K and
A may themselves require exponential space in a succinct game. This does not
solve implicit-state or implicit-recommendation instances automatically.

**Proof.** Given any safe channel, choose a maximizing guessed state g(y) for
each message and merge all messages sharing that guess. Safety is preserved
because the cone {z>=0:Az>=0} is closed under addition. Guessing success is
preserved EXACTLY: within a group the same coordinate dominates every column,
and hence dominates their sum. The resulting channel is LP feasible with
objective V(L), proving LPopt>=V*. Conversely any feasible z is a safe channel
whose true guessing utility is at least its diagonal score. Therefore
V*>=LPopt, giving equality. At an optimum a strictly better true guessing
score would contradict equality. This proof handles non-tight independent
rows; extreme-point/rank enumeration and perfect-privacy equalities are
unnecessary. The finite decision-problem extension replaces guessed states
by decisions d and objective sum_(theta,d)gain(d,theta)z_(theta,d); merge by
optimal decision. That is established decision-rule compression in this
particular obedience cone, not a novel revelation principle.

### Limited alphabet

With at most k public messages, exact optimization equals the maximum of the
same LP restricted to labels S subset Theta, |S|<=k. Enumerating such S takes
N^{O(k)} LPs; this is XP in k, not FPT(k), and no polynomial algorithm for
variable k is inferred. A polynomially computed unrestricted optimum can
be garbled to k messages retaining at least k/N of its guessing utility:
keep the k labels with largest diagonal scores, merge all others into any
kept label. Their diagonal contributions survive, their sum is at least k/N
of the unrestricted objective, and cone addition preserves safety. This is
a simple lower bound, not an approximation-hardness claim or a sharp theorem.
Deterministic state releases retain Phase16's exact NP-hardness; changing to
randomized releases is a genuine change of feasible set.

## P17-D2 — a natural common-benefit task with two independent tight rows

Three singleton-capable volunteers have common benefit1 and cost1/2. Require
conditional margin delta=1/10. Four equiprobable states have empty probability
4/13. The singleton recommendation probabilities are, respectively,

 state A: (4,2,3)/13;  B: (2,4,3)/13;
 state C: (3,4,2)/13;  D: (3,2,4)/13.

Every work recommendation has margin1/2. Agent i's statewise abstention
unnormalized margin slack is

    (2/5)*(1-p_i)-4/13 = (2/5)*(3/13-p_i).

The three slack-row columns, in units2/65, are

    A=(-1,1,0), B=(1,-1,0), C=(0,-1,1), D=(0,1,-1).

The rows span dimension2; they sum to zero pointwise, and each averages to
zero under the prior. Hence a safe public column z must satisfy both
z_A=z_B and z_C=z_D. Guessing utility is at most1/2 because, for each column,
its maximum coordinate is at most half its total mass. Revealing AB versus
CD attains1/2 and preserves margin1/10. This example has multiple genuinely
independent incentives, not one scalar balancing inequality in disguise.
Their sum alone is the zero constraint and would allow unsafe full revelation.
Even retaining the nonzero aggregate row1+row3 allows the unsafe pool AC,
where individual row1 is negative. Scalar replacement loses strategic content.

This is a small exact witness, not a hardness result or a new rank theorem.
Its role is to validate that P17-D1 really handles independent obedience rows
in a natural common-benefit contribution game.

## P17-D3 — what recommendation redesign actually changes

Suppose the state is payoff-irrelevant, types/receiver side information do not
depend on it, and the only restriction on recommendations is their overall
unconditional law pi. If any delta-obedient implementation exists, pi is itself
a delta-CE: sum every public/state-conditioned linear incentive inequality.
Conversely if pi is delta-CE, choose K(a|theta)=pi(a) for every theta and reveal
theta completely. Every posterior recommendation law remains pi, so all
conditional incentives and the unconditional outcome law are preserved, while
state guessing becomes1. Thus under these assumptions joint redesign removes
ALL fixed-K disclosure difficulty. Any objective depending only on the
unconditional recommendation/payoff law is unchanged. This is a direct
averaging/independence fact, useful for locating a nontrivial question, not a
new information-design theorem. State-dependent payoffs/types, state-specific
performance constraints or a genuinely fixed K can prevent this argument.

One must also distinguish two joint architectures. If a coordinator may draw
an unrestricted pair(a,y) conditional on theta, joint-law design and obedience
are linear in J(theta,a,y). If the public channel must depend ONLY on theta
and remain independent of recommendation randomness conditional on theta,
then J(a,y|theta)=K(a|theta)L(y|theta) requires rank-one conditional tables;
when both factors vary this is generally nonconvex. It cannot be silently
replaced by the unrestricted joint-law LP.

Exact counterexample: one state, two volunteers B1,c1/2. Mechanism0 always
recommends singleton{0} and releases tag0; mechanism1 uses singleton{1},tag1.
Both are obedient with margin1/2 and satisfy conditional independence. Their
equal mixture as a JOINT law has mass1/2 on({0},0),({1},1), and zero off the
diagonal; it is still obedient but not conditionally independent (marginal
products give1/4 to every pair). An unrestricted coordinator can correlate
these random choices; the declared state-only-independent architecture cannot
produce this exact joint target. It CAN produce the same unconditional action
law using an independent tag. Nonconvexity of exact J is not a claim that all
unconditional payoff regions are nonconvex, nor a complexity proof.

## Primary comparison and actual scope

* Dughmi–Xu, *Algorithmic Bayesian Persuasion*, author-hosted SIAM version,
  https://www.haifeng-xu.com/files/abp_siam.pdf : actually read §2,printed p8,
  direct-signal argument immediately before LP(2.1). They give one signal per
  receiver action and the state/action LP, with explicit-input representation
  limits. P17-D1 uses that established direct-decision compression and adds
  fixed-law obedience rows; this is a scoped method application, not a new
  generic polynomial signaling theorem.
* Rassouli–Gündüz, *On Perfect Privacy*, arXiv1712.08500v8,21Jan2021,
  https://arxiv.org/pdf/1712.08500 §III Theorem1,eq7–9, actually read Phase16:
  posterior extreme-point mixing LP, rank support bounds. Established prior;
  P17-D1 avoids enumeration for a finite decision objective rather than
  claiming the posterior-polytope method is new.
* Asoodeh–Diaz–Alajaji–Linder, *Estimation Efficiency Under Privacy Constraints*,
  arXiv1707.02409v2,13Aug2018, https://arxiv.org/pdf/1707.02409 : actually read
  §I and §II-D Definition3/Theorem3. Optimizing correct guessing under privacy
  constraints is explicit prior. Their stated distinction between unrestricted
  output alphabet and the original alphabet needs closer reconciliation with
  decision-rule merging; no source error or new cardinality theorem is claimed
  on this incomplete comparison. Their constraint is privacy guessing rather
  than the explicit conditional-obedience row matrix here.
* Bergemann–Morris2016 primary BCE body, actual Phase15 reading, supplies direct
  information/obedience prior; see phase15-information.md. LP obedience and
  averaging/revelation arguments are mature tools. A new general randomized
  disclosure optimization claim is unwarranted.

Candidate contribution here is a carefully scoped multi-row algorithm and
information-architecture boundary in the fixed-law research programme. It is
not currently an independently significant new paper theorem. No new manuscript,
companion changes, external contact or author sign-off. Exact checks and actual
adversarial review are recorded below when completed.

## Exact checks and separate proof attack

`python3 -m unittest experiments.test_phase17_disclosure -v` passes seven
exact-rational tests. They cover all15 deterministic partitions of the
four-state independent-row example; an unsafe scalar-aggregate relaxation;
message splitting/merging with exact guessing preservation; non-tight rows
and limited-alphabet garbling; the exported LP against an explicit feasible
half-guessing certificate; full-disclosure joint redesign; and the rank-one
nonconvexity witness. The implementation EXPORTS an LP and transforms supplied
channels; it does not contain a general LP solver or claim an exhaustive
continuous-channel search. The half-guessing upper bound is proved above.

The separate substitution branch independently reconstructed D1--D3, including
both LP inequalities, the k/N garbling bound, the2/65 slack normalization,
the rank-two upper bound and the exact joint-law architecture distinction;
no proof defect was found. This is internal AI adversarial review, not external
peer review, author sign-off or originality clearance.
