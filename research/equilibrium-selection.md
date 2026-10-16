# Equilibrium selection: fixed points, private types and implementation

16 October 2026. Status labels are essential: AG-E1 is an established theorem
with a reconstructed proof; AG-E2 is standard group-action selection;
AG-E3--E5 are exact model comparisons/counterexamples, with novelty unresolved.
Author: Nicholas Ham. Initial reconstruction, models and tests: root Codex.
No software agent is assumed to have welfare interests or a fixed hidden
utility merely because it can be represented as a player.

## AG-E1: the mixed-equilibrium obstruction suggested in the brief is absent

Let Gamma be any finite game and G a finite group of its CARDINAL typed
automorphisms. Typed maps act on independent mixed profiles by transporting
player marginals and their pure action labels. There always exists a mixed
Nash equilibrium x with gx=x for EVERY g in G. No splitting of the player
projection or strategy-trivial matching is required.

This is established mathematics, not a new discovery. For exact automorphisms
Nash's 1951 result is explicitly recalled as Theorem7 in the directly inspected
long author version of Tewolde et al.2025. The cardinal formulation follows
from preservation of best responses (canonical Game Fairness U5); alternatively
use its canonical cardinal normalization. Pure NE or an efficient subset can
lack a fixed point, but the whole mixed NE set cannot in this finite model.
Thus “automorphisms permute equilibria with no fixed equilibrium” requires a
restriction such as PURE equilibria, efficiency or implementation. It is
incorrect as an obstruction to mixed-profile selection here.

**Independent proof reconstruction.** The mixed-profile space X is a product
of finite simplexes. G acts affinely by marginal permutations. Its fixed set
X^G is compact convex nonempty: average any profile as a vector of marginals.
For x∈X^G, BR(x) is a nonempty compact convex product of best-response
simplexes. Cardinal automorphisms preserve preferences, so BR(x) is G-stable.
Averaging any y∈BR(x) gives a fixed best-response profile. Hence
B(x)=BR(x)∩X^G has nonempty compact convex values and a closed graph. Kakutani
on X^G supplies x∈B(x), a G-fixed mixed Nash equilibrium. Averaging arbitrary
EQUILIBRIA is not this proof: their average need not be an equilibrium.

Ordinal automorphisms preserve pure best-response orders against pure opponents,
so act on pure NE, but need not act on mixed NE. Do not apply E1 to them:
Game Fairness U5 has the explicit ordinal/mixed counterexample at pinned commit
f75ec9f7f0ff3b74226baed67a2727eccf0220d3. No counterpart result is silently
assumed for a Bayesian or dynamic game.

## AG-E2: abstract selection and its actual restrictions

For a game class closed under a specified finite relabeling group, a
relabeling-equivariant deterministic selector from a nonempty relabeling-equivariant solution
correspondence exists iff each input stabilizer fixes some solution.
Necessity: a stabilizer element must fix the selector's output. Sufficiency:
choose a fixed solution on one representative per game orbit and transport
it; stabilizer fixedness makes this independent of the transporting map.
This is a set-theoretic existence statement, not a continuous, measurable,
efficiently computable or decentralized selection theorem.

For one game and finite G, average a point mass at any solution over G to
obtain an invariant finite-support probability measure on solutions. This
works even if its equilibrium set is infinite. It is a lottery OVER mixed
profiles or over pure profiles, not their marginal average. If every support
point is a Nash profile, drawing that profile then independent actions gives
a correlated-equilibrium distribution on actions: each product equilibrium
satisfies every CE linear incentive inequality and their convex mixture does.
Its marginal-average product need not be NE or reproduce the joint law.

For exact G and a continuous G-invariant objective J, a maximizing mixed NE
exists by compactness. Averaging its orbit as a lottery preserves maximum J
and G-invariance. A deterministic maximizing fixed NE need not exist.
Summed utility is such an objective only with the specified common numerical
calibration; independent role-affine recodings do not preserve that sum.
An external task-success objective may be specified instead, avoiding an
interpersonal sum. None of this asserts the selected outcome is normatively fair.

