# Phase 17 — theorem-level originality audit and an exact compression barrier

16 October2026. Nicholas Ham's Agent Games programme. Codex originality branch.
This note distinguishes verified mathematics, derivation from known results and
unresolved priority. Its classifications are research judgements, not external
peer review or proof of absence from the literature. The original manuscript and
companion repositories are unchanged.

The audit demotes broad originality claims for P14-A, P16-T1 and P16-H. Their
precise statements can still be useful, but their proof ingredients have short
connections to established mathematics. A further result, P17-X below, gives
an unconditional structural boundary: read-TWICE monotone tasks already need
superpolynomial exact LP descriptions of the entire CE payoff/success region.
The lower-bound engine is Rothvoss's theorem, explicitly prior. The additional
work is identifying a perfect-matching face inside a simple contribution game.

## 1. P14-A: a short protected extension, not a new purification principle

**Classification:** technically distinct, straightforward structural extension
of known minimal-support ideas; exact priority of the designated projection
has not been resolved. The FPT algorithm is a standard rational-LP consequence
once the support theorem is proved. Do not call the whole result already known
without a source matching the protected-payoff conclusion; equally, do not
present a new general CE-purification method.

Closest original source actually inspected: Kerman–Tenev, *Information design
for weighted voting*, Economic Theory2024, https://d-nb.info/1350115320/34 ,
Lemma1 (PDFp10) and AppendixC proof (PDFp32). It already removes unsuccessful
recommendation patterns and thins successful ones to minimal winners in its
persuasion problem, preserving the sender objective. Its receivers infer a
payoff state and its incentive model differs from complete-information costly
work. Its statement does not preserve an arbitrary designated vector of worker
payoffs, so citing Lemma1 alone is not a proof of P14-A. It is direct geometric
and proof-method precedent; the elementary extension must be supplied.

Here is that extension explicitly. In a monotone contribution game, delete
one unprotected worker j from a successful A only if success survives. For
every other selected worker, pivotality weakly increases. For every existing
abstainer, repairability weakly decreases; both changes improve obedience.
The removed j contributed -c_j to its work row, since it was nonpivotal. It
now contributes +c_j to its abstention row, since restoring its action cannot
change the still-successful outcome. Other old row contributions weakly
improve. At failure, deleting a worker also removes a -c_j work contribution;
restoring that one action cannot repair because the original profile failed,
so the new abstention contribution is again+c_j. This proves CE preservation
by iteration. For conditional delta margins, changing j's recommendation
moves the delta recommendation-mass term; the new abstention increment is
c_j-delta, explaining precisely the condition delta<=c_j. Protected workers
are never deleted, so their actions and success — hence their utilities —
are exactly preserved.

At the end every unprotected success worker is pivotal. If T is any minimal
winner inside the reduced A, every unprotected worker of A must belong to T;
otherwise removing it would retain T. Thus A=T union C for a protected subset
C. Failure support lies inside the protected set. The (m+1)2^k column bound
and FPT(k) rational LP follow immediately. This is the actual additional
proof beyond the geometric thinning source, rather than an inference from
terminology such as 'purification'. Harsanyi-style purification of mixed
strategies is a different subject and should not be invoked as its proof.

The preservation is substantive compared with deleting ALL unnecessary work:
a law giving a designated worker zero by mixing success and failed work can
lose that payoff after full thinning. But selective thinning and its row
proof are short. The statement is a plausible useful structural lemma; no
inspected evidence establishes that it alone is a major new theorem.

## 2. P16-T1: reverse differentiation plus exact tree marginals

**Classification:** technically distinct task-class corollary/explicit
formulation using established methods. The exact read-once contribution-game
statement has not been located in the inspected sources; no new general
compact-CE principle or differentiation method is involved.

There is a particularly direct derivation. Replace AND(x,y) by xy and OR(x,y)
by x+y-xy. A read-once formula gives a multilinear arithmetic polynomial f
agreeing with the Boolean task. Multilinearity yields

    partial f/partial x_i = f(x_i=1)-f(x_i=0).

