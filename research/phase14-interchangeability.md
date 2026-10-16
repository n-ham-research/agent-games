# Phase 14: contextual substitution with observations and all deviations

Status: **proved finite-model preservation statements; established-method
adaptations, originality unresolved**. This branch does not identify game
symmetry with software-agent equivalence. It develops a concrete sufficient
certificate for a component substitution, including stochastic state aggregation,
private observations, persistent private randomness and explicit strategy
semantics. The core ideas have substantial bisimulation and perfect-recall
precedent. The theorem is useful as a correctly scoped model, not a claim to
invent bisimulation or prove equivalence of actual LLM systems.

## 1. Finite component and context model

Fix players `1,...,n` and a finite horizon `H`. An open component has a finite
operational state set `X`, context-input alphabet `E`, joint decision-action
alphabet `A=product_i A_i`, and a joint stochastic step kernel

    K_t(x',o',y,r,b | x,a,e).

Here `o'=(o'_1,...,o'_n)` are the next private observations, `y` is the public
interface output, `r` is a reward record, and `b` records specified resource
usage: tool calls, permission checks, messages, or other declared counters.
All alphabets and supports are finite; kernels are rational for the algorithmic
claims. The component's state may include tool state, internal queues,
permissions and persistent operational memory. Anything a player can inspect
must appear in its observation, not only in an analyst's hidden state.

A context has its own finite state, supplies `e`, updates from the permitted
interface transcript and its own private inputs, and may contain the other
agents, tools and a task monitor. It has no side channel to hidden component
state. Its randomization, observations, timing and payoff computation are
included explicitly when the component and context are composed. A variable-
length protocol can be padded to `H` with a terminal flag and null steps.
This is a synchronous finite semantics, not an asynchronous fairness theorem.

Player `i` has perfect recall of its private observations, its own actions,
and public outputs to which it has access. Write this record as `h_i^t`.
A behavioral strategy specifies an arbitrary probability distribution over
`A_i(h_i^t)` at each such history. The menus `A_i(h)` encode permitted tools
and actions; they must agree under the proposed substitution. Randomization
is independent across players conditional on their respective information.
Correlated recommendations may instead be emitted by the context as joint
private observations. They must not be silently replaced by independent coins.

Utilities are bounded functions `U_i` of the retained semantic record
(abstract component states, unchanged context states, observations/actions,
interface outputs, and reward/resource records), using the same cardinal values on the two systems. Any dependence
on discarded concrete state must be encoded in retained reward labels; it
cannot be omitted and then assumed payoff-irrelevant. Observations need not reveal
reward records or hidden state. For approximate statements let the range width
of `U_i` be at most `R_i`. Nash equilibrium means ex-ante equilibrium among
all these history-dependent behavioral strategies; regret is

    Reg_i(sigma)=sup_tau_i E[U_i(tau_i,sigma_-i)]-E[U_i(sigma)].

It is not automatically sequential equilibrium, subgame perfection, a bounded-
memory equilibrium, or an equilibrium against policies with additional sensors.
A fixed implementation policy is one member of this strategy class. Equality
of its behavior alone does not compare the component's other available policies.

The candidate distinctions in the user brief are thus tests relative to a
specified interface, context class, utility representation and strategy class.
No universal hierarchy among behavioral, strategic, utility, contextual and
computational equivalence is assumed.

## 2. A checkable state-aggregation certificate

