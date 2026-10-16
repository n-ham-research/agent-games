# Five broad questions after Phase 11

16 October 2026. Rank 1 is highest overall priority. Ratings are qualitative
research judgments, not claims that a proposed theorem is true. S/G/N/T/A mean
significance, generality, potential novelty, tractability, and agent-system relevance;
H/M denote high/medium. Prior statements are linked in phase11-literature.md.

| Rank | Question | S/G/N/T/A |
|---|---|---|
| 1 | Incentive-preserving compressed representations | H/H/H/M/H |
| 2 | Verification–incentive–reliability frontier | H/H/H/M/H |
| 3 | Decentralized cost of symmetry-preserving implementation | H/H/H/M/H |
| 4 | Optimal equilibrium selection beyond invariant Nash | H/H/H/M/H |
| 5 | Approximate symmetry under learned payoff error | H/H/M/H/H |

## 1. Which compact representations make action-orbit algorithms useful?

Known: Tewolde action-orbit polynomials; graphical-neighborhood symmetry;
compact CE algorithms; this phase's explicit-factor adaptation. Gap: q alone
does not bound expectation cost for circuits, and payoff-table input can already
be exponential. Candidate: a representation theorem giving f(q,k) poly(L,log1/ε)
invariant-Nash computation whenever conditional expectations admit efficiently
constructible degree-k orbit polynomials, with matching evaluation barriers for
representations outside this class. Separate representation recognition,
automorphism certification, polynomial construction and strategy reconstruction.
First experiment: ordered local factors on cycles and hypergraphs, not fully
anonymous games. Application: central coordination of bounded local task
interactions. A theorem merely restating the polynomial encoding is insufficient;
identify a substantial new representation class or prove a necessary barrier.

## 2. What replaces flat workload when service may fail and verification costs?

Known: honest-and-obedient collective-action mechanisms; guaranteed-success
screening specialization P11-M5; binary trusted-query calibration AG-V1. Gap:
sharp welfare versus failure, verification and communication for heterogeneous
finite independent costs and general success families. Candidate: dual lower
bounds, tight for threshold/coverage families, on information or subsidy needed
to exceed the minimum-mean-coalition benchmark at reliability1−δ. The candidate
is open, not implied by the binary upper bound. Begin with three agents,
three costs, a two-contributor task and verified subset queries. Application:
redundant distributed execution with costly capability certification.

## 3. When does convex averaging have an economical distributed realization?

Known: group averaging preserves affine objectives and linear incentives;
anonymous-election and exact-sampling theories already address symmetry breaking.
Gap: averaging does not preserve private independence, message alphabets or
bounded seeds. Candidate: characterize realization of equivariant mechanism
kernels by a specified public-seed, local-message and visible-role architecture,
with additive resource bounds expressed through stabilizer output orbits and
communication complexity. The entropy diagnostic is only a necessary centralized
bound. Start with transitive cyclic groups, then nontransitive typed roles.
Application: distinguish a central recommendation service from deployable local
policies. Any result must specify shared knowledge, IDs, timing and errors.

## 4. Can efficient incentives be selected without sacrificing them to invariance?

Known: averaging preserves CE and its invariant linear objective, but averaging
independent Nash profiles need not preserve Nash. AG-O1c optimizes only invariant
Nash; the gap to unrestricted Nash can be large. Candidate: characterize local
interaction/group pairs for which a welfare-maximizing Nash equilibrium can be
chosen invariant, or bound the loss using quotient interaction structure.
Anti-coordination rules out a universal equality. Application: decide when a
symmetry restriction is an acceptable welfare design choice. Search finite
potential/team games before making a broad general theorem conjecture.

## 5. What guarantees survive approximate automorphisms?

Known: exact invariance and standard payoff-perturbation regret bounds; neither
gives free symmetry discovery from noisy learned capabilities. Gap: joint
inference, robustness and reconstruction costs. Candidate: if supplied typed
maps form an exact group and distort every pure payoff by at mostδ, solve the
averaged game and lift an invariant ε-equilibrium with regret at most ε+2δ;
then establish sharp sample/query requirements for certifyingδ in local-factor
representations. The first implication is a routine perturbation corollary,
not the ambitious contribution. Application: calibrated learned task costs;
no claim that real LLMs play Nash or possess intrinsic welfare.

Next phase should pursue questions1–2 as the main theorem programme, use3 as
the implementation audit, and retain4–5 as alternatives. Avoid expanding all
five into separate small examples. Publication readiness also requires original
real-algebraic source verification and a decision on whether algorithmic and
mechanism-design narratives belong in one paper.
