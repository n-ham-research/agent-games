# Phase 16 — independent payoff-hardness audit and homogeneous robust extension

16 October2026. Nicholas Ham's research programme. This branch independently
reconstructed P15-S4 directly from pure-profile utilities and implemented fresh
checks importing NO earlier-phase game helpers. The same AI instance developed
part of Phase15, so this is an independent derivation/implementation, not an
independent human reviewer or a fresh model's audit. Root and separate agents
supply additional proof attacks. Novelty remains provisional.

## P16-H1/H2 — audit outcome and stronger restricted theorem

P15-S4 survives reconstruction: with B=1 and costs1/2,3/4, minimum target CE
payoff is0 in YES instances and at least1/4 in NO instances. Its reduction,
encoding, NP certificate and distinct approximation statements are sound.
The claimed NO lower bound is not generally an attained equality.

A useful strengthening removes ALL cost heterogeneity. Every agent can have
cost exactly1/2. Then YES minimum CE payoff is0; NO minimum is at least1/2.
Zero-payoff feasibility remains NP-complete. Two-sided optimal-value additive
error strictly below1/4 is NP-hard. This is a restriction improvement, not
merely a better constant.

Moreover, for every fixed rational 0<=delta<=1/2, consider laws with conditional
obedience margin at least delta at each positive-probability recommendation.
In the same homogeneous game, YES minimum payoff is EXACTLY delta, while NO
minimum is at least1/2+delta. The gap remains1/2. For example delta=1/4 gives
minimum1/4 versus minimum>=3/4 despite strict positive incentives whenever a
recommendation occurs. Thus the earlier hardness is not confined to weak
obedience or exact zero punishment. These are private literal-action CE laws,
not reporting mechanisms or decentralized implementations.

## Independent construction and all-agent obedience proof

Positive SUBSET SUM asks if some subset of positive integers a_j sums to T.
Reduce to inputs 0<a_j<T as follows. If T=0 or any a_j=T, map to fixed YES
((1,1),T=2). Discard a_j>T. If no retained items or their sum<T, map to fixed
NO ((2,2),T=3). Otherwise all remaining items satisfy the required restriction.
Positive integer T=1 is automatically settled in these cases. These operations
are polynomial and preserve YES/NO without solving the residual instance.

There is a protected target i, an item worker for each retained item and a
backstop r. Set quota Q=2T+1 and weights

    w_i=1,    w_j=2a_j,    w_r=Q.

For pure active set A use the original utility, not an inferred surrogate:

    u_j(A)=1[sum_{h in A} w_h>=Q]-c_j 1[j in A].

A recommendation law is CE iff for each agent and each recommendation a,
the unconditional sum of the recommended-versus-switched utility difference
is nonnegative. A positive conditional margin delta subtracts delta times
the probability of that recommendation from the same row. Zero-probability
recommendations impose no conditional constraint.

The only singleton winner is r. No pair consisting of i and one item worker
wins: 1+2a_j<=2T-1<Q. In every instance the known profile {r} is a successful
pure Nash equilibrium: r's gain from work is1-c_r>0, and every abstainer saves
its positive cost by abstaining from an already completed task. Hence finding
some successful minimal winner or equilibrium is easy even on hard instances.

### General backstop calibration

Give target cost c in(0,1), backstop cost b in(0,1), item costs any numbers
in(0,1). Suppose a selected item subset sums to T and let M contain i and
those item workers. It has total weight exactly Q and is inclusion-minimal:
removing any positive-weight member drops the sum below Q. Put t=1-b and
assume t<=c. The probability law

    Pr(M)=t,
    Pr({i})=t(1-c)/c,
    Pr(empty)=1-t/c

is well defined. Target works with probability t/c; task succeeds with
probability t. Its work-obedience gain is t-c(t/c)=0, so its expected payoff
is0. Its abstention signal, if present, is empty, and it cannot repair alone.
Every selected item worker works only at M, is pivotal there and gains
1-c_j>0; when it abstains on failure it cannot repair empty or {i}. An item
outside M always abstains, cannot repair either failure and saves cost on
success. Backstop always abstains; its deviation would replace success
probability t by certainty at cost b, so its gain from obedience is b-(1-t)=0.
This verifies every action-contingent IC row. Literal private recommendations
are essential: public revelation of {i} could make the backstop deviate.

