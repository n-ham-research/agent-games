# Allocation information and structural identification

16 October 2026. Proved elementary candidates AG-A1–AG-A5; novelty unclaimed.
This note specializes linear algebra and finite decision theory to allocation.
It does not claim a new general principle of decision-focused prediction.
Author: Nicholas Ham; initial derivation and exact checks: Codex allocation agent.
Independent review status is recorded by the integrating researcher.

## Model and provenance

A coordinator receives truthful, externally measured data before allocating.
The unknown capability parameter is w in a finite-dimensional **real vector
space** W, without positivity, boundedness or prior restrictions. There is a
nonempty finite set D of feasible assignments. Assignment d has known linear
reward b_d(w); the coordinator maximizes that single disclosed objective.
There is no strategic reporting, decentralization or learning. An observation
is the exact vector Lw, for a fixed linear map L. A selector may use arbitrary
computation and a fixed tie order. No welfare or fairness interpretation follows
without separately specifying receipts and stakeholders.

For comparison let T:W→U be a fixed linear structural discrepancy: the property
to identify is Tw=0. For a canonical typed-game automorphism this is D_g|_W;
Game Fairness Phase 9 owns the symmetry kernel criterion. The frozen feasibility
pin is bcf8bfcbd185962576b78a4ccd729e361231dea9; that pin precedes Phase 9, so
it is not used as a source pin for the later criterion. The current owner is
`game-fairness/research/phase9-identification-and-stability.md`, P9-I1,
at commit f75ec9f7f0ff3b74226baed67a2727eccf0220d3.
This note compares a different task kernel, rather than reproducing that
canonical symmetry-identification proof.

## AG-A1: exact allocation information on a full linear class

Fix d0 and let B:W→R^(|D|−1) have rows b_d−b_d0. The following are equivalent:

1. A deterministic rule s(Lw) is optimal at every w in W.
2. ker L is contained in ker B.
3. Every reward contrast factors through L.

Consequently the minimum number of unrestricted, nonadaptive real scalar
linear measurements is rank B. It is the dimension of the affine span of the
reward functionals, rather than the dimension of W.

**Proof.** Given t in ker L, s(0)=d* must be optimal at both t and −t. For every
d this gives b_d*(t)≥b_d(t) and b_d*(t)≤b_d(t), so all rewards agree on t.
Thus Bt=0. Conversely the kernel inclusion makes B constant on every L-fiber;
recover those contrasts and maximize them. Linear factorization follows by
well-definedness on im L, followed by extension to the observation codomain.
The kernel inclusion implies rank L≥rank B, and taking L=B attains equality. ∎

The same necessity holds for randomized rules that are optimal almost surely,
or have exactly the full-information expected reward at every w: every action
in the fixed support at observation zero must maximize at both t and −t.

For a restricted domain C⊂W, the correct general condition is instead

    intersection { argmax_d b_d(w) : w∈C, Lw=y } ≠ empty

for every attainable observation y. This follows directly by choosing one
common maximizer per fiber. The full-space rank theorem fails on a positive
orthant: b0=0,b1(w)=w with w≥0 needs no observation, although rank B=1.
Affine rewards also need separate treatment: b0=0,b1=1 on W have a constant
optimal action, while homogenization followed by the unrestricted-space
argument is invalid because the homogenizing coordinate is fixed at 1.

## AG-A2: when task information is smaller, larger or incomparable

Write R_B and R_T for the row spaces in W*. The minimum scalar ranks for task
allocation and structural testing are rank B and rank T, respectively.
A task-minimal observation B also identifies structure exactly when
R_T⊂R_B; structural measurements T suffice for allocation exactly when
R_B⊂R_T. The two tasks admit the same sufficient-observation class exactly
when their row spaces agree. Equal ranks alone do not imply this. A single
observation sufficient for both needs minimum rank dim(R_B+R_T), attained by
stacking B and T. These are direct consequences of AG-A1 and the canonical
structural criterion. No universal information ordering holds.

