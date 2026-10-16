# Phase 15 — succinct task representations and credible-payoff complexity

16 October 2026. Candidate derivations by the succinct-task AI branch in Nicholas
Ham's programme; the constant-gap reduction was suggested independently by the
root agent and strengthened here to approximate-obedience output. No novelty
clearance or external peer review. Only this note and its two experiment files
are owned by this branch.

The principal new candidate is a constant-gap hardness result for minimizing
ONE agent's credible CE payoff in binary-weight threshold tasks. It separates
easy task membership, easy discovery of some minimal winner and easy discovery
of some equilibrium from optimizing the protected payoff. The positive results
below are exact algorithmic applications of established compact-CE and dynamic-
programming methods, not new general LP or CE machinery.

## Model and output conventions

There are n explicitly listed agents, simultaneous binary actions and privately
addressed recommendations from a centralized mediator. At active set A,

    u_i(A)=B F(A)-c_i 1[i in A],    0<c_i<B.

F is monotone, F(empty)=0. Success probability is s; work marginal is x_i;
expected payoff is B s-c_i x_i. A CE satisfies two unconditional obedience
rows per agent. Conditional margin delta requires the obedience gain in each
row to exceed delta times that row's recommendation mass. In a later hardness
extension, eta-approximate obedience means each unconditional row is >=-eta;
this is a DIFFERENT relaxation from positive conditional margin.

Rational B,c,delta and supplied linear payoff/reliability objectives and side
constraints have binary encoding length L. A recommendation mechanism output
means an explicitly represented rational law (or the flow representation below
with its proved polynomial reconstruction), not an unspecified oracle sampler.
A general succinct sampler may hide hard expectation evaluation; our output
hardness does not silently assume such evaluation is free.

## P15-S1 — an exact summary-flow representation

Suppose a deterministic layered binary-choice computation processes agents in
a fixed order. Its state after processing i agents belongs to a set of size at
most M, its initial state is fixed, and each action gives one specified next
state. The final summary t must determine success F(A)=f(t). Additionally,
for every agent i, its realized action a and final summary t must determine
its utility and switching gain; write the latter as g_i(t,a). These are exact
promised functions, with rational values of polynomial bit length. A summary
that merely predicts realized success is INSUFFICIENT.

Then the entire joint success/CE-payoff region has an explicit rational
extended formulation of size O(n M^2) flow variables/conservation rows plus
2n obedience rows. The description assumes transitions/state labels are
available in polynomial time in their explicit encoding. It also represents
positive conditional-margin regions, and cost-blind endpoint-obedient regions,
by changing the corresponding row coefficients. No protected-set parameter k
is needed; any desired projection follows afterwards.

### Construction

For each attainable terminal summary t make a separate copy of the layered
computation DAG. Keep only edges on an initial-to-t path. Distinguish edges
labelled 0 and 1 even when they have the same endpoints. Put a nonnegative
flow y^t_e on every edge. Impose conservation at internal nodes. The source
outflow lambda_t and terminal inflow agree; impose sum_t lambda_t=1. Other
terminal nodes have been removed. For layer i let

    z_i,a,t = sum_{edges at layer i labelled a} y^t_e.

Then z_i,0,t+z_i,1,t=lambda_t. Use

    s=sum_t f(t)lambda_t,
    x_i=sum_t z_i,1,t,
    u_i=B s-c_i x_i,
    sum_t g_i(t,a) z_i,a,t >= 0   for every i,a.

For positive conditional margin replace g by g-delta; the same formula
subtracts delta times the recommendation mass. More general utilities can
likewise be accumulated from their terminal/action values.

### Exactness, complexity and reconstruction

