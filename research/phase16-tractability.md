# Phase 16 — local deviation information in read-once tasks

16 October2026. Nicholas Ham; root Codex development. Candidate task-class
application, not a new junction-tree or DP-to-LP theorem. Independent computation/resource-branch reconstruction passed; details in AG-P16-REVIEW.md. Finite complete-information binary contribution games throughout.

## P16-T1: linear-size full payoff formulation for read-once monotone formulas

Let the task F be supplied as a binary AND/OR formula whose n leaves are n
DISTINCT workers, each appearing once. At active set A, worker i receives
B F(A)-c_i 1[i in A], rational B>c_i>0. Private central recommendations, no
reports or decentralization promise. For any rational conditional margin delta>=0,
the full expected-utility/success region has an O(n)-size exact rational LP.
Construction, rational optimization, projected membership and recovery of a
polynomial-support recommendation law are polynomial in n and input bit length.
This remains true for heterogeneous costs, all protected coordinates, linear
side constraints and cost-blind endpoint obedience. Margin regions may be empty.

This identifies a natural class beyond bounded final aggregation: an AND of n/2
independent OR pairs has exponentially many minimal winners, but the formula and
LP are linear. Ordinary graphical-game interaction width can still be large
because every worker receives the GLOBAL success benefit. We do not infer the
result simply from the formula being a tree.

## Local lift and the pivotality lemma

For each formula node v retain two Boolean variables (b_v,p_v). The first is
the realized subformula value. The second says changing this node's value,
while holding the other disjoint subformulas fixed, changes the ROOT value.
Set p_root=1. For a gate with children l,r impose these local relations:

    AND: b_v=b_l b_r; p_l=p_v b_r; p_r=p_v b_l.
    OR:  b_v=b_l OR b_r; p_l=p_v(1-b_r); p_r=p_v(1-b_l).

For any leaf assignment these relations have a unique extension. Upward
evaluation fixes b, and downward propagation fixes p. Because sibling subtrees
use disjoint workers, the ordinary Boolean sensitivity chain rule along the
unique root-to-leaf path gives

    p_i = F(A union {i}) - F(A minus {i}).

One can prove this inductively: at AND, altering the left input changes the
parent iff the right input is1; at OR iff the right input is0; multiply by
parent sensitivity and repeat. Disjointness ensures the sibling value does not
also change when worker i toggles. Consequently selected work has switching
gain B p_i-c_i, and abstention gain c_i-B p_i. The deviation data is local at
the leaf even though utility contains global success.

## Exact local-marginal LP

Each node state has four possibilities. Introduce its unary mass m_v(b,p).
For each gate introduce a triple mass q_v(state_v,state_l,state_r), supported
only on the relations above (at most64 entries). Impose nonnegativity, each
triple's three unary marginal equalities and root normalization. Set root
masses with p_root=0 to zero. For a single-leaf formula use just root masses.
The gate scopes form a junction tree: adjacent scopes intersect only at the
state of their shared formula node. There are O(n) variables/constraints.

Every law of worker actions lifts to a feasible set of these local masses.
Conversely sample a root state from m_root and recursively sample both child
states using q_v/m_v. Zero-mass states need no conditional definition. Tree
consistency gives a global distribution with exactly the specified gate and
unary marginals. Every supported assignment satisfies the local relations,
so it is the unique lift of its worker actions and has the correct pivotality.
No independence assumption is imposed on the original recommendation law:
reconstruction may change correlations, but preserves every statistic below.

Impose the exact unconditional conditional-margin inequalities

    sum_p m_i(1,p)(B p-c_i-delta) >=0,
    sum_p m_i(0,p)(c_i-B p-delta) >=0.

Read outputs as s=sum_p m_root(1,p), x_i=sum_p m_i(1,p), u_i=B s-c_i x_i.
Thus every utility/success/obedience row is preserved both ways, proving
exactness of the claimed region. Ordinary CE is delta0. For a type-blind law,
work uses the largest supported cost and abstention the smallest; typewise
outputs use the respective cost. No truthful reporting result follows.

For explicit support rather than the conditional tree sampler, repeatedly
choose a positive root state, then a positive compatible triple at each gate.
Subtract the minimum of all selected unary/triple masses from that global
lift. The residual remains nonnegative and locally consistent with reduced
common normalization. At least one positive entry vanishes each time, so O(n)
profiles suffice. Exact rational arithmetic has polynomial bit length in the
LP solution encoding. A single recommendation draw is then a central rational
lottery and n privately addressed bits. Fair-bit sampling can use expected
polynomial time; no bounded worst-case random-bit depth or decentralized
implementation is claimed. The experiments implement the sparse reconstruction,
but do not implement a rational LP solver.

## P16-T2: two-terminal series-parallel edge-activation networks