### A natural assignment calculation

Let n agents fill n fixed tasks bijectively, with arbitrary real completion
scores C_ij. The score of permutation π is sum_i C_i,π(i). Measurements may be
arbitrary linear combinations of this matrix. Exact optimal assignment requires
precisely **(n−1)^2** scalar linear measurements, for n≥2.

**Proof.** All permutation differences have zero row and column sums. Their
span equals that subspace: for any i,j<n, choose two permutations that differ
only by assigning rows i,n to columns j,n in opposite ways, extending the
remaining bijection arbitrarily. Their difference is the rectangle
E_ij−E_i,n−E_n,j+E_n,n. These (n−1)^2 rectangles are independent and span the
zero-margin subspace. Apply AG-A1. Equivalently, use the measurements
z_ij=C_ij−C_i,n−C_n,j+C_n,n. If two matrices have equal z, their difference
has form r_i+c_j, adding the same total to every bijection. ∎

This is familiar assignment-polytope geometry, not a novel dimension theorem.
It also shows that linear measurements sufficient for all optimal decisions
identify all assignment score differences, including nonwinning comparisons.
This stronger consequence depends on the unrestricted real parameter domain.

Compare **physical row interchangeability** of agents 1 and 2 with tasks held
fixed: T(C)=(C_1j−C_2j)_j has rank n. This is a capability-array symmetry test,
not an assertion about a complete normal-form game's actual automorphism group.
For n=2 allocation rank 1 is smaller than interchangeability rank 2. For n=3
allocation rank 4 is larger than rank 3. Moreover, within n=3 the measurement
tasks are incomparable:

* C=0 and C with row 1 identically 1 and all other rows zero have equal B
  (all assignments tie), but different interchangeability status.
* C+ has only C_31=1 and C−=−C+. Both have T=0. Every optimal assignment at
  C+ assigns agent 3 to task 1; every optimum at C− avoids that assignment.
  Their optimum sets are disjoint, so T cannot support exact allocation.

Here the common row-space dimension is 2 (row-difference vectors whose
column coefficients sum to zero), so joint allocation and swap testing require
4+3−2=5 scalar measurements, not the sum 7.

Thus even symmetric-looking role data need not suffice for task decisions, and
optimal allocation may ignore structural differences that add assignment-wide
constants. For all-row interchangeability the discrepancy has rank n(n−1),
which exceeds (n−1)^2. These comparisons concern a specified symmetry test;
identifying the entire symmetry group is a further task.

## AG-A3: bounded noise and a sharp two-decision bound

Assume exact task sufficiency and remove redundant observation coordinates,
so L maps onto R^m. Choose vectors a_d with
b_d−b_d0=a_d L and a_d0=0. Observe y=Lw+e with ||e||≤ε in a disclosed norm,
and maximize a_d·y. If d* is a true optimum and d̂ is selected, then

    b_d*(w)−b_d̂(w) ≤ ε ||a_d*−a_d̂||_* ≤ ε K,
    K=max_{d,e} ||a_d−a_e||_*.

**Proof.** Observed optimality gives (a_d*−a_d̂)·y≤0. Substitute Lw=y−e
and use the dual-norm inequality. ∎

This is a deterministic worst-case guarantee, without a distribution, sample
size claim or statistical confidence statement. A margin greater than εK
between the true best and all alternatives guarantees correct selection.
The bound uses contrast sensitivity; small singular values can make K large.

For two actions it is the **exact deterministic minimax worst-case regret**
over the full W and ||e||≤ε. Let c=a_1−a_0. Compactness of the finite-dimensional
unit ball supplies z with ||z||≤1 and c·z=||c||_*. At observation y=0 both
Lw=+εz and Lw=−εz are possible. Whatever action the deterministic rule selects,
one of these states has regret ε||c||_*. The bound above attains it. If randomized
selection is allowed and expected regret is measured, fair randomization at the
tie changes this lower-bound argument; the deterministic minimax value must not
be silently transferred to that setting.

