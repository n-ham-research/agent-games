# Actual Phase 12 review and corrections

16 October 2026. Two separate same-family Codex branches developed compact
representations and selective verification. Root developed the reliability
capacity extension, reconstructed the branch proofs and integrated sources.
Each branch independently attacked the other's proofs after initial development.
The compact branch reconstructed V12-C (including closed form and attainment)
from root/verification draft; verification independently reconstructed P12-C1/C2
and checked the decomposable C3 bit-height reasoning. Root read both full notes,
checked the typed quarter-turn, regret/TV extraction, audit coupling and voluntary
action continuations. No proof defect was found in the final stated candidates.
This is internal AI review, not external mathematical review or author sign-off.

## Actual narrowing and repairs

* Closest-prior search found Schoenebeck–Vadhan2006 already has counting-output
  Nash hardness using the same gadget principle. The claimed possible addition
  was narrowed to the three-action-orbit symmetry refinement.
* Ben-Porath–Dekel–Lipman2014 already has the key reduced-form audit inequality.
  The one-worker formula was classified as an adaptation, not a new principle.
* Arbitrary threshold extrapolation of the one-worker formula failed: credible
  shutdown changes the attainable punishment. Exact3/16 versus3/4 witness kept.
* A reliability counterexample requires selected audits and disproves monotonic
  audit cost across prescribed targets (3/8 versus3/16). We explicitly distinguish
  this from monotonicity of an optimized relaxed feasible set.
* The mechanism frontier was restricted to inclusion-minimal successful
  coalitions or failure. Redundant realized coalitions can obey under private
  uncertainty, so the LP is not an unrestricted mechanism-optimality theorem.
* Empty-scope decomposable repeated squaring invalidates a generic inference
  bit-complexity shortcut. The positive class excludes it explicitly.
* Original BPR book text was found on a mirror; exact sampling/output and
  intermediate-bit bounds were inspected. Root retrieved the intermediate
  bound; compact reviewer independently inspected output/sampling statements
  and checked conversion using that bound. Mirror provenance and the failed
  original-host fetches remain disclosed. No general solver was implemented.

## Exact checks and completeness limits

58 standard-library Fraction/integer tests pass:41 retained +8 compact +9 audit.
Compact enumeration covers every n2 Boolean function/pure profile and chosen
asymmetric n3 functions; orbit sizes through n8, precision bounds through n31,
and a rational regret grid. It is not exhaustive over arbitrary circuits.
Audit tests enumerate types, target lotteries and all unilateral reports/best
final actions for their fixtures: n2–5 binary thresholds and asymmetric finite
multitype/nonmonotone rules. A rational grid corroborates the closed-form audit
objective but does not establish continuous optimality; the exchange argument
and coupling proof do. No unrestricted game/mechanism enumerator is claimed.

Primary-text comparisons and access limits are in both notes and
phase12-source-audit.md. Li's full model/proofs remain uninspected; indexed
introduction access is not counted as full-body verification.

Final import verification, clean-copy build, page inspection and companion
checks are recorded in the handover. No external contact or submission.

Clean-copy validation caught a preexisting build-check encoding assumption:
pdfTeX's fresh log contained raw8-bit bytes from the added bibliography, so
Python's UTF8 read failed after successful compilation. The checker now
decodes with replacement while matching ASCII diagnostics; latexmk errors
still fail the build normally. Final clean-copy checks repeated after repair.
