# Phase 18: persistent types, repeated assignments and finite memory

Nicholas Ham; Codex-assisted exploratory analysis. This branch separates
repeated TASK interaction from repeated CHEAP TALK and distinguishes workload
criteria from utility equality. No companion repository is changed. Results
below are scoped candidates/corollaries; no significant originality is asserted.

## Model and stage incentives

Two agents can each complete a repeated task alone. In each period t they
choose work/abstain, success is their OR, and utility is B*success-c_i*work.
A private cost c_i in[l,h], 0<l<h<B, is drawn ONCE and remains fixed. Both use
a common discount beta in(0,1). Normalize total utility by(1-beta). Before or
between tasks they may exchange free nonbinding messages; no transfers,
verification or type-dependent communication costs are allowed. Type imitation
of another full strategy is a legal deviation. Public monitoring reveals both
actions; the public assignment protocol determines a role after every history.

Every prescribed exactly-one-worker stage profile is a strict pure NE for
EVERY allowed cost vector: the assigned worker gains B-c_i from working and
the other saves c_i by abstaining. Any exogenous role schedule continued
independently of past actions is therefore a subgame-perfect equilibrium
of the repeated action game: each period's unilateral deviation reduces its
own payoff and changes no future assignment. No folk-theorem punishment or
discount threshold is needed for this statement. If role messages themselves
are strategically produced, their incentive conditions remain additional.
For each fixed type vector this is an SPE in the complete-information repeated
action game; because the same strict action incentives hold at every belief
about other costs, it also supplies sequential rationality for the corresponding
private-type model without reports. Public monitoring does not by itself
verify private costs or secure a coin.

## P18-S1: repeated tasks do not elicit persistent scalar costs for free

Consider ANY protocol whose prescribed strategies always produce exactly one
worker and success each period, for every private type profile. Suppose the
entire communication/action protocol is an ex-post equilibrium. Then agent1's
expected normalized discounted workload

    D_1(c_1,c_2)=(1-beta) E sum_t beta^t a_1,t

is independent of BOTH private costs. Agent2 has D_2=1-D_1. Thus repeated
interaction, arbitrary history-dependent messages, public monitoring and
future role reassignment cannot make expected discounted work respond to
persistent private costs under these efficiency restrictions.