If ker L is not contained in ker B, deterministic worst-case regret is unbounded
already with noiseless data: at observation zero, pick a kernel direction on
which some contrast with the selected action is nonzero, choose its sign and
scale arbitrarily. On bounded capability sets this conclusion need not hold;
use the fiber criterion or a restricted robust optimization problem instead.

## AG-A4: scalar rank is not communication complexity

The preceding rank lower bounds apply to **fixed linear real measurements**.
They are not bit lower bounds. One real coordinate has unlimited precision;
fixed measurement counts, adaptive comparisons, sample sizes and message
lengths are different resources.

With an informed centralized sender and unrestricted deterministic messages,
a finite decision set needs at most |D| messages: send one selected maximizer.
For bijective assignment every permutation is the unique maximizer of some
matrix (put 1 on its entries and 0 elsewhere), so distinct such matrices must
receive distinct messages whenever their optimal permutations differ. Thus
exact one-way communication needs exactly n! messages, or ceil(log2(n!)) bits
with fixed-length binary messages. This model lets the sender solve allocation;
it says nothing about decentralized agents each knowing one row, privacy,
computational cost or learning. Arbitrary real encodings also defeat any
unqualified rank-based information lower bound.

## AG-A5: truthful observation is a substantive assumption

In a two-agent, one-task direct-report model with capability types t_i∈{0,1},
let the coordinator maximize reported capability, breaking a reported tie by a
fair lottery. If each agent values receiving the task at 1 regardless of its
capability, and transfers or verification are absent, truthful reporting is
not a Bayesian Nash equilibrium for independent fair binary types. Type 0
gets assignment probability 1/4 by reporting 0 and 3/4 by reporting 1.
The rank/fiber theorems therefore do not establish incentive compatibility.
If instead the agent's receipt is 1 only when assigned and genuinely capable,
type 0 is indifferent: changing utilities changes the strategic conclusion.
No generic mechanism-design impossibility follows from this tiny witness.

## Primary-source comparisons and novelty limits

The following original article bodies were opened on 16 October 2026.

* Elmachtoub, Liang and McNellis, ICML 2020,
  [Decision Trees for Decision-Making under the Predict-then-Optimize Framework](https://proceedings.mlr.press/v119/elmachtoub20a.html),
  original PMLR PDF. Its model learns uncertain objective parameters from data
  and evaluates downstream decisions. This already separates prediction quality
  from decision quality; our fixed linear observation model supplies no learning
  guarantee or empirical improvement over it.
* Mandi, Bucarey, Mulamba and Guns, ICML 2022,
  [Decision-Focused Learning: Through the Lens of Learning to Rank](https://proceedings.mlr.press/v162/mandi22a.html),
  original PDF pp.1–3 inspected. Its finite feasible solutions and parameterized
  objectives closely overlap the decision skeleton. It develops ranking-based
  training losses with historical features/data, while our theorem assumes
  noiseless linear measurements on every point of a full vector space. Ranking
  and preserving objective differences are therefore established ideas.
* Elmachtoub and Grigas,
  [Smart “Predict, then Optimize”](https://optimization-online.org/wp-content/uploads/2018/12/6398.pdf),
  author preprint (2018 URL; published Management Science 68(1),2022).
  The opening model and decision-error objective were inspected. It is a major
  prior baseline for regret from predicted linear costs. Our elementary
  dual-norm noise bound is not claimed as a new regret principle.

No 2020–2026 source search establishes absence of this exact rank statement.
The full-space theorem and assignment calculation are elementary applications;
the comparison with a separately specified structural discrepancy is a useful
cross-project formulation with provisional originality at most. Neither this
note nor its tests establish a novel AI-agent theorem. More promising open
questions impose decentralized row ownership, finite-bit communication,
strategic reports, bounded nonnegative scores or privacy constraints; these
change the information problem substantially and need their own prior-art audit.
