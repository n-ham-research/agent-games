# Phase 14 — protected payoff regions and information-constrained punishment

16 October2026. Nicholas Ham's Agent Games programme; candidate derivations
and exact checks by the continuation branch. No originality clearance.

## 1. Model and obedience margins

A finite monotone task F excludes the empty coalition. Binary work at active
set A yields B*1[A in F]-c_i*1[i in A], with 0<c_i<B. Recommendations are
private and actions simultaneous. Throughout delta>=0. Unless stated otherwise
costs are complete information. A delta-obedient law has conditional utility gain at least delta
against switching its recommended action, for every recommendation of positive
probability. Equivalently each unconditional CE margin is at least delta times
the recommendation probability. This is a stronger requirement than ordinary
CE or additive epsilon-regret; delta=0 is ordinary CE.

These results concern continuation play. They do not automatically preserve
strategic reporting incentives in an encompassing private-type mechanism.

## P14-A — protected-agent normal form for an entire payoff projection

Fix any protected subset J of agents, k=|J|. From each coalition A repeatedly
delete an unprotected worker whenever deletion preserves success; on a failure
delete every unprotected worker. Let phi_J(A) be the resulting coalition.
Then pushforward through phi_J:

- preserves success and every protected agent's action and payoff exactly;
- weakly raises all unprotected agents' payoffs;
- preserves CE;
- preserves delta-obedience whenever delta<=min_{j outside J} c_j.

The empty minimum imposes no restriction if all agents are protected.

Proof. This is a protected version of P13-P1's success-preserving deletion.
Retained workers become weakly more pivotal; persistent abstainers face weakly
fewer repair opportunities. A removed worker contributed -c_j to its old work
margin; deleting that contribution improves the margin including its delta
right side. It adds +c_j to the abstention margin and adds delta to that
right side, so improves the latter when delta<=c_j. Protected agents retain
their recommendation probabilities, so their improved obedience margins need
no extra restriction. Payoffs are preserved for them because both success and
own work are unchanged. Iteration proves the claim. QED.

The cost restriction for margin preservation cannot be dropped. With B=1,
minimal winners {0,1} and {2,3}, costs (1/10,2/5,2/5,2/5), and delta=1/5,
the equally weighted law on {0,1} and {0,2,3} is delta-obedient. Deleting
redundant worker0 from the second outcome creates an abstention signal giving
it gain only1/10<delta. Ordinary CE survives, but the specified positive margin
does not. Protected agents do not suffer this recommendation-mass change.

### Exact projected-region representation

Let M be the inclusion-minimal successful coalitions. A canonical success A
has every worker outside J pivotal. Every minimal successful T subset A must
therefore contain A\J, so A=T union C for some C subset J. Retain only those
unions whose unprotected workers really are all pivotal. Canonical failures
are precisely losing subsets C subset J. Thus there are at most

    |M|*2^k successful columns and 2^k failed columns.

The CE payoff region PROJECTED ON J is exactly the projection of the polytope
of probabilities on these columns. No loss of any protected payoff vector
occurs: the normal form preserves every such vector simultaneously. Conversely
any feasible canonical law is itself a CE. For delta-obedient regions this
remains exact under the displayed cost bound.

More specifically, for j outside J, workers are pivotal whenever selected, so
work obedience reduces to

    (B-c_j-delta)*x_j >= 0.

Their only substantive constraints are restoration inequalities

    B*sum_{failed C: C+j in F} q_C <= (c_j-delta)*(1-x_j).

Protected agents retain their ordinary two action-contingent inequalities,
with delta times the associated recommendation masses. Their payoffs remain
B*s-c_j*x_j. This describes arbitrary positive and negative target levels
(in fact CE utilities here are nonnegative), not only the zero face.

For one protected non-singleton i, failure support reduces to empty and {i};
winning support consists of minimal winners or a minimal winner plus i, with
the pivotality test above. For simultaneous punishment of a small group J,
only its 2^k possible failed-work patterns are needed. For J empty one recovers
Pareto-improving minimal-success/empty-failure purification. For J=N there is
no promised reduction. Enumerating M can be exponentially costly in a succinct
task representation; this is a structural extended formulation, not a claimed
polynomial algorithm from an arbitrary membership oracle.

### Parameterized computation from a minimal-winning hypergraph

