# Phase 11 — actual review record

16 October 2026. Two separate Codex instances developed the orbit and mechanism
branches; root developed the verification, averaging and circuit boundaries.
The branches were initially separate. The mechanism instance reconstructed
AG-O1/O1b/O1c; the orbit instance attacked P11-M2/M3/M5 and the M4 endpoint
condition. Root read both complete notes, reconstructed the arguments, and
reviewed the experiments. Both instances then independently attacked root's
AG-V1/S1/H1 without editing those files. This is shared-model internal review,
not external mathematical peer review, author sign-off or novelty clearance.

## Defects and repairs

* Root rejected the initial claim of dominant-strategy truthful procurement in
  the full reporting/action game. With B=2, own cost3/2, an opponent of cost1/2
  who reports low but always abstains, truthful losing followed by unpaid
  completion gives1/2; underreporting to win a tie can give1 after payment1/2.
  The note and manuscript now claim only an ex-post honest-and-obedient
  equilibrium against truthful reports and prescribed continuations. An exact
  regression witness is retained.
* Both reviewers independently found that AG-S1 needed affine J: an invariant
  convex quadratic on the two-coordinate simplex is maximized only at exchanged
  vertices. The hypothesis and counterexample are now explicit and checked.
* Reviews required p interior for the reliability inequality, kappa>=0 for the
  verification-price formula, exclusion of all extra private signals, an
  almost-every-seed qualifier, and uniform-cheapest selection only for full
  search. Incorporated.
* Root/algorithm review corrected the interpretation of the one-orbit circuit
  reduction: expected-value evaluation counts satisfying assignments, but
  equilibrium output is trivial and invariant regret is zero. No regret
  hardness is asserted.
* Prior-art comparison removed any suggestion that the normal-form Tewolde
  bound is inherently XP-only: the explicit-table logarithmic absorption
  applies to that baseline too.

## Checks and limits

41 exact standard-library tests pass:20 retained baseline,8 mechanism,8 orbit,
5 resource checks. The counting check exhausts all256 three-input Boolean
truth tables. The experiments validate finite reductions and witnesses, not
an implemented real-algebraic solver or an asymptotic runtime benchmark.

Primary comparisons include Tewolde Appendix E, Brandt–Fischer–Holzer,
Battaglini–Palfrey §2.2/footnote12, and nonobligatory Pandora inspection.
The original real-algebraic sampling coefficient-bit/output theorem remains a
full-body source-access gap, explicitly disclosed rather than silently cleared.
No theorem has received an external review or originality clearance.

The manuscript builds to11 pages without undefined references or overfull
boxes. All11 rendered pages inspected at contact-sheet scale: margins,
equations, proof endings and bibliography are legible with no clipping.
Final import, clean-copy, companion and push results are in phase11-handover.md.
