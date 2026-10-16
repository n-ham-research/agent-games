# Phase 13 — When coalition mechanisms are computationally usable

16 October 2026. Nicholas Ham's Agent Games programme; candidate development
and exact checks assisted by Codex. This branch investigated the requested
intersection of compact task descriptions, strategic verification, and symmetry,
while testing whether the Phase12 orbit obstruction can survive coarse accuracy.
No companion repository was changed. All novelty judgments remain provisional.

The strongest new candidate is **counting-hard invariant equilibrium output
with two action orbits and player transitivity**, sharp against the trivial
one-orbit case. It is proved below as P13-Q; fine approximation and the
invariance requirement are substantive. The positive mechanism result is a
**fully specified count-coordinate algorithm** for
fixed numbers of role/cost categories. It computes the exact welfare–reliability–
audit frontier without listing labeled profiles or coalitions, within the
Phase12 minimal-coalition/shutdown implementation architecture. This is a useful
constructive application, but symmetry reduction of Bayesian mechanism LPs is
established prior. It should not be advertised as a new general algorithmic
principle. A natural weighted-threshold counting reduction gives the contrasting
exact-value barrier. A constant-accuracy q3 equilibrium refinement is possible,
but yields only established-style BPP hardness, not counting hardness.

## 1. P13-H: histogram frontier with pointed incentives and a sampler

### Input and implementation class

There are explicitly listed N players partitioned into r known roles, role a
having n_a>=1 players. Within role a, costs are independent and identically
distributed on explicitly listed positive rational values c_(a,1),...,c_(a,t_a),
all strictly below a common benefit B. Write p_(a,c)>0 for each supported type's
rational probability, and K=sum_a t_a. Priors of different roles may differ.
Each player's utility is B times task success minus its realized cost if it
works. A role's audit price kappa_a>=0 is fixed, external, and not charged to
its subjects. No transfers or fines are introduced.

A coalition succeeds iff its vector of role counts g belongs to an upward-closed
set F within the box product_a{0,...,n_a}. A polynomial-time exact membership
routine for F is part of the input; its running time is charged. No singleton
succeeds, and at least one successful coalition exists. Roles can therefore
represent different tools or permissions. This includes ordinary thresholds,
weighted thresholds with one common weight per role, and coverage systems with
one fixed coverage pattern per role. It does not put a constant bound on r for
arbitrary coverage/weighted instances.

The mechanism class is the precise Phase12 V12-C class: direct private cost
reports, perfect pre-action audits, voluntary binary work, a target lottery over
inclusion-minimal successful coalitions or empty failure, and credible all-abstain
shutdown after detected dishonesty. Weak honest-and-obedient Bayesian equilibrium
is required. Auditing may be adaptive in the lower bound; the attaining mechanism
uses the selective direct audit construction. The claim is not that arbitrary
nonminimal or multistage mechanisms have no better frontier.

The prior, task, objective and resource constraints are invariant under the
product of symmetric groups permuting players **within** each role. In
particular this is not a full player-anonymity assumption. Constraints can
include an ex-ante reliability floor, an expected audit budget, welfare bounds,
and role/type-specific interim requirements, provided they are linear and
respect these role permutations.

### Theorem

For fixed K the exact attainable welfare–reliability–audit polytope of this
implementation class has a rational LP with N^{O(K)} variables and constraints,
constructible in N^{O(K)} times a fixed polynomial in input bit length and
membership-evaluation time. Any rational linear objective over this polytope
can be optimized in the same polynomial-size LP sense. An optimal rational
mechanism and a central exact sampler can be reconstructed with polynomial
encoding length and expected running time for fixed K.

This is an **XP(K)** algorithm statement. It is not a proved FPT(K) bound, nor
a polynomial algorithm when every agent has a distinct role. N must be counted
in the input/output size: binary encoding enormous populations by role sizes
alone would make N^{O(K)} a pseudopolynomial statement. It is not the q-only
invariant Nash algorithm of Phase11; it optimizes a specified mechanism polytope.

### Coordinate construction

Let h=(h_(a,c)) be a cost-report histogram, with sum_c h_(a,c)=n_a. Its prior
probability is

    P_h = product_a [n_a! / product_c h_(a,c)!]
                    product_c p_(a,c)^(h_(a,c)).