### Exact anti-coordination witness

Two players choose 0 or1; both receive 1 if actions differ and0 otherwise.
Bare player exchange and simultaneous action complementation are exact
symmetries. Pure NE are (0,1),(1,0); neither is fixed by player exchange.
The unique fully mixed NE is (1/2,1/2); it is fixed but yields task
success1/2 and total receipt1. A fair lottery on the two pure NE yields
success1 and total receipt2 and is invariant. Thus efficient equilibrium
selection forces randomization OVER profiles if it must respect player
exchange, despite the existence of a deterministic symmetric mixed profile.
The anti-coordination example itself is established (Cheng et al.2004,
Table1c), not a new counterexample.

**Anonymous implementation limitation.** Suppose both agents use the SAME
local policy, have identical observations, can read a public random variable R
with the same interpretation, and have IID private random seeds
conditional on R. With no distinguishable roles or communication, their binary
actions are IID Bernoulli(p(R)). Their success probability is
E[2p(R)(1−p(R))]≤1/2. Public randomness alone does not implement the efficient
anti-correlated lottery under these anonymity constraints. The bound is attained
by independent fair actions, and these actions form the mixed NE.
A device sending private complementary recommendations attains success1,
obeying CE incentives. Alternatively, distinguishable role labels plus a
public fair bit let agents choose opposite actions; this drops the identical-
observation restriction. The impossibility concerns an explicit architecture,
not an impossibility of randomized equilibrium selection or all communication.
It is closely related to prior anonymous symmetry-breaking and zero-shot
coordination work; no novelty claim is made.

## AG-E3: finite Bayesian volunteer game and a sharp mediation gap

**Complete model.** Two agents have private costs theta_i in {1/2,3/2},
independently equiprobable under a common known prior. Each sees only its own
cost before choosing a_i in {0,1} simultaneously; there are no reports or
transfers in the base game. If at least one agent volunteers, both receive
benefit2; a volunteer additionally pays its cost. Thus

  u_i(a,theta)=2*1[a0+a1≥1]−theta_i*a_i.

A behavioral policy chooses a probability of volunteering at each own type;
private random seeds are independent. The externally calibrated total receipt
is W=4*1[a0+a1≥1]−theta0*a0−theta1*a1. The ex-ante environment is invariant
under simultaneous agent/type-coordinate exchange. At mixed cost profiles
the realized game is not invariant under bare player exchange. Interim beliefs
are conditional on own type by the disclosed iid prior; at equal own-type
labels the two agents have identical interim problems. No claim equates
ex-ante symmetry with every type profile's stabilizer.

**(a) Unique symmetric BNE.** It is volunteer at cost1/2, abstain at cost3/2.
Let alpha,beta be the shared probabilities at low/high type and
q=(alpha+beta)/2 the opponent's volunteering probability. The gain from
volunteering rather than abstaining is 2(1−q)−theta. If q<1/4, both types
strictly volunteer, contradicting q<1/4; if q>3/4 both abstain, contradicting
q>3/4. If q=1/4 the low type must volunteer and q≥1/2; if q=3/4 the high
type must abstain and q≤1/2. In the remaining interval low volunteers and
high abstains, yielding q=1/2 and strict gains +1/2 and−1/2. This is the
unique symmetric behavioral BNE; it has expected welfare5/2. Asymmetric
BNE do exist: a designated agent volunteers at both types and the other
always abstains. This has expected welfare3 but privileges a role.

**(b) An information-and-correlation gap, not merely equilibrium existence.**
Allow any publicly randomized local policies, distinct across labeled agents,
but the public randomness is independent of the private types and there is
no private-type communication or correlated private device. Conditional on
the public seed, expected welfare is multilinear in the four local behavioral
probabilities. Its maximum occurs at a deterministic type policy for each
agent. There are four policies N (never), L (low only), H (high only), A(always).
The exact welfare matrix, rows/columns N,L,H,A, is

       N     L     H     A
  N    0    7/4   5/4    3
  L   7/4   5/2    2    11/4
  H   5/4    2    3/2    9/4
  A    3   11/4   9/4    2

