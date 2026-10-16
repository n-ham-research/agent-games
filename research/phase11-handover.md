# Agent Games Phase 11 handover

16 October 2026. Author Nicholas Ham. Completed research expansion after the
Phase10 review. No external review, novelty clearance or submission.

## Main outcomes

1. **General private-cost contribution tasks.** For independent positive costs
   below B and any known nonempty upward-closed successful-coalition family,
   guaranteed-success no-transfer equilibrium communication cannot condition
   an agent's interim workload on its own cost. The sharp frontier is nB minus
   the cheapest coalition's expected cost. First best is possible iff a fixed
   coalition is cheapest almost surely. Public designation already attains the
   optimum, so richer private communication does not improve this particular
   guaranteed-success frontier. This is close to established honest-and-obedient
   screening, not a claimed new general principle.
2. **Representation-sensitive orbit algorithms.** Explicit additive local tables
   support the invariant Nash polynomial reduction, q-only FPT input-size
   refinement, and welfare optimization within invariant Nash. Exact algebraic
   sampling is an external black box; original-source bit/output verification
   remains outstanding. The experiments implement small exact reductions,
   not a general equilibrium solver. The FPT refinement also applies to the
   prior explicit normal-form bound; no artificial separation is claimed.
3. **Priced information and limits.** For arbitrary n iid binary private costs,
   trusted verification has a sharp expected-query frontier and zero-error
   lower bounds. Convex affine mechanism averaging can preserve welfare while
   changing implementation resources. Succinct q1 circuits can encode counting
   in exact payoff values even when outputting invariant Nash is trivial.

## Read first

* phase11-volunteer-mechanisms.md: P11-M1–M5, full protocol model, proofs,
  reliability bound, parameterized calibrations and procurement correction.
* phase11-orbit-algorithms.md: AG-O1/O1b/O1c/O2–O5, construction, runtime,
  precision, reconstruction and oracle costs; primary comparisons.
* phase11-information-resources.md: AG-V1/S1/H1, complete proofs and boundaries.
* phase11-literature.md: inspected sources, close prior work and access limits.
* phase11-priorities.md: five ranked major questions, precise gaps, candidate
  statements and applications. Best main leads: incentive-preserving compact
  representations and sharp reliability/verification bounds. No substantial
  original theorem is declared achieved merely by this expansion.
* ../reviews/AG-P11-REVIEW.md: actual independent internal reviews and repairs.

## Reproduction and manuscript

41 exact tests pass (20 baseline +21 new), all3 frozen imports match hashes,
and the frozen toy script runs unchanged. The11-page manuscript builds without
undefined references or overfull boxes; every rendered page was visually
inspected. Native LaTeX editor/compile tools were not exposed; existing local
latexmk was used without installing dependencies. A clean copy containing only
tracked/nonignored candidate files repeated import verification, all41 tests
and a successful11-page build at /tmp/ag-p11-clean-3_er3yvq. Generated PDFs and
renderings remain ignored or outside the repository.

Both companions retain their baseline commits and preexisting untracked ZIPs:
game-fairness f75ec9f7f0ff3b74226baed67a2727eccf0220d3;
game-symmetry e896a5cae79c5c63a81be16f1577bc365e67a5a6.
No original feasibility, proposal, Cortex/Gantry or unrelated files changed.
The user authorized committing/pushing completed work in logical units.

Phase12 source update: see phase12-source-audit.md. The previously missing
sampling/bit/output statements were inspected in original author-book text
through a disclosed mirror. Historical access failures above remain accurate.