The number of histograms is

    H = product_a binomial(n_a+t_a-1,t_a-1) <= (N+1)^(K-r).

At h a successful outcome is a selected-worker count vector y satisfying
0<=y_(a,c)<=h_(a,c), whose role totals g_a=sum_c y_(a,c) are inclusion-minimal
in F. Check minimality by F(g)=true and F(g-e_a)=false for every g_a>0.
Failure is a separate outcome denoted 0; the all-zero worker vector is not
misclassified as successful. At most (N+1)^K candidate y vectors are checked
per histogram. F itself can be tabulated on its role-count box with
at most (N+1)^r membership calls; neither labeled coalitions nor type profiles
are needed.

The principal variables are **joint** masses z_(h,y)=P_h f_h(y), and z_(h,0),
not conditional probabilities with an uncharged prior oracle. Impose

    z>=0,     sum_(y or 0) z_(h,y)=P_h.

For an arbitrary player in role a with reported type c, define linear interim
success and workload variables

    s_(a,c) = [1/(n_a p_(a,c))]
                  sum_(h,y successful) h_(a,c) z_(h,y),
    x_(a,c) = [1/(n_a p_(a,c))]
                  sum_(h,y successful) y_(a,c) z_(h,y).

The occurrence factor h is essential for **pointed** success. Dropping it or
using an unconditional histogram law in an incentive constraint gives the
wrong conditional prior. For workload the selection factor y takes its place.

Add alpha_(a,d), beta_(a,d) for successful-unselected/selected audit mass:

    0<=alpha_(a,d)<=s_(a,d)-x_(a,d),
    0<=beta_(a,d)<=x_(a,d),
    B alpha_(a,d)+(B-c_(a,c)) beta_(a,d)
       >= B(s_(a,d)-s_(a,c))
          +c_(a,c)(x_(a,c)-x_(a,d))          for all a,c,d.

These are V12-C's exact joint report/action incentive capacities, not ordinary
truthful-allocation constraints substituted without voluntary-action analysis.
The reliability, gross welfare and external audit cost are respectively

    R = sum_(h,y successful) z_(h,y),
    W = N B R - sum_(h,y successful) z_(h,y) sum_(a,c)c_(a,c)y_(a,c),
    A_kappa = sum_(a,d) n_a p_(a,d) kappa_a
                                      (alpha_(a,d)+beta_(a,d)).

For count use kappa_a=1. Thus every desired budget/objective above is linear.
The LP has at most H[(N+1)^K+1]+O(K) variables and H+O(K^2) constraints besides
nonnegativity and the desired frontier bounds, using sparse coefficient rows.
Its bit encoding length is N^{O(K)} times a fixed polynomial in the rational
input length. This counts both reading input and writing the count-policy table.

### Proof of exactness

First average any feasible labeled mechanism over role-preserving permutations,
including its audited-agent identities and recommendations. Independence and
identical within-role priors make this preserve Bayesian joint-deviation
incentives, reliability, welfare and expected audit prices. Convexity preserves
all specified linear constraints. This does not preserve an imposed independent
local-policy architecture; such a restriction is not part of this theorem.

An invariant target lottery at a reported labeled profile is determined by h
and y, and conditional on those counts is uniform over choices of y_(a,c)
players from each role/type cell. This follows because the stabilizer of the
reported profile acts transitively on those coalitions. Conversely choosing h,y
and uniformly selecting within each cell gives an invariant feasible target.
Its workers are pivotal because the role-count vector is inclusion-minimal.
For a focal player in cell (a,c), the elementary size-bias identity is

    Pr(H=h | focal cost c) = h_(a,c) P_h/(n_a p_(a,c)).

Conditional on h,y its work probability is y_(a,c)/h_(a,c) whenever h_(a,c)>0.
Multiplying proves the displayed s,x formulas, including zero cells without
division by h. All selected workers strictly obey because c<B; unselected
workers prefer abstention. Failure and detected-lie shutdown are Nash
continuations because no singleton can restore success.

