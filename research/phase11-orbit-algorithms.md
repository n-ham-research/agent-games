# Phase 11 — Incentive-preserving orbit algorithms

Author Nicholas Ham; development and exact checks assisted by Codex. 16 October
2026. These are proved method corollaries and counterexamples, not novelty
claims. They concern finite complete-information games with exact rational
utilities; they do not establish truthful type elicitation or decentralized
implementation. No companion repository is modified.

## 1. Prior result that changes the research question

Tewolde, Zhang, Oesterheld, Sandholm and Conitzer, *Computing Game Symmetries
and Equilibria That Respect Them*, AAAI 2025, is direct prior art. The
[24-page author manuscript](https://emanueltewolde.com/files/symmetries.pdf),
accessed 16 October 2026, Section 5 and Appendix E, Theorem 9 (PDF pages 8 and
23), gives an action-orbit Nash algorithm with runtime polynomial in normal-form
input size, log(1/epsilon), and (qn)^q, where q counts orbits of the disjoint
union of player actions. The displayed bound is polynomial for fixed q; its parameterized classification
needs the input-size observation below rather than an automatic XP-only label. Its two-player
bound uses 2^q. Proposition 18 and Theorem 8 give PPAD and team-game CLS completeness. Theorem 9's orbit-polynomial method is
therefore the baseline, not a proposed discovery here. No unprinted revision
date is assigned to the downloaded author version.

Two other primary texts were inspected:

* Papadimitriou and Roughgarden,
  [*Computing Correlated Equilibria in Multi-Player Games*](https://theory.stanford.edu/~tim/papers/sym.pdf),
  author PDF, Sections 3–4: compact representations, symmetric games and
  correlated-equilibrium algorithms are prior territory.
* Jiang and Leyton-Brown,
  [*A General Framework for Computing Optimal Correlated Equilibria in Compact Games*](https://arxiv.org/pdf/1109.6064),
  arXiv:1109.6064v1, Sections 2–3: deviation-adjusted social welfare gives a
  general sufficient algorithmic route for optimal CE in compact games.

Brandt, Fischer and Holzer, [*Equilibria of Graphical Games with Symmetries*](https://webspace.maths.qmul.ac.uk/felix.fischer/publications/bfh_graphsymm.pdf),
author preprint dated 27 January 2010 (published TCS 2011), Definition 3 and
Section 5/Theorem 6 were inspected after the publisher returned 403. Their
symmetry is a local common-payoff-function/neighborhood-count condition, not
an arbitrary supplied typed automorphism group. Theorem 6 gives polynomial
mixed-equilibrium computation for their symmetric graphical games when action
count is O(log k/log log k), with k neighborhood size. It proceeds through a
smaller ordinary symmetric game. AG-O1 instead uses bounded action-orbit
count and factor arity, allows ordered neighbor effects and sums of factors,
and does not require their neighborhood anonymity. Neither result generally
subsumes the other. The overlap makes originality provisional.

## 2. Local interactions replace player count by interaction arity

Let A_i be explicitly listed finite actions. Suppose each player's payoff is
an explicitly listed sum of rational factors

    u_i(s) = sum_{F in F_i} f_{iF}(s_F),   i in F,   |F| <= d.

Factor scopes contain their focal player; dummy dependence is allowed. L is the
binary input length of all scopes, factor tables, action lists and supplied
group generators. Negative factors are allowed. The supplied typed maps generate
a group G of **exact automorphisms of the sum game**. Individual factors need
not be permuted or preserved. This validity is a promise, not a free efficient
automorphism-discovery algorithm.

Write Omega for the disjoint union of pairs (i,a), and q for its G-orbit count.
Let w(i,a) be an orbit index, and c_iw count actions of player i in orbit w.
Invariant independent mixed profiles have the unique representation

    sigma_i(a) = x_{w(i,a)},   x_w >= 0,
    sum_w c_iw x_w = 1.

Thus x denotes probability **per action**, not total orbit mass. Constraints
need only one representative of each player orbit. If b is the number of player
orbits, then b <= q, because action orbits cannot cross player orbits.

### AG-O1 — Bounded-arity action-orbit Nash reduction

For this representation, exact invariant Nash equilibria are the solutions of a
rational polynomial system with at most q+b <= 2q variables, O(q+b) constraints,
and degree at most D=max(2,d). Its coefficients can be constructed in polynomial
time in L. Standard fixed-dimensional real-algebraic algorithms give runtime

    (q D)^{O(q)} poly(L)

for an exact real-algebraic solution, with the usual algebraic-number output
representation. Rational epsilon-Nash profiles can instead be produced with an
additional polynomial dependence on log(1/epsilon). This is a computational
corollary of established orbit reduction and real-algebraic feasibility, not a
new equilibrium-existence theorem. The displayed bound is FPT in the joint parameter (q,d). For explicit factor
tables it also yields FPT in q alone by the logarithmic-arity argument below.
It does not assert a polynomial algorithm when q grows with input size.

**Proof.** For each action-orbit representative (i,a), expand

    P_w(x) = sum_{F in F_i} sum_{t in A_{F\{i}}}
             f_{iF}(a,t) product_{j in F\{i}} x_{w(j,t_j)}.

Each term has degree at most d-1. The inner enumeration is bounded by the
explicit factor table size, so all q polynomials, including aggregation of
coincident monomials, have polynomial encoding size in L. Transport of the
whole payoff under G shows the conditional payoff is the same for every
representative of w on an invariant profile; factor-by-factor invariance was
not needed. Add a value variable v_B per player orbit B and impose

    P_w(x) <= v_B,
    x_w (v_B - P_w(x)) = 0

for all action orbits w lying over B, together with normalization and
nonnegativity. A normalized player has at least one positive action, so these
conditions say exactly that all used actions maximize conditional payoff.
Their largest degree is max(2,d). Normalization gives x in [0,1]; v_B is bounded
by the sum of absolute factor maxima, whose encoding length is polynomial in L.
Invariant Nash existence is the established finite-game fixed-point result.
Real-algebraic sampling for s polynomial constraints of degree D in O(q)
variables has arithmetic/bit complexity (sD)^{O(q)} times a polynomial in input
coefficient length. It applies here with s=O(q).

For rational approximate output, approximate an algebraic solution and repair
normalization using orbit masses. More explicitly, use the orbit masses r_w=c_iw*x_w at a representative player i of each
player orbit. These masses form one simplex per player orbit, and c_iw is
constant over that player orbit. Round each simplex to a rational grid of
mesh at most delta/(2q), put any remaining mass into one coordinate, and
then set x_w=r_w/c_iw. This preserves every normalization and gives every
marginal l1 error at most delta. Algebraic comparisons at a grid boundary
can be made exactly, or a slightly finer grid can absorb approximation error. For bounded
utilities |u_i|<=M, changing every marginal by at most delta in l1 changes any
conditional or realized payoff by at most 2Mn delta, by total-variation
coupling of product distributions. Regret therefore changes by at most 4Mn
delta. Taking delta<=epsilon/(4Mn), with the trivial M=0 case handled
separately, requires polynomially many extra precision bits. The marginal
norm, rather than an unqualified coordinate norm, matters here. This is not
an implementation algorithm for strategic reports. QED.

### AG-O1b — Explicit-table logarithmic absorption

With the same explicit local-table input, the runtime is in fact f(q) poly(L),
including algebraic output: q alone is an FPT parameter. This refinement uses
input size, not an additional game-theoretic theorem.

**Proof.** Eliminate every singleton-action player by substituting its unique
action into all factors. Singleton status is preserved by every typed
bijection, so the reduced game inherits the exact group action. Ignore
incentive constraints of removed players, who had no deviations. The remaining
action-orbit count q' is at most q. If a residual factor involves t active
players, its explicitly listed original table had at least 2^t entries, so
t<=log_2 L. A conditional expected-payoff polynomial therefore has degree at
most log_2 L, and the complementarity system has degree at most 2+log_2 L.
The AG-O1 bound becomes (q log(L+2))^{Cq} poly(L) for a universal constant C.
For a=Cq and t=ln(L+2), t^a exp(-t)<=(a/e)^a; hence
(ln(L+2))^{Cq} <= (Cq/e)^{Cq}(L+2). All q-dependence can be absorbed into a
computable f(q), leaving a fixed polynomial exponent in L. The same observation
applies to the normal-form Tewolde bound after singleton elimination because
its full table has at least 2^{n'} profiles. Thus AG-O1b does **not** distinguish
our result from that prior by claiming the prior is intrinsically XP-only.
The sparse representation difference is that the entire global payoff table
need not be read or stored. QED.

This argument fails for circuit/oracle factor descriptions with exponentially
large scopes but short encodings; there the degree need not be logarithmic in
input length. A circuit is not silently treated as an explicit table.

### AG-O1c — Welfare selection within the invariant Nash set

For explicit rational welfare weights alpha_i, an eta-optimal invariant Nash
equilibrium can be found in f(q,d) poly(L,log(1/eta)) time, with exact algebraic
Nash output; AG-O1b makes q alone an FPT parameter for explicit tables. This is
a standard real-algebraic optimization corollary. It does not compare the
invariant optimum to welfare of unrestricted Nash equilibria.

**Proof.** Expected weighted welfare is the polynomial

    W(x)=sum_i alpha_i sum_{F in F_i} sum_{t in A_F}
          f_{iF}(t) product_{j in F} x_{w(j,t_j)},

of degree at most d. Its encoding can be constructed in polynomial time in L
(including the weights). Appending W(x)>=z for a rational threshold z to the
AG-O1 constraints adds one inequality without new variables. Feasibility
queries therefore have the same parameter dependence. A rational bound on
|W| is B=sum_i |alpha_i| sum_F max_t |f_{iF}(t)|, whose encoding length is
polynomial in L. Start with lower bound -B (feasible by invariant Nash
existence), upper bound B, and bisect. Retain a witness for each feasible
threshold. After O(log((B+1)/eta)) queries, the retained algebraic Nash witness
has W>=OPT-eta. This is bit precision, not polynomial dependence on 1/eta.
A final rational approximation can preserve epsilon-Nash and lose at most
another eta welfare: with marginal l1 error delta, product coupling gives
|W(sigma)-W(tau)|<=2Bn delta, so choose delta small enough for both this bound
and the AG-O1 regret bound. B=0 and M=0 are handled trivially. QED.

**A family beyond full anonymity.** On a directed cycle of n>=4 agents, each
with binary actions, u_i(s)=1[s_i=s_{i+1}], cyclic rotation is an exact player
transitive automorphism. Arbitrary player permutations are not: exchanging two
adjacent vertices changes a directed dependency. For the rotation subgroup,
q=2 and d=2, independently of n. The all-half profile is an invariant mixed NE.
For the larger subgroup also generated by simultaneous action complement,
q=1 and that invariant independent profile is forced. The construction and
proof apply to heterogeneous local scopes whenever their *sum game* has the
supplied automorphisms; they do not require an ordinary full matching or a
splitting result from Game Symmetry.

This illustrates the useful parameter: efficient construction of expected
**deviation payoffs**, not merely counting joint-profile orbits. A constant
q can coexist with exponentially many such profile orbits.

## 3. A complete deviation-orbit LP for correlated recommendations

Let S=product_i A_i. G acts on S and on deviations
D={(i,a,b): a,b in A_i, a!=b}. Let O_1,...,O_m be profile orbits and choose one
d_z=(i_z,a_z,b_z) from each of the r deviation orbits. Define

    R_zl = (1/|O_l|) sum_{s in O_l} 1[s_i=a]
            (u_i(s)-u_i(b,s_-i)),   (i,a,b)=d_z.

Let c_l be an invariant objective's value on O_l; for a nonconstant objective
replace it by its orbit average, but then symmetry averaging need not preserve
its optimum. Here assume the objective itself is invariant.

### AG-O2 — Exact orbit CE program and sparse orbit support

The invariant CE maximizing the given objective are exactly the lifts of

    maximize c^T y
    R y >= 0,   y >= 0,   sum_l y_l=1,

where lifting means assigning probability y_l/|O_l| to each s in O_l. There is
an optimal solution using at most r+1 profile orbits. It attains the same
optimum as unrestricted CE for an invariant objective.

**Proof.** An invariant distribution is uniform within each orbit, so the
unconditional CE obedience constraint for d_z is precisely (Ry)_z>=0. Every
other deviation is a G-transport of one representative; exact payoff
preservation and invariance of the distribution make its regret equal to that
representative's. Consequently no incentive constraint is omitted. Conversely
all representative constraints imply all CE inequalities. Averaging any CE
under G remains CE and leaves invariant objective expectation unchanged,
proving equality of optima. A vertex optimum exists in the compact LP. If t
variables are positive, a basic solution needs t independent active constraints
beyond the zero coordinates; at most r obedience constraints plus the simplex
equality are available, giving t<=r+1. QED.

This is ordinary linear symmetry reduction specialized to CE, not a new general
polynomial-time compact-game theorem. With a supplied list of m orbits and an
exact routine returning the r*m coefficients, LP work is polynomial in m,r and
coefficient bit length. **The coefficient routine, orbit construction and
sampling/lifting costs are part of the algorithm.** Enumerating all profiles
is a correct baseline and may be exponential in n. Supplied generators alone
do not imply a polynomial profile-orbit list or a polynomial regret-sum oracle.
Uniform sampling from an orbit is also a separate representation requirement;
a huge uniform orbit should not be expanded into a claimed polynomial-size
explicit joint-distribution output. A central sampler that chooses an orbit
and then a uniform element, followed by private recommendations, implements the
CE if available; no anonymous-independent local implementation follows.

## 4. Exact failures of tempting reductions

### AG-O3 — Orbit welfare tables do not preserve incentives

Two players have binary actions and exact player-swap symmetry. Define
u_0(0,0)=u_0(1,1)=0, u_0(0,1)=1, u_0(1,0)=-1 and u_1(a,b)=u_0(b,a).
Let the second game be the negative of both payoffs. Both have the same profile
orbits {00}, {01,10}, {11}, and welfare zero on every profile. Their orbit
welfare descriptions, including orbit cardinalities, are identical. In the
first game action 0 strictly dominates 1 for both players; in the second,
action 1 strictly dominates 0. The unique CE are respectively delta_00 and
delta_11. Thus even optimal-CE reconstruction cannot be justified from
welfare-only orbit data. Pointed deviation data, or an oracle equivalent to it,
is essential. This does not refute orbit representations that retain the full
equivariant payoff vector or all required pointed payoffs.

### AG-O4 — Transitivity does not bound profile-orbit complexity

For binary actions and rotation group C_n, each profile orbit has size at most
n; hence there are at least 2^n/n profile orbits. The action-pair orbit count
is only two. Player transitivity, including a strategy-trivial transitive
section, therefore does not by itself make profile enumeration polynomial.
This is a counting obstruction for that algorithm, **not** a computational
hardness theorem. The cycle family above shows why local-factor algorithms
can succeed even when a whole-profile orbit table cannot be constructed in
polynomial time.

### AG-O5 — CE lifting does not supply independent implementation

In binary anti-coordination, the uniform lottery on 01 and 10 is invariant,
is CE, and succeeds with probability one. Identical independent local policies
with action-1 probability p succeed with probability 2p(1-p)<=1/2. Even a public
seed with identical seed-conditioned local marginals and conditional independence
preserves this upper bound after averaging. The same public bit *with distinct
role-labelled complementary policies* implements the lottery. Thus the missing
resource is architectural; a reduced LP does not create the necessary private
recommendations or distinguishable roles. This is the classical witness already
used in AG-E2, retained here to prevent an algorithm/implementation conflation.

## 5. Research recommendation and contribution boundary

The useful broad result from this pass is AG-O1's explicit sparse-input degree
bound, accompanied by AG-O2's exact incentive-preserving CE representation.
Both are established-method corollaries. The highest-value open question is
which succinct game classes have efficiently computable pointed-orbit regret
sums and low action-orbit complexity **without** full anonymity, and whether
those inputs support cheap decentralized implementation. Local factor arity is
one sufficient condition; it is not a necessity theorem. No generic benefit
from player transitivity, full player image or splitting has been proved.

For distributed task-allocation games whose interactions are explicitly local,
whose exact typed symmetries are certified, and whose q and d are small, AG-O1
permits central equilibrium calculation without storing the full joint table.
It guarantees approximate unilateral incentive compatibility, not high welfare,
truthful revelation, communication efficiency, learning convergence or rational
behavior by actual LLM agents. A substantial original contribution would need
a sharper tractable representation theorem or an implementation lower bound
beyond the prior algorithms, rather than another orbit-count formula.

## 6. Source-access and verification record

The real-algebraic complexity ingredient is an established external algorithm,
not an algorithm implemented by the experiment. The primary Tewolde appendix
proof of Theorem 9, PDF pp23–24, explicitly applies Renegar's system-solving
bound with polynomial dependence on the remaining system parameters and
constructs inverse-exponential rational approximations. Basu's
[author survey](https://www.math.purdue.edu/~sbasu/raag_survey2011_final.pdf),
Theorem 2.15, separately states the singly exponential sample-point arithmetic
bound. Exact sample-point representations and their polynomial coefficient-bit
dependence are the standard sampling ingredient invoked here. The original
Renegar Part I publisher body returned 403; the Cornell approximation report
TR858 returned 405 even via an approved read-only download; the original
Basu–Pollack–Roy author book link failed. These full-body access gaps are
retained rather than silently counted as independent original-source checks.
Before publication, check the precise sampling/bit-complexity formulation in
the original real-algebraic reference, including exact-output encoding. The
polynomial reduction, q-only logarithmic absorption, incentive equivalences
and rational rounding arguments above are independent local proofs.

Eight exact tests pass in `experiments/test_phase11_orbits.py`: conditional
polynomials versus full expectations on directed cycles; a nontrivial invariant
p=2/3 equilibrium; typed action maps and failure of full player symmetry;
offsetting nonsymmetric factors; every deviation in each compressed CE row
against full inequalities for a grid of orbit mixtures; welfare-table incentive
loss; exponential cyclic profile-orbit growth; and the CE/independence gap.
The experiment enumerates small profiles for validation; it is not a general
real-algebraic equilibrium solver and does not empirically establish asymptotic
runtime. A second agent independently reconstructed AG-O1/O1b/O1c and found no
mathematical defect, while retaining the real-algebraic original-source gap.
The root review is separate; internal AI review is not external peer review.

Phase12 source update: see phase12-source-audit.md. The previously missing
sampling/bit/output statements were inspected in original author-book text
through a disclosed mirror. Historical access failures above remain accurate.