Therefore welfare≤3 for ALL such protocols, whether or not obedient. This is
attained by a designated volunteer (itself BNE); mixing the two designated
profiles with a public fair bit gives an ex-ante exchange-invariant selection
law and the same welfare. Conditional on the seed, it selects a BNE. It is
NOT an independent mixed BNE after the seed is hidden; it is public correlation.
If anonymity additionally requires identical local code and observations,
then conditional on every public seed, the same conditional local action
policy (including its private randomization law) is used. The optimal
unrestricted symmetric policy welfare is41/16, NOT the symmetric-BNE value5/2.
It is attained by low volunteering surely and high volunteering with probability
1/4, which is not an equilibrium. To prove the bound, put
q=(alpha+beta)/2; W=8q−4q²−(alpha/2+3beta/2),
and for fixed q minimize costs using low type first. On 0≤q≤1/2 this gives
7q−4q², increasing to5/2; on1/2≤q≤1 it gives5q−4q²+1,
maximized at q=5/8 with value41/16. Thus public noise cannot close that
sharper anonymous performance gap. Do not infer equilibrium feasibility from
this team-optimal local policy.

**(c) An informed private mediator attains13/4, obediently.** A trusted mediator
observes actual costs externally (NOT unverified reports), recommends exactly
one minimum-cost agent to volunteer, choosing uniformly at cost ties. The
other receives abstain. At every realized type profile the volunteer's gain
from obedience instead of abstaining is2−theta_i>0. The abstainer would
only add their cost by deviating, so obedience holds ex post and hence
conditional on own type and private recommendation. This defines a Bayes
correlated recommendation scheme for the original private information.
It attains the ex-post welfare optimum at every type profile: at least one
volunteer is better than none since min cost<4; adding a second only costs
more. E[min cost]=3/4, giving welfare4−3/4=13/4. This beats the best public-
randomness/no-type-communication architecture by exactly1/4 and its symmetric
BNE by3/4. The scheme is equivariant in distribution, including tied types.
These bounds separate information, public correlation, anonymous local policies
and private recommendations; they are not universal communication lower bounds.

**(d) Types are not costlessly elicited.** If the mediator instead trusts reports,
the truthful recommendation rule with fair reported ties is not incentive
compatible without transfers or verification. A low-cost agent facing a high-
cost opponent is surely selected when truthful and selected with probability
1/2 after falsely reporting high; the benefit remains2 and expected cost drops
from1/2 to1/4. Facing a low-cost opponent, false high avoids volunteering while
the opponent does so, also improving expected receipt by1/4. Thus the deviation
is profitable even interim under the stated prior. The obedient externally
informed mediator is not a truthful direct mechanism.

This is an explicit finite counterexample campaign, not a claim to invent the
volunteer's dilemma, Bayesian mediation or information design. Related Bayesian
correlated equilibrium literature must be compared before promoting novelty.

## AG-E4: the Bayesian existence statement needs its own proof

Consider a finite Bayesian game with nonempty finite types/actions, common
prior, and positive marginal probability of each type retained in the model.
A Bayesian automorphism must transport types, actions and prior, and preserve
for every agent/type the ordering of conditional expected-payoff deviations
under that transport (exact preservation suffices). Ex-ante utility equivalence
alone is not enough to assume this interim property.

The behavioral space is the product of simplexes over every agent/type pair.
Conditional expected payoff is linear in the focal behavioral choice with
others fixed, so its interim BR product has nonempty compact convex values
and closed graph. The finite Bayesian automorphism group acts affinely on
this space. At a fixed behavioral profile its BR product is invariant. The
same fixed-space Kakutani construction as E1 gives an invariant behavioral
BNE. This is a direct standard fixed-point corollary, not a new extension
of the companion's normal-form structural classification. Zero-probability
types can be removed or assigned an explicitly specified off-path convention;
do not divide by zero prior probabilities.