Proof: success is always one under every prescribed type profile, so true
cost c yields utility B-c D_i(c,c_-i). By imitating another type c' for the
ENTIRE protocol, its utility becomes B-c D_i(c',c_-i): the other player's
observable history has exactly the prescribed c' law. Ex-post IC in both
directions and c>0 force own workload to ignore own type. Exactly-one work
implies complementarity, forcing both workload functions constant as in the
one-shot two-volunteer argument. Discounted convergence follows bounded
utilities; arbitrary finite or almost-sure finite cheap talk is covered only
when the stipulated terminal/default actions and complete-strategy imitation
are well defined. No equilibrium is inferred without those semantics.

The best worst-case ratio of expected normalized WORK COST to the efficient
per-period cost is consequently (h+l)/(2l), attained by a type-independent
uniform public role lottery. The endpoint proof is exactly Phase17's fixed-
lottery argument applied to D instead of a one-period probability. This also
extends pairwise to ANDs of disjoint two-volunteer subtasks when each subtask
always has exactly one worker. This is a repeated no-transfer type-imitation
corollary, not a new revelation theorem. Allowing temporary task failure,
redundant work, verified costs, changing private types or additional utility
components breaks its hypotheses. In particular evolving-value dynamic
allocation literature does NOT contradict it: future allocations can screen
changing valuations while our fixed positive scalar rescales the same total
burden in every period.

## P18-S2: exact discounted workload balance has a memory boundary

Now remove reports/cost elicitation and ask for a public role schedule. A
motivated allocation criterion is equal discounted WORKLOAD on every realized
path:

    (1-beta) sum_t beta^t a_1,t = 1/2,
    a_2,t=1-a_1,t.

This compares identical action burdens, not utility equality when costs differ;
it is a specified allocation objective, not a definition of fairness. Ex-ante
role impartiality, equal long-run frequencies and pathwise discounted balance
are different criteria. In particular randomizing the initial phase of
alternation gives each player expected workload1/2, but realized discounted
loads are 1/(1+beta) and beta/(1+beta), not1/2.

**Existence with unrestricted history.** A balanced binary sequence exists
iff beta>=1/2. If beta<1/2 the first action contributes either0 or1-beta>1/2;
the remaining normalized total is at most beta<1/2, so balance is impossible.
For beta>=1/2 maintain residual r in[0,1], initially1/2. If r<=beta choose
bit0 and set r'=r/beta; otherwise choose bit1 and set
r'=(r-(1-beta))/beta. The intervals [0,beta] and[1-beta,1] cover[0,1], so
r' remains in[0,1]. Inductively

    1/2=(1-beta) sum_(t<T) beta^t a_1,t + beta^T r_T.

The remainder tends to zero. Every period's role assignment remains a stage
pure NE, so the resulting schedule defines an SPE even though its memory or
arithmetic representation need not be bounded. This is an elementary binary
beta-expansion construction, not a new repeated-game existence theorem.

**Rational discount and finite autonomous controllers.** If beta is rational,
a finite-state deterministic autonomous role controller can achieve exact
pathwise balance iff beta=1/2. Here autonomous means time-homogeneous finite
memory, with no unbounded external clock, advice tape, hidden storage or
unbounded information-bearing public signal stream. Fresh independent
randomness remains allowed in the randomized case below. Finite deterministic output is eventually
periodic. Write its bit generating function as

    A(z)+z^L C(z)/(1-z^P),

where A is a binary prefix polynomial of degree<L and C a binary period
polynomial of degree<P. Balance implies that beta is a root of the INTEGER
polynomial

    Q(z)=2(1-z)[A(z)(1-z^P)+z^L C(z)]-(1-z^P).

The constant coefficient is either1 or-1, including L=0; hence Q is not the
zero polynomial. If beta=p/q in lowest terms, the rational-root theorem
forces p=1. With beta>=1/2 and beta<1 this means q=2, so beta=1/2. At beta1/2
the schedule (1,0,0,...) attains balance with a two-state controller. It does
NOT have equal long-run work frequencies, illustrating the criterion distinction.

For rational beta>1/2, a finite-state randomized autonomous controller cannot
achieve pathwise balance almost surely either. If it did, after any reachable
state s all positive-probability continuations would have the same remaining
weighted sum v(s): two different values could not be offset by the identical
prefix on reaching s. For each positive transition labelled bit a to s',

    v(s)=(1-beta)a+beta v(s').

One may select one such outgoing transition per reachable state. The resulting
deterministic eventually-periodic path telescopes to the same initial value
1/2 (the bounded tail vanishes), contradicting the deterministic result.
This also covers random initial states by selecting one positive-probability
initial state. Randomness does not supply a hidden unbounded counter.

This is an impossibility of EXACT pathwise burden balance with finite
AUTONOMOUS memory, not a finite-memory impossibility for NE, expected balance,
or arbitrary exogenous observation-driven controllers. Giving the agents a
public clock or the nonperiodic schedule as advice changes the resources.

## P18-S3: finite-memory approximation and explicit implementation

For beta>=1/2 take the first T bits of the residual algorithm and then repeat
bit0 forever. Each player's normalized discounted workload differs from1/2
by at most beta^T, with opposite signs. A deterministic counter chain plus
absorbing tail uses at most T+1 public states; no messages or tool calls are
needed after deployment. The repeated action profile is still an SPE because
roles are exogenous and exactly one worker is prescribed each period. With
rational beta and target epsilon, choose T with beta^T<=epsilon; for fixed
beta this is O(log(1/epsilon)) states. Arithmetic and stored bit-description
cost is polynomial in T and the rational encoding of beta; if beta approaches1,
the explicit dependence is O(log(1/epsilon)/(1-beta)), not polynomial in the
binary encoding of 1/(1-beta). Controller mode bits are logarithmic in T,
while its read-only table/advice has O(T) bits. This is a constructive upper
bound, not a matching approximation-memory lower bound.

A one-bit public initial role lottery followed by fixed roles forever has
perfect EX-ANTE workload balance and an SPE with constant memory, while its
realized loads are0 and1. Thus expected balance and pathwise epsilon balance
have radically different implementations. No comparison of participants'
cardinal utilities is smuggled into these workload statements. For anonymous
agents an orientation/role channel remains necessary; identical common bits
alone cannot select different workers, as Phase17 showed.

## Strategic-message counterexample and monitoring scope

The honest private-bit election from Phase17 (broadcast fair bits until they
differ; bit1 works) can be run before every repeated task. An agent always
broadcasting0 obtains success without ever working against an honest opponent;
its positive discounted gain is c_i/2. Repeating the same protocol does not
repair its strategic defect. Public monitoring of broadcasts reveals outcomes,
not whether a bit was fairly sampled. Enforcing unbiased randomization requires
a different commitment/cryptographic/trusted randomness model or an incentive
proof. A public role schedule here bypasses that manipulation only by declaring
the assignment device/clock outside unilateral control and charging it as a
resource. This is not a decentralized secure coin-flipping construction.

## Primary comparison and originality outcome

[Boker–Henzinger–Otop, The Target Discounted-Sum Problem,
arXiv2511.22979v1 (28November2025)](https://arxiv.org/pdf/2511.22979)
was actually inspected at its introduction, beta-expansion equivalence,
Theorem8 discussion and eventually-periodic analysis. This explicitly revised
and expanded the LICS2015 paper, noting corrections to some earlier statements.
It already treats binary discounted sums, existence for discounts at least
1/2 and eventual periodicity. S2's interval recursion is a direct elementary
specialization, not a new existence principle or target-sum decision algorithm.

More decisively, [Bertrand–Ghorpade–Rajasekaran–Rubin–Vardi,
The Stochastic Target Discounted-Sum Problem, arXiv2609.03670,
primary September2026 text](https://arxiv.org/pdf/2609.03670)
was inspected at Theorem15 and Proposition16. Proposition16 gives EXACTLY
the discount2/3, unnormalized target3/2, binary-output single-state MDP example:
unrestricted memory achieves the exact target while finite memory cannot.
That is our normalized-half workload instance at beta2/3, so the memory
phenomenon is ALREADY KNOWN. The text attributes the underlying example to
Chatterjee–Forejt–Wojtczak2013 Proposition1; the original2013 body was not
retrieved here, and is not counted as independently inspected. Our all-rational-
discount half-balance criterion has a short rational-root proof and a repeated
assignment interpretation, not evidence of a major new general theorem.

[Akiyama–Frougny–Sakarovitch, On the Representation of Numbers in a Rational
Base, primary author extended abstract](https://www.irif.fr/~cf/publications/AFSwords05.pdf)
was inspected at its opening numeration-system comparison. Its particular
rational-base expansion is NOT silently identified with our normalized binary
discount stream. It provides broader numeration/finite-transducer context,
while the target-discounted-sum sources above are the closer direct comparison.
The source explicitly calls itself an extended abstract, not the final2008
journal version. No historical first-source claim is made.

Balseiro–Gurkan–Sun2019's primary dynamic no-money allocation text was inspected
in Phase17. It relies on a committed planner, changing private valuations and
future allocation promises, which explains why its repeated efficiency theorem
is not defeated by S1's PERSISTENT scalar-cost imitation argument. Abraham et
al.'s cheap-talk implementation results likewise have architectural and
punishment assumptions; a public role device is not their secure implementation.
Neither literature is replaced by the short action-stage SPE observation here.

**Assessment.** This was an ambitious test outside payoff-region geometry,
but exact memory barriers substantially overlap established discounted-sum
verification. The practical theoretical takeaway is the distinction among
persistent versus evolving types, expected versus pathwise assignment criteria,
and autonomous memory versus a free public clock. These explicit boundaries
are useful; they do not currently justify an original standalone paper or
further polishing of the same rational-root example. A stronger next inquiry
would permit evolving task-specific private capabilities and quantify which
verified state/communication resources sustain an incentive-compatible local
assignment process. No such new implementation theorem was obtained here.

## Verification and actual independent review

Eight exact tests pass under
`python3 -m unittest discover -s experiments -p test_phase18_sequential.py`.
They check rational residual invariants and approximation tails, both half-
discount finite implementations, generating-function polynomial identities
and their constant coefficients across tiny prefixes/periods, exclusion of
tiny periodic schedules at four rational discounts, alternation versus phase
lottery loads, every stage deviation's positive loss, and all tiny persistent-
type workload tables. These do not implement a general repeated-game solver
or independently certify target-sum literature. Proofs supply the generality.

The information branch independently reconstructed S1–S3 and reran all eight
tests. It explicitly checked the stochastic-controller proof by conditioning
on a positive finite prefix and then choosing support edges; the chosen
infinite path need not have positive probability for the bounded-tail
identity. No defect found. This is internal AI review, not external peer
review or an originality certification.

This branch reciprocally reconstructed `phase18-endogenous-information.md`.
The certain-success entropy/list-size interpolation and private/public size
bound were checked, as were the low-success binary-KL inequality, weighted
Jensen argument and singleton/empty attainment. One actual hypothesis gap was
found: its standalone low-success claim needed tau=(c+delta)/B<=1; without it
allowed parameters produced an invalid Bernoulli channel. The author added
that restriction explicitly. No further defect found after the repair.

This branch independently attacked `phase18-strategic-geometry.md` G1–G3.
In the collision polymatrix game the work row is a negative sum of collision
probabilities, so CE and CCE support exactly independent sets; nonobedient
same-coordinate marginals are indeed a cube because collisions remain
physically possible. Its constant equilibrium payoffs and weak-dominance
scope are essential. In the best-shot variant, the calibrated1/4-margin work
slack is exactly negative collision probability; STAB containment and all
perfect matchings being strict pure NE give exact face equality, without
assuming equality of the whole marginal region. The augmented-moment
intersection/projection no-gap bound also reconstructs correctly. No defect
found; none of this review removes the stated source/priority uncertainty.

Root's `phase18-projections.md` was separately reconstructed. Protected
matching-edge completion by two-edge swaps avoids every remaining forbidden
protected edge. On a failed protected-only subset, adding one worker covers
at most2k+2<2m vertices, hence every abstainer's switching gain is c. Successful
matching workers are pivotal. Protected work slack is exactly
min(x_i,s)-(c+delta)x_i>=0 by the displayed marginal bounds. The two threshold
couplings preserve all target marginals, including s0/s1 branches, and yield
at most2k+2 pure profiles. This proves simultaneous sufficiency as well as
the universal necessity inequalities. No defect found. It is a direct
fixed-projection calculation, not an inherited matching lower bound.