Suppose workers are DISTINCT edges of a supplied two-terminal series-parallel
network with a supplied binary series/parallel decomposition. A task succeeds
iff selected edges connect the terminals. Edge-disjoint series composition is
AND, parallel composition is OR, so the decomposition is exactly the required
read-once formula. Therefore T1 gives a linear-size full CE payoff LP and
polynomial exact optimization/reconstruction for this network reliability
class. The same statement applies to directed compositions consistently
oriented from source to sink. No ordinary independent edge-reliability
assumption is needed: the CE law is allowed to correlate all edge actions.

The decomposition and one-worker-per-edge assignment are part of the input.
One worker controlling repeated edges is a different task. This is not a
claim for all graphs of treewidth2, or all bounded-treewidth task circuits.
Series/parallel recognition is unnecessary for the theorem because its witness
is supplied and can be checked by the recursive graph composition.

## P16-T3: small graph width alone is insufficient for capacitated success

For a capacitated variant, let worker i activate one parallel s-t edge of
binary capacity w_i, and define success as max-flow at least binary quota Q.
The maximum flow is the sum of capacities of active edges, exactly a weighted
threshold. P16's homogeneous positive-margin payoff-hardness reduction therefore
already applies to TWO vertices with parallel edges (underlying simple graph
width1). A supplied series-parallel decomposition and tiny graph width alone
do not imply polynomial protected-payoff optimization for binary-capacitated
threshold flow. This is a direct corollary of the threshold theorem, not an
independent new hardness method. It contrasts with T2's unit connectivity
target; numeric encoding and success semantics are essential.

Elkind et al. §4.2/Theorems4.4–4.5 and §4.3 already make the same conceptual
connectivity-versus-binary-flow distinction for cooperative power indices.
In particular their read-once translation and network representations are
PRIOR; our claimed consequence concerns a different costly-work CE payoff
region. This adjacent result substantially limits representation-novelty claims.

## General sufficient width statement, and why it is not the contribution

More generally, suppose a finite local-constraint encoding of action profiles
has a supplied tree decomposition, such that (i) every original profile has
some extension, (ii) every satisfying extension encodes correct success and
ALL switching gains, and (iii) required output/obedience terms fit in supplied
bags. Bag distributions with exact separator consistency yield an exact CE LP
of size polynomial in encoding length times D^{O(t)}, with state domain D and
width t. This is standard junction-tree marginal-polytope machinery, with the
same sparse extraction argument. Encoding construction/width verification
cannot be omitted or inferred from a small success-only circuit.

T1 supplies a concrete width2 encoding on four-state nodes in linear time,
which is the task-specific useful fact. This general statement is not asserted
as a newly discovered structural characterization, nor as a necessary condition
for all tractable representations. Counting variables or named structural
parameters without constructing the deviation encoding proves no FPT theorem.

## Counterexample and scope

Read-once cannot simply be dropped from the lift: F=x AND x at x0 gives local
child sensitivities0, although changing worker x makes F change from0 to1.
Reconvergent changes can affect both gate inputs, defeating the single-path
chain rule. This refutes the proposed lift, not polynomial tractability for
that particular redundant formula (which simplifies to x). Similarly, a final
connected-component partition omits bridges; T2 works through edge-disjoint
recursive sensitivity instead of assuming connectivity summaries suffice.
No new facet/dimension classification is obtained merely from this LP.

## Source comparison and finite verification

* Wainwright–Jordan2008, [primary monograph text](https://www.cs.columbia.edu/~blei/fogm/2020F/readings/WainwrightJordan2008.pdf), Proposition4.1 and junction-tree discussion: tree local marginals are globally realizable. This is exactly the mathematical method behind our marginal LP, explicitly PRIOR.
* Elkind–Goldberg–Goldberg–Wooldridge2009, [author primary text](https://www.cs.ox.ac.uk/people/leslieann.goldberg/papers/mcn.pdf), §3.4 and §4.2 (especially the explicit connectivity/read-once translation and Theorem4.4): compact read-once coalitional representations and polynomial value computations are established, including connections to series-parallel network flow games. Those are close representation precedents; cooperative values/core allocations are not the costly-action CE region studied here.
* Papadimitriou–Roughgarden2008 and Jiang–Leyton-Brown2011 compact-CE optimality criteria from Phase15 also apply once lifted deviation-adjusted objective optimization is supplied. Thus a headline claim of a new CE optimization principle is unwarranted. The candidate increment is the explicit full-region local sensitivity formulation and resulting natural read-once/network class; its exact priority remains unresolved.

Four exact tests independently check every AND/OR binary tree on ordered distinct
leaves through n5, all profiles, leaf sensitivities and gate relations; sparse
rational reconstruction and all obedience statistics; zero-marginal branches/
single leaves; and the repeated-variable failure. These finite checks supplement
the induction/junction-tree proof, not replace it or establish novelty.
