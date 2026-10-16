# Phase 11 — information resources, symmetry and representation limits

16 October2026. Author Nicholas Ham; root Codex development. Proved candidate
applications of standard search, symmetry and counting ideas; originality is
unresolved. The cost formulas below are calibration results for a whole iid
family, not a new general theory of information acquisition. All resources
and timing are explicit. No companion repository is modified.

## AG-V1: an exact welfare-versus-verification frontier for arbitrary n

There are n≥2 agents with iid private costs C_i∈{l,h}, Pr(low)=p∈(0,1),
0<l<h<B. Exactly one agent will perform a shared-success task, giving each
agent benefit B and charging the selected agent its actual cost. The public
prior and n are known. A coordinator can sequentially query an external
trusted verifier to reveal any one previously uninspected actual cost. Each
query counts one unit of verification; it is not a cheap-talk report. Agents
cannot manipulate the verifier, no transfers are available, and messages
containing private costs, or any other type-dependent signals to the coordinator,
are excluded. Histories, stopping and selection depend only on verifier answers
and randomness independent of costs.
After observing query results the coordinator privately recommends one worker;
that worker completes voluntarily since B>C_i, and the others abstain. All
recommendations are ex-post obedient. Public/private coordinator randomization
is allowed and independent of costs. Query addresses and recommendation costs
are NOT charged as if they were free communication bits: they are outside
this verification-count objective and must be added in a communication model.

Write a=1−p, Delta=h−l, cbar=pl+ah. With no inspection, optimal welfare is
W0=nB−cbar. With true full information first best is
WFB=nB−l−Delta*a^n. Put

  Rstar=sum_{j=0}^{n−2} a^j = (1−a^(n−1))/p,
  v=p*a*Delta.

For expected query budget r≥0, the sharp optimal gross welfare is

  W(r)=W0+v*min(r,Rstar).

For a hard worst-case budget m∈{0,...,n−1}, it is

  W_m=nB−l−Delta*a^(m+1),

and that policy uses expected queries (1−a^m)/p. Exact first-best selection
requires worst-case at least n−1 queries, with minimum expected cost Rstar.
For target w∈[W0,WFB], the minimum expected verification count is
(w−W0)/v. Targets below W0 need zero; targets above WFB are impossible.
If p=0,1 or l=h the types are effectively constant and zero queries suffice;
the displayed divisions are used only in the nondegenerate regime.

**Proof, including arbitrary adaptive/randomized protocols.** If a low cost
has been observed, no further observation can improve the selection cost below
l. If no low has been seen and at least two agents remain uninspected, every
uninspected cost is still iid under the public history. Without another query,
choosing an uninspected agent costs cbar in expectation; known high costs are
worse. A query reveals low with probability p and otherwise high. With a low,
optimal cost falls from cbar to l; with a high and at least one uninspected
agent left, the optimal fallback cost remains cbar. Each such useful query
therefore reduces conditional expected final selection cost by precisely
p(cbar−l)=v. Querying the last uninspected agent cannot improve the selection
because it is already no worse in expectation than known highs and is the
only uninspected option; discovering high leaves all costs high. Repeating
queries or querying after a low is found has zero gain.

Let U count useful queries. Iterated conditional expectation for this bounded
finite search gives cost reduction exactly v E[U] for terminal posterior-
optimal choice, and at most that for any other terminal rule. E[U]≤E[Q]
for total queries Q. The probability a j-th useful query can occur is at most
a^(j−1), for j≤n−1: its predecessors must all be high; adaptive addressing
and independent randomization cannot alter that probability. Hence
E[U]≤Rstar. This proves the expected-budget upper bound. Inspect in a fixed
or independently random order until the first low or n−1 high inspections;
then choose a found low, or the only uninspected agent. It has expected count
Rstar and first-best cost l+Delta*a^n. Mix this entire policy with no inspection
using independent probability min(1,r/Rstar); the linear bound is attained.
With a worst-case cap m, inspect at most m in that same policy; E[U]≤
(1−a^m)/p is sharp, giving W_m by substitution.

For zero-error first best, on a history of fewer than n−1 high observations
there are at least two uninspected agents. Every binary completion has
positive posterior probability. Whatever worker is selected, a possible
completion makes that worker high and another low, so stopping would be
inefficient. Thus inspection must continue until a low is found or only one
uninspected worker remains, proving the sharp worst-case/expected lower bounds.
The argument holds for almost every independent random seed after conditioning on it. ∎

For an exchange-equivariant allocation law, choose an independent uniform
random ordering of agents. The full-search policy, conditional on any cost
profile, selects uniformly
among the minimum-cost agents (and uniformly among all agents when all high).
The inspection-count distribution is unchanged. Truncated and mixed policies
also have equivariant outcome laws, without always selecting a cheapest worker. Thus the optimum can respect
agent permutations at NO additional verification count in this model. Sampling
that ordering may have a randomness/addressing cost; zero cost here does not
claim a free decentralized anonymous implementation.

If each query costs kappa>=0 in the coordinator objective, optimal net welfare is
W0+max(0,v−kappa)*Rstar: choose no useful inspections when kappa≥v, all when
kappa<v. A query budget or intermediate gross target produces the stated
linear frontier, rather than an unsupported global claim about minimum
communication bits. This is a special iid binary optional-inspection problem;
Pandora/nonobligatory-inspection literature is substantial prior art.

## AG-S1: mechanism averaging, and exactly what it preserves