Reverse differentiation sets the output adjoint to1. At an AND node, the
adjoint sent to one child is the parent adjoint times the other child's value;
at OR it is the parent adjoint times one minus that value. These are EXACTLY
P16-T1's p relations. On Boolean assignments they are Boolean. Read-once is
what makes the derivative equal the worker's discrete deviation; formal
arithmetic differentiation of x*x at x=0 is0, whereas changing the underlying
Boolean worker changes the output by1.

Primary differentiation precedent actually read: Darwiche, *A Differential
Approach to Inference in Bayesian Networks*, arXiv1301.3847, whose PDF is the
UAI2000 proceedings text, https://arxiv.org/pdf/1301.3847 , Section5 PDFpp8–9.
It propagates node values upward and adjoints downward to compute derivatives
in linear time. This is original-source evidence for the differentiation
machinery, not a claim that its Bayesian-inference theorem states our CE
result. The journal2003 text was not retrieved here. Baur–Strassen1983 was
searched, but full-text endpoints failed; its body is NOT counted as read.

Now retain each node's value and adjoint as one four-state variable. Each gate
constrains a parent and its two children. These scopes form a junction tree,
so consistent local masses realize a genuine global law; adding the 2n
obedience rows gives the claimed O(n)-size formulation. This step follows
standard exact tree-marginal theory. Wainwright–Jordan2008 primary monograph,
https://www.cs.columbia.edu/~blei/fogm/2020F/readings/WainwrightJordan2008.pdf ,
Proposition4.1 and its constructive proof (printed78–79) establish exactness
of tree local marginals. Grouping gate triples gives precisely the familiar
junction-tree extension. Sparse extraction and rational LP are standard.

The same derivation gives a known-framework optimization proof. For any
linear objective and CE dual prices, the deviation-adjusted objective becomes
a root term plus local leaf terms in (action,pivotality). Maximize this
additive objective on the four-state tree by ordinary dynamic programming.
Jiang–Leyton-Brown2011 Proposition1 then yields optimal CE; its dual proof
handles the chosen linear objective as well. No separate difficult global
strategic search remains after this local lift. Full-region EF is more
explicit than just an optimal-value oracle, but tree marginal construction
already explains that additional conclusion.

Elkind–Goldberg–Goldberg–Wooldridge2009 primary author text,
https://www.cs.ox.ac.uk/people/leslieann.goldberg/papers/mcn.pdf , Sections3.4
and4.2, especially Theorem4.4, already studies read-once coalitional formulas,
pivotality/power calculations and the series-parallel connectivity translation.
Cooperative power indices differ from costly-work CE, but both the natural
representation and its network interpretation have explicit close precedent.
Do not advertise series-parallel/read-once correspondence as newly discovered.

Therefore the useful local strategic formulation is a scoped corollary of
familiar differentiation, tree consistency and compact-CE optimization. A
strong publication claim needs additional representation structure or a sharp
boundary — for example the repeated-worker investigation and P17-X below.

## 3. P16-H: an elementary costed transfer of classical voting relevance

**Classification:** technically distinct restricted transfer/corollary, not a
new combinatorial hardness core or generic optimal-CE complexity phenomenon.
The exact common-cost fixed-margin statement remains a candidate whose
priority is unresolved. Its value lies in natural restrictions and a short
sharp certificate, not proof depth.

Matsui–Matsui2000 Section4 Theorem2, primary article
https://orsj.org/wp-content/or-archives50/pdf/e_mag/Vol.43_01_071.pdf , already
makes weighted-voting non-dummy recognition NP-complete. Restricted positive
SUBSET SUM and the target-weight1 parity encoding give a self-contained
relevance proof; this is not the new part. The additional steps are simply:
add a singleton backstop; set all costs1/2; in YES mix a target-containing
minimal winner at probability1/2+delta with failed target-only work at
1/2-delta. Every occurring conditional margin is at least delta, and target
payoff is exactly delta. In NO target is a dummy, so it never works under
obedience; backstop abstention forces success, and target payoff, to be at
least1/2+delta. The general backstop lower bound shows delta is also a global
YES lower bound. This is the entire reduction increment over relevance.

