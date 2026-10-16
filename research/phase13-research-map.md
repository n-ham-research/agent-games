# Phase 13 — open exploration and focused theorem development

16 October 2026. Nicholas Ham's Agent Games programme. This map implements the
strategy update alongside the focused Phase13 brief. It does not make the most
recent theorem a requirement for every future investigation. Fairness is mapped
here from read-only companion sources; its canonical repository is unchanged.
No independent fairness phase, manuscript, or theorem registry was created there.

## What each programme is trying to explain

Agent Games asks what information, incentives, computation and physical
resources make cooperation possible, efficient and robust. Game Fairness asks
when independently motivated assignment, opportunity or treatment comparisons
are related to utility-preserving structure. Both need explicit decision models;
neither question is answered by declaring symmetry sufficient by definition.

Read-only canonical baselines: Game Fairness
f75ec9f7f0ff3b74226baed67a2727eccf0220d3, particularly U1/U5, A1, P7-A1–A6,
P8-B1–B3 and P9-F1; Game Symmetry
e896a5cae79c5c63a81be16f1577bc365e67a5a6 for exact typed matching, transitivity
and splitting. No result below reclaims their ownership or changes their scope.

## Agent Games: research map across six themes

| Theme | Significant precise question | Existing foundation and initial decision |
|---|---|---|
| Coordination | Which private/public signal channels permit a jointly obedient continuation giving a specified payoff vector? | CE/BCE and information design are prior. P13-P2 now solves the zero-payoff face for monotone tasks; full payoff/channel tradeoff remains open. |
| Information | Which observations preserve all relevant deviation opportunities when replacing or aggregating agents? | Game Fairness P9-I1 identifies a specified linear discrepancy, not strategic revelation. Blackwell comparisons and strategic information orders are prior; study a fixed observation/strategy architecture before claiming a new hierarchy. |
| Incentives | When do unilateral safety values equal jointly attainable punishment values? | Minimax security alone is insufficient. P13-P2 gives an exact structural criterion; private costs and partial audit disclosures remain a substantial gap. |
| Symmetry and computation | How do group structure, expectation access and accuracy jointly control equilibrium or mechanism complexity? | Tewolde and symmetry-aware mechanism design are prior. P13-Q gives a two-orbit fine-precision barrier; P13-Qapprox gives its standard sampling counterpart. P13-H is a practical XP count reduction, not a new algorithmic principle. |
| Equilibrium and learning | Which efficient/punitive recommendations survive approximate obedience, altered information or local learning? | Hart–Mas-Colell CE learning and near-potential dynamics are prior. The margin bound below shows zero punishment is fragile; no convergence-to-efficient-outcomes claim is made. |
| Sequential systems and robustness | Which finite-state substitutions preserve deviations and continuation information, including memory and role visibility? | Bisimulation alone can fail to preserve Nash under conventional strategy semantics. A strategy-compatible finite-state interchangeability theorem, with robustness and reconstruction costs, is a worthwhile open target. |

### Three priorities that compete on significance

1. **Information-constrained credible cooperation.** Characterize the lowest
   jointly obedient payoff under a specified public/private recommendation
   channel and a positive obedience margin. Candidate objective: extend the
   zero-face criterion to a positive-payoff frontier or prove a structural
   obstruction for partial disclosure. Applications include private delegation
   and robust worker recommendations. It must not assume all agents' costs
   become common knowledge after auditing only one liar. This is the strongest
   fresh lead from the open exploration, not a restatement of the audit LP.
2. **Precision-sensitive interchangeability.** Separate exact/fine and ordinary
   approximate coordination under weak player transitivity. P13-Q/Qapprox make
   the question concrete without requiring ordinary anonymity. Next target:
   inverse-polynomial accuracy with several roles or resource-limited sampling,
   or a new compact representation where a deterministic stronger algorithm
   genuinely goes beyond current orbit reductions. Do not call a standard
   one-dimensional bisection method a new discovery.
3. **Contextual agent substitution.** Fix finite-state agents, visible histories,
   allowable unilateral deviations and a resource budget. Seek necessary and
   sufficient simulation/transport conditions for preserving equilibrium
   regret and task outcome laws when an agent is replaced. First prove a
   restricted finite-horizon theorem or counterexample; do not invent an
   unrestricted equivalence with bisimulation. This can escape the contribution
   model and connect tools, permissions, knowledge and persistent memory.

These are research objectives, not promised true theorem statements. One phase
should develop only one or two leads after adversarial and prior-art checks.
Approximate symmetry, learning, assignment and decentralized communication stay
active alternatives; they are not eliminated by choosing a temporary focus.

## Fairness: return to foundations, rather than more masking designs

The following are recommendations for the canonical fairness programme. They
are not new fairness theorems proved or published by Agent Games.

