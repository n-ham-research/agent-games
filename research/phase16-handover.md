# Phase 16 handover — adversarial audit and structural task classes

16 October2026. Nicholas Ham. Research proofs and exact checks are complete;
originality remains provisional and internal AI review is not external review.
The foundation manuscript and companion repositories remain unchanged.

## 1. Independent verification of P15-S4

phase16-hardness-audit.md reconstructs directly from pure utilities, with fresh
standard-library code importing no earlier game helpers. Separate resource and
root proof attacks verify all conditional rows, parity, preprocessing, encoding,
NP witnesses and approximation semantics. P15-S4 passes. Original cost set
{1/2,3/4}: optimum0 versus>=1/4. A meaningful strengthening now fixes EVERY
cost at1/2: optimum0 versus>=1/2. For every fixed conditional margin
0<=delta<=1/2, exact YES optimum is delta and NO optimum>=delta+1/2.
Pure backstop play remains feasible, so this is optimization hardness rather
than difficulty finding any equilibrium or any positive-margin law.

The NO certificate is a sum of the target work and backstop abstention rows.
Value accuracy<1/4 for the homogeneous variant is hard; approximately optimal
law output and approximate obedience have separate explicit thresholds in the
proof. General weak-obedience constants can approach1 by changing fixed costs,
but common-cost gap1/2 is optimal within this particular calibrated family,
not a claimed globally optimal reduction. Constant tuning is not prioritized.

## 2. Strongest prior comparisons and novelty judgment

The hardness note compares actual primary passages in Matsui–Matsui,
Papadimitriou–Roughgarden, Jiang–Leyton-Brown, Barman–Ligett and Ostroy–Song.
Voting relevance and generic optimal/approximate CE hardness are already known;
our backstop/CE transfer is short. No inspected theorem has been shown to state
the exact homogeneous fixed-margin single-payoff restriction, but that is not
priority clearance. It should not be promoted as a fundamentally new complexity
phenomenon or a substantial standalone theorem merely because its proof works.

Root checked Elkind et al. read-once MC-nets/series-parallel translations and
Wainwright–Jordan exact tree marginals. Disclosure found exact perfect-privacy
method overlap; substitution found exact observer/synthesis/INDEX overlap.
Branch notes give source versions, inspected locations and inaccessible-source
limits. The strongest prospective contribution is a coherent protected-region/
structural-class/boundary package, still requiring exact novelty scrutiny.

## 3. General structural tractability progress

P16-T1 in phase16-tractability.md supplies an O(n)-size full CE payoff/success
LP for binary read-once monotone AND/OR tasks, arbitrary rational costs and
conditional margin. Each node stores realized value and root sensitivity;
local constraints retain every worker's switching gain. Gate triple marginals
form an exact junction tree; sparse subtraction recovers O(n) support centrally.
This avoids exponentially many minimal winners. The new task-specific fact is
the small deviation-preserving lift, not a new junction-tree theorem.

The general supplied-width sufficient condition is explicitly standard-method
machinery. It charges construction and correct deviation/output bags; raw task
success width does not suffice. No necessary-and-sufficient tractability
classification or general bounded-treewidth task theorem is asserted.

## 4. New algorithms, separations and counterexamples

P16-T2 gives the read-once result for two-terminal series-parallel connectivity
with a supplied decomposition and one worker per edge. P16-T3 shows binary-
capacitated flow-threshold success is already payoff-hard on two vertices with
parallel edges, directly by the weighted-threshold theorem. Numerical input
and success semantics matter even on tiny underlying graphs.

Repeated-worker x AND x invalidates the naive sensitivity chain rule. This
refutes an encoding, not tractability of that redundant formula. Module/discovery
tests cover all distinct-leaf trees through n5 and direct rational reconstruction.
No LP optimizer is implemented, and no runtime measurement is asserted for one.

## 5. Substantive safe-disclosure investigation

phase16-disclosure.md proves strong NP-completeness of deterministic safe state
guessing for TWO fixed identical volunteers at required margin1/10 and a
uniform explicit prior. The undisclosed fixed recommendation law is already
obedient. Exact safety becomes balanced partitioning; 3-PARTITION gives the
hardness. This is not constant-gap approximation hardness and is not claimed
for weak obedience of the same law.