Papadimitriou–Roughgarden2008 Theorems5.7/5.10 and Barman–Ligett2015's
approximate-equilibrium quality hardness already establish the broad
existence-versus-optimization and approximation-hardness themes. Those
statements do not logically imply hardness of every subclass: the explicit
costed embedding is still needed for THIS fixed-benefit threshold class.
Ostroy–Song2006 explicitly studies minimum weighted CE payoffs and LP dual
interpretations, so the objective and a dual-certificate perspective are not
new either. Precise original-source passages/versions were actually inspected
in phase16-hardness-audit.md and phase15-succinct.md. None of those inspected
statements has been shown to imply the exact homogeneous-margin theorem
WITHOUT this additional elementary construction.

At maximum margin delta1/2 the YES law is just a pure minimal winner, making
the relevance connection especially transparent. Interior delta allows a
lower privately correlated payoff, but the reduction is still short. Retain
it as a sharp computational boundary accompanying stronger structure, rather
than repeatedly polishing the same gadget or presenting it as a standalone
major complexity breakthrough.

## P17-X — read-twice formulas can forbid compact exact payoff LPs

### Statement

For every fixed conditional margin0<=delta<=1/2, there is a family of
contribution games with B=1 and EVERY cost1/2 such that:

- task success is a monotone AND/OR formula of size O(N), with N workers and
  each variable occurring exactly TWICE;
- success can be evaluated in O(N) time;
- the joint region of success and ALL expected worker payoffs over
  delta-obedient private recommendations has linear extension complexity
  at least 2^{Omega(sqrt(N))}.

The lower bound is unconditional and permits arbitrary real coefficients and
arbitrarily many auxiliary variables. It concerns an EXACT simultaneous LP
representation of the whole region, not a specified optimizer, an approximate
relaxation, or a projection onto a fixed number of protected workers.

### Task and exposed face

Let G=K_(2m), with one worker per edge e, so N=binom(2m,2). Edge e covers its
two endpoints; task success means every vertex is covered by a working edge.
Equivalently

    F(x)=AND_{v in V} OR_{e incident to v} x_e.

Each variable appears in its two endpoint clauses. Expanding the clauses
and outer conjunction into binary gates uses O(N) nodes, without duplicating
any further occurrence. All numerical parameters are fixed constants.

Write R_delta for the joint payoff/success region. Let s be success and
x_e work marginals; u_e=s-x_e/2, so x_e=2(s-u_e) is an affine coordinate
change. Both inequalities

    s<=1,    sum_e x_e-m*s>=0

hold for EVERY law, before imposing incentives: a successful edge cover on
2m vertices uses at least m edges; failed profiles have nonnegative size.
Their equality intersection

    H={s=1, sum_e x_e=m}

is therefore a nonempty exposed face (intersection of two faces) of R_delta.
Any law on H succeeds almost surely. Its successful profiles have at least
m working edges and their expected size is m, so each supported profile has
exactly m edges. Covering2m vertices by m edges forces every vertex degree1:
the supported coalitions are perfect matchings.

Conversely, every perfect matching is a pure recommendation profile with
conditional switching gain EXACTLY1/2 for every worker. A selected edge is
pivotal, since removing it exposes two vertices; an abstaining edge can only
waste cost on an already successful task. Consequently every distribution on
perfect matchings is delta-obedient for every delta<=1/2, regardless of which
recommendations have zero probability. It belongs to H.

Hence H is affinely isomorphic, via x_e=2(1-u_e), to the perfect-matching
polytope of K_(2m). This proves equality, not merely containment of a few
hard vertices in a potentially easy polytope.

### Unconditional extension-complexity consequence

Rothvoss's primary journal-version author text,
https://arxiv.org/pdf/1311.2369 , arXiv1311.2369v4 dated17March2017, Theorem1
(PDFp3), gives perfect-matching extension complexity2^{Omega(2m)}. Its
introduction also explicitly recalls monotonicity under projecting a face.
Given any exact LP extension of R_delta, add the two displayed face equalities
and apply the affine coordinate map; this is an extension of the matching
polytope. Equalities need not count as inequalities; counting them as paired
inequalities changes the size by at most4. Thus

    xc(R_delta)>=xc(PM(K_(2m)))-O(1)=2^{Omega(m)}
                  =2^{Omega(sqrt(N))}.