If M is explicitly supplied as m subsets of an explicitly listed n-agent set,
and B,c,delta and objective coefficients are rational of total binary length L,
this is an algorithm with runtime 2^{O(k)} times a fixed polynomial in n,m,L.
Generate T union C for each T in M and C subset J; test all outside workers'
pivotality by subset membership in M. Generate losing C subset J. Form the
canonical probability LP with the displayed O(n) obedience rows, normalization,
and any desired linear constraints on success/protected utilities. Standard
rational LP computes membership or a linear optimum over the exact projected
region in time polynomial in this generated encoding. In particular one
agent's minimum credible CE payoff is polynomial-time computable in this
minimal-winning-hypergraph input, even when the full action table has2^n rows.
This is FPT in k, not a claim of polynomial dependence on an arbitrary compact
task circuit or an unlisted minimal-winning family.

The output is a rational law on at most (m+1)2^k explicit coalitions, with
polynomial bit length in the generated LP. Sampling its column distribution
and privately addressing worker/abstention recommendations takes polynomial
expected bit/time cost in that output encoding and n via exact integer
rejection. Fair-bit worst-case sampling depth may be unbounded. The theorem
invokes standard rational LP. The exact canonical column/row constructor is
implemented and checked; no general LP optimizer was implemented here.

The same support reduction works for cost-blind laws in P14-B: apply deletion
to the same type-independent law and use endpoint IC. Outside worker rows use
B-h_j-delta, restoration rows use l_j-delta, and protected endpoint rows remain
explicit. It preserves each protected type's payoff because success and own
work are unchanged. Thus the joint (success, protected typewise payoff) region
has the same FPT support description, under delta<=min outside l_j. Prior
probabilities do not enter these all-supported-type endpoint requirements.

**Failed simultaneous-minimum inference.** Different designated-worker pure
NE give different agents their individual security minima, but this does not
prove simultaneous attainment is impossible. For two equal-cost volunteers
B=1,c=1/2, independent fair actions are a mixed NE giving BOTH players their
security minima1/2. Thus the natural extrapolation from conflicting designated
roles fails. All-agent zero is impossible when any singleton exists, because
that singleton secures B-c_i>0. More general simultaneous targets are handled
by the protected-region formulation, not a blanket incompatibility claim.

## P14-B — cost-blind recommendations: sharp typewise payoff and robustness

Now each agent privately knows its cost in a finite support with endpoints
0<l_j<=h_j<B. A COST-BLIND mediator receives no type reports or cost observations
and draws its private recommendation law independently of all realized types.
The prescribed strategy is to obey for every supported type. No claim is made
about general uninformed mediators receiving strategic messages, or mediators
whose recommendation law depends on others' observed costs.

For such a fixed law, delta-obedience for every type is exactly

    B*pivotal_work_j >= (h_j+delta)*x_j,
    B*repair_abstain_j <= (l_j-delta)*(1-x_j).

The first condition is hardest for the highest cost; the second for the lowest.
These endpoint inequalities are direct incentive consequences, not a new notion
of robust correlated equilibrium. They do not require independent private costs:
the law is independent of the entire type vector, and only one's own cost enters
its utility given prescribed recommendation-following actions.

Let S be the nonempty singleton-capable set. Assume delta<=min_j l_j and put

    s_delta = 1-min_{j in S}(l_j-delta)/B.

Every cost-blind delta-obedient law has success probability s>=s_delta. Indeed
for any singleton j, deviating from an abstention recommendation to volunteering
succeeds for sure. At its lowest type,

    B*s-l_j*x_j >= B-l_j+delta*(1-x_j),

so B*s>=B-l_j+delta+(l_j-delta)*x_j>=B-l_j+delta.
For ANY target i and supported actual cost c, work obedience and pivotality
p_i<=s yield x_i<=min{1,B*s/(h_i+delta)}. Therefore

    u_i(c) >= B*s_delta-c*min{1,B*s_delta/(h_i+delta)}.       (1)

To substitute s_delta, note that B*s-c*min{1,B*s/(h_i+delta)}
is nondecreasing in s because c<=h_i. The bound is prior-independent within
the cost-blind model and holds whether or not its attaining structure exists.

### Sharp attainment for substantial task classes

Suppose i is non-singleton, belongs to a minimal successful coalition T, and
has NO non-singleton pair-repairer: {i,j} is unsuccessful for every j outside
S union {i}. Necessarily |T|>=3 and T excludes singleton agents. Also assume

    delta <= min_{j in T}(B-h_j).

