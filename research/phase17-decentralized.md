# Phase 17: decentralized equilibrium selection, information and incentives

Nicholas Ham; Codex-assisted exploration. Finite contribution games, no new
manuscript. This is a competing selection direction, not another CE-polytope
result. Novelty remains provisional and classical methods are identified below.

## Model and the architectural distinction

Workers choose binary work actions. Payoff is B F(A)-c_i 1[i in A], with common
B and 0<c_i<B. Communication happens before the one-shot action stage; it is
free, nonbinding, and has no utility effect except through that terminal
outcome. Costs are either (a) truthful read-only local input, or (b) private
strategic types that cannot be verified. These are DIFFERENT models.
There are no transfers, deposits, cost-burning messages, commitments, trusted
private recommendations or external randomness carrying hidden role labels.
Actions and messages may be randomized; resources are charged explicitly.

A successful pure NE is precisely an inclusion-minimal winning coalition:
workers must each be pivotal (else dropping work saves c_i), and every
abstainer benefits by saving cost on a task already completed. Conversely
pivotal work gains B-c_i>0 and abstention gains c_i>0. This elementary
observation does not imply agents learn or select such an equilibrium.

## P17-E1: constructive local selection under honest cost inputs

Suppose F is a supplied read-once AND/OR formula on distinct workers. With
positive costs, compute at each leaf its cost; at AND add child minimum costs,
and at OR take the smaller child's minimum cost, breaking ties through a
supplied ordered-port convention. A top-down activation bit activates both
children at AND and only the selected child at OR. Inactive subtrees output
no work. The resulting coalition is a minimum-cost successful coalition and
therefore inclusion-minimal. It is a successful pure NE and maximizes welfare
among successful profiles, since welfare is nB minus total work cost.
Under this specified common cardinal payoff scale, it also beats every failed
profile: successful total cost is below nB and failed welfare is nonpositive.
No fairness criterion is introduced by this welfare convention.

Induction proves the cost recurrence because the two subtrees use disjoint
workers. The protocol sends O(n) scalar/activation messages along formula
edges, in O(height) synchronous rounds (bottom-up then top-down). If total
rational cost encoding is L, each partial sum has O(L+log n) bits, so an explicit
upper bound is O(n(L+log n)) transmitted bits. Exact comparisons/additions have
polynomial bit complexity. Positive costs are required for the minimality
conclusion. A supplied series/parallel edge decomposition gives the same
protocol for its connectivity task. Repeated workers invalidate the recurrence.

This is classical AND/OR dynamic programming. It does not require a central
private correlation mediator: each gate runs a local deterministic operation.
It DOES require honest execution of those operations and accurate local
inputs. Gate processes/routers are part of the communication architecture,
not assumed Byzantine-proof or incentive-compatible. The root's activation
is a task-control message, not a proof that all players voluntarily execute
this protocol. Once a coalition is publicly announced the action stage is
strictly obedient, with margin min_i{c_i,B-c_i}, but MESSAGE deviations remain
unresolved. Cheap computation of a strict terminal NE is insufficient for an
equilibrium of the enlarged communication game.

## P17-E2: private-cost incentive obstruction, even with unlimited cheap talk

Consider two singleton-capable volunteers F=x_1 OR x_2, costs in a common
interval [l,h] with 0<l<h<B. A protocol/selection rule must always succeed
with EXACTLY ONE worker for every type profile. Assume truthful use of each
private type is an ex-post equilibrium of the complete communication/action
protocol (or, more strongly, a dominant-strategy direct rule). Every player
may imitate the entire strategy prescribed for another own type. No
verification, type-dependent communication costs or transfers are available.

Then the probability p of choosing player1 is independent of BOTH private
costs. Thus the only possible implemented outcome rules are fixed lotteries
over the two pure successful equilibria. This is a necessary condition on
outcomes, not a claim that every arbitrary cheap-talk protocol realizes them.
A public fixed lottery followed by terminal best responses does realize such
an outcome if a public randomization service and distinct role identifiers
are available; communication-free deterministic role1 selection also does.