V12-C now supplies necessity of the alpha/beta capacity rows even for adaptive
audits, and its constructive selective auditing attains them: on a successful
target, audit an unselected role-a report-d agent with probability
alpha_(a,d)/(s_(a,d)-x_(a,d)), and a selected agent with probability
beta_(a,d)/x_(a,d), omitting zero denominators. Shutdown follows detected lying.
Therefore the LP is neither a relaxation nor merely a sufficient family: every
mechanism in the specified class maps into it with no greater resource cost,
and every LP point has the stated implementation. Averaging establishes equality
with the nonsymmetric labeled optimum **within this architecture**. QED.

### Exact rational output and randomness cost

Computing P_h uses factorials and rational powers with O(N) exponents. Their
binary lengths are polynomial in N and input rational lengths; e.g. log(N!) is
O(N log N). Standard rational LP bit complexity produces a rational optimum
with polynomial encoding length in the constructed LP. No real-algebraic Nash
sampling black box is used here.

On receiving reports, compute h, sample y with probabilities z_(h,y)/P_h, then
choose a uniform y-sized subset in each cell. One can choose subsets by
successive exact rational inclusion probabilities, or by uniform integer ranks
in combinatorial number systems; neither expands all coalitions. Audit rates
are explicit rational coins. A rational finite distribution can be sampled
using a common denominator and uniform integer sampling. Uniform integers in
{0,...,M-1} use ceil(log2 M) fair bits with rejection and fewer than two trials
in expectation. Consequently expected random bits and runtime are polynomial
in the explicit policy's encoding and N. The sampler outputs labeled worker recommendations and audited identities.
A full per-player recommendation vector has length Omega(N); sparse lists
with default abstention can be shorter, and their actual length is charged.

This is a central sampler with addressing and private recommendations, not a
free anonymous distributed implementation or a communication-bit theorem.
Exact fair-bit sampling can require unbounded worst-case bits for non-dyadic
probabilities. Thus the computational implementation is almost-surely finite
with polynomial expected cost, or a finite rational-coin kernel in the abstract
mechanism model; it is not always a bounded-depth fair-bit protocol.

## 2. P13-W: exact first-best values are hard for weighted thresholds

The following obstruction concerns a natural compact task description, without
arbitrary utility circuits. It separates fixed role multiplicity from arbitrary
binary-encoded worker weights. The reduction is an application of standard
counting knapsack, not a novel source of counting hardness.

**Claim.** Exact expected first-best gross welfare is #P-hard under polynomial-
time reductions for a single weighted-threshold task, even with independent
costs having at most two supported values per agent, all positive and below a
common B=3, and with no successful singleton coalition. The task is always
feasible. Computing the exact optimal gross welfare in the verified minimal-
coalition architecture is equally hard when the audit budget permits auditing
every agent (or audit price is zero). This is a **value** lower bound, not a
mechanism-output lower bound, and the obstacle already exists in planning.

**Construction and extraction.** Given positive integer weights w_1,...,w_n
and integer quota T>=1, let alpha=1/[2^(n+1)(n+1)]. Regular agent j has weight
w_j and independent cost alpha or 2, each with probability 1/2. Add a fallback
agent of weight T and deterministic cost1. Add a mandatory gate agent of
weight M=sum_j w_j+T+1 and deterministic cost alpha. The single threshold is
M+T. All actors' costs are in (0,3). Without the gate total available weight is
sum w_j+T<M+T, so it is mandatory. The gate alone fails; every other singleton
also fails. Gate plus fallback always succeeds.

Let L be the random set of cheap regular agents. A coalition using any costly
regular agent costs at least2+alpha and is worse than gate plus fallback,
which costs1+alpha. If sum_(j in L)w_j<T, the cheapest successful coalition is
therefore gate plus fallback. Otherwise the cheapest success is gate plus a
minimum-cardinality covering subset of L, with cardinality m(L)<=n, since
n alpha<1. Thus its realized optimal cost is

    C*(L)=alpha + 1                       if L fails to cover T,
    C*(L)=alpha + alpha m(L)              if L covers T.

Set F=#{L: sum_(j in L)w_j<T}. Then

    2^n(E C* - alpha) = F + alpha sum_(covering L) m(L),
    0<=alpha sum_(covering L)m(L) <=alpha n 2^n <1/2.

