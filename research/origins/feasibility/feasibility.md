# Agent Games — focused feasibility assessment

16 October 2026. Proposed working title: *Symmetry, Incentives and Coordination
in Multi-Agent Systems*. This is an exploratory directory, not a new Git
repository or a publication manuscript.

**Recommendation: continue a bounded mathematical feasibility study, but do not
establish a third publication project yet.** Observable reassignment coherence is
the strongest distinctive direction; task-specific observation design is second.
Incentive design is useful as a falsification/control strand, with a substantially
higher prior-art burden. The examples below show that the distinctions matter;
they do not yet supply an independently novel agent-systems theorem.

## Ownership and source pins

The two existing repositories remain canonical. These are read-only references
to their state at the start of this assessment; no source proofs were copied.

| Canonical result | Source and pinned commit | Use here |
|---|---|---|
| P8-C1 observer-quotient coherence | `game-fairness/research/phase8-behavior-and-identification.md`, `bcf8bfcbd185962576b78a4ccd729e361231dea9` | Operational finite controller model; no new extension theorem claimed. |
| P8-I1 shared calibrated interventions; P8-O1 observation kernels; P8-O3 biased masks; P8-O4 all-r threshold | Same fairness commit; `research/phase8-observation-operators.md` | Distinguish task decisions, candidate symmetry tests, and full-table identification. Phase 9 minimal/noisy identification belongs in Game Fairness. |
| P7-A1 and P8-B1 opportunity envelopes | Same fairness commit; `research/phase7-assignment-opportunities.md` and P8 behavior note | Fixed participant utility, disclosed beliefs, timing and response policies are additional data. |
| P3-E2 binary full-actual-player-image potential; sharp ternary splitting candidate | `game-symmetry`, `2b2a9c44ad9ad10284dc265aba4d82e52c6741d5`; `research/phase3-equilibria.md`, `research/external-review-briefing.md` | Static-game hypotheses only; no dynamic extension and no efficiency inference. |