Proof: fix the other's type and let q_i(c_i,c_-i) be own work probability.
Since success is certain at every prescribed type profile, true cost c yields
B-c q_i(c,c_-i). Mimicking c' gives B-c q_i(c',c_-i). Incentive compatibility
and c>0 imply q_i(c,c_-i)<=q_i(c',c_-i). Reverse the roles of c,c' to get
equality. Hence q_1 depends only on c_2, and q_2 only on c_1. Exactly one
worker implies q_1(c_2)+q_2(c_1)=1 for all profiles, forcing both constants.
This argument applies directly to arbitrary multi-round randomized cheap talk
when type imitation is a legal deviation; it does not require mechanically
applying a revelation principle. It also applies to a trusted direct mediator
under the same always-success/exactly-one/no-transfer promise.

Consequences:

- Exact cheapest-worker selection is impossible, even though E1 computes it
  with constant local work and honest cost communication.
- The best worst-case approximation ratio for expected TOTAL WORK COST is
  exactly (h+l)/(2l), attained by the uniform fixed lottery. For fixed p,
  the profiles (h,l) and (l,h) have optimum l and force worst ratio at least
  1+(h/l-1)max(p,1-p). Conversely a uniform lottery has ratio
  (c_1+c_2)/(2 min(c_1,c_2))=(1+max(c_1,c_2)/min(c_1,c_2))/2,
  maximized at these extreme profiles. This is a cost approximation, not a payoff-ratio
  or calibrated-fairness theorem. As l tends to zero there is no uniform
  constant approximation over all positive costs.
- For eta-ex-post IC rather than exact IC, a type imitation gives
  |q_i(c,c_-i)-q_i(c',c_-i)|<=eta/l. Moving between (l,h) and (h,l) through
  one other profile changes p by at most 2eta/l. Averaging the selected costs
  at those two profiles therefore gives at least
  (h+l)/2-(h-l)eta/l. This is a valid lower bound (possibly vacuous for large
  eta), not an asserted sharp approximate frontier.

None of these impossibilities survives automatically if failure or redundant
work can be used as report-dependent punishments, if costs are verified, if
payments/effort-burning messages are allowed, or if repeated future tasks
alter continuation utilities. Always succeeding with exactly one worker is
an economically meaningful efficiency requirement AND a substantive restriction.
A protocol using failure as an incentive instrument is outside this theorem.

## P17-E3: a many-worker structured extension

For an AND of m disjoint two-worker OR pairs, require success and exactly one
worker in EVERY pair at every type profile. All workers have costs in[l,h].
The E2 imitation proof makes each own work probability independent of its
own cost. Fix costs outside one pair. Complementarity of its two work
probabilities then forces that pair's selection probabilities to ignore BOTH
of its costs, though they may depend on other pairs' costs.

Choose independently for each pair one of the two orientations (l,h) or(h,l)
with equal probability. Conditional on all other pairs' costs, each pair's
expected selected cost is (h+l)/2. The efficient cost is ml for EVERY such
profile. Therefore some profile has total expected cost at least m(h+l)/2,
and no ex-post IC always-minimal selector improves the worst-case ratio
(h+l)/(2l). Independent uniform role selection in each pair attains the ratio
on all cost profiles, with m public random bits or an equivalent preshared
role-assignment source. The source's role correlation and communication are
resources; anonymous players receiving identical bits do not acquire distinct
roles. This extends the boundary to read-once tasks with 2^m successful pure
NE, rather than asserting that efficient selection follows from many equilibria.

## Anonymous communication and the missing incentive step

With identical local observations, identical deterministic code and no
identifiers, two volunteers exposed only to a COMMON random string have
identical conditional actions. They cannot select exactly one worker.
Independent private randomness with no communication also cannot guarantee
exactly one: independent Bernoulli actions have positive failure or redundancy
unless deterministic roles differ, which anonymity forbids.

A simple honest-execution protocol fixes this: each broadcasts a fresh fair
bit; if bits differ, the bit1 player works, else repeat. It terminates almost
surely, uses two rounds on average and four transmitted bits on average.
After R rounds the unresolved probability is 2^-R. Finite bounded private
random tapes cannot give zero-error anonymous role selection, since the event
of identical tapes has positive probability and keeps the two views symmetric.
Unbounded fair-bit repetition escapes the bounded-tape argument. These are
classical randomized leader-election observations, not new lower bounds.

Crucially this protocol is NOT a communication equilibrium for costly workers:
against an honest fair-bit opponent, a player who always broadcasts0 eventually
causes the opponent to broadcast1 and do the work. It still gets B with no
cost, while honest play gives B-c_i/2. Even with no private-cost reports,
randomization itself is a profitable strategic-deviation target. The terminal
selected profile being a strict pure NE does not cure this. This exact witness
refutes the tempting inference 'distributed leader election + terminal NE
implies decentralized equilibrium implementation'. It does not prove that all
cheap-talk implementations are impossible.

## Resource-constrained substitution: deliberate stopping point

The Phase14 total-variation coupling already yields regret loss at most twice
the uniform payoff error when every deviation transports. Replacing exact
sequential observations by an estimated default-policy error does NOT make
that uniform guarantee: a deviator can steer into rare unseen histories.
No new synthesis/resource theorem follows just from attaching an epsilon to
the observer from Phase16. This branch therefore does not create another
approximate-bisimulation corollary. A useful next result must synthesize a
uniform error certificate under bounded deviations or establish a structural
class where it is efficiently checkable. Existing exact observer/INDEX work
is retained, not repackaged as a new contribution.

## Primary comparison, significance and next question

[Abraham–Dolev–Geffner–Halpern, Implementing Mediators with Asynchronous Cheap
Talk, author PDF dated20October2019](https://www.cs.cornell.edu/info/people/halpern/papers/podc19.pdf)
was inspected at §§1–2's mediator/cheap-talk distinction and asynchronous
termination/default-action discussion. It explicitly treats strategic deviations
from mediator implementations and conditions involving player counts,
punishments, known utilities and communication architecture. Thus ordinary
protocol correctness is emphatically not a new substitute for incentive-
compatible implementation. Our tiny imitation obstruction is not a general
cheap-talk impossibility and does not contradict its positive theorems.

[Balseiro–Gurkan–Sun, Multiagent Mechanism Design Without Money, Operations
Research2019 author-hosted full text](https://people.duke.edu/~psun/bio/NoMoney.pdf)
was inspected at the introduction's one-period impossibility intuition and
future-allocation incentive approach, and §5's comparison of budget-based
repeated mechanisms. Their no-transfer allocation setting and repeated future
promises are direct warning against interpreting E2 as a new general
impossibility of information elicitation. Their planner allocating a desirable
resource differs from workers undertaking costly effort, and their repeated
mechanism is not an automatically decentralized version of our protocol.
No theorem is transferred across that distinction without a separate proof.

[Procaccia–Tennenholtz, Approximate Mechanism Design Without Money, primary
full author text](https://www.cs.toronto.edu/~nisarg/teaching/2556s20/papers/facility.pdf)
was inspected at the strategyproofness/approximation definitions and facility
selection results. Approximation lower bounds from incentive constraints are
established methodology; E2's proof is an elementary application of the fact
that under guaranteed success all positive-cost types prefer lower own work
probability. It is not a new mechanism-design principle or a claimed new
constant for their different facility-location objective.

[Itai–Rodeh, Symmetry Breaking in Distributed Networks, author-hosted full
text](https://csaws.cs.technion.ac.il/~itai/publications/lord/all.pdf)
was inspected at the opening anonymous symmetry/expected-termination discussion.
The accessible text is an author manuscript, not silently identified with a
verified final pagination/version. Randomized anonymous leader election and
its termination/communication trade-offs are established; our two-player
protocol is only an exact small witness exposing its incentive gap.

**Assessment.** The serious finding is an architectural boundary: local
computability and strict terminal equilibrium leave a separate information-
elicitation/communication game. This branch gives an explicit structured task
application and exact counterexamples, but the proofs rely on mature dynamic
programming, type imitation and leader-election ideas. They should not be
promoted as a major original theorem without a much closer domain-specific
prior search. Repeated interaction, verified costs or permissioned role tokens
are promising ways to change the boundary; each must have its own utility and
communication model. A genuinely stronger next target is a repeated local
protocol with an ex-post/Bayesian equilibrium guarantee and quantified
communication, WITHOUT silently importing a trusted allocation planner.
No such convergence/implementation result has been established in this pass.

## Exact checks and provenance

Nine exact tests pass under
`python3 -m unittest discover -s experiments -p test_phase17_decentralized.py`.
They compare read-once local selection to every pure coalition on representative
four-leaf trees and rational costs, check successful-NE/minimality equivalence,
enumerate all two-type half-grid lottery tables and find only constant IC
ones, reject cheapest-worker truthfulness, verify minimax ratios and the approximate-IC endpoint bound, check a
cross-pair-dependent truthful selector's random-orientation lower bound, and
calculate truncated election/manipulation and identical-tape probabilities.
The tests do not implement general cheap-talk equilibrium search or prove
learning convergence. Analytic proofs provide the general statements.


## Actual independent reviews

The information branch independently reconstructed E1–E3, including the
ex-post type-imitation argument, fixed-lottery conclusion, minimax ratio,
approximate-IC bound, pair-orientation extension and the anonymous election
manipulation. It found no defect under the explicit always-success/exactly-one
and no-transfer assumptions. This is internal AI review, not external peer
review or a priority determination.

This branch reciprocally reconstructed `phase17-disclosure.md` D1–D3. Cone
addition and merging by common optimal decision preserve safety and guessing
value; the limited-alphabet enumeration is XP, and the k/N garbling guarantee
holds. The three-volunteer rank-two example's slacks and paired-column upper
bound were checked directly. Payoff-irrelevant recommendation redesign and
the exact joint-law conditional-independence nonconvexity example have the
stated different scopes. No proof defect found; prior-art qualifications are
important and no new general privacy theorem was independently identified.

The final P17-X proof in `phase17-originality.md` was independently attacked.
For every edge set, |A|-m F(A)>=0; intersecting equality with success one
forces every supported successful edge cover to have exactly m edges, hence
be a perfect matching. Conversely every matching has conditional switching
gain 1/2 for every edge worker, so the face is EXACTLY the matching polytope
under the affine utility/work map, for all stated margins. Rothvoss's primary
arXiv1311.2369v4 Theorem1 and face-projection monotonicity passages were opened
and checked against the cited transfer. No defect found. This imports its deep
lower bound rather than proving it anew. The same hard face already exists
without incentives; no causal incentive gap, runtime hardness or fixed-size
protected-projection conclusion follows.

Root's `phase17-representations.md` T1/T2 were also separately reconstructed.
Shared ordinary leaf bits couple the r+1 actual/counterfactual worlds, while
fixed repeated-worker assignment cells enforce all occurrences jointly. Root
value differences plus the cost term c_j(1-2b_j) give exact repeated-worker
switching rows; ordinary sensitivity remains valid on the unique occurrence
path. Summing IC over hidden assignment cells (rather than imposing extra
conditional IC) and tree consistency yield the claimed full-region FPT lift.
Sparse extraction preserves all constraints. For T2 the fixed working probes
have gains 1/2-y_j, so 2^m terminal summaries are necessary under that specified
architecture despite a linear local-factor LP. No defect found. These reviews
establish neither task-class priority nor a new general compression theorem.