Write x*=min{1,B*s_delta/(h_i+delta)}. Because h_i+delta<=B, x*>=s_delta.
The law

    T: probability s_delta,
    {i}: probability x*-s_delta,
    empty: probability 1-x*

is delta-obedient for EVERY supported type and attains (1) for ALL types of i
simultaneously. A worker i pools pivotal success and failed work; its smallest
work margin is at h_i, where B*s_delta-(h_i+delta)*x*>=0. Its abstention
signal is empty failure and gives utility gain c>=delta. Every selected
partner in T is pivotal, with work gain B-c_j>=delta. Its abstention signal
cannot restore failure from {i} or empty, so gains c_j>=delta. Outside
non-singleton abstainers also cannot repair these failed profiles. Singleton
abstainers see failure probability1-s_delta, giving margin at least delta by
its definition. All recommendation events of zero probability are omitted.

This includes a singleton backup worker plus any residual task whose minimal
coalitions involving i require at least three participants and no alternative
pair with i. Other residual minimal coalitions need not be absent.

### Consequences and exact examples

With complete-information costs take l_j=h_j=c_j. Formula (1) becomes the
EXACT minimum credible delta-obedient payoff in this task class, not merely
a lower bound. At delta=0 it reduces to

    min_CE u_i = max{0, B-min_{j in S}c_j-c_i}.

Thus zero is one face of a positive-payoff frontier. Positive delta makes the
minimum strictly positive, including at the highest cost; the zero construction
is a genuine weak-obedience boundary.

With private costs, a lower type c<h_i has a strict positive payoff floor
whenever s_delta>0. For B=1, singleton cost9/10, target costs {1/5,4/5},
and a residual triple containing i, at delta=0 we have s_delta=1/10,
x*=1/8. The sharp low-type minimum is3/40 while the high-type minimum is0.
An informed mediator knowing the target's realized low cost can instead give
that low type zero by the complete-information construction. Merely substituting
its realized cost into a cost-blind design would silently give the mediator
information it does not possess.

For positive delta=1/20 with other residual costs1/2, the same endpoints give
s_delta=3/20,x*=3/17. The low and high payoffs are39/340 and3/340. All action
recommendations satisfy the stated conditional margin, not just unconditional
small regret.

### Private information pooling defeats a cellwise success floor

The cost-blind restriction matters more than merely choosing a conservative
cost endpoint. In the preceding B=1 example, suppose the mediator externally
observes only i's cost, privately; the two types have equal probabilities.
At low type1/5 recommend empty failure surely. At high type4/5 use
T with probability1/5, {i} with probability1/20, and empty with probability3/4.
Every type of i receives zero. Each residual partner is pivotal whenever told
to work and cannot repair either failure alone. Singleton s always abstains,
sees unconditional success probability1/10, and is indifferent to volunteering
at cost9/10. This is Bayesian obedience conditional only on each agent's OWN
type and recommendation; it is not a state-by-state complete-information CE.
If i's low type were announced publicly, the singleton would know shutdown and
repair it. Thus applying the singleton floor separately to a mediator's PRIVATE
information cells is false. A cost-dependent hidden kernel can couple credible
punishment across cells. No strategic truthful-report implementation of this
external information is asserted.

## Failure and information boundaries

- The protected normal form preserves protected payoffs, but need not preserve
  utility vectors of unprotected agents exactly. Claiming an exact full payoff
  polytope on minimal-success/empty support would contradict Phase13's zero
  punishment witnesses.
- One cannot infer simultaneous impossibility merely because players need
  different designated-worker pure equilibria for their individual minima:
  private mixed/correlated play may attain them together, as the two-volunteer
  example above shows.
- Blind bound (1) is not proved for a mediator privately observing a signal
  correlated with i's type. Singleton agents may then face only an average
  success rate, allowing success probabilities conditional on that signal below
  s_delta. The unconditional floor cannot be applied separately to each hidden
  cell. Publicly known type partitions do permit applying the argument within
  each cell using its largest supported cost, but no private-cell claim is made.
- Arbitrary CE continuation laws cannot be inserted after audits without
  checking what audit identities, results and recommendations reveal. Additional
  public information may destroy the pooling that makes these laws obedient.