For scalar tight constraints, balanced pair columns give a transportation LP
for optimal randomized guessing. On the SAME instances randomized optimum is
3/4 whereas deterministic optimum is at most1/4. Perfect-privacy prior already
supplies the extreme-column principle, so only the restricted volunteer
embedding/operational boundary is a novelty candidate. Private refinement
cannot repair an unsafe FIXED joint recommendation/public law: averaging its
putatively safe refined obedience rows contradicts the negative original row.
Redesigning the law is outside that fixed-law impossibility.

## 6. Sequential resource-bounded substitution

phase16-substitution.md gives a complete support-observer existence criterion
and explicit bounded deterministic-adapter constraint certificate under an
observation-refinement architecture. Forward baselines use dK modes; reverse
replacement deviations use L modes, since rich observations can simulate the
sparse sensor without memory overhead. All hidden action/input paths and
permissions are included; default behavior is insufficient.

A sequential binary-output INDEX example has O(n) latent states per layer but
requires2^n sparse controller modes for exact behavior versus a one-mode rich
controller. This means n memory bits, not exponential bits. Trusted storage,
query channels and setup/update access are charged. Observer, bounded synthesis
and INDEX methods are primary prior; this useful operational contract does not
yet justify a separate original-mathematics manuscript.

## 7. Updated broad research map

phase16-assessment.md maintains coordination/incentives, information,
selection, learning, symmetry, robustness, sequential interchangeability and
foundational fairness/assignment. No convergence/decentralized selection result
is inferred from centralized CE feasibility. Canonical fairness calibration and
opportunity caveats remain essential; task automorphisms alone establish no
fairness principle or cheap private sampler. Both companion repositories remain
read-only at their previous pinned commits.

## 8. Ranking

1. Protected projection plus concrete read-once/network tractability and
   homogeneous robust payoff-hardness boundary, as a prospective PACKAGE.
2. Deterministic safe-disclosure hardness and randomized operational separation.
3. Existing circuit fine-precision and oracle zero-error symmetry restrictions,
   kept distinct from CE payoff optimization.
4. Resource contracts as engineering foundations with substantial exact prior.

This ranks significance and likely originality prospects, not journal readiness.

## 9. Dedicated manuscript recommendation

There is enough coherence to PLAN a focused paper on credible contribution-game
payoff computation. There is not yet enough novelty evidence to open another
manuscript or substantially expand the foundation paper. Prioritize the exact
protected-thinning and natural-class comparisons; the short classical relevance
transfer alone does not meet the requested ambition. No title commitment,
new repository/manuscript, submission, external contact or authorship change.

## 10. Next high-value questions

* Does protected thinning preserve a useful maximal payoff projection under
  materially broader incentives, with a characterization unavailable from
  ordinary CE LPs and known thinning?
* Which controlled repeated-worker formulas admit a constructed bounded-width
  deviation encoding, beyond the read-once class?
* What changes for safe disclosure with TWO independent tight incentive rows,
  beyond rank-two perfect-privacy transportation?
* Can approximate sensor replacement preserve budgeted deviations with a
  nontrivial tractable synthesis theorem, rather than another exact observer?
* Which specified decentralized selection/learning or calibrated assignment
  model turns a feasible payoff target into an implementable/fair procedure?

## Validation and delivery

All166 exact standard-library tests pass (139 previous +27 new) in both the
working tree and clean copy /tmp/ag-p16-clean-leane0fc. Both pass import
verification for all three frozen sources, the unchanged frozen toy models and
scripts/build.sh. Clean compilation produces the unchanged11-page manuscript.
git diff --check and README local-link checks pass. These tests corroborate
finite identities/constructions; they do not establish novelty or replace proofs.

Research commit8dfdf82 contains the proof/experiment work; a subsequent logical
integration commit contains this handover, assessment, reviews and ledgers.
Push result is reported after execution in the delivery message. Both companion
HEADs remain f75ec9f7f0ff3b74226baed67a2727eccf0220d3 and
e896a5cae79c5c63a81be16f1577bc365e67a5a6, with only their preexisting untracked
ZIP files. No paper/frozen-source/companion file changed.