Consequently F=floor[2^n(E C*-alpha)]. Taking T=C+1 recovers the number of
knapsack subsets of total weight <=C. All input rational lengths and the exact
expectation's denominator length are polynomial; the extraction does not ask
for an exponentially long output. Every first-best success can be taken
minimal because all costs are positive, and B N exceeds its cost, so
first-best gross welfare is W*=3(n+2)-E C*. Full successful-path audits followed
by shutdown implement each such minimal target under V12-C. Hence the same
optimal gross value is attained in that verified mechanism class. QED.

There is no contradiction with P13-H: the distinct binary-encoded regular
weights generally create many roles. Nor is an FPTAS or inverse-polynomial
additive approximation ruled out: the rounding extraction needs exponentially
fine absolute precision. Deterministic near-counting and pseudo-polynomial
knapsack algorithms are substantial existing literature; a practical algorithm
should exploit them rather than treating this exact-value barrier as universal
intractability. Claiming that this proves every encoding of an optimal
mechanism is difficult would repeat the earlier value/output mistake.

## 3. P13-Q: a sharp two-orbit invariant-output barrier

The broader exploration revealed a simpler construction than adding ever more
matching-pennies gadgets. Every player can be interchangeable under a cyclic
automorphism, while the **location of its unique invariant equilibrium** reveals
a counting threshold. Here the game has no distinguished decision-player role.
This is invariant-equilibrium output hardness; unrestricted equilibrium output
is a different problem.

### Theorem and exact input/output scope

From a Boolean circuit F on n>=2 inputs and an integer 0<=K0<2^n, construct in
polynomial time a rational payoff-circuit game with N=n+1 binary-action players
and a supplied action-label-preserving cyclic player permutation. The supplied
group is player transitive and has exactly q=2 player-action orbits. In fact the
full exact typed automorphism group also has exactly these two action orbits.
All pure payoffs lie in [0,1]. There is exactly one independent mixed Nash
profile invariant under the supplied cyclic group, with every marginal interior.

Every **exactly invariant** ordinary epsilon-Nash profile with

    epsilon <= alpha * 2^(-n-1) / 8,      alpha=1/(2n),

identifies whether #SAT(F)>K0 from the side of1/2 on which its common marginal
lies. An algorithm running in f(q) poly(L,log(1/epsilon)) and returning explicit
rational invariant marginals for these circuit inputs would therefore count
satisfying assignments in polynomial time. Binary search uses O(n) calls.
This does not prove hardness for ordinary coarse accuracy, output merely near
the invariant set, unrestricted equilibrium output, or explicit factor tables.

### Construction

Index players modulo N. At pure profile s, player i reads the cyclically ordered
opponent tuple

    z_i=(s_(i+1),s_(i+2),...,s_(i+n)).

Use the same F at every player, without symmetrizing F over all input positions.
Set

    theta=(K0+1/2)/2^n,
    D_i(z_i)=1/2 -(1/n)sum_(j=1)^n z_ij + alpha(F(z_i)-theta),
    u_i(s_i=0,z_i)=1/2,
    u_i(s_i=1,z_i)=(1+D_i(z_i))/2.

The actual action-1 minus action-0 payoff difference is **D_i/2**, not D_i.
Because |D_i|<=1/2+alpha<=3/4, these are bounded rational payoffs. Each circuit
uses one F copy and a rational average of the input bits. Rotation transports
the ordered opponent tuple unchanged, so the supplied cyclic map is an exact
automorphism. It acts transitively on the N action-0 pairs and on the N action-1
pairs, but never interchanges those labels: q=2.

For completeness, no full exact typed automorphism can map an action0 to an
action1. Conditional on one's own action0 the pure payoff is identically1/2.
Conditional on action1 it is nonconstant: its values on opponent all-zero and
all-one profiles differ by

    [1+alpha(F(0^n)-F(1^n))]/2 >=(1-alpha)/2>0.

The property of a constant conditional payoff is preserved by every typed
bijection of opponents' pure profiles. Thus full exact automorphisms preserve
action labels. Cyclic transitivity then shows the full action-orbit count is
also2, although its player permutation group can be larger for special F.
We supply generators for the exact cyclic subgroup, not a generator list for
the complete automorphism group. A problem formulation demanding complete
full-group generators as input would need an additional argument.

