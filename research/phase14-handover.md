# Agent Games Phase 14 handover

16 October2026. Nicholas Ham. Baselinebd2e7d0. Three serious competing branches,
separate development, reciprocal attacks and root reconstruction. No external
peer review, novelty clearance or author sign-off. No new manuscript/repository,
external contact, authorship change or submission.

## 1. General continuation-payoff regions

**P14-A** is the strongest positive candidate. For any monotone contribution
task with known positive costs below B, protect a set J of k agents and delete
only unprotected work while preserving success. This preserves their entire
payoff vector exactly, weakly raises other payoffs and preserves CE. Success
is also unchanged. The exact projected (success,protected-payoff) region has
at most(m+1)2^k canonical coalition columns, where m counts minimal winners.
It handles simultaneous targets and arbitrary positive continuation levels,
not just one agent's zero face. It is NOT a representation of the full payoff
vector unless every agent is protected. Conditional delta-obedience is preserved
only under the stated bound on removed workers' costs.

An explicitly listed minimal-winning hypergraph therefore gives a genuine
2^{O(k)}poly(n,m,L) exact rational LP construction/optimization algorithm.
Individual minimum credible CE payoffs are polynomial-time computable in that
representation. There is no uncharged enumeration of an implicit winner family;
the general LP solver is invoked, not implemented or benchmarked. A canonical
LP constructor and exact small-instance row checks are supplied.
Proof, algorithm, bit/sampler scope: phase14-continuations.md.

**P14-B** gives sharp payoff envelopes under a genuinely information-restricted
architecture: a mediator's recommendation law is independent of all costs and
messages. Highest costs govern work IC and lowest costs govern abstention IC.
In the stated no-pair-repairer coalition class, the payoff envelope is attained
simultaneously for every target type, including positive conditional margins.
It includes a closed form for positive minimum complete-information payoff.
A privately type-informed mediator can defeat cellwise application of the
blind bound by pooling other agents' obedience. This is not truthful revelation
or an arbitrary post-audit private-type mechanism theorem.

## 2. Symmetry-constrained complexity progress

**P14-Q** reaches constant Nash error and constant approximate invariance in
a PURE-PAYOFF ORACLE model. Player-transitive cyclic binary games have actual
full action-orbit count2. Deterministic and randomized zero-error algorithms
require exponentially many queries; high-confidence Monte Carlo is polynomial.
The lower bound even permits an oracle returning all pointed deviation payoffs.
An inverse-polynomial-accuracy variant has a near-full-table query bound.
This is unconditional query complexity, not new explicit-circuit computational
hardness. The oracle hides an arbitrary Boolean table. The finite-family
random-tape proof justifies the zero-error claim and does not prove a Monte
Carlo lower bound. Approximate invariance is global orbit diameter, not a small
error under just the supplied generator. Complete full-group generators are
not supplied. P13-Q's exact invariant-output/fine-precision circuit result is
preserved unchanged. See phase14-complexity.md.

## 3. Formal contextual agent-interchangeability model

The model has finite operational state, input ports, joint actions, private
observations, public outputs, retained reward/resource labels, finite horizon
and perfect-recall observation/action-history strategies. Contexts cannot read
discarded state or change menus invisibly. Behavioral, strategic, utility,
contextual and computational comparisons are model-relative; no hierarchy is
asserted.

**P14-I1** gives a many-to-one stochastic quotient certificate preserving the
joint private-observation/interface law for EVERY legal joint action/input.
It preserves all contextual record laws, all unilateral deviations, utilities,
regrets and NE/approximate NE. Utilities must factor through retained records;
the complete retained initial joint law includes context/private-input
correlations. **I2** transports independent persistent private randomization
under perfect recall against all opponent choices. It does not promise equal
memory or computation. **I3** gives row-TV-to-record-TV and the sharp factor2
payoff-error-to-regret bound. Counterexamples cover lost private information,
matching marginals but different signal correlation, extra permissions,
initialization correlation and bounded-memory failure.
These are established bisimulation/Kuhn/coupling adaptations with explicit
operational scope, not a new universal equivalence theory. Sources and exact
certification/sampling costs: phase14-interchangeability.md.

