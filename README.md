# Agent Games

Mathematical research by **Nicholas Ham** on information-constrained coordination,
incentives and equilibrium selection in finite multi-agent systems.

Working paper: **Symmetry, Incentives and Equilibrium Selection in Multi-Agent
Systems**. This is an initial research draft, with verified finite-model
arguments and provisional originality, not a submitted or externally reviewed
publication. Actual LLM behavior is not assumed to satisfy these ideal models.

## Start here

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
