# Agent Games — Phase 15 internal adversarial review

16 October2026. Author Nicholas Ham; same-family Codex assistance. Independent
instances here means separately developed/reconstructed proofs, not external
peer review, independent human verification or author sign-off.

## Actual development and reconstruction

Root read the full Phase14 review and repository instructions, then reused three
existing separate agent instances as explicitly requested. p12_compact developed
summary-flow formulations and the weighted-threshold payoff-gap theorem;
p12_verification developed information/disclosure; p5_splitting developed
resource contracts. Exclusive branch files and tests avoided shared editing.
Root separately proved capped-coverage flow exactness and supplied the initial
weighted parity/singleton-backstop reduction; compact strengthened its gap and
approximate-obedience certificate.

* p5 independently reconstructed S1–S4: terminal-conditioned path decomposition,
  action-labelled parallel edges, O(nM²) size, polynomial rational support,
  threshold switching coefficients, capped-count coverage and zero-feasibility
  NP certificate. It found no proof defect. Root independently checked the
  YES law, NO dual identity and payoff approximation thresholds.
* p5 independently reconstructed root coverage: final cap2 multiplicities
  determine pivotal/repair events; per-terminal DAG flow gives an actual joint
  law, with n9^d size. No defect found.
* compact independently attacked information: factorization within literal
  recommendations, safe-release inequalities, strict row/column counterexample,
  posterior-odds bounds and threshold algebra, adaptive ratio composition and
  type-only privacy failure. No defect found. Root also checked each formula
  and the conditional1/12 margin by direct calculation.
* verification independently reconstructed resource R1–R3: forward/reverse
  controller budgets, mixed-interface certificate, stochastic factorization,
  rational-field caveat, four-cycle rank separation, MQ/N success and retained
  TV. No substantive defect. It requested the saturation qualifier for K/N;
  author changed this to min(1,K/N). Root read the full proof and checked its
  external-storage, output-alphabet and retained-record restrictions.

## Actual narrowing and rejected extrapolations

Primary comparisons identified exact prior Cohen–Rothblum1993 Theorem3.2, so
factorization algebra is classified PRIOR, not new. Barman–Ligett2015 and
Jiang–Leyton-Brown2011 make the positive DP method substantially prior as well.
Matsui–Matsui2000 already establishes weighted relevance hardness. No general
algorithmic novelty is inferred from this campaign's new formulations.

Other retained failures: success-only coverage masks lose pivotality; connected
partitions lose bridge information; binary weights invalidate a polynomial-in-
encoding claim for the pseudo-polynomial LP; individually safe public signals
may be unsafe jointly; type privacy can disclose all recommendation randomness;
literal-action channel lower bounds do not cover type-contingent plans;
perfect-recall equivalence does not preserve controller-mode budgets; modes
and bits differ logarithmically. NO payoff in the gap theorem is >=1/4, not
necessarily exactly1/4. Conditional positive margins and unconditional negative
row slack remain separate concepts.

No manuscript/layout edits or companion changes. No external contact, authorship
change, submission or empirical LLM experiment. Frozen sources verified. Final
validation totals and clean-copy details are recorded in phase15-handover.md.