Any law on pure profiles routes each profile's probability down its unique
labelled path in its final-summary copy. All displayed statistics and rows are
then exactly the original game's statistics and obedience inequalities.
Conversely, decompose each nonnegative DAG flow into source-to-terminal paths.
Following positive edges from the source always reaches its terminal: flow
conservation prevents a positive path from getting stuck. Subtract the smallest
edge flow along that path and repeat. Every extraction kills an edge, so at
most the total number of positive edges many profiles are produced. Each
label sequence is a pure profile with exactly the promised final summary.
Thus decomposition preserves all displayed rows, payoff coordinates and
success, although it can change correlations that none of those rows measure.
This proves equality of projected regions, not equality of arbitrary laws.

There are at most M terminal copies, O(nM) nodes/edges in each, and O(nM^2)
total flow size. Building the rational LP and invoking polynomial-time rational
LP gives exact feasibility, membership and linear optimization in
poly(n,M,L), including any polynomial list of extra linear constraints on
these coordinates. Rational feasible/optimal solutions have polynomial bit
length in this generated LP. Path subtraction preserves polynomial bit length
(common denominators, or exact rational arithmetic), and decomposition gives
an explicit polynomial-support rational law. A central mediator samples this
law using integer rejection and sends n private bits; expected fair-bit/time
cost is polynomial in the output encoding and n. Fair-bit worst-case depth
need not be bounded. This is no decentralized communication protocol.

This lemma is established network-flow/compact-CE machinery specialized to a
checkable sufficient-summary promise. It is not an independently novel
algorithmic framework. Importantly the constructive primal LP avoids an
unjustified assumption that arbitrary action marginals can be coupled into
coalitions having a specified summary.

## P15-S2 — weighted thresholds without listing minimal winners

Let integer weights w_i>0 and quota Q satisfy 1<=Q<=W=sum_i w_i. Task success
means total weight t>=Q. Use partial weight as the layered state, with
transition t -> t+a w_i. M<=W+1. The final total and own action determine all
deviation coefficients:

    g_i(t,1)=B*1[t>=Q and t-w_i<Q]-c_i,
    g_i(t,0)=c_i-B*1[t<Q and t+w_i>=Q].

Work is useful precisely when the agent is pivotal; abstention is costly to
deviate from precisely when the agent could repair failure. Therefore S1 gives
an O(n(W+1)^2)-size exact extended formulation for the ENTIRE CE payoff/
reliability region. Rational costs may all differ; no anonymous-cost or equal-
weight assumption is imposed. Positive conditional margins require no thinning
cost restriction because no thinning is used. Infeasible margin specifications
are detected by the LP. Cost-blind all-type obedience uses c_i=h_i in work
rows and c_i=l_i in abstention rows; protected typewise utilities use their
respective type costs in B s-c_i x_i. Type-independence of the recommendation
law remains essential.

Consequences:
- Unary-weight threshold input: exact polynomial-time optimization and sampler
  reconstruction, with no explicit minimal-winning-hypergraph input.
- Unweighted threshold: W=n, so the displayed LP has O(n^3) size, despite up
  to binomial(n,ceil(n/2)) minimal winners. This special positive result is
  already encompassed by established anonymous-game CE optimization.
- Binary-weight threshold: the algorithm is PSEUDOPOLYNOMIAL. Replacing weights
  by ranks or capping totals merely at Q can lose pivotality information. No
  polynomial dependence on log W is asserted.

A separation implementation is also immediate from established optimal-CE
frameworks: condition on terminal t and maximize the dual's additive action
scores along the corresponding DAG. This is a weighted subset-sum DP, not a
new separation-to-optimization theorem. The explicit primal flow formulation
is convenient when success/protected-payoff side constraints and exact central
sampler output matter.

## P15-S3 — coverage with a small feature universe

Each agent owns an explicitly listed subset S_i of an r-element universe;
success requires covering every feature. Store the number of selected owners
of each feature, truncated at TWO. There are at most M=3^r summaries. Processing
agent i with action a updates every coordinate by

    v_j -> min(2,v_j+a*1[j in S_i]).