## 4. Targeted novelty comparisons

Root found and inspected the primary Cavaliere February2000 working paper,
including rendered model/proposition equations. This advances the previously
unresolved source gap; the published2001 full body remains uninspected. Several
working-text claims need qualification and are checked locally rather than
imported as valid general lemmas. No assertion about corrections in the unseen
published text is made. Source version, SHA256 and theorem-level comparison
are in phase14-literature.md. Current CE-payoff geometry literature was also
inspected during the broader search.

P14-A's protected projection/FPT consequence is the main increment to scrutinize;
CE LPs/thinning are prior. P14-B's endpoint reasoning is standard, with attained
information/margin consequences the candidate extra content. Hart–Nisan already
supplies the query adversary/randomization principle. Probabilistic quotients,
strategy-compatible Nash preservation and perfect-recall realization are mature
prior. No candidate has originality clearance.

## 5. Exact evidence and adversarial review

111 standard-library exact tests pass:82 retained,10 continuation,7 complexity,
9 interchangeability and3 root source/initialization checks. Separate branches
reciprocally reconstructed the proofs; the FPT corollary received an additional
explicit review. Root independently checked each main proof and discovered an
initial-joint-law assumption that is now explicit. A reviewer similarly required
utility factorization through retained records. Full actual review and finite
completeness limits: ../reviews/AG-P14-REVIEW.md.

No test collection establishes external validity or novelty. Finite checks do
not enumerate all CE, all stochastic contexts or all oracle algorithms; general
proofs supply those conclusions. No general LP/Nash solver or LLM experiment
was run. Canonical mathematical/algorithmic artifacts and exact fixtures are
preserved.

## 6. Updated research map, ranking and next phase

phase14-assessment.md updates coordination, information, incentives, symmetry,
learning, sequential systems and the read-only foundational fairness connection.
Rank1: protected continuation region/FPT theorem. Rank2: sharp information/margin
payoff envelopes. Rank3: strong-symmetry zero-error query restriction. Rank4:
contextual substitution as a useful but prior-heavy foundation.

Next pursue one of two substantive gaps: protected regions from a useful succinct
winner representation without listing minimal coalitions, or bounded-memory/
resource-preserving contextual substitution with a weaker checkable certificate.
Specified partial disclosure and positive-margin continuation regions are a
competing information-design lead. Keep the oracle result separate from circuit
claims. Do not require every future theorem to extend these constructions.

Foundational fairness remains an independent agenda: opportunity equivalence,
cross-role calibration, opponent information and impartiality. Strategic
substitution is not subjective assignment indifference, and preserving selected
utilities does not make agents interchangeable. Canonical Game Fairness U1/U5,
A1 and P7-A ownership and exact companion pins remain unchanged.

Keep one11-page foundation manuscript, unchanged this phase. No result is added
merely because it has an internal proof. Further exact closest-prior comparison
is required before promotion; a possible continuation/information/computation
paper should follow the contribution, not the number of branches. No separate
paper or publication-ready claim is made.

## Reproduction and repository boundaries

Local and clean-copy checks:111 tests, all3 frozen-import hashes, unchanged frozen
toy script, manuscript build and whitespace checks. The clean copy includes
only tracked/nonignored candidate files; no third-party download is required.
The manuscript remains11 pages with no source/layout change this phase.

Game Fairness remains f75ec9f7f0ff3b74226baed67a2727eccf0220d3 with preexisting
game-fairness.zip; Game Symmetry remains
e896a5cae79c5c63a81be16f1577bc365e67a5a6 with preexisting games-symmetry.zip.
Original/frozen proposals, Cortex and Gantry are unchanged. Verified work is
committed/pushed in logical units under the user's explicit instruction.
