# Second-priority manuscript — 20 October 2026

**Proposed title:** *Information, Incentives and Symmetric Equilibria in Finite
Coordination Games*. Author: Nicholas Ham. The symmetry-first manuscript in
game-symmetry is the first intended submission; this paper is second.

## Recommendation

The existing finite-model paper is mathematically reviewable and has received
presentation polish, but its originality and selection of central contributions
still need a human scope decision before submission. Do not promote the later
Phase 12–19 notes into this paper under an editorial campaign. No general LLM
rationality, welfare or learning theorem is asserted.

The core results are the guaranteed-success screening bound (Proposition 6.1),
the exact trusted-verification welfare/query frontier (Proposition 7.1), and
the explicitly tabulated local-factor orbit reduction (Proposition 8.1).
The last result is conditional on the stated real-algebraic sampling bounds;
the representation and exact-output assumptions are not removable. Earlier
allocation, mediation and state examples provide model comparisons and retain
their elementary/classical attributions.

## Integrity and review

- Compared with baseline d4d34eb; title, roadmap, semantic references,
  bibliography metadata, acknowledgements and table layout improved.
- Independent internal mathematical review identified a genuine omitted
  hypothesis in the existing binary query exposition. Explicit `0<p<1` is now
  stated; degenerate priors require no queries. The strict-gap boundary wording
  was aligned. The reviewer checked and approved the repair.
- No other theorem-level defect found; no later research result promoted.
- MATHEMATICAL-REVIEW.md and PUBLICATION-REVIEW.md record the sequential reviews.
  They are shared-context internal AI reviews, not external peer review or
  Nicholas Ham's approval.
- All 244 tests and three frozen feasibility-import checks pass. Clean source
  build, source-bundle compile, rendered pages and PDF destination checks are
  recorded in VERIFICATION.md and pdf-audit.json.

## Bibliography and novelty limits

Classical invariant equilibrium, screening, nonobligatory inspection, graphical
games, action-orbit computation and compact CE methods are credited. The current
claims are adaptations/specializations with provisional originality, not an
established new general theory. Brandt–Fischer–Holzer and Papadimitriou–Roughgarden
journal identifiers and the Monderer–Shapley DOI were completed using primary
publication metadata. Existing source-version qualifications remain: notably
the Basu–Pollack–Roy solver text was accessed through a disclosed mirror of an
updated author-posted text, not a freshly inspected published edition.

Outstanding: human judgment on significance/coherence, specialist originality
comparison, approval of statements and AI disclosure, and policy checks for the
eventual submission venue. None delays the separate symmetry paper.

## Deliverables

`output/pdf/agent-games.pdf` and `output/pdf/agent-games-source.tar.gz` are the
review artifacts; `paper/main.tex` is the maintained source. No submission,
repository visibility change, journal contact or empirical study occurred.