| Priority | Independently motivated question | Precise gap and candidate investigation |
|---|---|---|
| F1 | When do equal opportunities before assignment imply a coherent structural interchangeability? | P7-A already identifies downward convex opportunity sets and shows local equality does not imply simultaneous symmetry. Seek natural rigidity/observability hypotheses under which role-wise opportunity maps glue into one typed action transport. Start with exposed essential actions and ordered opponents; retain non-gluing counterexamples. Requiring an automorphism as part of the fairness axiom would make the result circular. |
| F2 | What information does literal assignment indifference require? | A1 already proves role-specific utility preferences do not identify cross-role calibration. Specify one participant's common consequence space, risk preferences and assignment timing; seek a minimal elicitation/identification theorem for role lotteries, not another symmetry-entry test. Compare ordinal, cardinal and common-risk models without unjustified interpersonal sums. |
| F3 | Does inability to distinguish opponents explain a particular symmetry notion? | F3/P7-A3–A4 show multiset/exchangeable observations lose ordered structure. Define admissible opponent-observation and policy classes first; classify when observational opportunity equivalence lifts to individual anonymity or exact typed symmetry. Generic equivalence is already false. A useful result would explain the precise lifting assumptions rather than count masks. |
| F4 | Can an impartial decision rule unify equal treatment across game solutions? | VNM/Nash/Shapley act on different objects. An equivariant selector framework is established group reasoning; add an independently justified calibration or consistency requirement that yields a new characterization or impossibility. Harsanyi supplies a relevant impartial-preference baseline. No universal fairness axiom is asserted here. |

F1/F2 are the strongest foundational opportunities; F3 is a structural bridge,
and F4 is higher-risk conceptual work. All four must compete with established
social-choice, decision-theory and fair-division results, not merely with our
own finite examples. The original 1944 edition remains a historical-source
question; nothing in this phase claims new access to it or substitutes a later
edition without disclosure.

## A common warning: strategic equivalence is not utility or fairness equivalence

An established observation helps keep the programmes connected without forcing
a new theorem: adding b_i(a_-i) to a player's payoff leaves every own-action
incentive difference unchanged. Thus pure/mixed Nash and correlated obedience
are preserved, while calibrated role prospects can change. Exact/cardinal
utility automorphisms need not be preserved. Candogan et al.'s decomposition
already treats these nonstrategic terms; the point here is research selection,
not originality.

For example, start with u_0=a_0 and u_1=a_1, binary actions. Replace u_0 by
v_0=a_0+10a_1 and leave v_1=a_1. Both have the same strictly dominant actions
and the same unique NE/CE (1,1). In the first game player exchange is exact;
in the second no cardinal player exchange exists (the own0 player's utility
has four distinct values, the other has two). Calibrated utilities at the same
outcome are11 and1. Consequently behavioral indistinguishability alone cannot
justify literal fairness of positions. The companion's calibration caveat
remains essential even when all strategic predictions agree.

## Primary literature actually inspected for this broader map

* Candogan–Menache–Ozdaglar–Parrilo, [Flows and Decompositions of Games](https://arxiv.org/pdf/1005.2405), original author text, introduction, normalized games and nonstrategic component discussion: strategic differences and utility levels serve different purposes. Candogan–Ozdaglar–Parrilo, [Dynamics in Near-Potential Games](https://arxiv.org/pdf/1107.4386), §2/maximum pairwise difference: incentive-sensitive robustness is established prior, not a new metric proposed here.
* Gutierrez–Harrenstein–Perelli–Wooldridge, [Nash Equilibrium and Bisimulation Invariance](https://arxiv.org/pdf/1808.09213), LMCS2019, abstract and §1 inspected: conventional history-state strategies need not preserve Nash existence under bisimilarity; alternative strategy semantics matter. Full proofs were not audited in this map.
* Harsanyi, [Cardinal Welfare, Individualistic Ethics, and Interpersonal Comparisons of Utility](https://hceconomics.uchicago.edu/sites/default/files/pdf/events/Harsanyi_1955_JPE_v63_n4.pdf), JPE1955, §§I–II inspected: explicit ethical/interpersonal assumptions belong in fairness modeling; no global characterization theorem from this paper is claimed as newly verified here.
* Cherry–Smith, [Strategically Valuable Information](https://www.lonessmith.com/wp-content/uploads/2016/12/blackwell.pdf), draft dated7December2014, introduction inspected. Its strategic comparison question is close prior, but visible unresolved citation placeholders mean this draft is not a final-source authority. Blackwell's1953 original full body was not retrieved in this pass; no theorem-level source certification is claimed.
* Existing canonical fairness literature records retain their actual VNM/Nash/Shapley source versions. New focused contributions cite their own closest primary sources in the coalition, computation and verification-review notes.

## Stopping rules and recommendation

Broad exploration is not a requirement to produce a theorem in every row.
Stop a branch if its proposed theorem is a known method corollary without a
new structural consequence. Keep exact failed conjectures. Promote only after
independent proof reconstruction and a meaningful primary-source comparison.
The present map identifies a foundation-oriented fairness agenda and three
Agent Games opportunities; the focused notes develop two actual candidates.
The manuscript need not dictate either agenda, and no publication split is
justified merely because two branches exist.