Original P15 calibration b=3/4,c=1/2 gives masses1/4,1/4,1/2. Its conditional
rows are: target work0; target abstain1/2; selected-item work1/2; every
item abstention1/2; backstop abstention0. Item workers recommended abstention
can also see M if outside it, but switching still only wastes cost. These
calculations concern recommendation-conditional utility differences, not
only nonnegative unconditional totals.

### Homogeneous costs and positive conditional margins

Set EVERY cost to1/2. For fixed0<=delta<=1/2 use

    Pr(M)=1/2+delta,    Pr({i})=1/2-delta.

The target always works. Its conditional work gain and payoff both equal
delta. Backstop always abstains and its conditional gain is delta. Each
selected item worker is pivotal whenever told to work and gains1/2. Whenever
an item worker abstains it either cannot repair failure or would waste cost
on success, so its conditional gain is1/2. Hence every occurring
recommendation has margin at least delta. At delta=0 the law has two equally
likely profiles; at delta=1/2 it reduces to the pure minimal winner M.

For ANY delta-obedient law with these homogeneous costs, backstop abstention
implies

    s-1/2-x_r/2 >= delta(1-x_r),
    s >= 1/2+delta+(1/2-delta)x_r >= 1/2+delta.

Thus target payoff s-x_i/2>=delta because x_i<=1. The constructed law attains
this bound in YES instances, proving the stated EXACT YES optimum. This lower
bound does not use subset relevance and is valid in both YES and NO.

## NO parity, payoff gap and approximate obedience

If the original subset instance is NO, the target is never pivotal. A coalition
already containing r succeeds without i. Otherwise its item weight is even;
adding weight1 crosses odd quota2T+1 iff the item sum is exactly2T, which is
precisely a target-T subset. This excludes target pivotality at every pure
profile, not merely at minimal winners.

For any law let x_i,x_r be work marginals and s success probability. Write
G_i1 and G_r0 for its target-work and backstop-abstention unconditional
obedience gains. In a NO instance,

    G_i1=-c*x_i,
    G_r0=s-(1-b)-b*x_r,
    u_i=(1-b)+b*x_r+G_r0+G_i1.                 (dual certificate)

This is a columnwise identity, so does not assume obedience. With CE rows
nonnegative it proves u_i>=1-b: original gap1/4, homogeneous gap1/2.
Alternatively target work is strictly dominated, forcing x_i=0, while the
backstop's always-work deviation supplies a success floor. The displayed
identity quantifies both in a single transparent inequality.

For unconditional eta-approximate CE, each row can be >=-eta, and therefore

    u_i >= 1-b-2eta.

This is not conditional-margin obedience. Homogeneous YES still has exact CE
payoff0; homogeneous NO has payoff>=1/2-2eta for every eta-approximately
obedient law. For example eta=1/32 gives NO payoff>=7/16, ruling out a
polynomial algorithm returning such a law whose target payoff is at most the
EXACT CE optimum plus1/8, unless P=NP. An explicit rational output law can
be evaluated in polynomial time. No claim about arbitrary black-box sampler
expectation evaluation is smuggled into this implication.

With POSITIVE conditional margin delta in the homogeneous game, target work
is impossible in NO: its conditional gain, whenever recommended work, is
-1/2<delta. Thus x_i=0 and the earlier backstop bound yields

    u_i=s >= 1/2+delta+(1/2-delta)x_r >= 1/2+delta.

The feasible set is never empty: pure profile {r} has every occurring
conditional gain1/2, hence is delta-obedient for all delta<=1/2. This prevents
an accidental reduction based merely on feasibility of positive margins.

### How strong can this construction's gap be?