In E3 this yields the actual symmetric threshold BNE, not the efficient
mediator outcome. A realized asymmetric type profile may have a trivial player
stabilizer even though the prior game has an ex-ante swap. The mediator's
output is equivariant ACROSS exchanged type profiles rather than forced to
assign equal actions at a mixed-type realization.

## AG-E5: potential, efficiency and learning controls

Importing the feasibility public-good example gives a fully symmetric exact-
potential game whose GLOBAL potential maximizer is the worst pure equilibrium
for the separately specified welfare objective. This counterexample predates
this repository; do not relabel its import as a new result.

For a positive-welfare price comparison, let n=3 binary agents have common
receipt epsilon>0 at all-zero,1 at all-one,0 otherwise, with0<epsilon<1.
The only pure NE are the two unanimous profiles, both strict. The common
receipt is an exact potential. Pure-equilibrium PoA=max W/min_NE W=1/epsilon
is unbounded, while PoS=1. Thus even ordinary full exact symmetry and an
aligned common-interest potential do not bound equilibrium efficiency.
This is an elementary coordination-game control, not a new price-of-anarchy
theorem. Mixed or correlated price notions need their own specified solution set.

Strict unilateral improvements in a finite exact-potential game increase the
potential and therefore terminate at a pure NE. Simultaneous updates need not:
two-player common-interest coordination, starting (0,1), simultaneous unique
best responses alternate (0,1) and(1,0). Weak better responses may cycle on
plateaus. A fair asynchronous schedule of strict improvements differs from
arbitrary self-play or no-regret dynamics.

For asynchronous log-linear learning, select one player uniformly and redraw
its action with probabilities proportional to lambda^{u_i(a_i,s_-i)}, lambda>0.
In a finite exact-potential game, the unique stationary distribution is
pi_lambda(s) proportional to lambda^{Phi(s)}. Proof: positive transition
probabilities and self loops give irreducibility/aperiodicity; for profiles
s,t differing only in player i the common conditional normalization cancels,
P(s,t)/P(t,s)=lambda^{u_i(t)−u_i(s)}=lambda^{Phi(t)−Phi(s)}.
This gives detailed balance. As lambda→infinity the stationary distribution
concentrates on global potential maximizers, which still need not maximize
welfare (the feasibility example). This is established log-linear-learning
mathematics; exact detailed-balance checks corroborate a toy instance only.
No finite-time convergence rate, decentralized communication guarantee or
no-regret result is inferred from it. The stationary low-noise limit is not
the same as a single best-response path.

## Source positioning and next work

Theorem7 in Tewolde et al.'s long author manuscript explicitly credits Nash1951
for invariant mixed equilibria. Its exact-game setting does not establish
cardinal/ordinal distinctions automatically; those use canonical U5.
Hu et al.2020 and Treutlein et al.2021 directly study symmetry, zero-shot
coordination and labeling constraints, so E2 is not empty territory.
Bergemann–Morris2016 defines Bayesian obedience/consistency and characterizes
outcomes under richer information; E3 is a tiny transparent comparison, not
an alternative general theory. Foundational potential and log-linear learning
are prior. See literature-review.md for inspected passages and access limits.

The most promising next result would impose finite decentralized private
communication, verification or bounded incentives and sharpen E3's architecture
gap, or combine partial-state feedback with genuine costly synchronization.
Simply proving invariant lotteries exist, or another potential existence fact,
is not a viable originality claim.

## Failed claim retained after adversarial review

The initial E5 control asserted only the two unanimous pure NE for every
n≥3. Both separate reviewers refuted this at n=4: profile0011 and its
permutations are weak NE, since no unilateral move reaches unanimity. Their
zero welfare also invalidates the asserted positive-denominator PoA formula
in that generalization. E5 is now explicitly n=3, which suffices for the
unbounded positive-welfare ratio. The exact n4 witness is preserved in tests.
