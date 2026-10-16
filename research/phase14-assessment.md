# Phase 14 — ranking and an updated research map

16 October2026. Nicholas Ham. Open exploration and focused proof development
remain distinct modes. The current11-page manuscript is unchanged. Proofs,
resource models and actual independent reviews are in the three Phase14 notes.
No candidate is novelty-cleared or externally reviewed.

## Ranked contributions

| Rank | Result | Significance and originality prospects |
|---|---|---|
| 1 | P14-A: exact protected CE payoff projection and FPT(k) computation from minimal-winning hypergraphs | Strongest positive structural/algorithmic result. Handles all simultaneous protected payoff targets and reliability. Thinning/CE LPs have close prior; the protected normal form and representation consequence merit targeted overlap checking. |
| 2 | P14-B: sharp cost-blind payoff envelope with conditional obedience margins | A precise bridge from complete-information punishment to a genuinely restricted-information model. Endpoint inequalities are standard; simultaneous all-type attainment and hidden-cell counterexample are the task-specific candidate increment. |
| 3 | P14-Q: constant-accuracy two-orbit deterministic/zero-error query barrier | Strong unconditional boundary, permitting constant approximate invariance. The broad adversary/randomization method is established; the symmetry restriction is the possible addition. This is NOT explicit-circuit coarse-accuracy hardness. |
| 4 | P14-I: contextual finite-state preservation certificate and limits | Useful rigorous model, many-to-one aggregation and all-deviation transport. Core bisimulation, Kuhn realization and coupling are prior; not presently a new general equivalence theorem. Its stronger research opportunity is resource-preserving substitution. |

Ranking is a research judgment, not a claim that rank1 is publication-ready.
The first two can form one coherent continuation/information narrative; the
query theorem remains a competing computational contribution. The contextual
branch warrants continued development only where it improves on mature theory.

## Research map after actual proofs

**Coordination and incentives.** Move from one zero-payoff face to exact projected
payoff regions. Protect k agents while removing unprotected wasted work; this
preserves all protected utilities and success and gives only(m+1)2^k columns.
Next precise question: can an analogous formulation avoid explicit enumeration
of minimal winners for a meaningful network/coverage representation? A membership
oracle alone is not an uncharged enumeration algorithm. A second gap is
positive-margin/private-signal payoff regions when knowledge varies by player.
Do not assume the cost-blind envelope applies in each hidden signal cell.

**Information and robustness.** Blind recommendations are a well-defined extreme,
not a synonym for all uninformed mechanisms. Private pooling can lower a type's
payoff below a cellwise singleton-security bound; publicly disclosing the cell
changes obedience. Next investigate a specified small information partition or
a precise disclosure channel, with endogenous reporting checked separately.
The margin delta is a conditional gain requirement, not additive regret or a
behavioral model guaranteeing that a noisy agent obeys.

**Symmetry and computation.** Ordinary accuracy does not remove every information
barrier: zero-error black-box algorithms can need exponentially many queries
where high-confidence Monte Carlo succeeds with polynomial queries. The
input distinction is central. A next result should either establish a genuinely
new succinct-input algorithm/lower bound or exploit additional verifiable
structure for a deterministic stopping certificate. Merely rephrasing the
oracle theorem as circuit hardness would be incorrect.

**Sequential interchangeability.** P14-I supplies a foundation with permitted
contexts, observations, action menus, retained utilities, private memory and
resource logs. A useful next objective is a necessary-and-sufficient or weaker
checkable certificate for a fixed bounded-memory software context class.
Perfect-recall realization can preserve strategic laws while increasing memory
or computation; that gap is a substantive target. The fixed default trace,
individual observation marginals and matching component initial marginals are
each insufficient for the stronger substitution claim.

**Learning and selection.** Current results preserve NE/approximate regret or
characterize CE recommendations; they do not select a unique outcome or prove
learning convergence to the intended law. Studying which protected payoff
targets can be reached by a specified finite-memory learning rule remains an
independent route. Do not attach an unproved learning claim to the FPT LP.

**Foundational fairness.** Retain the read-only Phase13 F1–F4 agenda: independently
motivated opportunity equivalence, cross-role calibration, ordered/unordered
opponents and impartial decision principles. P14-I makes a relevant distinction:
state aggregation with payoff/deviation transport is a model-relative strategic
preservation property, not subjective assignment indifference or a moral
fairness criterion. P14-A preserves a chosen utility projection without making
the agents interchangeable. Neither theorem justifies relabeling an automorphism
condition as fairness. Canonical U1/U5/A1/P7-A and Game Symmetry matching/splitting
results remain pinned to their companion commits; neither repository is edited.

## Counterexamples that changed the programme

* Protected thinning preserves ordinary CE but can destroy a positive margin
  if a removed worker's cost is smaller than delta. The exact bound on delta
  is substantive, not a decorative regularity condition.
* Individual designated-worker minima need not conflict: mixed play can attain
  both volunteers' security minima. Simultaneous feasibility requires the
  protected-region constraints, not intuition from pure selections.
* A privately type-informed mediator can pool singleton obedience across cells;
  the unconditional success floor cannot be imposed separately in each cell.
* Behavioral/default-trace equality omits tools/permissions and private signals.
  Equal individual signal marginals do not preserve their joint correlation.
  Matching initial component marginals does not preserve correlations with a
  context's private input. Utility must factor through retained records.
* Erasing a private random seed under perfect recall does not preserve a
  memoryless-controller resource constraint.
* The query lower bound cannot be recast as an explicit-circuit lower bound;
  Monte Carlo confidence and zero-error correctness are different guarantees.

## Source and publication decision

The Cavaliere source gap has advanced to actual primary working-body inspection,
with exact preprint inconsistencies recorded rather than accepted as theorems.
The2001 final text remains uninspected. General payoff-polytope, persuasion,
query and bisimulation literatures are close prior, with versions/locations
recorded in phase14-literature.md and branch notes.

Keep one foundation manuscript unchanged. Do not create another paper merely
because three branches have proofs. Before a manuscript promotion, compare
P14-A's exact projection and hypergraph FPT consequence with the strongest
compact-CE and public-good results, then decide whether the structural theorem
supports a genuinely useful paper. If the originality survives, a continuation/
information/computation paper is more coherent than collecting every result.
The separate oracle theorem needs its own significance assessment; the contextual
framework currently supports further exploration rather than a standalone
novelty claim. No publication readiness or external sign-off is asserted.
