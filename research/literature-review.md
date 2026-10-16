# Targeted literature and positioning — 16 October 2026

This is a bounded primary-source review, not an exhaustive novelty audit.
Model/rationality/information/symmetry/theorem overlap are distinguished below.
Full-body access is claimed only for identified passages. No third-party PDF
is tracked. Conference calls establish audience, not mathematical novelty.

## 2020–2026 coordination and equilibrium work

### Hu et al., ICML2020 — Other-Play

[Original PMLR paper](https://proceedings.mlr.press/v119/hu20a/hu20a.pdf),
introduction and model description inspected. Partially observed cooperative
Markov games are known to both agents; independently constructed policies face
unknown partners without agreeing on label conventions. Known state/action
symmetries enter the other-play objective. RL experiments do not assume actual
LLMs are rational utility maximizers. This directly precedes our discussion of
symmetry and unavailable correlation. We do not claim the anonymous one-shot
bound or a connection between symmetry and coordination is unexplored. Our
static, exact Bayesian examples do not imply an improvement over other-play.

### Treutlein et al., ICML2021 — label-free coordination

[Original paper](https://proceedings.mlr.press/v139/treutlein21a/treutlein21a.pdf),
Sections4–5 and informal Theorems7–8 inspected. The label-free coordination
formalism treats separately chosen learning algorithms over Dec-POMDPs.
The two-stage lever example exposes a limitation of ordinary other-play;
other-play with tie-breaking has optimality/equilibrium claims in that formalism.
Private observation and decentralized policy construction are explicit, and
isomorphism-respecting tie-breaking is substantial prior art. Our fixed-point
selection facts and finite public/private-device distinctions are elementary
comparisons, not a replacement theorem. Appendix-level complete formal proofs
were not all reconstructed in this pass.

### Marris et al., 2022 — neural equilibrium solvers

[Author preprint arXiv:2210.09257](https://arxiv.org/pdf/2210.09257),
Section3 inspected. Normal-form inputs and equilibrium incentive constraints
feed equivariant approximators; the selection framework combines welfare and
relative-entropy objectives, especially correlated/coarse-correlated equilibria.
There is no private-type state in this model. Agents' rationality appears in
the target solution concept rather than an assertion about actual LLM behavior.
This is prior equilibrium selection with payoff normalization and symmetry;
our averaging and objective observations are not new neural-solver results.
The search metadata's broad mention of NE must not obscure the (C)CE focus
of the section actually read.

### Duan–Ma–Deng, arXiv:2301.11481v2, 27 April2023

[Original author paper](https://arxiv.org/pdf/2301.11481), Section5,
Theorems5.3/5.6/5.7 and their example constructions inspected. Payoffs are finite
normal-form arrays; equivariance is imposed on equilibrium approximators
under action relabelings. Theorem5.3 excludes certain asymmetric pure outputs;
Theorem5.6 preserves optimal welfare within its equivariant (C)CE class;
Theorem5.7 shows severe welfare losses for equivariant NE approximators.
These are direct prior-art objections to presenting our generic selection/
efficiency distinction as novel. Their function-class and normalization
hypotheses differ from our local-policy/private-type implementation model;
that difference alone is not originality. No private reporting or persistent
state theorem is supplied by this comparison. Do not promote our simple
anti-coordination witness to a new impossibility theorem in this territory.

### Tewolde et al., AAAI2025 and long author version

[Long author manuscript](https://emanueltewolde.com/files/symmetries.pdf),
Section4/Theorem7 and the equilibrium-respecting definitions inspected;
[proceedings version](https://www.cs.cmu.edu/~conitzer/symmetriesAAAI25.pdf)
also inspected for introduction/coordination examples. It explicitly recalls
Nash1951's invariant mixed-equilibrium existence and studies symmetry detection
and equilibrium-computation complexity. Exact player/action bijections are
modeled; no private-type inference or restricted correction controller is
assumed. This establishes that unrestricted fixed mixed NE is a baseline,
not an open research target. The author version is a long updated paper; no
unprinted revision date or equality with every arXiv version is asserted.
Finding symmetric equilibria may remain computationally hard even when they
exist. Cardinal and ordinal distinctions here use canonical Game Fairness U5.

### Sun et al., IJCAI2025 survey; Zhu et al., ACL2025 benchmark

[IJCAI official paper](https://www.ijcai.org/proceedings/2025/1184.pdf),
opening scope inspected: surveys game-based LLM evaluation, game-theoretic
methods and social impacts. It maps research, not a single rational-agent
theorem or our novel-contribution evidence.

[MultiAgentBench official record](https://aclanthology.org/2025.acl-long.421/)
and original scope/architecture described in the imported feasibility source
record: empirical collaboration/competition across communication structures.
We refreshed the official record; the earlier recorded PDF-page inspection
was not silently counted as a new full-body read here. Identity/role structures
are experimental choices. Its measured LLM behavior cannot certify our finite
Bayesian or controller theorems. It is an eventual protocol comparator only.

### 2026 community context

[AAMAS2026](https://cyprusconferences.org/aamas2026/) and
[EC2026](https://ec26.sigecom.org/) official pages were opened. They are relevant
communities, not proof of a research gap. The
[EC workshop](https://llm-incentives.com/), dated6July2026, explicitly discusses
opaque objectives, information acquisition and delegation. Its webpage's
illustrative chatbot dialogue is not a theorem or empirical validation.
No participation, funding inquiry or external contact occurred. The supplied
survey/venue growth figures are not needed for a mathematical claim here;
we did not infer a causal growth rate attributable to LLMs.

## Supporting sources and classical baselines

- **Decision-focused allocation, 2020/2022.** Primary Elmachtoub–Liang–McNellis,
  Mandi et al. and Elmachtoub–Grigas passages were read by the allocation
  instance; exact source versions and comparisons are in
  allocation-information.md. Predicting objective costs versus preserving
  decisions is established; our full-linear rank calculation is an application.
- **State abstraction, 2021.** Makdesi–Girard–Fribourg original model and
  Proposition5 were read by the state instance; see persistent-state-costs.md.
  Its monotone/set-valued learned systems differ from our known finite carrier.
  AAMAS2024 memory-control body remained inaccessible. Weighted automata,
  feedback refinement and controller-memory lower bounds need further review.
- **Bergemann–Morris2016.** [Original author/published text](https://economics.mit.edu/sites/default/files/publications/paper_79_bce.pdf),
  printed493, Definitions1–2 and informational-robustness scope inspected.
  Obedience conditions condition on own information and recommendation; they
  do not guarantee truthful elicitation. Our externally informed volunteer
  mediator is a finite transparent example in this prior framework, not a new
  theory of Bayesian correlation. Stronger information-comparison theorems
  from the article are not required by our proof.
- **Monderer–Shapley1996.** [Original paper](https://www.tau.ac.il/~mansour/sem-game-02-03/monderer-potential-96.pdf),
  printed127–129, Lemma2.1/Corollary2.2/Lemma2.3 inspected. Potential existence
  and strict unilateral improvement termination are prior. Our incentive
  examples and exact checks are controls, not discoveries of potential games.
- **Marden–Shamma2012.** [Publisher record](https://doi.org/10.1016/j.geb.2012.03.006)
  and [author publication list](https://web.ece.ucsb.edu/~jrmarden/publications.html)
  inspected; original full-body comparison not completed. The record identifies
  asynchronous/full-action log-linear learning as prior. Our note proves its
  stated Gibbs law by detailed balance directly, without claiming novel
  convergence theory or to have read an inaccessible proof body.
- **Cheng et al.2004.** [Author-hosted notes](https://strategicreasoning.org/wp-content/uploads/2016/12/notes-symetric.pdf),
  Table1c and symmetric-equilibrium discussion inspected. Anti-coordination
  already separates pure symmetric selection from mixed existence.
  Nash1951's original printing was not newly inspected: one old document URL
  redirected to an unrelated site and was discarded. The invariant theorem's
  attribution is supported by the primary Tewolde and Cheng texts above.

## Claim-to-prior assessment

| Claim | Current assessment |
|---|---|
| Invariant mixed NE, pure fixed-point obstruction, orbit averaging | Established; not candidate novelty. |
| Equivariance can reduce efficient NE choices; CE randomization can help | Directly substantial prior Duan/Tewolde/zero-shot coordination literature. |
| Linear allocation contrast rank; assignment dimension | Standard finite linear estimability/assignment geometry applied; novelty unclaimed. |
| Public-local versus informed-private welfare gap in the specified Bayesian game | Exact model-specific comparison; compare volunteer/public-good and information-design literature before any novelty claim. |
| Checkpoint correction cost and state-feedback escape | Operational application of canonical coherence, not new splitting theory. |
| Actual LLM agents follow these objectives or gains | Not investigated and not claimed. |

The first report establishes a reproducible programme and meaningful negative
results, not a cleared original paper. The strongest next question is a
costed, decentralized private-information protocol with explicit incentive or
verification restrictions, sharpening the volunteer architecture gap beyond
standard Bayesian correlation. State feedback/cost restrictions are a second
lead. Do not abandon them because the baseline mathematics is classical;
do not package the baseline alone as a newly established AI theory.
