# Phase 15 handover — succinct tasks, disclosure and resource budgets

16 October2026. Nicholas Ham. Phase14 review implemented with three independently
developed branches and root reconstruction. Novelty remains provisional;
internal AI review and exact tests are not external verification. Manuscript
unchanged; both companion repositories unchanged.

## 1. Attempt beyond enumerated minimal winners

P15-S1 gives an exact terminal-summary flow formulation whenever the summary
retains all own-action deviation coefficients, not just success. It handles
correlations through actual source-terminal path flows. P15-S2 applies it to
integer-weight thresholds; P15-S3/root coverage applies it to small requirement
universes. Both represent the FULL expected payoff/reliability region, hence
all protected projections, without listing minimal winners.

Proofs: phase15-succinct.md and phase15-coverage.md. This is a rigorous successful
extension for two natural succinct classes; connectivity, arbitrary coverage,
graph dependencies/treewidth and arbitrary monotone circuits are not solved.

## 2. Algorithms and hardness

Threshold LP size O(n(W+1)²), W=sum weights: polynomial for unary weights and
unweighted thresholds, pseudopolynomial for binary weights. Coverage LP size
O(n9^d), d=universe size: FPT(d), heterogeneous costs allowed. Rational LP
provides exact optimization/membership and polynomial-support central law
reconstruction. Experiments construct/test DAGs and flows; no LP solver or
claimed runtime benchmark is implemented.

Binary weights already make one protected worker's zero-CE-payoff feasibility
NP-complete. P15-S4 distinguishes minimum payoff0 from >=1/4, with B1 and costs
only1/2,3/4. Thus additive payoff accuracy<1/8 is NP-hard; constant approximate-
obedience slack can also be allowed as specified in the note. Membership,
finding SOME minimal winner and finding SOME pure NE are easy in the gadget.
This is not hardness of finding any CE. Positive methods are established compact-
CE/DP adaptations; the natural single-payoff gap is the candidate increment.

## 3. Information-constrained continuation regions

phase15-information.md characterizes a prescribed literal-action/public-output
law by stochastic channel factorization plus conditional obedience. More private
mediator information can simulate less, with receivers' information fixed.
Safe public disclosures satisfy an exact cone of obedience inequalities.
Two strictly safe deterministic disclosures need not compose safely, so there
need not be a finest safe partition. Exact local posterior-odds bounds quantify
margin loss under a full residual-world likelihood-ratio restriction. These
extend the blind/private examples using established information methods.

Type-contingent plans are explicitly outside the literal-action factorization
lower bound. Public disclosure, private mediator knowledge and recommendation
randomness cannot be collapsed into one scalar information resource.

## 4. Resource-preserving substitution

phase15-resources.md supplies forward dK baseline compilation and reverse eL
all-deviation budget contracts with a checkable supplied all-action/mixed-interface
certificate. One-cut response channels require the appropriate-field nonnegative
rank in memory modes; that algebra is EXACT PRIOR Cohen–Rothblum1993 Thm3.2.
A repeat-read versus sparse-read example has optimal success min(1,MQ/N), with
M modes and a Q-value trusted stored message, and a matching implementation.
N=2^k modes means k bits, not exponential bits. CPU, program size, repeated
access, external storage and output bits are distinct resources. This is not
an unrestricted new strategic-equivalence or controller-synthesis theorem.

## 5. Counterexamples and retained failures

Coverage bits omit pivotality; component partitions omit bridges. Individually
safe public releases can expose failure jointly. Perfect type privacy can leak
the sampled coalition and destroy obedience. Type-dependent local plans can
implement outcomes impossible for blind literal recommendations. Perfect recall
can hide a required finite-controller memory increase. Matrix ordinary rank
need not equal nonnegative rank. The NO payoff bound is not always attained.
Details and exact tests are in branch notes and AG-P15-REVIEW.md.

## 6. Targeted novelty comparisons

phase15-literature.md and branch notes compare compact CE (Papadimitriou–
Roughgarden; Jiang–Leyton-Brown), aggregative DP/hardness (Barman–Ligett),
weighted-voting relevance/DP (Matsui–Matsui), least-core network LPs (Tanaka–
Matsui), BCE/Blackwell information orders, privacy/incentive methods, finite-
memory games and exact stochastic factorization. Positive algorithmic machinery
and factorization algebra are credited as prior. P14-A protected projection and
P15-S4 precise natural-class gap still require deeper exact overlap checking.
Cavaliere2001 final endpoint retry failed; the2000 working body remains the
actual inspected text, and new mathematics was not blocked on it.

## 7. Refreshed broad map

phase15-assessment.md covers eight themes: coordination, information,
selection/learning, symmetry/computation, robustness, sequential systems,
interchangeability and foundational fairness/assignment. Canonical calibrated
symmetry averaging gives useful feasible invariant payoff targets, but neither
equal payoffs nor automorphisms define fairness. No companion changes.
P13-Q circuit fine precision and P14-Q oracle constant-accuracy zero-error
remain distinct; the new CE payoff-optimization hardness does not conflate them.

## 8. Ranking

First: protected normal form plus natural succinct representation/payoff boundary.
Second: information-constrained credibility and disclosure. Third: existing
precision/oracle symmetry restrictions. Fourth: resource contracts as a promising
but heavily prior-method branch. Ranking concerns significance and originality
prospects, not publication readiness. No new facet/dimension classification or
general decentralized implementation theorem is claimed.

## 9. Eventual paper structure

Keep the current foundation paper conservative. A focused contribution-game
payoff-region paper is the leading prospect if exact novelty checking succeeds;
include information constraints only if they strengthen its central question.
Resource substitution remains an independent programme until it yields a
substantial theorem beyond established composition/factorization/coding. Do not
split papers merely to package branches. No submission, external contact or
authorship change performed.

## Verification and repository delivery

All139 exact standard-library tests pass in the working tree and clean copy
/tmp/ag-p15-clean-fhl25yse (111 previous +28 new). Both copies pass frozen-import
verification, the unchanged frozen toy models and scripts/build.sh; the clean
build produces the unchanged11-page manuscript. git diff --check passes.
No general LP optimizer is implemented; these tests corroborate formulas and
construction identities rather than certify novelty or replace proofs.

Research commit: 25aaced. This handover, rankings, literature/review records and
ledgers are delivered in a separate integration commit on main. Push outcome
is reported in the delivery message after execution. Companion HEADs remain
f75ec9f7f0ff3b74226baed67a2727eccf0220d3 and
e896a5cae79c5c63a81be16f1577bc365e67a5a6, with only their preexisting untracked
ZIP files. No paper source, frozen import or companion file was changed.