At terminal v, success means all coordinates positive. A selected agent is
pivotal exactly if success holds and some feature of S_i has v_j=1. An
abstainer repairs exactly when failure holds and all zero coordinates belong to S_i.
These tests determine g_i(v,a), so S1 gives exact optimization of the whole
CE payoff/reliability region and reconstruction in poly(n,9^r,L): FPT in
feature-universe size r. Costs can remain arbitrary and every agent may be
protected. This is a direct compact-CE/finite-state DP adaptation; no claim
that the exponent 9^r is optimal or new is made.

Ordinary binary coverage bits do NOT suffice. If two agents cover the same
single feature, the selected set {i} and the selected set {i,j} have the same
coverage bit and i's same action, but i is pivotal only in the first. The
truncated multiplicity state repairs precisely this missing deviation data.
For network connectivity, a final connected-component partition similarly
fails to record whether an individual selected edge is a bridge. Neither
example proves computational hardness; it refutes a proposed summary and
prevents transferring S1 solely from easy success recognition. No generic
bounded-treewidth or arbitrary monotone-circuit tractability is claimed.

## P15-S4 — a constant-gap obstruction already at ONE protected agent

For binary-weight threshold tasks, deciding whether one agent can receive zero
CE payoff is NP-complete. It is NP-hard to distinguish minimum payoff 0 from
minimum payoff >=1/4, with B=1 and costs drawn from {1/2,3/4}. Thus protected-
payoff optimization does not extend to poly(n,log W,L) merely by fixing k=1.
The hardness concerns explicit succinct threshold input and ordinary payoff
accuracy, not a pure-payoff oracle or exponentially fine precision.

### Reduction and YES witness

Take positive SUBSET SUM items a_1,...,a_m and target T, restricted to
0<a_j<T. This restriction remains NP-hard: discard a_j>T; an a_j=T or T=0
is an immediate YES; empty/insufficient remaining sums are immediate NO.
Map these solved cases to fixed restricted YES ((1,1),T=2) or NO ((2,2),T=3)
instances, and otherwise retain the restricted instance. All numbers and
weights use polynomial binary length.

Add target i of weight 1, item agents of weights 2a_j, and backstop r of
weight Q=2T+1. Quota is Q. All item agents and i cost 1/2; r costs 3/4.
The backstop is the only singleton winner; no pair {i,j} with an item agent
wins, since a_j<T. Task membership is a binary sum/comparison. The singleton
{r} is a known minimal winner and a known pure Nash equilibrium in every
instance, so finding some minimal winner/CE is EASY here.

If some item subset sums to T, the coalition M consisting of those items
and i has weight exactly Q and is inclusion-minimal successful. Positivity of
item weights proves every selected item pivotal; removing i drops weight to
Q-1. Use private recommendations

    Pr(M)=1/4,    Pr({i})=1/4,    Pr(empty)=1/2.

Target i works with probability1/2 and is pivotal with probability1/4,
so its work-obedience margin and expected payoff both equal zero. Its only
abstention signal is empty, which it cannot repair alone. Each selected item
is pivotal whenever recommended work. Every item abstaining on failure cannot
repair empty or {i}; on success its work would only waste cost. Backstop r is
always recommended abstention and sees success probability1/4, so is
indifferent between abstaining and paying3/4 to guarantee success. Hence the
law is CE and gives i zero. Every CE utility is nonnegative here because
always abstaining guarantees a nonnegative payoff, so the minimum is exactly0.

### NO gap and a useful dual certificate

Without an exact-T subset, i is never pivotal: without r the item weight is
even, and adding weight1 crosses the odd quota only at item total2T. If r is
present the task already succeeds. Therefore, for EVERY recommendation law,
i's work row is g_i,1=-x_i/2. The backstop's abstention row is

    g_r,0=(3/4)(1-x_r)-(1-s)=s-1/4-3x_r/4.