### Unique invariant equilibrium and extraction proof

A profile invariant under the supplied rotation gives every player the same
action-1 probability p. Under independent mixing write

    f(p)=E_(n iid Bernoulli(p)) F,
    D(p)=1/2-p+alpha(f(p)-theta).

For p<q, coupling each input bit gives

    |f(q)-f(p)|<=n(q-p),
    D(q)-D(p)<=-(1-alpha n)(q-p)=-(q-p)/2.

Thus D is continuous and strictly decreasing. Also D(0)>1/4 and D(1)<-1/4
with endpoint strictness following 0<theta<1 and alpha<=1/4. There is a unique
root p* in (0,1); both actions are best responses there. Pure invariant profiles
p=0,1 are not Nash, and an interior invariant Nash must have D=0. This proves
uniqueness among invariant Nash profiles. It does not prove the full game has
only one unrestricted equilibrium. The profile p* is also invariant under every
full exact typed automorphism, since all such maps preserve action labels.

At the fair profile,

    D(1/2)=alpha[(#SAT(F)-K0-1/2)/2^n].

Set g=2^(-n-1). If #SAT(F)>K0, D(1/2)>=alpha g. For any p<=1/2,
strict decrease gives D(p)>=alpha g and the regret of mixing p is

    (1-p)D(p)/2 >=alpha g/4.

If #SAT(F)<=K0, any p>=1/2 similarly has regret

    p[-D(p)]/2 >=alpha g/4.

The displayed epsilon is strictly smaller than that wrong-side bound. Hence
every invariant epsilon-equilibrium satisfies p>1/2 on yes instances and
p<1/2 on no instances. Reading an explicit rational marginal and comparing to
1/2 is polynomial time. The accuracy encoding has O(n+log n) bits, as do
alpha and theta; output precision is charged. The construction and binary
search prove the counting reduction. QED.

### Why two orbits is the first possible boundary

If a supplied exact typed group has q=1 action orbit, every invariant independent
profile assigns the same probability to every player-action pair. Transitivity
forces equal action counts; normalization determines the uniform marginal at
every player. Exact payoff transport at this uniform invariant profile equalizes every
player's action-conditional payoffs: two of its actions lie in the same orbit
via a map fixing that player. Thus the forced profile is directly Nash.
It is therefore writable from the action
lists with no expected-payoff computation. In the present binary setting every
marginal is1/2. This is a promise statement: verifying that the supplied maps
are exact automorphisms is a separate problem.

Consequently P13-Q gives the smallest possible action-orbit count for this
fine-precision invariant-output obstruction, under rational pure-payoff circuit
representation. This comparison does not transfer to explicit payoff tables,
where the known action-orbit method is polynomial for q2; the expectation's
coefficient construction is the missing resource here.

### P13-Qapprox — ordinary accuracy has a randomized benchmark

For any N>=2 player-transitive binary game with supplied exact group G having
q=2 action orbits, pure payoffs in [0,1], and polynomial-bit polynomial-time
pure-profile evaluation, an invariant epsilon-Nash profile can be found with
probability at least1-delta in randomized time polynomial in input length,
N,1/epsilon and log(1/delta). Here 0<epsilon,delta<1. This is a standard
one-dimensional bisection/concentration corollary, not a new numerical method
or a deterministic fine-precision tractability claim.

Each player has exactly one action in each orbit: player transitivity makes
its counts in each orbit constant, positive and summing to2. Orient its labels
by those two orbits, even if the original labels differ. Every invariant profile
then uses a common probability p for orbit1. Exact payoff transport makes the
representative conditional payoff difference

    A(p)=E[u_i(orbit1,s_-i)-u_i(orbit0,s_-i)]

valid for every player. Product coupling gives
|A(p)-A(q)|<=2(N-1)|p-q|. Ordinary mixed regret is at most |A(p)|.

Evaluate A(0),A(1) **exactly** using two pure profiles for each endpoint. If
A(0)<=0 return p=0; if A(1)>=0 return p=1. Otherwise A(0)>0>A(1), giving a
continuous root bracket [0,1]. No monotonicity is required. Put

    T=ceil(log2(4(N-1)/epsilon)),
    M=ceil[32 epsilon^(-2) ln(2T/delta)].

At each of at most T stages, estimate A at the dyadic bracket midpoint with M
fresh independent sampled opponent profiles. Each paired payoff difference is
in [-1,1]. Conditional Hoeffding concentration and a union bound make every
adaptive-stage estimate accurate to epsilon/4 jointly with probability at
least1-delta: at any queried midpoint its conditional failure probability is
at most 2 exp(-M epsilon^2/32)<=delta/T. The conditioning is on the previous
history, which fixes the next midpoint; fresh sampling is essential.

Stop when the estimate has absolute value at most epsilon/2: the true |A| is
at most3epsilon/4. Otherwise its sign is correct, so replace the matching-sign
bracket endpoint and retain a root. After T stages without stopping, the width
is at most epsilon/[4(N-1)]. Return its midpoint. Its distance from some
bracketed root is at most half that width, so |A|<=epsilon/4. In both cases
unilateral regret is at most epsilon for every player, on the certified sampling
event. The output has **exact** invariance because all oriented marginals are
the same dyadic number.

A dyadic midpoint at depth j can be sampled exactly with O(j) fair bits per
opponent action. Hence Bernoulli sampling, two pure-payoff evaluations per
sample, and writing all N dyadic marginals have polynomial bit/runtime costs.
This is a high-probability algorithm, not a zero-error regret certificate.
Semantic symmetry and bounded efficient pure evaluation remain promises or
separately supplied certificates; orbit traversal itself is polynomial on the
explicit generators. A representation hiding repeated-squaring rational output
cannot be called a polynomial pure evaluator merely because all values are
bounded.

Thus the counting barrier distinguishes polynomial dependence on
**log(1/epsilon)** from this randomized inverse-accuracy benchmark. The
construction does not demonstrate ordinary inverse-polynomial-accuracy hardness
for player-transitive q2 games. The algorithm is retained to prevent precisely
that overinterpretation.

### Prior comparison and significance

Schoenebeck–Vadhan already turn circuit acceptance expectations into equilibrium
output bits. The new candidate is the **player-transitive two-orbit root
construction**, with unique invariant equilibrium and constant-payoff labeling
that certifies even the full group's orbit count. It is not claimed that
counting-hard circuit games, the small-dimensional polynomial Nash encoding,
or invariant equilibrium existence are new. Targeted searches for symmetric
circuit games, player-transitive Nash hardness and two action orbits did not
locate this exact restriction; absence from those searches is not novelty
clearance. Papadimitriou–Roughgarden's anonymous/symmetric-game algorithms use
explicit count descriptions; cyclicly ordered arbitrary Boolean dependencies
are not those anonymous inputs. The mathematical relation worth retaining is:
**strong interchangeability and a one-dimensional invariant strategy space do
not make fine-precision strategic output cheap when expected payoffs are hidden
in a compact program**.

## 4. P13-E: what survives at constant equilibrium accuracy?

### The unchanged counting reduction fails at coarse accuracy

In Phase12 C1 set theta=(K+1/2)/2^n and consider circuits with #SAT equal to K
and K+1. In either case the identical profile making **all** players, including
the decision player, fair has pair regrets zero and decision regret
2^(-n-2). Thus for any epsilon>=2^(-n-2) this same explicit profile is an
acceptable output on opposite threshold instances. A proof based on decoding
the decision marginal from every valid output cannot survive that tolerance
without changing the construction. This refutes the attempted unchanged
constant-accuracy/#P extension; it is not a general impossibility theorem for
other reductions.

### Constant-accuracy q3 BPP reduction

**Claim.** Producing an explicit ordinary epsilon0-Nash profile for rational
payoff-circuit games remains BPP-hard under polynomial-time reductions when
epsilon0=1/100 and the supplied exact group has q=3 action orbits. This means a
deterministic polynomial algorithm would derandomize the standard promised
circuit-acceptance problem. It is not #P- or NP-hardness, and does not preclude
a randomized polynomial-time algorithm. This is a constant-orbit adaptation of
Schoenebeck–Vadhan's established constant-accuracy XOR construction.

Take an n-input Boolean circuit F promised to accept at most1/3 or at least2/3
of its uniform inputs. Choose k with 25^k>=24n and m=nk. Construct m matching-
pennies pairs and one decision player as in Phase12. Let F' on m bits apply F
to the parities of n disjoint k-bit blocks. Replace its decision payoff by the
average of F' on the first-m coordinates over all m pair rotations and four
global quarter-turns; set its alternative payoff to1/2. This is polynomial
circuit size. The same supplied two generators still have q=3.

At any ordinary epsilon0-NE, the matching-pennies regret identity gives
|p_j-1/2|<=2epsilon0 for every paired player's marginal. Any block parity of k
independent such bits, allowing coordinate complementation, has distance from
fair at most (4epsilon0)^k/2=(1/25)^k/2. Each transformed first-m tuple consists
of distinct players' bits, so disjoint parity blocks remain independent. Their
joint law is within n(1/25)^k/2<=1/48 of uniform. Every term in the group
average is therefore within1/48 of uniform F acceptance probability. The
actual decision payoff differs from1/2 by at least1/6-1/48=7/48. Assigning half
or more probability to the inferior decision action would give regret at least
7/96>epsilon0. Its marginal consequently identifies the promised answer. QED.

**Why this is a modest boundary result.** Schoenebeck–Vadhan2006 already obtain
constant/poly-accuracy BPP hardness through XORs of matching-pennies inputs.
Our addition is the explicit q3 symmetry refinement; significance and novelty
are limited accordingly. The promise acceptance problem itself has an immediate
sampling algorithm. Indeed for the entire original Phase12 constructed family,
with arbitrary F and threshold theta, sample uniform F inputs to estimate its
acceptance probability to epsilon/2 accuracy, put all matching-pennies players
fair, and choose the better estimated decision action. With the corresponding
high probability the result is an invariant epsilon-NE. Hoeffding concentration
gives O(epsilon^(-2) log(1/delta)) samples, polynomial pure circuit evaluation
and explicit output cost. This is a randomized algorithm polynomial in
1/epsilon, not log(1/epsilon), and supplies no deterministic derandomization.

We have not established constant-accuracy counting hardness, hardness for
bounded-width/local tables, correlated-equilibrium hardness, or a new general
tractable Nash class. The study identifies precisely which stronger statements
would require new mathematics rather than amplification rhetoric.

## 5. Primary literature comparison and discovery assessment

Sources actually inspected on 16 October2026:

* Papadimitriou and Roughgarden, [*Computing Correlated Equilibria in
  Multi-Player Games*](https://ranger.uta.edu/~weems/NOTES6319/PAPERSONE/papadimitriou.pdf),
  JACM55(3),2008, original29-page article through a university-hosted copy,
  Section7/Theorem7.1, printed14:25–26, inspected. Its symmetric-game Nash
  algorithm uses count-structured utility polynomials. The circuit-query
  difficulty is separately noted in Section8. This is direct prior for the
  low-dimensional algebraic method and representation caveat, not a proof
  that arbitrary cyclicly ordered Boolean dependencies admit cheap expected
  payoff construction. P13-Q does not contradict that theorem.
* Daskalakis and Weinberg, [*Symmetries and Optimal Multi-Dimensional Mechanism
  Design*](https://www.cs.tau.ac.il/~fiat/cgt12/EC_2012/docs/p372.pdf), EC2012,
  Theorem3.1, Sections4–5.1, Remark1.2's constant-support qualification, plus
  the [31-page full version](https://arxiv.org/pdf/1112.4006). They already
  symmetrize Bayesian mechanism LPs, preserve truthfulness/objectives, and
  obtain exact polynomial algorithms for constant discrete support in specified
  symmetric auction settings. Their setting has payments and different outcome
  feasibility. P13-H does not claim their symmetry principle or finite-LP
  technique is new; its task-specific contribution is the explicit pointed
  count coordinates combined with V12-C audit capacities and coalition sampler.
  No claim is made that arbitrary task-mechanism feasibility follows from
  bidder symmetry alone.
* Schoenebeck and Vadhan, [*The Computational Complexity of Nash Equilibria in
  Concisely Represented Games*](https://people.seas.harvard.edu/~salil/research/nash-ec.pdf),
  EC2006, Theorems7.5–7.6, PDF p9, read in Phase12 and rechecked here. Their
  constant-accuracy proof already uses XORs of nearly fair matching-pennies
  players. P13-E is a supplied-orbit refinement, not a new general BPP lower
  bound or a route from randomized hardness to #P hardness.
* Stefankovic, Vempala and Vigoda, [*A Deterministic Polynomial-time
  Approximation Scheme for Counting Knapsack Solutions*](https://arxiv.org/pdf/1008.1687),
  abstract/introduction and dynamic-programming theorem statement inspected.
  Rizzi and Tomescu, [*Faster FPTASes for Counting and Random Generation of
  Knapsack Solutions*](https://www.sciencedirect.com/science/article/pii/S0890540119300276),
  publisher abstract and indexed original article text inspected. Exact
  counting is standard #P-complete; efficient approximation is mature prior.
  We do not claim the exact/approximate knapsack divide as new, or that
  weighted-threshold tasks are generically intractable at ordinary accuracy.

The strongest candidate for further review is P13-Q, especially its sharp q1/q2
boundary for invariant output; its novelty still needs expert source checking.
A separate important outcome is a **negative novelty assessment** of treating
histogram compression alone as an ambitious discovery. It gives a mathematically
complete usable computational consequence of the audit theorem and a natural
representation boundary; it does not yet justify a separate algorithms paper.
The q3 constant-accuracy extension is similarly a clean but modest refinement.
Keep these as supporting results and devote the next main discovery effort to
a general implementability/punishment theorem or a structural input class whose
tractability goes beyond count enumeration. A proposed FPT algorithm in the
number of role/types would require avoiding the explicitly large histogram
policy output, perhaps with a genuinely succinct separation/sampling theorem;
no such result has been proved here.

## 6. Exact checks and implementation limits

Eleven exact rational/integer tests in experiments/test_phase13_computation.py
check histogram probabilities against labeled independent profiles; minimal
role patterns against every selected worker's pivotality; pointed compressed
success/workloads against full labeled coalition lotteries with two distinct
roles and priors; every report deviation after audit reconstruction; weighted-
threshold counting extraction for several weights and every small quota;
parity probabilities and amplification bounds; the shared-profile coarse-
accuracy obstruction; every three-input Boolean function under every pure
profile for the q2 typed rotation; and q2 strict monotonicity and wrong-side
regret bounds for every threshold and a rational marginal grid; and bounded-
error sign bisection on all small cyclic instances, exact endpoints, and a
nonmonotone three-root polynomial. These tests use exact deterministic bounded
errors, not a stochastic experiment claimed to prove a confidence bound. All pass.

The experiment constructs coefficient evaluations and explicit small-instance
lifts. It does not implement a general rational LP optimizer, solve a counting-
hard instance at scale, or test asymptotic running-time claims. The LP
optimization step invokes standard polynomial-bit rational linear programming;
its input construction, output kernel, and sampling costs are proved above.
The displayed histogram LP itself is the algorithmic artifact, not an empirical
claim that a general mechanism solver was executed.

## Independent internal reviews

The coalition branch independently reconstructed P13-H/W/E and found no
mathematical defect. It checked pointed size bias, pivotal role-minimal
coalitions, the weighted gate/fallback extraction, and independence after XOR
rotation. A separate source-review branch independently attacked P13-Q,
including the D/2 regret scale, strict monotonicity, the full-group constant-slice
argument and the distinction between supplied cyclic generators and full-group
generator input. It found no defect and the input qualification was incorporated.
These are separate same-family AI reviews, not external peer review or novelty
clearance. Root proof reconstruction and source assessment remain separate.

The source-review branch separately attacked P13-Qapprox and found no defect:
its checks cover action-orbit orientation, nonmonotone root bracketing, exact
endpoint evaluation, adaptive conditional concentration, the sample constant32,
and explicit dyadic bit costs. N>=2 and efficient bounded rational pure
evaluation are hypotheses, not automatically verified properties of arbitrary
arithmetic circuits.
