# Phase 15 — coverage without minimal-winner enumeration

16 October 2026. Nicholas Ham; root Codex development. P15-S3-C is a proved
candidate application of established compact-CE/flow methods, not a new general
linear-programming or dynamic-programming principle. Independent resource-branch proof reconstruction passed; see AG-P15-REVIEW.md.

## Model and statement

There are n binary workers, a nonempty universe U of d requirements, sets
S_i subset U, rational B>0 and 0<c_i<B. Success means the active workers cover
U. Assume the union covers U. Complete information, private recommendations,
central mediator; no communication-free implementation is asserted. Fix rational
conditional obedience margin delta>=0 (delta=0 gives CE).

**P15-S3-C.** The full expected-utility/success region of delta-obedient laws admits
an exact rational extended LP with O(n 9^d) variables and constraints plus 2n
obedience inequalities and n+1 output equations. Consequently exact membership
and linear optimization, including any protected payoff projection or rational
linear calibrated allocation requirement, are FPT in d, with time
9^{O(d)} poly(n,L), allowing polynomial factors in d. This charges the explicit
set incidences and rational bit length L. It does not require enumerating minimal
covers, does not bound d by the protected-set size, and does not assert novelty
clearance. Empty feasible regions for positive delta are permitted.

## Construction and proof

For each active set A define z_e=min(2,|{i in A:e in S_i}|), so z lies in
{0,1,2}^d. Split the distribution by this FINAL count vector z. For each z use
an ordered layered DAG: layer i records the capped counts of the first i workers.
A binary edge at worker i adds S_i if its action is work, capping at 2. Its
source is the zero vector and its sole permitted terminal is z. Nonnegative
edge flows obey conservation, with total mass q_z entering and leaving this
DAG; sum_z q_z=1. There are at most 3^d states per layer and 3^d DAGs.
Dead states may be omitted; they do not increase the bound.

Every law induces these flows. Conversely, finite acyclic flow decomposition
writes each DAG flow as a nonnegative sum of source-terminal paths. Each path
is one active set, with exactly final z. Thus the formulation is exact, rather
than a relaxation that only matches independently specified marginal counts.

Let s(z)=1 iff all z_e>0. For an edge at i with action a, utility is
B s(z)-c_i a. If a=1, i is pivotal precisely when s(z)=1 and some e in S_i has
z_e=1. Its obey-minus-deviate coefficient is B times that indicator minus c_i.
If a=0, switching repairs failure precisely when s(z)=0 and every zero-count
element belongs to S_i. Its coefficient is c_i minus B times that indicator.
Subtract delta on every edge before summing each action's row. Nonnegativity
of these 2n sums is EXACTLY the unconditional form of conditional-margin
obedience, including vacuous zero-probability signals. Utility and success
outputs are also linear in flows. This proves both inclusions and the size bound.
Rational LP bit complexity gives the algorithmic corollary.

A greedy path decomposition removes at least one positive edge on each extraction,
so obtains at most as many support profiles as positive edges, with polynomial
rational arithmetic and bit growth in the LP solution encoding. This gives a
central exact recommendation law and sampler; it is not an implementation of an
LP solver in the experiment. No protected-thinning margin restriction is needed:
this construction represents original laws without modifying their actions.

## Consequence and limitation that matter

Merely tracking the covered subset is insufficient: one and two workers both
covering the only requirement have identical coverage but different work
incentives. Capping multiplicity at TWO retains the needed pivotal information.
Two workers per disjoint requirement already give 2^d minimal covers. The LP
avoids enumerating covers and handles arbitrary heterogeneous costs and all
payoff coordinates. Its exponential dependence on d is substantive.

For network reliability, coverage of edges/vertices is not s-t connectivity.
A connectivity partition alone does not tell whether a selected edge is a
bridge: a path and a triangle are both connected, while deleting a given edge
can disconnect only the path. The coverage theorem therefore supplies no
unproved bounded-treewidth connectivity algorithm. Graph/circuit treewidth is
not an automatic bound on the information needed for ALL unilateral deviations.

## Prior and verification

Papadimitriou–Roughgarden, January 2008 author version,
[Computing Correlated Equilibria in Multi-Player Games](https://timroughgarden.org/papers/cor.pdf),
abstract and introduction inspected this phase: compact CE existence computation
and optimal-CE tractable subclasses predate this work. Anonymous-game and
bounded-treewidth results are established, not new claims here.

Jiang–Leyton-Brown, 2011 WINE extended abstract,
[A General Framework for Computing Optimal Correlated Equilibria in Compact Games](https://www.cs.ubc.ca/~kevinlb/papers/2011-WINE-OptimalCorrelated.pdf),
§3 Proposition 1 and §4.1 inspected: deviation-adjusted welfare optimization
suffices for optimal CE. Here fixing z makes that objective edge-additive and
DAG-optimizable, so tractability also follows from their framework. Our explicit
flow construction adds a direct primal formulation and reconstruction, without
claiming this general method is original. No coverage-specific priority is
asserted without a deeper literature search.

Exact tests check every ordered triple of subsets of a two-element universe,
all action profiles and all deviations, arbitrary rational costs/margin, flow
reconstruction statistics, exponential-cover and insufficient-mask witnesses.
These finite checks support the identities; the proof establishes generality.
Code: experiments/phase15_coverage.py; four tests in test_phase15_coverage.py.
No LP optimization implementation or external verification is claimed.