Within the GENERAL weak-obedience family the certified gap is1-b, with target
cost required to satisfy c>=1-b. Choosing small fixed b and large fixed c makes
it approach1. There is no attained unit gap with b>0. This numerical tuning
alone is not a separate research contribution. Under a COMMON cost c=b the
condition is c>=1/2, so this family's certified gap1-c is maximized at the
homogeneous choice c=1/2. No global optimality among all possible reductions
or all contribution games is asserted.

At delta=1/2 the robust homogeneous version becomes pure-minimal-winner
relevance: YES has a pure equilibrium including i, NO never does. This makes
the classical weighted-voting relation particularly explicit. For interior
delta, a private correlated law provides the sharp smaller protected payoff.

## Complexity and careful decision/output claims

The reduction uses m+2 explicitly listed agents. Weight encodings have length
O(sum_j bit(a_j)+m+bit(T)); costs, B and fixed delta require only constant
additional bits. No payoff table or minimal-winner enumeration is needed.
Recognizing success and computing any pure switching gain are polynomial
binary sum/comparison operations. The hardness is ordinary computational
hardness for succinct threshold input, not a query lower bound, #P statement,
or fine-precision output barrier. It is compatible with pseudopolynomial
weight DP and is not claimed strong NP-hardness.

Zero-payoff CE feasibility belongs to NP, also for the common-cost restriction.
The conceptual full-profile LP has 2n obedience inequalities, normalization and
one target-payoff equality. A nonempty face admits a basic feasible law with
O(n) nonzero profile probabilities. Rational determinant bounds give polynomial
bit length because each coefficient has polynomial input bit length and the
number of active rows is O(n). Each selected profile has n bits. A verifier
computes every utility, two action-conditioned rows per agent, normalization
and target payoff directly. This proves NP membership without requiring a
polynomial algorithm to enumerate all profiles or to optimize the LP.

For fixed positive delta, the decision 'does a delta-obedient law have target
payoff <=delta?' is likewise NP-complete, with the same few-row certificate
and exact YES lower bound. The NO gap is1/2. Linear row coefficients include
-delta times recommendation mass, not a constant subtracted once per row.

Value and law approximations must remain distinct:
- With common costs, a value within two-sided additive error strictly below
  1/4 separates opt0 from opt>=1/2. With fixed positive margin delta the same
  accuracy separates optdelta from opt>=delta+1/2.
- Returning an EXACT obeying law with objective at most optimum+epsilon is
  already hard for any fixed epsilon<1/2, because YES output is below the NO
  lower bound. This one-sided performance convention differs from value error.
- Approximately obedient law output has the explicit degraded NO bound above.
  A general approximation claim must specify the row-slack convention and
  whether objective accuracy is relative to exact or approximate CE optimum.
- No hardness of finding SOME CE or delta-obedient law is obtained: {r} works.
- Expected payoff over a polynomial explicit rational law is easy to evaluate;
  arbitrary succinct sampler circuits may conceal additional counting issues.

## Ruthless primary comparison and novelty assessment

Actually reopened/inspected16October2026:

1. Matsui–Matsui, *A Survey of Algorithms for Calculating Power Indices of
   Weighted Majority Games*, ORSJ43(1), March2000, Section4 Theorem2 and its
   PARTITION proof, https://orsj.org/wp-content/or-archives50/pdf/e_mag/Vol.43_01_071.pdf .
   Non-dummy recognition is ALREADY NP-complete. Small-target-weight/parity
   relevance is therefore classical. Our reduction should explicitly be called
   a reduction FROM weighted-voting relevance, even if SUBSET SUM gives its
   self-contained proof. The only additional mathematics needed is the
   backstop and the short all-agent CE witness/gap certificate. This is a
   modest task-specific transfer, not a new NP-hard combinatorial core.
2. Papadimitriou–Roughgarden, *Computing Correlated Equilibria in Multi-Player
   Games*, author PDF https://timroughgarden.org/papers/cor.pdf , Section5.3
   Theorem5.7/reconstruction, Section5.4 anonymous games and Section5.5
   Theorem5.10/proof. Optimal CE complexity and the gap between finding some
   CE and optimizing it are long-established. Their displayed hardness classes
   and reductions do not by themselves establish our common-cost weighted-
   threshold/single-protected-agent restriction. Conversely, our result is not
   a new general separation between equilibrium existence and optimization.
