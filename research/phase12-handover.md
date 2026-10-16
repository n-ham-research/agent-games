# Agent Games Phase 12 handover

16 October 2026. Nicholas Ham. This phase concentrated on the two authorized
programmes, with separate initial development and reciprocal adversarial review.
No new repository or manuscript was created. No originality clearance,
external peer review, contact or submission is claimed.

## Answers to the nine review questions

1. **Strongest candidates:** V12-C, a necessary-and-sufficient selective-audit
   characterization for voluntary minimal-coalition/failure targets; P12-C1,
   a constant-action-orbit refinement of circuit equilibrium-output hardness.
2. **Complete proofs:** P12-C1/C2 and the explicitly classified C3 corollary;
   V12-A/B/C, including arbitrary finite-type formulas, constructive attainment,
   adaptive-audit lower bounds and a closed-form per-report solution. See
   phase12-compact.md and phase12-verification.md. Independent internal attacks
   found no defect within the final assumptions.
3. **Disproved extrapolations:** the one-worker audit formula fails for redundant
   tasks; a prescribed lower-reliability target can need more auditing; bounded
   arithmetic inference does not ensure bounded bit output. Exact witnesses
   and finite coverage are in tests and phase12-assessment.md.
4. **Closest literature:** Schoenebeck–Vadhan2006 already supplies the counting-
   output gadget principle; Ben-Porath–Dekel–Lipman2014 supplies verification
   reduced forms; Battaglini–Palfrey2024 supplies honest/obedient collective
   action; Li2020 treats limited punishments, with full proof access unresolved.
   Friesen–Domingos2016 and Tewolde2025 cover the main positive-method ingredients.
5. **Genuinely new result?** No genuinely new tractable class was established.
   The q3 refinement and voluntary-action/reliability characterization are
   precise proved candidates whose originality still needs targeted review.
   We stopped promoting the positive inference branch once it proved to be
   a known-method XP corollary. No generic breakthrough is asserted.
6. **Applications:** redundant computation, verification teams and coverage
   allocation admit the audit construction if priors are independent, costs
   below shared benefit, audits perfect, target coalitions minimal, and a
   committed coordinator can privately address workers and shut down on lying.
   It implements one honest/obedient equilibrium. The algorithmic barrier
   warns against inferring precise Nash tractability from cheap circuit
   evaluation plus symmetry alone. No LLM performance claim follows.
7. **Unresolved:** succinct frontier optimization; unrestricted nonminimal
   recommended coalitions; correlated types; noisy audits; inability to commit
   to punishment; payment/audit/reliability substitution; a new structured
   expected-payoff class yielding FPT beyond current representations. Central
   private recommendations are not a decentralized bounded-message protocol.
8. **Strongest direction:** verification produced the stronger positive result,
   V12-C. Algorithms produced a sharper limitation, with close counting prior.
9. **Publication:** retain one conservative foundation paper for now. If overlap
   review validates a substantive audit contribution, a separate mechanism paper
   is plausible; the algorithm paper needs more than the current refinement.
   Do not create either additional paper yet.

## Exact model scope of V12-C

Independent finite costs c in (0,B), voluntary binary work, no transfers/fines,
perfect cost audits before final action, no intrinsic audit cost to its subject,
known success technology with no successful singleton. The honest target is a
lottery over inclusion-minimal successful coalitions or empty failure. For each
agent/report there are two audit capacities: successful-unselected and
successful-selected. Their incentive effects are B and B-c, respectively.
Audit unselected agents first; selected audits are sometimes necessary when
reliability depends on reports. Detection triggers an all-abstain Nash
continuation. This is a weak honest/obedient implementation, not unique or
full implementation. The resulting finite LP describes welfare/reliability
under audit budgets only in this target architecture. Its explicit tables may
be exponential in a compressed task specification.

## Source audit and manuscript restraint

The missing original real-algebraic statements were inspected in an original
BPR updated-book transcription on a disclosed mirror. Exact-output definitions,
sampling and intermediate integer-size bounds now have precise locations;
phase12-source-audit.md records the bit-operation conversion and provenance.
Author-host/publisher authentication remains advisable before submission.
This is not an implemented algebraic solver.

The existing paper remains11 pages. Only source-status/citation and bibliography
layout were updated; Phase12 exploratory theorems remain in reviewed research
notes. Native editor/compile tools are not exposed, so existing latexmk was
used without installation. All pages inspected after the citation change;
the final bibliography pages were rerendered after preventing split entries.
No undefined references or overfull boxes.

## Verification and boundaries

58 exact standard-library tests pass (41 retained,8 compact,9 verification).
All3 frozen imports match hashes, and the unchanged frozen toy script runs.
A clean copy of tracked/nonignored candidate files repeats verification,
58 tests and the11-page build; no ignored download is required. Exact finite
search limits are in ../reviews/AG-P12-REVIEW.md; proofs establish the
unbounded statements. README, theorem/novelty/dependency/AI/review records updated.

Game Fairness remains f75ec9f7f0ff3b74226baed67a2727eccf0220d3 with its
preexisting game-fairness.zip; Game Symmetry remains
e896a5cae79c5c63a81be16f1577bc365e67a5a6 with its preexisting games-symmetry.zip.
No companion, frozen original proposal, Cortex or Gantry changes.
The user explicitly authorized verified logical commits and push to the
existing agent-games repository; commit identities are reported in chat/git.
