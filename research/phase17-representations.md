# Phase 17 — repeated workers and representation-dependent compression

16 October2026. Nicholas Ham; root Codex derivation. Complete finite candidate
proofs; originality provisional. This does not rename treewidth or claim a new
general junction-tree theorem. No manuscript promotion.

## P17-T1: FPT in the number of workers occurring repeatedly

Let F be a supplied monotone binary AND/OR FORMULA of occurrence size S. Each
worker controls one binary action; a worker can label many leaves. Let R be the
workers labelling at least two leaves, r=|R|. Other workers label exactly one
leaf. Utilities are B F(A)-c_i 1[i in A], rational0<c_i<B. All leaves of one
worker share its action. Private central recommendations, complete information,
conditional margin delta>=0. There is an exact full utility/success-region LP
of size S 2^{O(r)}, with construction, rational optimization/membership and
polynomial-support central recommendation recovery in 2^{O(r)}poly(S,L).
Here L includes rational input/objective/side-constraint bits. r is computed
by counting labels, not supplied by an uncharged oracle. This is FPT(r), not
XP in r or a bound in maximum number of occurrences per worker.

### Why ordinary conditioning is insufficient

Fixing the actual repeated actions makes each residual task read-once in other
workers. However those residual laws cannot be optimized independently and
then mixed without the repeated workers' switching constraints. Their deviation
changes ALL their occurrences jointly. The construction below retains these
counterfactual outcomes under the SAME ordinary-worker actions, not independent
couplings for each alternative residual formula.

### Construction

For each actual assignment b in{0,1}^R introduce one local-marginal copy of the
formula tree, of common mass lambda_b>=0, with sum_b lambda_b=1. At each node
store r+1 Boolean values: v^0 for actual b, and v^j for b with repeated worker
j toggled. All these evaluations share the same ordinary-worker leaf actions.
Additionally store actual root sensitivity p, as in P16-T1. A node has at most
D=2^{r+2} states.

At every gate all r+1 value coordinates obey the gate's Boolean operation.
The sensitivity obeys the P16 actual-value relations, using only v^0:
AND children p_l=p_parent v_r^0,p_r=p_parent v_l^0; OR uses complements.
Root p=1. An ordinary worker's leaf has every value coordinate equal to its
single action. Every occurrence of repeated worker j instead has its values
fixed by b and each designated flip, so occurrences are automatically consistent.
Its p value may be stored but is NOT interpreted as that worker's influence.

For each b use nonnegative node-state and supported gate-triple masses with
all unary marginal equalities, root mass lambda_b, and the stated leaf/root
restrictions. At most D³ supported triples per gate are needed (indeed only
2^{2r+3} before leaf restrictions); multiplied by2^r copies this is S2^{O(r)}.
All generation is explicit finite Boolean enumeration, with rational coefficients.
Tree consistency is exact: sample a positive root and recursively its compatible
child pairs, or use sparse subtraction. Every supported global state satisfies
the gate rules, so is the unique lift of its ordinary actions together with b.
In particular the counterfactual worlds always reuse the actual ordinary actions.

For ordinary worker i, sibling subtrees contain no other occurrence of i.
Even though OTHER workers can repeat, changing i leaves every sibling unchanged.
The original unique-path sensitivity proof therefore still gives its root
switching effect p_i. Sum its two action-conditioned rows from leaf marginals
across b, using work gain Bp_i-c_i, abstention gain c_i-Bp_i, subtracting delta
per recommendation mass. This is not conditional obedience separately given b:
workers are NOT told b, so inequalities must be summed over the hidden b cells.

For repeated worker j, read its actual action b_j and its switching gain directly
from ROOT state:

    B(v_root^0-v_root^j) + c_j(1-2b_j).

Sum only cells with the corresponding b_j, again subtract delta times mass.
Outputs are s=E v_root^0; ordinary x_i from their actual leaf; repeated x_j from
sum_b b_j lambda_b; u_i=B s-c_i x_i. Every CE/margin law induces these tables,
and every feasible table system reconstructs an actual law preserving all rows
and outputs. This proves equality of the FULL projected region.