- Conditional positive margins rule out zero punishment when singleton agents
  impose a positive success floor; additive epsilon-obedience is a different
  relaxation and does not imply the same operational robustness guarantee.

## Prior comparison and source access

P14-A is a structural corollary/extension of the Phase13 thinning proof, whose
geometric minimal-support operation has close Kerman–Tenev2024 persuasion prior.
The candidate extra content is the exact projection for protected payoff vectors
and its restoration-capacity interpretation. Generic CE polytopes and LP payoff
optimization are established, not discoveries. P14-B's endpoint IC and margin
inequalities are standard incentive methods; its simultaneously sharp task-class
payoff envelope and information gap need targeted novelty research.

Primary texts actually inspected16October2026:
- Taneva and Wiseman, *Strategic Ignorance and Information Design*, March2023
  author manuscript https://ipl.econ.duke.edu/seminars/system/files/seminars/3540_paper.pdf .
  Introduction, Section2 and AppendixA Definition4 inspected. They characterize
  implementable distributions under agents' endogenous Look/Ignore choices,
  with explicit restrictions on state/action correlation. Our exogenously
  cost-blind mediator is different; no novelty is claimed for the broad principle
  that information constraints restrict equilibrium distributions.
- Misra, Wisniewski, Kallesoe and Bujorianu, *Robust Correlated Equilibrium:
  Definition and Computation*, arXiv2311.17592v2, July2025,
  https://arxiv.org/pdf/2311.17592 , Section3 Definition2 inspected. It treats unobserved
  disturbance-perturbed costs and robust equilibrium/learning, not our exact
  conditional-margin task-specific punishment envelope. Robust CE terminology
  already exists and is not claimed here.
- Cavaliere, *Coordination and Provision of Discrete Public Goods by Correlated
  Equilibria*, February2000 primary SIeP working paper, located subsequently by
  root: https://www.siepweb.it/siep/wp/wp-content/uploads/2021/03/1395874217004.pdf .
  I read Section2 via decoded font text and visually inspected PDF pp8–11
  (printed7–10). It studies normalized common-cost threshold contributions;
  Proposition1 restricts to symmetric CE, Lemma2 gives efficient symmetric CE,
  and Lemma3 discusses pure-NE lotteries. This establishes direct prior on the
  underlying contribution/CE programme. It does not directly state the inspected
  heterogeneous-hypergraph protected-payoff theorem. Some displayed count-only
  claims require qualification; see root's phase14-literature.md for the exact
  source/version and theorem-level comparison. The final2001 published body
  was NOT obtained. Thus the primary-preprint gap has advanced substantially,
  while final-version comparison and originality remain unresolved.

No manuscript promotion is recommended solely on internal proof completion.
The regional normal form and information-sensitive sharp payoff envelope are
competing candidates for further review, not a general solution to private
information or an empirical guarantee for LLM systems.

## Verification and contribution record

Ten exact Fraction tests pass: protected normal forms across all166 nonconstant
four-agent monotone tasks using Phase13 certified continuation witnesses; exact
preservation of protected utilities and outside pivotality; conditional-margin
preservation; type-blind endpoint inequalities against every endpoint type
profile; interior and saturated payoff-frontier branches; explicit information
and positive-margin gaps; the necessity of the margin cost bound; private type-pooling Bayesian obedience; the simultaneous-security-minima counterexample; and generated projected-region LP columns/coefficients against full coalition images.
These are construction/identity checks, not an implemented general CE-region
optimizer or an empirical necessity proof. P14-A/B necessity is analytic above.
No files outside this branch's three owned artifacts were edited.

Independent internal reconstruction by the computation branch found no defect
in P14-A or P14-B, including the conditional margin bookkeeping, singleton
floor, monotonicity and exact endpoint attainment. The parameterized LP
consequence was added subsequently and was then separately checked by the
interchangeability branch, including explicit minimal-hypergraph input,
canonical column count, rational bit complexity and cost-blind endpoint version. This
is same-family AI checking, not external peer review or novelty clearance.

The interchangeability branch separately reconstructed the protected-region
normal form, restoration rows, cost-blind endpoint constraints, sharp three-outcome
construction including saturation, exact numerical examples, and hidden-cell
Bayesian pooling witness. It found no proof defect under the explicitly stated
nonnegative-margin and endpoint bounds. At that review time Cavaliere remained unavailable; root subsequently located
the primary February2000 working paper, inspected above. The final2001 body
is still uninspected.
