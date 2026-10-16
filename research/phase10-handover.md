# Agent Games — initial campaign / Phase 10 handover

16 October 2026. Public repository: https://github.com/n-ham-research/agent-games .
Author Nicholas Ham. Working title retained: *Symmetry, Incentives and
Equilibrium Selection in Multi-Agent Systems*. All novelty remains provisional;
there is no external peer review, author sign-off or submission.

## Established project, preserved work

The author explicitly overrode the earlier feasibility recommendation and
authorized public repository creation. The repository was created and cloned
at /home/nick/Repositories/n-ham-research/agent-games. The local proposal's
feasibility.md, exact toy_models.py and README.md were imported verbatim under
research/origins/feasibility, with three SHA256 records and original paths.
The original local proposal is preserved unchanged. Its historical defer-
creation recommendation is retained, not presented as current authorization.

Research ownership is separate: game-symmetry at
e896a5cae79c5c63a81be16f1577bc365e67a5a6 owns structural lifting/binary
potential; game-fairness at f75ec9f7f0ff3b74226baed67a2727eccf0220d3 owns
utility, assignment and observation results. Neither companion was modified.
The observer-quotient and symmetry-identification proofs are referenced, not
claimed anew. Build script and preamble were adapted from the pinned fairness
infrastructure; no third-party PDF or generated build is tracked.

## Principal mathematical findings

### A. Allocation information is not ordered by symmetry information

With finite assignments, linear reward b_d(w) and an unknown capability vector
ranging over an unrestricted real linear class, exact optimal selection from
Lw is possible iff kerL annihilates every reward contrast b_d−b_e.
Consequently the minimum unrestricted scalar measurement rank is the contrast
rank. For bijective n×n assignment this is (n−1)^2, while a specified physical
agent-row swap test has rankn. At n2 the task needs fewer scalars; at n3 it
needs more, and the row spaces are incomparable. Joint n3 rank is5.

This is a standard estimability/assignment-geometry application, not a new
communication-complexity theorem. Positivity, boundedness, private row ownership,
finite messages and strategic reports change the model. Noisy regret is
bounded by the measured contrast's dual-norm sensitivity, with a sharp
DETERMINISTIC two-decision minimax proof. A direct-report witness shows
truthful data cannot simply be assumed in an incentive problem.

### B. Symmetry, mixed equilibrium and private coordination

A key correction to the initial possible conjecture: every finite game has
a mixed NE invariant under all exact automorphisms (classical Nash result).
The fixed-space BR proof also applies to cardinal groups; ordinal groups
need not preserve mixed NE. Thus the unrestricted mixed-existence obstruction
is not a new open problem. Pure, efficient or resource-constrained selection
remains different. Invariant lotteries exist classically; identical anonymous
local policies with only common public randomness cannot realize the efficient
anti-correlated device in the elementary witness.

The fully specified private-cost volunteer game gives four sharp values:

| Feasible solution/architecture | Expected calibrated welfare |
|---|---:|
| Unique symmetric behavioral Bayesian NE | 5/2 |
| Best identical local policies, unconstrained by incentives | 41/16 |
| Best labeled local policies + type-independent public randomness | 3 |
| Externally type-informed obedient private mediator | 13/4 |

The public-local bound holds even for non-equilibrium policies, by multilinearity
and all16 deterministic policy pairs. The informed mediator is ex-post efficient
and its recommendations are obedient even conditional on private type. It is
not a truthful direct mechanism when reports are unverified: low types gain
by exaggerating costs. The ex-ante swap, interim conditional problems and
asymmetric realized type profiles are kept distinct. This is an exact finite
architecture comparison with extensive Bayesian-correlation prior art, not
an originality-cleared new general theorem.

A finite Bayesian invariant-equilibrium argument is supplied separately under
positive type marginals and explicitly interim-best-response-preserving groups.
No normal-form existence or classification theorem is transferred without proof.

### C. Persistent state creates a cost only with specified task/actuator limits

For the C4→C2 carrier with calibration-sensitive task checkpoints and a fixed
+1 swap actuator, exact successful tracking costs c floor(T/2). A parity-aware
controller with both primary directions pays no corrections despite nonsplitting.
One bit of persistent memory suffices when role parity is otherwise unavailable;
role feedback supplies that bit for free. Priced reverse actuation gives
floor(T/2)min(c,d), and final-only checkpoints have periodic rather than linear
cost. A split extension still incurs positive cost under restricted actuators.
A regular finite-group checkpoint model has an explicit attained correction-
cost formula. These are operational control applications, not new splitting
or general communication theorems. They make the task relevance and architecture
of any positive cost explicit.

### Supporting incentive and learning controls

The preserved public-good model has potential-global selection that is poor
for welfare. A three-player positive coordination control has unbounded pure-
equilibrium PoA despite full ordinary symmetry. Both reviewers refuted root's
initial extension to n≥4: 0011 creates extra weak NE with zero welfare. The
failed generalization is retained and exactly tested. Strict unilateral
improvement, simultaneous best-response cycling and asynchronous log-linear
stationarity are distinguished; the Gibbs law is proved directly and checked
as an exact finite Markov chain. No arbitrary no-regret, convergence-rate or
LLM-rationality claim is made.

## Sources, scrutiny and publication assessment

The targeted review covers 2020 other-play, 2021 label-free coordination,
2022 decision-focused/neural-equilibrium work, 2023 equivariant-approximator
limits, 2025 game-symmetry computation/LLM surveys/benchmarks and 2026 official
community/workshop context. Actual proof-hypothesis comparisons and access gaps
are in literature-review.md. Especially important: Duan2023 already establishes
strong selection/welfare limits, and Tewolde2025 explicitly recalls invariant
mixed existence. Bayesian mediation and potential/log-linear methods are prior.
No broad “game theory for AI” novelty is asserted.

Root and two initially separate internal instances reviewed all principal
branches, with counterexamples and repairs recorded in reviews/AG-P1-REVIEW.md.
This is same-family internal criticism, not blind or external review. The
initial seven-page manuscript contains only scoped proved arguments and
established baselines; the full model qualifications remain in research.
It is a coherent foundation for pursuing the third paper, not a completed
originality-cleared paper. The original broad working title remains; the
information-constrained selection focus may determine a later title.

## Reproduce and next decision

Run import verification, unittest discovery, frozen feasibility script and
scripts/build.sh as in README. All 20 tests pass; all 3 frozen imports verify.
The manuscript builds without unresolved references or overfull boxes, and
all7 rendered pages were visually inspected. Native document tools were not
exposed, so the established local LaTeX build was used. A clean git-archive checkout independently passed the same 20 tests, all
3 import checks, the frozen feasibility script and the manuscript build
without ignored files or downloads.

The strongest next campaign should impose costed private communication,
verification or incentives on the volunteer architecture gap, compare the
exact result with volunteer-dilemma and information-design literature, and
seek a theorem that survives those natural constraints. Partial feedback and
costed state synchronization are a second lead; decentralized bounded-domain
allocation supports both. See open-questions.md for precise questions.

No Cortex/Gantry change, LLM experiment, external contact, authorship change,
funding inquiry or publication submission occurred. Research and review records
are public only through the explicitly authorized repository creation/push.