Both are unconditional obedience gains, not conditional values. Consequently
in every law in a NO instance,

    u_i=s-x_i/2 = 1/4+3x_r/4+g_r,0+g_i,1.

A CE has both rows nonnegative, proving u_i>=1/4. The NO minimum need not
EQUAL1/4; for example the backstop may be the only possible source of success.
This is a constant separation in utilities on a fixed bounded payoff scale.
Computing a value with two-sided additive error strictly below1/8, or returning
an exact CE whose target payoff is within additive error<1/4 of its minimum,
would decide SUBSET SUM. A claimed general sampler-output hardness must state
how its target payoff is read; the conclusion here applies directly to exact
value output or polynomial explicit-law output, where evaluation is easy.

The same identity strengthens the conclusion to relaxed output. If every
unconditional obedience row may be as low as -eta, then in NO instances
u_i>=1/4-2eta. YES still has an exact CE of payoff0. For example, an algorithm
returning an eta=1/64 approximately obedient explicit law whose target payoff
is at most the EXACT CE minimum plus1/16 cannot exist in polynomial time
unless P=NP. Its YES payoff would be <=1/16; its NO payoff would be >=7/32.
This does not equate unconditional eta-slack with a conditional obedience
margin, nor assert hardness of finding an arbitrary approximate CE.

### Membership and what the hardness does not mean

Zero-payoff feasibility is in NP. The full-profile CE LP, although it has
exponentially many columns, has only 2n obedience rows, normalization and the
one target-payoff equality. If feasible it has a basic feasible law on O(n)
coalitions, with rational probabilities of polynomial binary bit length in n
and L (standard determinant bounds). The coalition descriptions have n bits;
all utilities and switching gains are checked by polynomial binary arithmetic.
Thus a polynomial explicit-law witness can be verified. The theorem is not a
claim that arbitrary CE membership is hard: membership of an explicit law is
easy. It is not a strong-NP-hardness claim; the unary/pseudopolynomial positive
algorithm remains consistent. The reduction uses a singleton backstop, exact
private recommendations and weak obedience; no decentralized implementation
or positive-margin zero punishment is asserted.

## Primary prior comparison and actual access

Texts inspected16October2026; references below are original author/journal
texts, not claims inferred from inaccessible citations.

- Papadimitriou–Roughgarden, *Computing Correlated Equilibria in Multi-Player
  Games*, author PDF https://timroughgarden.org/papers/cor.pdf , Section5.3
  Theorem5.7, Section5.4 Theorems5.8–5.9 and Section5.5 Theorem5.10. It already
  gives separation-based optimal-CE algorithms, anonymous-game optimization,
  reconstruction and broad succinct-game hardness. Our threshold/coverage
  positives are applications of this established programme; neither optimizing
  a projection nor outputting a polynomial-support CE is itself novel.
- Jiang–Leyton-Brown, *A General Framework for Computing Optimal Correlated
  Equilibria in Compact Games*, arXiv1109.6064v1 (28September2011),
  https://arxiv.org/pdf/1109.6064 , Section3 Proposition1/proof, weighted variant
  and Section4.1 Proposition4 inspected; WINE extended abstract also inspected
  at https://www.cs.ubc.ca/~kevinlb/papers/2011-WINE-OptimalCorrelated.pdf .
  Their deviation-adjusted-welfare optimization criterion directly yields the
  positive algorithm once our final-summary DP is supplied. We do not claim
  a new general tractability framework or separation theorem.
- Matsui–Matsui, *A Survey of Algorithms for Calculating Power Indices of
  Weighted Majority Games*, ORSJ43(1), March2000, Section4 Theorem2 and its
  PARTITION proof inspected, https://orsj.org/wp-content/or-archives50/pdf/e_mag/Vol.43_01_071.pdf .
  Weighted-voting non-dummy recognition is already NP-complete, and its parity/
  small-weight relevance mechanism is classical. The candidate increment in
  S4 is converting relevance into a CONSTANT GAP in one agent's credible CE
  payoff, including approximate obedience, by a singleton security floor and
  an explicit zero-payoff law. The survey cites earlier Prasad–Kelly1990;
  that final article has not been inspected here.