3. Jiang–Leyton-Brown, *A General Framework for Computing Optimal Correlated
   Equilibria in Compact Games*, arXiv1109.6064v1 (28September2011),
   https://arxiv.org/pdf/1109.6064 , Section3 Proposition1 and Section4.1.
   Their deviation-adjusted objective method is the correct algorithmic context.
   It neither asserts all succinct CE objectives are tractable nor supplies
   hardness of every subclass when a sufficient separation method fails.
   Our positive dynamic programs are applications; S4's negative result needs
   the separate explicit reduction, not merely lack of a small summary.
4. Barman–Ligett, *Finding Any Nontrivial Coarse Correlated Equilibrium Is Hard*,
   arXiv1504.06314v1 (23April2015), https://arxiv.org/pdf/1504.06314 , introduction,
   Theorem3 approximate-equilibrium hardness discussion, Section4 framework and
   Section4.1 bounded-influence aggregative model. Near-optimal approximate CE
   hardness is ALREADY known generically, even with additional restrictions.
   Our claim can only concern the fixed-benefit weighted-threshold/common-cost
   subclass and a designated MINIMUM payoff. Binary-threshold jumps need not
   satisfy both their polynomial aggregate range and bounded-influence promise
   after normalization, so their positive theorem is not contradicted.
5. Ostroy–Song, *Correlated Equilibrium and the Pricing of Public Goods*,
   Autumn2006 author working paper https://repository.essex.ac.uk/8905/1/dp616.pdf ,
   introduction and general normal-form setup, worst weighted-payoff discussion
   and Section3 Theorem3/worst-case discussion inspected. Minimizing CE payoff and characterizing
   worst CE via duality are explicitly established topics. Their public-good
   interpretation of arbitrary normal-form outcome lotteries does not itself
   give a succinct weighted-contribution complexity classification. Our dual
   certificate is a particularly small instance of established LP reasoning,
   not a novel duality principle.

The Cavaliere February2000 working-paper comparison in phase14-literature.md
remains relevant: common-cost count-threshold symmetric CE are direct economic
prior. This audit retrieved the same working PDF, whose machine text is badly
encoded; it does NOT claim a new visual/full-source verification or access to
the final2001 publication. Do not conflate heterogeneous task weights with
heterogeneous costs or label our homogeneous weighted game anonymous: workers
can have different strategic importance despite equal costs.

**Assessment.** No inspected theorem has been shown to ALREADY STATE the exact
homogeneous, one-agent, fixed-gap (including positive conditional-margin)
classification. That observation is not originality clearance. Much of its
proof is a straightforward transfer from classical weighted-voting relevance
using elementary CE inequalities. The improvement is a sharply restricted,
natural cost-homogeneous contribution class and robustness beyond weak
obedience, not a new general complexity phenomenon. A focused contribution
might combine this boundary with a genuinely useful positive task class and
the protected-region structural theorem; this short hardness transfer alone
is weak evidence for a substantial standalone paper. A primary search should
continue for worst individual CE payoffs in weighted public-good games and
for prior costed embeddings of voting dummy recognition.

## Independent exact verification and contribution record

Eight new exact tests pass using Fraction arithmetic and direct utility tables.
They import only Python standard-library modules and this phase's independent
implementation. Checks cover unrestricted small SUBSET SUM preprocessing,
including empty lists, T=0, equal/oversized items; parity/relevance and known
backstop pure equilibrium; all conditional rows of original and common-cost
YES laws; positive margins0,1/20,1/4,1/2; general rational backstop/target
calibrations; NO dual identities column by column; positive-margin NO identities;
and approximation thresholds. Finite checks corroborate identities and examples;
the asymptotic reduction/NP certificate remain analytic proofs.

Root and the separate resource instance independently reconstructed the homogeneous
positive-margin extension without finding a defect; actual review is in AG-P16-REVIEW.md. No shared files, manuscript,
companion repository or commit were changed by this branch.