Public source snapshots:
[Fairness](https://github.com/n-ham-research/game-fairness/tree/bcf8bfcbd185962576b78a4ccd729e361231dea9),
[Symmetry](https://github.com/n-ham-research/game-symmetry/tree/2b2a9c44ad9ad10284dc265aba4d82e52c6741d5).
The exact finite controller group below is not asserted to be the complete
automorphism group of any normal-form game. It therefore neither proves nor
contradicts the sharp ternary theorem.

## Model C — reassignment, persistent state and future observations

**Question C.** Given physically available state transports, which observations
must be preserved to make repeated role reassignment operationally independent
of the reassignment path? Can we compute the least additional probe or reset
needed to remove a detectable obstruction, with its actual resource cost?

Specify a finite agent-role set I, a finite physical state space X containing
role labels and persistent tool/memory registers, an available reversible
implementation group H acting on X, and a surjection pi:H→P≤Sym(I). Its kernel
K changes internal implementation without changing recipient roles. The
coordinator chooses a normalized lift r(p) for each requested permutation.
Histories are finite words in requested permutations, applied right to left.
At this stage there is no strategic play: transports are controlled actions.
The coordination objective is equality of specified task-observable behavior
for histories with the same total role permutation.

A task specification supplies a finite family of future tests F: functions
f:X→Y_f representing observations after a disclosed continuation experiment.
Include visible role labels. Define the universal invisible subgroup

    N_F = {h∈H : f(hx)=f(x) for every x and every f∈F}.

Check that N_F is normal and contained in K before invoking P8-C1. A general
arbitrary observation partition need not have normal stabilizer. If the family
is closed under all transport precompositions, its invisible subgroup is
normal: conjugating h tests f∘g against g^{-1}x. Such closure is a substantial
task requirement, not a property to assume silently. Taking the normal core
of a nonnormal invisible subgroup is a sufficient conservative refinement;
it changes the observation specification and is not automatically an equivalent
criterion for the original experiment.

P8-C1 then says that some r is path independent for all tests precisely when
H/N_F→P splits. This is a **reuse** of the canonical theorem. Including future
tests matters: preserving today's output need not preserve tomorrow's task.
For a controlled deterministic system with finite actions A, transition
T:X×A→X and output q, one possible F is all fixed-control continuation maps
x↦q(T_w x). Finite-state partition refinement computes which states these
tests distinguish. Compatibility with H, role labels and normality must still
be checked. We do not claim a dynamic-game theorem from the static game result.

**C-toy (existing obstruction, operational specialization).** Take H=C4 acting
by addition on X=C4 and P=C2 by parity. Both odd lifts 1,3 of the role swap
square to 2; the identity lift is 0. Two swaps and no swap have equal role
labels, but leave different physical states for every initial x. With only
parity observations N=K={0,2}, so observable coherence exists. Adding a binary
terminal probe f(x)=1[x=0] makes N={0}. This subgroup is normal; a single
additional probe type thus exposes the obstruction under universal state
testing. At reference x=0 the probe returns 0 after two swaps and 1 after no
swap. No welfare loss follows until that probe is tied to an independently
specified task consequence or cost.

The C4 example already occurs in P8-C1. Its use here tests controller semantics,
not novelty. A worthwhile next result would combine finite-state observational
refinement with an explicitly costed intervention/reset problem under restricted
access. General extension splitting is not a new result; state abstraction and
bisimulation literature must be compared before proposing an algorithmic novelty
claim. An arbitrary destructive reset need not lie in H, and changes the model.

**What would warrant publication?** A new tractable criterion or sharp
cost/information separation for a natural class of persistent-state protocols,
beyond merely restating quotient splitting, plus an independently reproduced
example where task consequences are measured. Failure to find such a result
should leave this as an application section in the existing programme.

## Model O — task-relevant capability observations and fair assignments

**Question O.** For a specified allocation task, what is the minimum disclosed
observation needed to choose a role assignment satisfying an exogenous
opportunity or welfare requirement, and how does that budget compare with
identifying interchangeability or the full payoff table?

Specify agents I, roles J, a finite capability state Z with disclosed prior mu,
feasible assignments D, and physical receipt R_i(d,z). A sensor or communication
protocol supplies a stochastic channel Q(y|z), followed by an allocation rule
delta(d|y). Utilities W_i on a calibrated common physical consequence space and
the coordinator objective (for example total expected task completion less
cost) must be given separately. Capabilities, costs and permissions belong in Z
or feasible sets; they are not mere identity names. A procedural equivariance
condition for genuinely equivalent agents is one possible constraint, not a
complete fairness definition.

For a fixed decision problem with reward r(d,z), optimal expected reward is

    V(Q) = sum_y max_d sum_z mu(z) Q(y|z) r(d,z).

This is a standard finite Bayesian decision value. A deterministic aggregate
y=q(z) preserves the full-information optimum iff every positive-prior fiber
has a common maximizing decision for all its states. Proof: the maximum of the
sum is at most the sum of maxima; equality holds exactly when one decision
attains every positive-weight summand's maximum. This small criterion is an
elementary specialization of established decision theory, not a new theorem.
It can preserve optimal performance while concealing payoff entries, so it must
not be identified with a full-rank payoff observation operator. Additional
fairness constraints change feasible policies and can change the criterion.

**O-toy.** Exactly one of two agents can complete a task, equiprobably. Assignment
d∈{0,1} selects one agent; reward is 1[d=z]. A single disclosed capability bit
passes through a binary symmetric channel of known error e≤1/2. Exhausting all
four deterministic policies gives V=1−e. Without the bit V=1/2. Thus one accurate
bit has value 1/2, a quarter-error bit has value 1/4, and a fair-coin bit has
none. The truthful capability-bit policy is equivariant under simultaneously
swapping agents and state labels. Both agents have assignment probability 1/2
under the symmetric prior, while realized assignment is conditional on ability.
This separates equal ex ante selection probability from equal workload and
realized outcomes. No morally preferred criterion is deduced.

The bit above is an observation of the actual hidden state. Game Fairness's
masking operators instead recover payoff arrays from conditional expectations
over disclosed state mixtures. These are different orientations of a channel.
Bayesian conversion needs a prior; an invertible averaging operator need not
give the participant a perfectly informative one-trial signal. Counting contexts,
scalar measurements, communicated bits and repeated samples are four distinct
budgets. The new Phase 9 identification/stability results should be referenced
from their canonical owner when finalized, not duplicated here.

**What would warrant publication?** A sharp gap between the minimal protocol
for a task and that for certifying a specified shared role symmetry, under a
natural capability class and an explicit privacy/communication constraint.
Basic signal value, anonymity and the fixed-fiber criterion alone are prior
decision theory. Blackwell comparison, decentralized teams, sufficient
statistics, communication complexity and fairness-constrained allocation are
required comparison areas, not cleared territory.

## Model I — symmetric work incentives versus collective performance

**Question I.** Under local information and a specified payment budget, can a
permutation-equivariant utility design make every stable work allocation meet
a specified efficiency bound? Which additional assumptions beyond binary
interchangeability are necessary?

Specify n≥3 agents with binary effort a_i, simultaneous decisions, complete
knowledge of their utility table, and no communication. Let every agent receive
benefit B when all agents exert effort, and pay private cost c for effort:

    u_i(a)=B 1[all a_j=1]−c a_i,
    Phi(a)=B 1[all a_j=1]−c sum_j a_j,
    W(a)=sum_i u_i(a)=nB 1[all a_j=1]−c sum_j a_j.

The game has ordinary exact full player symmetry. The displayed Phi is an exact
potential by direct unilateral differences; no candidate theorem is needed.
If 0<c<B, both all-zero and all-one are strict Nash equilibria. At a partial
profile any contributor can save c by quitting unless they are at all-one;
thus these are the only pure equilibria. All-one uniquely maximizes welfare,
with W=n(B−c)>0; the worst equilibrium has W=0.

More strongly if c<B<nc, all-zero uniquely maximizes Phi, since every partial
nonzero profile has negative potential and Phi(all-one)=B−nc<0. Thus even
global potential maximization can select the worst-welfare equilibrium. For
n=3,B=3/2,c=1 the welfare optimum is 3/2, but the potential optimum is all-zero.
Potential-based convergence and permutation equivariance do not supply an
efficiency guarantee. This is a standard threshold public-good counterexample
calculation; no originality claim.

An external effort subsidy tau changes utilities by tau a_i. If tau>c, effort
strictly dominates shirking, so all-one becomes the unique equilibrium; but
the coordinator pays n tau and must include this cost in its objective.
For tau<c the all-zero trap remains. At equality weak equilibria remain.
Budget-balanced transfers, private costs, verifiability and local observations
are substantive constraints, not cosmetic changes. A serious model must select
which constraints are real. The present example assumes costs are known, so
it is utility design rather than an incentive-compatible revelation mechanism.

The canonical P3-E2 potentially extends potential existence to binary games
with full actual typed player image. It does not imply welfare alignment,
policy convergence under arbitrary updates, a convergence rate, or robustness
for LLM agents. Monderer–Shapley already supplies the finite potential/FIP
implications. An eventual agent result must add a specific constrained design
guarantee, not rename a pure equilibrium as successful cooperation.

## Source verification and comparison, 16 October 2026

Only primary article bodies, publisher records and author-maintained resources
support the statements below. A blocked body is recorded as a gap.

1. **Supplied utility-design link: genuine.** Paccagnan, Chandan and Marden,
   *Utility and mechanism design in multi-agent systems: An overview*, Annual
   Reviews in Control 53 (2022),315–328,
   [DOI/publisher](https://doi.org/10.1016/j.arcontrol.2022.02.002).
   The supplied `/am/pii/S1367578822000062` endpoint returned 403. The publisher's
   indexed article body was readable, including utility-design and conclusion
   passages; the [author publication list](https://web.ece.ucsb.edu/~jrmarden/publications.html)
   independently confirms metadata. It addresses shaping local preferences,
   equilibrium performance, information limits and constrained design. This
   establishes strong prior art against a broad “game theory for coordination”
   novelty claim. No review article is treated as proof of all original results
   it surveys; follow its original design papers before claiming an extension.

2. **Supplied ACL paper: genuine.** Zhu et al., *MultiAgentBench: Evaluating the
   Collaboration and Competition of LLM agents*, ACL2025,8580–8622.
   [Official page](https://aclanthology.org/2025.acl-long.421/) and
   [PDF](https://aclanthology.org/2025.acl-long.421.pdf), pp.8580–8582 directly
   inspected for scope and architecture. It evaluates LLM coordination across
   scenarios and communication structures. It does not make observed model
   behavior a proof about ideal finite utility maximizers. This is an eventual
   benchmark/protocol comparator, not evidence that our groups model LLM state.

3. **Supplied IJCAI2026 claim: verified, not fabricated.** Zeng et al., *A Survey
   on Value Alignment in Agentic AI Systems*, Survey Track,8078–8087,
   [official record](https://www.ijcai.org/proceedings/2026/896),
   [PDF](https://www.ijcai.org/proceedings/2026/0896.pdf),
   DOI10.24963/ijcai.2026/896. The official record and PDF first page and §5
   were inspected; §5 discusses communication and multi-objective alignment.
   Its broad research directions overlap the proposal, but do not establish
   a theorem about our extension or payoff-mask models. Current date matters:
   IJCAI2026 is past, not a future venue in this assessment.

4. **Potential baseline, actual original article inspected.** Monderer–Shapley,
   *Potential Games*, GEB14(1996),124–143,
   [institution-hosted original PDF](https://www.tau.ac.il/~mansour/sem-game-02-03/monderer-potential-96.pdf).
   Printed pp.127–129, definitions, Lemma2.1/Corollary2.2 and Lemma2.3 directly
   inspected. Existence and strict unilateral improvement termination are
   established. Our work example and potential/welfare distinction are controls,
   not a claim to discover the potential method.

5. **Permutation networks are substantial existing work.** Hao et al.,
   *Boosting Multiagent Reinforcement Learning via Permutation Invariant and
   Permutation Equivariant Networks*, ICLR2023. The
   [author repository](https://github.com/tjuHaoXiaotian/pymarl3) (redirects from
   supplied API-Network project found during search) identifies the paper and
   implementation; its [paper link](https://openreview.net/pdf?id=OxNQXyZK-K8)
   hit OpenReview browser verification. Full paper comparison remains open.
   [Agarwal et al.2019 original abstract](https://arxiv.org/abs/1906.01202),
   *Learning Transferable Cooperative Behavior in Multi-Agent Teams*, also
   explicitly claims permutation-invariant transferable multi-agent policies.
   Abstract-level scope only was checked. Do not claim invariance/equivariance
   for policies as a new idea, and do not confuse a network architecture's
   imposed symmetry with the actual game's automorphism group.

6. **Decision/extension literature gaps.** Canonical fairness P8 literature
   compares inspected author expositions of Blackwell dominance and the
   Dekel–Lipman–Rustichini support-function treatment. This assessment reuses
   their documented scope; it did not newly inspect Blackwell's original or
   a general bisimulation/automata or group-cohomology literature. Those gaps
   prevent declaring C or O novel. No funding eligibility or grant availability
   was investigated or inferred from the user's conversational attachment.

## Exact checks and a bounded continuation plan

Run `python3 toy_models.py` in this directory. It uses only integer arithmetic
and `fractions.Fraction`: both C4 lifts, all four signal policies for three
noise levels, and every pure profile/unilateral edge of the three-agent
work game are checked. Assertions establish only these finite examples;
the analytical arguments and canonical results supply general claims. There
are no LLM-agent experiments and no Cortex/Gantry changes.

Recommended next work, conditional on later authorization: (1) specify a real
finite persistent-state reassignment task and complete the state-abstraction
prior-art comparison; (2) use Game Fairness's canonical Phase9 results to set
up a constrained task-versus-certification observation problem; (3) keep the
threshold work game as an efficiency control. Seek a sharp theorem in one of
the first two directions before creating a repository or manuscript. A natural
new algorithm alone may warrant a systems experiment, while a standard
quotient-splitting application alone probably does not warrant a third paper.

## AI contribution and review status

One Codex subagent read both user briefs, inspected the pinned canonical notes,
checked primary source records/passages, formulated the three finite models,
derived the elementary criteria/counterexample calculations, and wrote the
exact script and this report. The user supplied the research direction and
historical programme. All mathematics is labeled as canonical reuse, elementary
specialization, candidate question, or unresolved novelty; no external referee,
human proof certification or empirical LLM result is claimed. On 16 October
2026 the parent Codex agent independently read the entire report and script,
reran the exact examples, and verified both pinned canonical hashes. It found
no mathematical or scope defect in the three models and approved the report.
This is internal AI review. No external contact, submission, author change,
Git initialization or GitHub repository creation occurred.

## Final canonical Phase 9 pins

The completed fairness continuation is now pinned at
`f75ec9f7f0ff3b74226baed67a2727eccf0220d3`, with research results in its
parent `452b413`. See `game-fairness/research/phase9-handover.md` and stable
IDs P9-I1, P9-S1–S3, P9-F1, P9-M1–M2. The updated symmetry review packet is
`e896a5cae79c5c63a81be16f1577bc365e67a5a6`. These supersede the baseline
snapshots only for the completed continuation; source ownership is unchanged.
Existing repositories were committed and pushed independently. This proposal
remains local, with no Git initialization, GitHub repository, third paper,
external contact or unrelated-project modification.