### Recovery and bit complexity

For each b choose a positive root state and descend by positive compatible
triples. Subtract the minimum chosen local mass, preserving every marginal
identity and reducing common mass. Each extraction zeros an entry; at most
S2^{O(r)} profiles result. Rational subtraction has polynomial bit length in
the generated LP solution. Standard rational LP yields the claimed FPT time
and support encoding. Fair-bit rejection gives a central expected-polynomial
sampler in that output encoding; no bounded-depth fair-bit or decentralized
implementation follows. The experiments implement local table transport and
sparse recovery, not a rational LP optimizer.

## P17-T2: a global terminal summary can be exponentially worse than local factors

Consider read-once F=AND_(j=1..m)(x_j OR y_j), all costs1/2 and B1. Restrict
to profiles in which EVERY x_j works and y_j is arbitrary. Success is always1,
and every probe x_j has the SAME own action1 in all profiles. Its work switching
gain is1/2-y_j. Thus the vector of probe switching gains has2^m distinct values.

Any deterministic terminal summary t(A) which determines each worker's switching
gain from only (t(A),own action) must assign distinct states to all these
profiles, by choosing a differing y_j and observing the same probe action.
It requires at least2^m states (at least m bits). Yet the SAME game has P16's
O(m)-size local-marginal payoff-region LP. This is an unconditional separation
between two specified representation architectures, not merely a statement
that an optimization problem is NP-hard. It explains why the P15 terminal-
summary recipe cannot be a universal structural explanation of tractability.

This is elementary distinguishability/counting, not a new general information
lower-bound method. It does NOT prove an LP extension lower bound, a lower bound
on arbitrary symbolic circuits, or that storing m bits is computationally hard.
It requires exact switching coefficients at all pure profiles, a stronger
representational contract than preserving only the feasible CE payoff region.
The separate read-twice matching-face result supplies a genuine exact-LP lower
bound for that latter object; the two conclusions must not be conflated.

## Task evaluation versus strategic representation

For any efficiently evaluable binary task, one complete pure-profile vector of
all switching gains can be computed by n+1 task evaluations. There is therefore
no inherent superpolynomial circuit-description overhead merely to calculate
deviations. The additional difficulty can lie in optimizing globally compatible
laws, or in the chosen exact representation architecture. A small task circuit
does not imply a small exact payoff-region LP; nor does a large LP extension
imply every optimization algorithm is slow. In P16's backstop/common-cost hard
instances, even physically optimal welfare and SOME pure NE are immediate
(backstop alone), while minimizing a designated CE payoff remains hard.
These precise distinctions are stronger than an undefined claim that
'strategic complexity' is universally greater than task complexity.

## Scope, comparisons and verification

All local-marginal mathematics is established junction-tree/compact-CE machinery
from the primary comparisons in phase16-tractability.md. The candidate increment
here is a concrete construction retaining only r+1 coupled evaluations rather
than2^r evaluations inside each node, yielding a single-exponential parameter
bound for an explicitly recognizable repeated-worker formula class. This can
also be understood as conditioning on a small repeated-variable backdoor;
conditioning/backdoors and finite constraint lifts are established ideas. No
claim of a new universal structural parameter or priority clearance is made.

A maximum occurrence bound of TWO alone does not give a polynomial-size full-
region LP: see phase17-originality.md and its matching-face proof. An arbitrary
small task-treewidth claim also needs an explicit correct deviation encoding.
Repeated workers controlling several edges of a series-parallel decomposition
fall under T1 when the number of such workers is small; worker costs are charged
once, and the worker's joint edge activation is represented by one shared bit.
The task is unit connectivity here, not general binary-capacitated flow.

Five exact tests check all binary AND/OR shapes with label sequences over three
workers through four leaves, every action profile and all ordinary/repeated
switch effects; explicit gate tables and size; sparse rational reconstruction
with TWO repeated workers and all margin rows; repeated-leaf sensitivity failure;
and the terminal-summary distinguishability family via actual task evaluations.
Finite tests supplement the construction/induction proof, not establish novelty.