Let z denote a finite direct mechanism vector (recommendation probabilities,
and additional costed resource probabilities if explicitly modeled). Let the
feasible class K be nonempty compact convex, defined by linear probability,
Bayesian joint reporting/action incentive, obedience and budget constraints.
A finite relabeling group G acts linearly on z and preserves K, the prior,
the physical utilities, and a continuous affine objective J(z). Then some optimal
mechanism is G-invariant. Moreover its optimum at each invariant linear
resource budget is unchanged by imposing G-invariance.

Proof. An optimum exists by compactness. The average |G|^(-1)sum_g gz remains
feasible by convexity, has the same invariant objective/resource expectation,
and is fixed by G. This is standard averaging, explicitly present for
honest/obedient mechanisms in Battaglini–Palfrey2024 p10 footnote12. It is NOT
an original general symmetry theorem. It also does not assert that the averaged
mechanism retains a particular nonconvex implementation architecture.

Invariance alone is insufficient: on the two-coordinate probability simplex,
coordinate exchange preserves J(z)=z_1^2+z_2^2, but only the noninvariant
vertices maximize it. This failed broader statement is retained explicitly.

For example, consider n identical agents and a task requiring exactly one
active agent. A product action law has zero-error success only when one agent
is surely active and every other surely inactive. To prove this, if a product
law assigns positive probability to exactly one active agent i, every other
agent has positive probability of inactivity. If i is not surely active,
all-inactive also has positive probability, a contradiction. Then any other
agent with positive active probability creates two-active with positive
probability. Thus the only zero-error product laws are designated workers.
They form a permutation orbit with no invariant product law for n>1.
Their averaged joint law is feasible under shared role-labelled correlation
but is not product. Convexifying the architecture has changed its resources.

No fixed message alphabet, private independence or decentralized-state budget
is automatically preserved by group averaging. One sufficient implementation
condition is closure under the relabeled protocols plus a public selector seed
whose value every agent can interpret using its role labels. The seed then
selects one whole feasible protocol before types/reports. Conditional honesty
and obedience are preserved if each selected protocol is itself honest and
obedient, and type-independent seed selection does not reveal private types.
Its randomness/communication cost belongs in the budget.

### A precise elementary randomness diagnostic

At a fixed input with finite stabilizer H, let E be a finite nonempty allowed
output set, stable under H. Its invariant distributions are mixtures of uniform
laws on H-orbits. Their minimum support size is the smallest orbit size m;
the minimum Shannon entropy (bits) is log2 m, since
H(output)=H(orbit)+sum_O weight(O) log2|O|. A deterministic decoder of an
independent finite seed therefore needs seed entropy at least log2 m.

For a UNIFORM b-bit seed and a deterministic decoder, exact invariant selection
is possible iff 2^b is a nonnegative integer combination of allowed orbit
sizes. Each member of an orbit needs the same integer number of seed atoms;
conversely assign those atoms equally. If E is one orbit of size3, no fixed
finite number of fair bits suffices. Two bits with rejection of one pattern
implement the uniform law with expected8/3 bits but unbounded worst-case bits.
This is a centralized exact-sampling fact, not a new anonymous leader-election
or arbitrary communication lower bound. Bias, approximation, role visibility
and stopping semantics change it.

## AG-H1: one action orbit need not make succinct payoff evaluation easy

Take any Boolean circuit F on n≥2 binary inputs. Let r be cyclic coordinate
rotation and c bitwise complementation. Construct n identical payoff functions

  u_i(s)=(1/(2n))*sum_{j=0}^{n−1}[F(r^j s)+F(c r^j s)].

This rational arithmetic/Boolean circuit has size polynomial in n and |F|,
not a local explicit factor table. Bare player rotation and simultaneous local
bit complementation generate exact typed automorphisms of this common-interest
game. They act transitively on all player-action pairs, so q=1, and their unique
invariant independent mixed profile is iid fair bits. It is Nash: conditioning
on one agent's action, complementation bijects the fair opponent configurations
and equates the two conditional payoffs.

Every rotation/complement is a permutation of the 2^n inputs. Therefore

  E[u_i(fair profile)] = # {s:F(s)=1}/2^n.

An exact polynomial-time expected-payoff evaluator on this succinct q=1 class
would count satisfying assignments of every Boolean circuit in polynomial time.
This is an explicit counting-SAT reduction, using the standard counting
complexity baseline, not a claim to invent succinct-game hardness. It
unconditionally proves the reduction; interpreting it as impossibility relies
on the usual counting-complexity separation assumption.

The statement concerns VALUE EVALUATION, not finding an invariant NE: the
profile is visibly uniform and computable without evaluating any payoffs.
Nor does it refute an eta-optimal-profile algorithm that need not output its
value when there is only one invariant profile. It establishes precisely why
runtime guarantees must retain input representation and expected-deviation
access. Counting orbits and writing down a profile do not provide a welfare-value
oracle. In this construction invariant regret is identically zero, so no
regret-evaluation hardness follows. This applies to compact global task-verification objectives;
it makes no empirical claim about an LLM or a restricted local-interaction game.

## Status and source boundaries

AG-V1 is a special optional-inspection calculation, AG-S1 is established
averaging, and AG-H1 is a standard-style counting reduction. No entry is
novelty-cleared. Their purpose is to expose precise architecture/representation
boundaries rather than produce many toy propositions. See phase11-literature.md
for inspected prior statements and source-access qualifications. Proof and
counterexample reviews must be recorded before manuscript promotion.