Let `phi:X -> Xbar` be surjective. The replacement has the same observation,
action, input, output, reward and declared-resource alphabets, and kernel
`Kbar_t`. For every allowed context, the complete retained initial joint law must be
the pushforward of the original joint law: this includes abstract component
state, context state, private task/context inputs, initial observations and
any initial public/reward/resource records, preserving their correlations.
Independent context initialization is a sufficient special case, not an
implicit assumption. Matching only the component-state marginal does not
satisfy this certificate. Require, for every time, original
state, legal joint action and context input,

    sum_(x':phi(x')=v) K_t(x',o',y,r,b | x,a,e)
        = Kbar_t(v,o',y,r,b | phi(x),a,e).                 (L)

This equality is for the **joint** tuple of successor abstract state and all
emitted labels, including correlated private observations. Equality of each
player's observation marginal is insufficient. Action availability is a
function of the retained private history, with identical menus. Condition(L)
is strong probabilistic lumpability with interface labels, checked against all
joint actions, not just the actions selected by a proposed equilibrium.

Hidden states in a fibre may have completely different internal transitions.
Only their aggregated interface laws must agree. In particular `phi` need not
be injective and the concrete system need not be isomorphic to its quotient.
A relation between two components can be certified through a common quotient
with this property on both sides. Local action/observation renamings can be
applied first when they are bijective and preserve the specified information.

**P14-I1: contextual outcome and deviation preservation.** Under(L), composing
the two components with any allowed context gives exactly the same law of
abstract operational states, all observation/action histories, public outputs,
reward records and declared resource records, for every behavioral strategy
profile. Under the history-identification transport, every unilateral deviation
is available on both sides. Expected utilities, all incentive differences,
regrets, Nash equilibria and epsilon-Nash equilibria consequently agree.

### Proof

Use the same complete retained initial draw on both sides, including context
state, private inputs and observations, with a concrete state sampled from
its conditional fibre given that entire draw. Couple context randomization
and each player's independent behavioral coin. As long as the retained
histories agree, the same strategy chooses the same action distribution and
the same context chooses the same input distribution. Condition(L) makes the
conditional law of the next retained tuple identical, regardless of which
concrete state in the current fibre is present. Sample that retained tuple
once, and sample a concrete successor from the appropriate conditional law.
This gives an induction through all `H` rounds. Zero-probability conditioning
branches can be filled arbitrarily because they never occur.

This argument is uniform over all admissible strategies, not only a fixed
profile. The two systems have the same private-history policy domains and
menus. Therefore any concrete unilateral behavioral deviation is literally an
abstract deviation on those histories, and conversely. The coupling applies
to every such deviating profile. Subtracting the identical baseline payoffs
and taking the same suprema proves equality of incentive differences and
regrets. Equilibrium equivalence follows. QED.

The same induction proves contextual composition: carry the context state
unchanged in the relation `(x,z) ~ (phi(x),z)`. The context's next-step kernel
is a function only of retained histories/ports, so summing over a component
fibre commutes with composing its kernel. Arbitrarily adaptive contexts are
allowed within this finite boundary. A context that reads discarded memory,
changes available actions, or observes unrecorded timing violates that boundary.

This is stronger than matching one default trace, but it does not claim that
ordinary state bisimulation with unrestricted state-history strategies preserves
NE. Here players cannot condition on discarded operational states. The
information restriction is part of the certificate, not an inferred consequence
of similar-looking software or equal state labels.

## 3. Erasing independent persistent private randomness

An operational refinement sometimes adds local coin memory that a player can
read, without revealing task-relevant information. This changes the literal
history alphabet, so the identity argument alone no longer suffices. There is
still an explicit all-deviations transport under perfect recall.

Allow a player's controller an initially independent finite private seed
`omega_i` and private coin-memory updates. The seeds are independent across
players and independent of all initial task/context randomness. The controller
can use its ordinary private history and seed, but the seed/memory can affect
the outside system **only through its declared actions**. No direct timing,
resource, permission or communication side channel is erased. With finite
horizon and finite private coin supports, all its private randomness can be
unrolled into one finite seed containing a coin for every possible local
continuation. Write its resulting deterministic policy as `f_i(h,omega_i)`.

For a history `h_i=(o_i^0,a_i^0,...,o_i^t)`, let `C_i(h_i)` be the seeds
consistent with all that player's previous actions along that history. Define

    beta_i(a | h_i)
      = sum_(omega in C_i(h_i)) nu_i(omega) 1[f_i(h_i,omega)=a]
        / sum_(omega in C_i(h_i)) nu_i(omega).             (P)

At a zero denominator choose any legal action. Such a history is unreachable
under this player's controller against every opponent profile: its own prior
actions would contradict every supported seed.

**P14-I2: private-memory elimination with all-opponent realization.** Formula(P)
replaces the seeded controller by a behavioral perfect-recall strategy with
the same complete outside-record law against **every** opponent profile and
allowed context. It is computed from the controller and its own history,
without knowing the opponents' strategies. Every behavioral strategy can be
implemented by an independent private random tape. Therefore enlarging the
admissible policy classes by this independent private-memory refinement changes
neither attainable profile laws nor unilateral regret, and transports NE and
approximate NE in both directions. Combining this transport with P14-I1 gives
the same conclusion after a stochastic state quotient.

### Proof of the opponent-independent posterior

Fix a full history of outside states, observations and actions compatible with
`h_i`. Its probability conditional on player `i`'s seed factors into the
indicator that the seed prescribes its recorded own actions, multiplied by a
factor from the environment, context and opponents. The latter factor does
not depend on this seed: by hypothesis all its effects on the outside system
are already specified by those recorded own actions. Summing compatible
outside histories preserves that factorization. Bayes' rule gives exactly the
prior restricted to `C_i(h_i)`, with no opponent-dependent likelihood factor.

For several independently seeded controllers, their conditional seed law
factorizes into these separate compatibility posteriors given a complete
outside history. Thus the next joint action law is the product of the(P)
behavioral laws. Induction proves equality of the whole outside-record law.
Fresh independent random tapes implement a behavioral strategy in the other
direction. These transports apply separately to each player's controller,
independently of all opponent choices. Every seeded deviation maps to a
behavioral deviation, and every behavioral deviation lifts back; hence the
suprema defining unilateral regrets agree. QED.

This is a finite operational version of the mixed/behavioral realization
principle under perfect recall, not a new claim about Kuhn equivalence.
The hypotheses exclude shared seeds, private information about the task,
side-channel disclosures and forgetting ordinary observations/actions. All
four exclusions matter.

### Explicit finite-controller implementation and its cost

For an explicit `M_i`-state private controller, formula(P) need not enumerate
all seeds. Maintain weights on its memory modes. Given a chosen action,
condition the weights by the controller's action probabilities; propagate them
through its private memory-update matrix using the observed local history.
There is no additional observation likelihood factor because of the proved
independence. This uses `O(M_i^2)` rational operations per update, plus action
sampling, when those matrices are supplied explicitly. Rational bit lengths
grow polynomially in `H,M_i` and the input rational lengths by multiplying
common denominators and summing finite products.

This filtered behavioral implementation may require a vector of rational
weights and perfect recall. It is **not** a controller with the same number
of memory modes or the same execution cost. Writing its full history table
may be exponential in `H`. A compressed input controller or simulator does
not make its posterior cheap by definition. Thus strategic realization
preservation does not establish bounded-memory or computational interchangeability.

## 4. Approximate interface laws imply a regret bound

Replace(L) by a total-variation row error at most `delta_t`, uniformly over
all concrete states, inputs and legal joint actions; retain the same menus and
observation alphabets. Initial retained laws agree. Let

    rho = min(1, sum_(t=0)^(H-1) delta_t).

**P14-I3.** For every allowed context and strategy profile, the outside-record
laws have total-variation distance at most `rho`. For utilities with range
width `R_i`, their expected values differ by at most `R_i*rho`; the regrets
of identified profiles differ by at most `2 R_i*rho`. In particular an
`epsilon`-NE transfers to an `(epsilon+2 R_i*rho)`-NE. The same statement
holds after the exact private-memory transport of P14-I2.

**Proof.** Couple equal histories, actions and context inputs until the first
mismatching retained step. Conditional on no earlier mismatch, maximal
coupling of the two next-step rows fails with probability at most `delta_t`.
A union bound gives failure probability at most `rho`; after a mismatch no
further coupling agreement is needed. This bounds total variation of the
complete record. The expected-value bound for a function of range width
`R_i` follows. Each unilateral gain subtracts two expectations, so its error
is at most `2 R_i*rho`, uniformly over all deviations. Taking the suprema in
both directions proves the regret statement. QED.

For a sum of `H` stage rewards in `[0,1]`, the safe range width is `H`, not
one. Declared cumulative resource statistics must likewise have a stated
range before obtaining an expectation-error bound. If an interface admits
hidden observations outside these common alphabets, a small error in public
outputs alone does not give this theorem.

The factor two in converting uniform payoff error to regret error cannot
in general be dropped. In a one-step one-player system, compare binary reward
probabilities `(1/2,1/2)` with `(1/2-epsilon,1/2+epsilon)`:
row error is `epsilon`, the first action is an original equilibrium, and its
replacement regret is `2epsilon`. This latter example attains the bound
`2 R_i rho` with `R_i=1`.

## 5. Why weaker tests fail

**Open-loop trace and reward laws miss private information.** Nature draws a
fair bit `b`. At the last stage one player guesses it and is paid
`1[guess=b]`. One component privately reveals `b` beforehand; another emits
only a blank. Both have identical public output and reward laws under every
fixed open-loop guess. In the blank component any fixed guess is optimal
with value `1/2`. Its constant-guess transport into the informed component
has regret `1/2`, since observing the bit permits value one. There is no
information-compatible all-deviations lift. Passive/open-loop contextual
classes are too weak for the claimed strategic conclusion.

**Matching each private marginal is not enough.** Two agents play an anti-
coordination game, receiving payoff one iff their bits differ. Before actions,
compare independent fair private bits with a common fair bit sent privately
to both. Each agent's observation marginal is the same. The policy copying
one's signal is a NE in the independent case, with payoff `1/2`; with the
common signal it yields zero and flipping one's recommendation has regret
one. The *joint* private observation kernel must be preserved, including its
correlation with task state and other agents' signals.

**An equal default trace does not preserve permissions.** A component exposes
only a null command; a replacement additionally permits an exploit yielding
utility one. The default null policy has exactly the same trace and utility
zero in both. It is an equilibrium in the first one-player system and has
regret one in the replacement. All action menus, not just exercised commands,
are part of strategic interchangeability.

**Independent private memory cannot be erased inside a memoryless class.**
With no observations, a controller samples one private fair bit and repeats
it at two times. Its outside action law assigns probability `1/2` each to
`00,11`. A behavioral controller with one constant memory state and fresh
independent fair randomization at the two times gives all four strings with
probability `1/4`. No such memoryless behavioral controller realizes the
persistent-coin law: equality of the first marginal forces probability
`1/2`, and independence then prevents the required perfect correlation.
With perfect recall, the second action can copy the remembered first action,
as P14-I2 permits. This is a failure of a resource-preservation claim, not a
counterexample to perfect-recall realization.

**Utility and computational distinctions.** Identical physical traces can
carry different private effort costs and hence different best responses.
Conversely all utilities can be constant while public outputs differ.
Controllers can have the same strategic laws but very different sampler or
memory costs. Thus none of these candidate labels alone establishes the
others without the declared tests and utility/resource conventions.

## 6. A limited necessity statement with resettable tests

A necessity theorem depends on the permitted contexts. Suppose a testing
context can reset a component to any specified concrete state, choose any
legal input/joint action, and read the entire next retained tuple
`(phi(x'),o',y,r,b)`. It can award a terminal indicator reward for any subset
of that finite tuple alphabet. If substitution preserves the expected reward
of every such one-step test, then(L) is necessary: singleton indicator tests
recover every row probability. The converse is immediate from(L).

This is an exact restricted testing characterization. It is not a theorem
that arbitrary passive trace equivalence implies a state bisimulation, nor
that an actual user can initialize or inspect hidden software state. Without
these reset/read capabilities a quotient condition may be sufficient without
being necessary. Outcome tests also cannot infer equality of unmodeled
execution costs.

## 7. Computation and evidence

For explicitly listed finite kernels, checking(L) and constructing a proposed
quotient requires summing rational entries by `phi` and comparing each
state/action/input row. This is polynomial in that full table's encoding
length, including joint-action and joint-emission dimensions. Those dimensions
may already be exponential in the number of players or factored inputs.
No polynomial semantic equivalence test for arbitrary programs is claimed.
Exact rational sampling uses uniform-integer rejection with expected bit/time
cost charged; arbitrary rational kernels need not have bounded-depth fair-bit
implementations.

`experiments/phase14_interchangeability.py` and its tests give a genuine
four-hidden-state to two-state quotient, two adaptive contexts, all pure
perfect-recall policy choices for a two-round two-player example, and
independent private-seed versus posterior-policy realization checks. They also
retain the information, joint-signal, permission, memory and approximate-regret
counterexamples. These are finite checks of the displayed models, not empirical
agent experiments or a proof for all stochastic programs.

## 8. Primary comparisons and originality limits

[Gutierrez–Harrenstein–Perelli–Wooldridge2019](https://arxiv.org/pdf/1808.09213),
*Logical Methods in Computer Science*15(3:32), primary 49-page article accessed.
Section4 Theorems4.1,4.3,4.8 already preserve Nash equilibria under
bisimilarity for explicitly chosen computation-based, trace-based and
bisimulation-invariant strategies. Theorem4.5 supplies the negative result for
ordinary run-based strategies; §6 treats nondeterminism. The inspected text
is not a general quantitative stochastic/private-observation theorem. Our
all-deviations and observation-history restriction has the same essential
purpose as their strategy-semantic restrictions. Equilibrium preservation by
appropriately restricted bisimulation is prior, not new here.

[Alur–Henzinger–Kupferman–Vardi1998](https://www.cs.huji.ac.il/~ornak/publications/concur98.pdf),
*Alternating Refinement Relations*, primary16-page author PDF accessed.
Its alternating simulation/bisimulation quantifies coalitional choices against
environmental choices and preserves the corresponding strategic temporal
properties. Our condition fixes a common labeled joint-action interface and
preserves its probability row for every action, a stronger concrete certificate
than merely matching a coalition's enforceable successor sets. The paper does
not justify silently transporting general-sum deviations with different
observations; its game-sensitive refinement principle is clear prior.

[Larsen–Skou, preliminary report](https://homes.cs.aau.dk/~srba/courses/FS-07/probabilistic_bisimulation.pdf),
primary9-page text accessed, defines probabilistic tests and separates process
relations; this is explicitly the preliminary report, not an authenticated
copy of the 1991 journal version. Its probabilistic-bisimulation/testing
programme is prior. [Edalat–Desharnais–Blute–Panangaden1997](https://www.cs.mcgill.ca/~prakash/Pubs/lics97.pdf)
is a primary author-hosted precursor extending probabilistic bisimulation to
Markov processes; Definitions 5.2–5.3 give surjective zigzag maps with exact
pushforward transition equality and bisimulation through spans. This is direct
prior for the probabilistic quotient certificate used here. No novelty is claimed for probabilistic lumpability or a
finite-horizon coupling/total-variation bound.

P14-I2 is a direct perfect-recall realization adaptation of the classical
mixed/behavioral equivalence principle. It is proved above instead of treating
it as an unexamined strategy correspondence. The original1953 Kuhn chapter
was not obtained in this branch. The primary modern comparison
[Heymann–De Lara–Chancelier, Kuhn’s Equivalence Theorem for Games in Product Form,
arXiv v2 (2022)](https://arxiv.org/pdf/2104.05249) was inspected at Theorem 17
and the §5.1 proof architecture: perfect recall gives mixed/behavioral
outcome-distribution equivalence, using conditional distributions and sequential
substitution. Its broader measurable product-form setting reinforces that
P14-I2 is an explicit finite implementation adaptation, not a new private-memory
equivalence principle. We do not replace its quantifiers with an unstated
uniformity claim: our opponent-independent finite posterior is proved directly.
The elementary reset/indicator necessity result and payoff-error-to-regret step
are also standard consequences.

**Assessment.** This branch supplies a rigorous usable specification for
agent-component substitution, with many-to-one stochastic state aggregation,
explicit correlated private observations, all-opponent deviation transport,
and resource limitations. It is more substantive than a static game
isomorphism observation, but the strongest present novelty claim is a scoped
synthesis and application framework, not a newly discovered general equivalence
theory. A genuinely new next step would require weaker checkable contextual
certificates, nontrivial bounded-memory/resource-preserving transports, or a
sharp necessity characterization for a useful restricted software context class.
No hierarchy, actual-LLM guarantee or computational speedup is inferred merely
from observational similarity.


## Independent review and verification record

The continuation branch independently reconstructed P14-I1–I3. It identified
one genuine wording gap: utilities originally referred to a complete record
without explicitly excluding discarded concrete state. The statement now
requires utility factorization through the retained record, including emitted
reward/resource labels. Root review also made initialization explicit: the
matched initial law is joint with context state/private inputs and retains
their correlations, rather than merely matching the component marginal. With that repair, the reviewer reported no further
defect in joint-label aggregation, opponent-independent seed posterior
transport, or the uniform total-variation/regret bound.

The owned exact experiment suite passes nine tests. It checks all 128 pure
profile/context pairs in the two-round many-to-one model, all unilateral pure
deviation regrets, private-seed realization against pure and mixed opponents,
three failed weaker equivalences, the memory limitation, and the sharp
one-step factor-two regret bound. These finite checks support examples and
implementation; the all-context claims rest on the proofs above.

Reciprocal review of **P14-A** in `phase14-continuations.md` independently
reconstructed success-preserving deletion, CE obedience after deletion, and the
canonical-column argument. The exact claim is the protected players’ payoff
projection together with success probability, not the full payoff region or
an arbitrary welfare optimum. With an explicitly supplied minimal-winning
hypergraph of m edges and k protected players, the candidate set has at most
(m+1)2^k columns and O(n) obedience rows. Incidence testing and rational LP
therefore give 2^{O(k)} poly(n,m,L) construction time; no uncharged enumeration
of an implicitly represented winning family is available. The positive-margin
version needs the stated bound on deleted workers’ costs. No defect was found.
The cost-blind endpoint-constraint envelope and simultaneous-type attainment
were also reconstructed, including the distinction between Bayesian obedience
and a CE condition imposed separately at every hidden type vector.

Reciprocal review of **P14-Q** in `phase14-complexity.md` independently checked
the constant-epsilon adversary. An adaptive zero-table transcript exposes at
most NQ oracle strings; changing only unseen entries preserves the transcript.
The approximate-invariance diameter bound controls every opponent-profile atom,
and the displayed probability and regret constants give the claimed
contradiction. The actual action-orbit count follows from the constant own-zero
versus nonconstant own-one payoff slices, without supplying full automorphism
generators. The zero-error randomized extension legitimately intersects finitely
many probability-one correctness events for fixed n. This is an oracle lower
bound, not an explicit-circuit input lower bound or a Monte Carlo lower bound.
No defect was found. These were separate algebraic reviews of the supplied
proofs, not independently discovered theorems or an independent code rewrite.