- Tanaka–Matsui, *Pseudo Polynomial Size LP Formulation for Calculating the
  Least Core Value of Weighted Voting Games*, arXiv2101.11180v2, author PDF
  dated24August2021, https://arxiv.org/pdf/2101.11180 , Section3 and AppendixA
  inspected. It explicitly uses a subset-weight DAG and a pseudopolynomial LP
  for the cooperative least core. Thus subset-weight paths/flow machinery is
  close established prior, although their payoff-allocation solution concept
  is distinct from costly-work obedience and our joint CE region.
- *Cooperation in Threshold Public Projects with Binary Actions*, IJCAI2021,
  https://www.ijcai.org/proceedings/2021/0015.pdf , Section2 utility equation(1),
  Section3 Theorem5 PARTITION reduction and Theorem6 inspected. Their utility
  includes reward proportional to total contributions and retained endowment;
  they prove cooperative pure-NE existence hardness in that model. Our fixed-
  benefit game always has an easily found successful pure NE when grand work
  wins; S4 instead concerns the minimum payoff of a specified agent over CE.
  This is close thematic and reduction prior, not a novelty clearance.

- Barman–Ligett, *Finding Any Nontrivial Coarse Correlated Equilibrium Is Hard*,
  arXiv1504.06314v1 (23April2015), https://arxiv.org/pdf/1504.06314 , introduction,
  Section4 Theorem4 and Section4.1 Theorem5/Corollary1 inspected. They already
  establish near-optimal approximate-CE hardness generally and use a terminal-
  aggregate-conditioned additive DP for positive results. Their positive class
  assumes polynomially bounded aggregates and bounded influence of aggregates
  on utility. Our binary-weight threshold discontinuity need not satisfy that
  joint normalization: keeping the threshold jump at unit scale leaves an
  exponentially large aggregate; normalizing the aggregate makes nearby totals
  produce a unit utility jump. Hence S4 does not contradict their positive
  theorem. Their terminal-conditioned DP is especially close method prior for
  S1–S2; general approximate-CE quality hardness is not claimed as new here.

General DP-to-network extended formulations and compact CE optimization are
mature. S1–S3 should be classified as rigorous representation-specific method
adaptations. S4 is the strongest candidate here; its newness would concern the
precise one-agent constant-gap credible-punishment statement, not SUBSET SUM,
dummy recognition or generic CE optimization hardness. A broader primary search
for this exact public-good CE payoff theorem remains necessary. No inference
from absence of a matching search result establishes novelty.

## Exact checks and remaining scope

Eight Fraction/integer tests currently pass. They enumerate weighted-threshold
DAG paths and switching identities for three-agent weights1..3 and all quotas;
compare whole-law flow statistics and exact path decomposition; exhaust the
three-agent/two-feature coverage masks and toggles; check coverage flow
reconstruction; and inspect restricted SUBSET SUM gadgets with T=2..5 and
one to three items, including all YES witness laws, NO target-pivotality and the columnwise dual certificate for approximate obedience.
The finite checks establish construction identities, not asymptotic hardness
or novelty. The experiment code constructs summary DAGs and transports/
decomposes rational flows; no rational LP solver is implemented and no measured
runtime claim is made for a general optimizer.

Unresolved: better weight-parameter bounds, nontrivial large-universe coverage
classes, useful bridge-sensitive connectivity summaries, succinct bounded-
treewidth monotone-circuit representations, and decentralization costs. Do not
transfer graphical-game treewidth results merely because the TASK circuit has
a small graph: each public-success utility can still depend on every worker.
No manuscript theorem promotion is recommended on internal proof alone.