The nonnegative-rank/slack-matrix and matching lower-bound mathematics is
ENTIRELY Rothvoss's prior contribution. We only transfer that theorem through
a newly identified task/payoff face. No proof of Rothvoss's deep theorem was
reimplemented or independently certified here.

### Meaning and limits

The same perfect-matching face already occurs in the NONOBEDIENT feasible
success/work polytope of the edge-cover task. Obedience retains that hard face
because all its pure profiles are equilibria. Thus this theorem does NOT show
an extension-complexity increase caused by incentives relative to the feasible
task-outcome polytope. It separates small task FORMULA/evaluation from compact
exact payoff geometry; it does not settle the stronger question of additional
intrinsic strategic compression cost. This distinction limits its conceptual
novelty and must survive every handover or manuscript summary.

This gives a sharp qualitative warning for controlled repetition: allowing
at most TWO occurrences per worker already loses the read-once guarantee of
a polynomial-size exact full-region LP. Formula syntax being a tree does not
control the strategic region when repeated occurrences identify the same
worker. The number of repeated workers in this construction is N; it does
not contradict FPT in that NUMBER, as opposed to maximum occurrence count.
Coverage's small-universe FPT bound also remains consistent: the universe
here has2m growing features, and the lower bound is exponential in that scale.
P14-A's FPT(k) explicit-hypergraph statement is not contradicted either:
all N workers are retained, and minimal edge covers are not explicitly listed.

Do not infer runtime NP-hardness from this result. Perfect-matching linear
optimization on this face is polynomial despite its exponential extension
complexity; even a proof of polynomial optimization for a larger region would
not invalidate the EF bound. The result does not rule out small semidefinite
representations, approximate LP descriptions, sequential algorithms, or an
algorithm computing a small-support law for one chosen objective. It also
makes no fixed-k lower-bound claim. Distinguishing those output/representation
notions is the purpose of this structural obstruction.

### Priority and significance assessment

A close game-theoretic precedent was also inspected: Ahmadinejad et al.,
*From Duels to Battlefields: Computing Equilibria of Blotto and Other Games*,
AAAI2016 primary proceedings PDF,
https://ojs.aaai.org/index.php/AAAI/article/download/10036/9895 , introduction
and matching-duel Section/Theorem6, PDFpp2,6. It already uses perfect-matching
polytope complexity to distinguish compact strategy descriptions from efficient
separation/equilibrium computation. Thus transferring matching geometry into
a game or warning that optimization need not require a compact LP is NOT new.
P17-X's narrower candidate is the read-twice contribution-game full-region face,
not the general game-theoretic relevance of extension complexity.

Targeted searches for CE payoff extension complexity and read-twice CE did
not locate this exact contribution-game statement. That is not a novelty
proof. Edge-cover/perfect-matching faces and extension-complexity transfer
are elementary established tools; a different solution concept alone does
not create new lower-bound technique. The useful candidate statement is the
unconditional READ-ONCE versus READ-TWICE exact strategic-region compression
boundary under identical costs and all fixed margins. This is a more informative
representation limitation than another weighted-threshold constant improvement,
but its task-specific priority still needs targeted external literature review.

## Exact checks and provenance

Five exact tests pass in experiments/test_phase17_originality.py. They check
the global supporting inequality for every coalition of K2,K4,K6; equality
coalitions against perfect matchings through K8; all workers' switching gains
at each small matching; a rational correlated mixture and affine payoff
recovery; and exactly-two variable occurrences/linear gate count. They do not
prove exponential extension complexity — Rothvoss's theorem does — nor
implement a CE optimizer. Only the three assigned branch files were edited.

## Publication recommendation

Do not present P14-A/P16-T1/P16-H as three independent major discoveries.
Their strongest honest narrative is a useful protected-region lemma, a natural
explicit tractability application and a sharply restricted elementary hardness
transfer. P17-X adds a genuinely different output-representation obstruction,
with deep external lower-bound input openly credited. Together with a rigorously
checked repeated-worker FPT theorem it could justify further focused paper
planning, but not a declaration that originality questions are settled. No
new manuscript or external submission is recommended solely on internal
agreement or absence of a matching search result.
