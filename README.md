# Agent Games

Mathematical research by **Nicholas Ham** on information-constrained coordination,
incentives and equilibrium selection in finite multi-agent systems.

Working paper: **Information, Incentives and Symmetric Equilibria in Finite
Coordination Games**. This 11-page finite-model manuscript is second priority,
after the symmetry-first paper. See [publication readiness](publication/READINESS.md)
for review records, technical checks and the outstanding novelty/scope decision.
It is not submitted or externally reviewed. Later research notes remain separate;
actual LLM behavior is not assumed to satisfy these ideal models.

## Start here

- [Phase 18 handover](research/phase18-handover.md), [ranking and research decision](research/phase18-assessment.md), and [preliminary outline only](research/phase18-outline.md).
- [Incentive-caused marginal geometry](research/phase18-strategic-geometry.md), [small protected projections](research/phase18-projections.md), [endogenous information](research/phase18-endogenous-information.md), and [sequential exploration](research/phase18-sequential.md).

- [Phase 17 handover](research/phase17-handover.md), [ranking and publication assessment](research/phase17-assessment.md), and [originality audit/LP lower bound](research/phase17-originality.md).
- [Repeated-worker representations](research/phase17-representations.md), [multi-constraint disclosure](research/phase17-disclosure.md), and [decentralized selection](research/phase17-decentralized.md).

- [Phase 16 handover](research/phase16-handover.md) and [contribution ranking/map](research/phase16-assessment.md).
- [Independent hardness audit](research/phase16-hardness-audit.md), [read-once/network tractability](research/phase16-tractability.md), [safe disclosure](research/phase16-disclosure.md), and [sequential substitution](research/phase16-substitution.md).

- [Phase 15 handover](research/phase15-handover.md), [ranking and broad map](research/phase15-assessment.md), and [targeted prior comparison](research/phase15-literature.md).
- [Succinct task algorithms and payoff hardness](research/phase15-succinct.md), [coverage formulation](research/phase15-coverage.md), [information and disclosure](research/phase15-information.md), and [resource substitution](research/phase15-resources.md).

- [Phase 14 handover](research/phase14-handover.md), [ranked assessment and map](research/phase14-assessment.md), and [source audit](research/phase14-literature.md).
- [Protected payoff regions](research/phase14-continuations.md), [constant-accuracy oracle boundary](research/phase14-complexity.md), and [contextual interchangeability](research/phase14-interchangeability.md).

- [Phase 13 handover](research/phase13-handover.md) and [broad research map](research/phase13-research-map.md).
- [Coalition continuation results](research/phase13-coalitions.md), [computation and precision boundaries](research/phase13-computation.md), and [independent verification audit](research/phase13-verification-audit.md).

- [Phase 12 handover](research/phase12-handover.md), [contribution assessment](research/phase12-assessment.md), and [actual review](reviews/AG-P12-REVIEW.md).
- [Constant-orbit lower bounds](research/phase12-compact.md), [selective-audit characterization](research/phase12-verification.md), and [real-algebraic source audit](research/phase12-source-audit.md).

- [Phase 11 handover](research/phase11-handover.md) and [five ranked research questions](research/phase11-priorities.md).
- [Local-factor orbit algorithms](research/phase11-orbit-algorithms.md), [private-cost mechanisms](research/phase11-volunteer-mechanisms.md), and [priced verification/representation boundaries](research/phase11-information-resources.md).
- [Phase 11 source comparisons](research/phase11-literature.md).
- [Initial campaign handover](research/phase10-handover.md).
- [Equilibrium and Bayesian selection](research/equilibrium-selection.md).
- [Allocation information](research/allocation-information.md).
- [Persistent-state costs](research/persistent-state-costs.md).
- [Primary literature and scope](research/literature-review.md) and
  [novelty ledger](research/novelty-ledger.md).
- [Manuscript source](paper/main.tex), [theorem ledger](research/theorem-ledger.md),
  [actual reviews](reviews/AG-P1-REVIEW.md).

The initial mathematical findings separate optimal allocation from structural
identification, invariant mixed-equilibrium existence from efficient and
resource-constrained selection, and algebraic nonsplitting from priced state
tracking. A two-agent private-cost example has symmetric BNE welfare5/2,
optimal public-local welfare3, and informed private-mediator welfare13/4.
Those are model-specific comparisons, not claimed new general game theory.

## Reproduce

Python3.10+ standard library; pdfLaTeX, BibTeX and latexmk are required for the
paper. No ignored downloads, third-party Python packages, API keys or LLM calls
are needed.

```sh
python3 scripts/verify_import.py
python3 -m unittest discover -s experiments
python3 research/origins/feasibility/toy_models.py
bash scripts/build.sh
```

The local paper is generated as `paper/build/main.pdf`; build outputs are
ignored. Exact `Fraction` tests verify all deterministic Bayesian type policies,
interim incentives, mediator obedience, allocation ranks/regret witnesses,
state-control schedules and a finite log-linear detailed-balance chain.
They corroborate proofs and preserve counterexamples; they do not establish
unbounded theorems, originality or empirical LLM guarantees.

## Provenance and boundaries

The approved local feasibility work is imported verbatim under
[research/origins/feasibility](research/origins/feasibility), with original
paths and SHA256 hashes in [the manifest](provenance/feasibility-import.json).
The original proposal is preserved. Its recommendation to defer this repository
is historical: the author explicitly authorized creation during Phase10.

[Game Symmetry](https://github.com/n-ham-research/game-symmetry) owns structural
symmetry and binary potential candidates;
[Game Fairness](https://github.com/n-ham-research/game-fairness) owns utility
invariance, assignment and observation theory. Exact result/commit dependencies
are [pinned here](research/cross-project-dependencies.md). Neither companion
was modified during this campaign. No Cortex/Gantry integration, external
contact, authorship change or submission is authorized or performed.

## Phase 19 research

[Ten-item handover](research/phase19-handover.md),
[assessment and research map](research/phase19-assessment.md), and
[internal review](reviews/AG-P19-REVIEW.md). The full uniform information frontier
is solved; ordinary-CE nonconstant-payoff hardness remains open. No new
manuscript or companion edits.
