# Phase 13 — broad exploration with two focused discoveries

16 October2026. Nicholas Ham's Agent Games programme. Baseline78510d1.
The latest strategy update was applied alongside the focused Phase13 brief:
open exploration competed with theorem development. No new manuscript,
repository, external contact, author change or publication submission.

## Findings worth reading first

**Credible continuation payoffs.** P13-P2 characterizes exactly when an agent
can receive zero in a correlated equilibrium of ANY finite monotone contribution
task with known positive costs below the shared success benefit. It handles
successful singletons as well as larger coalitions. Unilateral security alone
is insufficient: singleton costs impose a success floor, pair repairers impose
capacity constraints, and larger minimal coalitions change feasibility. A
private recommendation mechanism attains the criterion. This is a complete-
information continuation theorem, not an arbitrary private-cost audit theorem.
Its weak work obedience is essential; a positive-margin corollary gives a
strictly positive payoff floor. Proof: phase13-coalitions.md; robustness:
phase13-robustness.md.

**Interchangeability and accuracy.** P13-Q gives counting-hard fine-precision
INVARIANT equilibrium output with a cyclic player-transitive exact symmetry
and exactly TWO player-action orbits, even under the actual full group. One
orbit forces a directly writable uniform Nash profile. Thus the orbit boundary
is sharp for this representation/output/accuracy question. We supply exact
cyclic subgroup generators, not the full automorphism generator list.
A standard randomized sampling/bisection counterpart computes ordinary-
accuracy invariant equilibria in inverse-accuracy polynomial time. This
prevents extrapolation to constant-accuracy or unrestricted Nash hardness.
Proof and exact resource model: phase13-computation.md.

Both are complete reviewed candidates, with provisional originality. Neither
is promoted into the manuscript or described as externally peer reviewed.

## Answers to the ten focused Phase13 deliverables

1. **Final V12-C attack:** a separate instance not involved in Phase12 theorem
   development reconstructed necessity/attainment, private/adaptive audit
   timing, joint deviations and shutdown. No defect in stated scope; important
   nearby strengthenings are refuted. See phase13-verification-audit.md.
2. **Theorem-level prior comparison:** published BDL2014, BP2024 author body,
   Li2017 working paper and primary thesis were read at exact model/constraint
   locations. Li's thesis §2.5.2 eq2.21 already treats two audit categories and
   their priority allocation. V12-C is a task-specific endogenous-loss and
   voluntary-implementation synthesis, not a new LP or verification principle.
   Li2020 published final full body remains inaccessible, explicitly recorded.
3. **General coalition theory:** P13-P2 addresses jointly obedient punishment
   rather than only unilateral safety. Singleton-capable agents make literal
   shutdown impossible, yet private pooled recommendations can still support
   zero punishment. The exact criterion also identifies when they cannot.
4. **Impossibility/constructions:** sharp zero-payoff feasibility with explicit
   witnesses; positive-margin payoff floor; public/private punishment gap;
   success-preserving deletion keeps CE and welfare but can destroy truthful
   reporting. These do not solve a universal resource tradeoff for private types.
5. **Compact mechanisms:** P13-H constructs the exact histogram frontier LP and
   central sampler for fixed role/type counts, N^{O(K)} size: XP(K), not FPT.
   This is a useful symmetry-mechanism application with strong Daskalakis–Weinberg
   prior. P13-W gives natural weighted-threshold exact-value counting hardness,
   even without successful singletons. No mechanism-output hardness is inferred.
6. **Equilibrium complexity:** P13-Q sharpens three to two orbits while adding
   player transitivity, for exactly invariant fine-precision output. P13-E's
   constant-accuracy q3 refinement gives only BPP hardness, and unchanged
   counting extraction fails at coarse tolerance. Ordinary-accuracy randomized
   sampling is explicitly available in the q2 class.
7. **Counterexamples retained:** security0 need not mean credible0; public
   revelation can destroy private punishment; purification can break report IC;
   successful/minimal/empty support can lose punitive power; fine counting
   reductions do not give constant-accuracy counting hardness. Exact values
   and finite-search limits are in notes/tests/review.
8. **Novelty:** the two strongest structural candidates need further exact
   overlap review. Cavaliere2001 public-good correlation full text remains an
   important gap. CE/persuasion thinning, general worst-CE LPs, symmetric
   mechanism compression and circuit counting hardness are established prior.
   No result is novelty-cleared by absence from our searches.
9. **Strongest direction:** credible private cooperation/punishment is the
   strongest positive structural lead; the q2 precision boundary is an equally
   concrete computational alternative. Do not require every next phase to
   extend auditing. The independent contextual-agent-substitution question is
   a third serious exploratory option.
10. **Publication:** not ready for submission. Keep the current single11-page
    foundation manuscript unchanged. First close closest-source overlap and
    investigate whether the continuation theorem or q2 boundary makes a
    consequential contribution. A split remains conditional on that mathematics,
    not on the number of active branches.

## Broader strategy deliverables, including foundational fairness

phase13-research-map.md supplies the requested cross-theme map, established
literature, precise gaps/candidate objectives, applications and ranked next
choices. It covers coordination, information, incentives, symmetry, learning,
robustness and sequential systems. It also gives a foundation-oriented Game
Fairness map: coherent opportunity/assignment comparisons, calibration, ordered
versus unordered opponents, and impartial decision rules. Existing canonical
fairness proofs and counterexamples are pinned rather than rediscovered.
A strategic-equivalence/calibrated-role benchmark is checked exactly here.

Game Fairness was read only. This is a local cross-project research recommendation,
not a claimed new canonical fairness phase or permission to modify its files.
The scope honors the review's explicit companion boundary while addressing the
broader requested agenda. No global equivalence of symmetry and fairness is
assumed or proved. The map makes clear where observation/masking tools would
serve a foundational question and where they would merely become a detour.

## Reproduction and actual review

82 exact standard-library tests pass:58 baseline +4 independent audit +7 coalition
+11 computation +2 broader-exploration checks. Three frozen imports match hashes;
the frozen toy script remains unchanged. All166 nonconstant four-agent monotone
tasks and16 cost vectors are used for constructive criterion checks, NOT an
exhaustive LP proof of all infeasible cases. Audit fixtures independently solve
648 small rational LPs. Bisection checks are deterministic bounded-error tests;
the confidence theorem is proved, not inferred from sample runs.

Separate instance review, reciprocal proof attacks, root reconstruction and
actual source discoveries are recorded in ../reviews/AG-P13-REVIEW.md and the
independent audit note. Internal AI agreement is not external mathematical
review or author sign-off. No general optimization solver was implemented.
The mathematical LP/reduction plus small exact checks are the artifacts.

The existing manuscript build is rerun locally and in a clean copy of only
tracked/nonignored candidate files, alongside all82 tests and import verification.
It remains11 pages; no layout/source change or new rendering is needed this
phase. No ignored third-party download is required by any check.

Companion boundaries verified: Game Fairness remains
f75ec9f7f0ff3b74226baed67a2727eccf0220d3 with preexisting game-fairness.zip;
Game Symmetry remains e896a5cae79c5c63a81be16f1577bc365e67a5a6 with preexisting
games-symmetry.zip. Frozen origins, original proposals, Cortex and Gantry are
unchanged. Verified work is committed/pushed in logical units as authorized.
