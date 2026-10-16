# Phase 18 — comparable-coordinate complexity caused by obedience

16 October2026. Nicholas Ham's programme; strategic-geometry Codex branch.
The root agent proposed the ordinary collision-game construction. This branch
reconstructed it, strengthened its input representation to explicit polymatrix
payoffs, and developed a positive-margin best-shot variant. Known stable-set,
best-shot, CE and matching mathematics is explicitly credited. These are
short representation consequences, not originality clearance or external review.

## 1. What is being compared

N explicitly listed binary-action agents choose a_i in{0,1}. A centralized
private recommendation law is an arbitrary distribution pi over these profiles.
The output coordinates on BOTH sides are EXACTLY the N own-action marginals

    x_i=Pr_pi(a_i=1).

With no incentive constraints, every profile is physically allowed, including
colliding profiles. The marginal region is [0,1]^N, with2N inequalities: every
point is realized by independent Bernoulli actions. The strategic region uses
the SAME coordinates and SAME set of physically allowed profiles, but requires
CE obedience. There are no extra strategic-side reliability, utility, pairwise
collision or auxiliary output coordinates in this comparison.

Collisions are allowed outcomes with utility losses, not prohibited physical
feasibility constraints. If they were prohibited ex ante, the baseline would
already be the stable-set polytope and the claimed causal gap would disappear.
The result concerns RECOMMENDATION MARGINALS, not automatically payoff regions.

## P18-G1 — ordinary CE/CCE can change a cube into a matching polytope

Given a simple conflict graph G on N agents, let D=max(1,maximum degree) and

    u_i(a)=1-(a_i/D)*sum_{j adjacent to i} a_j.

All utilities lie in[0,1]. The game has two actions and an explicit polynomial-
size POLYMATRIX representation: for degree d_i>0, each adjacent pair contributes
1/d_i-a_i a_j/D to player i. Summing gives the displayed utility. Isolated
agents may have a constant unary payoff1; the lower-bound family has no
isolated agents. Each pair table has four entries and rational bit length
O(log N). Thus the result does not hide an exponential local payoff table or
an arbitrary payoff circuit. It is also a potential game: action differences
are those of minus the number of colliding active pairs, divided by D.

The work-conditioned CE row is

    E[1[a_i=1]*(u_i(a)-u_i(0,a_-i))]
      =-(1/D)*sum_{j adjacent to i}Pr(a_i=a_j=1).

Every term is nonpositive, so obedience forces each adjacent pair's joint
activation probability to zero. A finite union of these zero events shows
that EVERY supported profile is an independent set. Abstention rows are always
nonnegative: switching from0 to1 only risks an active-neighbor penalty.
Conversely, a law supported on independent sets has zero work gains and
nonnegative abstention gains, so is CE. Hence

    {CE laws}=all laws supported on independent sets,
    {CE action marginals}=STAB(G).

The same equality holds for COARSE correlated equilibrium. Its always-abstain
constraint is exactly the displayed nonpositive expression, so already excludes
all collisions. Once the support is independent, all coarse deviations obey.
This strengthening uses ordinary weak obedience; it does not supply positive
conditional margins.

### Exact extension-complexity separation

Take G to be the line graph of K_(2m). Its N=binom(2m,2) agents are edges of
the complete graph; two agents conflict precisely when those edges share an
endpoint. Independent sets are matchings. Therefore strategic marginals form
the MATCHING polytope, while unrestricted marginals remain the cube.
The face sum_i x_i=m is the perfect-matching polytope. Rothvoss's established
lower bound yields

    xc(CE marginal region) >= 2^{Omega(m)}=2^{Omega(sqrt N)},
    xc(nonobedient SAME marginal region) <= 2N.

This is unconditional, for arbitrary exact linear extensions, not merely the
number of facets in the original coordinates. The matching lower bound and
face-transfer method are prior mathematics. The graph has O(m^3) pairwise
interactions, so the explicit game description is polynomial in N. This is
also a superpolynomial separation in that explicit input length.

This genuinely meets the requested same-coordinate causal test: imposing
incentives changes a compact cube into a hard-to-represent polytope. It does
NOT meet a stronger requirement of hard equilibrium PAYOFF geometry: every
CE utility here equals1. Activation is weakly dominated by abstention, and
players are indifferent when no neighbor activates. The construction is
therefore economically degenerate as a payoff-selection model, even though
its recommendation geometry is a valid exact separation. Its mechanism is
ordinary weak-dominance support elimination, not a new general strategic
compression theorem. It would be misleading to omit these limitations.

## P18-G2 — positive-margin separation in a standard local public-good game

A variant replaces that indifference model with the familiar best-shot public
good. On the same graph set common cost c=3/4 and benefit1:

    v_i(a)=1[a_i=1 OR some neighbor activates]-(3/4)a_i.

Selected workers always receive1/4. Abstainers receive1 if a neighbor works,
and0 otherwise. All utilities remain in[0,1]. The graph and a constant-size
OR/count rule describe each local utility; this variant is not asserted to be
a polynomial LOCAL-TABLE graphical-game input when degree grows, nor a
polymatrix game. It is a standard succinct local-public-good representation.
Require conditional obedience margin delta=1/4 at every occurring private
recommendation.

A selected worker's switching gain is1/4 with no active neighbor and-3/4
otherwise. Subtracting delta times the work recommendation mass gives

    work delta-slack = -Pr(a_i=1 AND some neighbor activates).

Hence every delta-obedient law is supported on independent sets. Every MAXIMAL
independent set is a strict pure NE with conditional gains1/4 for workers and
3/4 for abstainers. A mixture of these pure profiles remains delta-obedient.
Therefore, writing C_delta for strategic marginals,

    conv{maximal independent-set indicators} subset C_delta subset STAB(G).

No equality of these three sets is assumed or needed. At G=line graph K_(2m),
all these sets satisfy sum_i x_i<=m, and every perfect matching is maximal.
The face sum_i x_i=m of C_delta is consequently EXACTLY the perfect-matching
polytope. This again gives

    xc(C_(1/4)) >=2^{Omega(sqrt N)},

compared with the nonobedient same-coordinate cube. Thus the separation also
exists at a fixed strictly positive conditional margin in a recognized local
coordination model. The supporting face consists of strict pure equilibria.
It does not follow that every feasible law is a lottery over strict pure NE.

### Essential calibration and failed stronger claim

The margin equals the maximum WORK gain1/4, which makes its work row a
nonpositive collision mass. The result is NOT proved for ordinary CE of this
best-shot game or for a whole interval of smaller required margins. The binding
margin is an exact support-selection device, even though abstention gains can
be larger and delta is strictly interior to the normalized payoff range.

For example, on a single conflict edge the law

    Pr(10)=Pr(01)=29/60,    Pr(11)=1/30

has all conditional gains at least1/8 but includes a collision. It fails the
1/4 work-margin requirement. Thus merely lowering delta need not preserve our
independent-support characterization. This is a counterexample to the proposed
proof method, not proof that the smaller-margin marginal region has a compact
LP. No robustness of the EXACT EF lower bound to obedience slack, utility
perturbations or approximate formulations is asserted.

## P18-G3 — why a sufficiently rich compact task lift cannot have this gap

A standard linear observation places a precise limit on causal claims. For any
chosen comparable outputs z(a), define the nonobedient MOMENT polytope

    Q=conv{(z(a),g(a)): all pure a},

where g_i,r(a)=1[a_i=r]*(u_i(a)-u_i(1-r,a_-i)) for binary actions. Positive
conditional margins instead use g_i,r(a)-delta*1[a_i=r]. The strategic output
region is exactly

    projection_z( Q intersect {all g_i,r>=0} ).

Every point of Q is an actual law's expected moments; the extra inequalities
are exactly obedience. Thus if Q has an exact q-inequality extension, strategic
outputs have one with at most q+2N inequalities. This is elementary
intersection/projection, not a new characterization theorem. It also applies
to polynomially many supplied deviations or output side constraints.

Consequently compactness of a representation already preserving all obedience
moments prevents a superpolynomial EF gap from merely appending those rows.
G1's cube forgets the moments: its augmented Q must itself be hard to represent,
by the contrapositive. There is no contradiction with the simple pairwise
utility tables. A small evaluator and a compact moment polytope are different
representation contracts. Comparing only the cube is a legitimate SAME-output
incentive separation, but not a claim that every rich task representation
incurs a new exponential overhead when linear IC rows are added.

This also explains how the new result differs from P17-X. There the compared
NONOBEDIENT payoff/success region already had the matching face. Here the
nonobedient MARGINAL region is a cube, and the matching face appears only
after obedience. The coordinate contract must remain explicit; exchanging
'payoffs' and 'recommendation marginals' in a summary would invalidate the
claimed distinction.

## Primary comparisons and actual source limits

- Rothvoss, *The matching polytope has exponential extension complexity*,
  arXiv1311.2369v4,17March2017, https://arxiv.org/pdf/1311.2369 , Theorem1 and
  face-projection discussion PDFpp2–3 actually inspected in Phase17. This is
  the entire deep lower-bound input; neither its theorem nor its technique is
  attributed to this research. The family-specific embedding is elementary.
- Dall'Asta, Pin and Ramezanpour, *Optimal equilibria of the best shot game*,
  author primary text https://arxiv.org/pdf/1002.3572 , opening model and
  maximal-independent-set discussion PDFpp2–4 inspected. The best-shot game
  and strict pure-NE/maximal-independent-set correspondence are established.
  Our candidate difference is the calibrated conditional-margin marginal face
  and exact EF comparison, not this equilibrium characterization.
- *Solving Graph-based Public Good Games with Tree Search and Imitation
  Learning*, NeurIPS2021 primary proceedings PDF,
  https://papers.nips.cc/paper/2021/file/0db2e204010400f5c506620adcd1ae68-Paper.pdf ,
  Section3 utility display and PSNE formulation inspected. It uses precisely
  the best-shot utility form with arbitrary costs. We rely only on that model
  and pure-equilibrium context, not blanket claims about absence of mixed NE:
  even two adjacent agents with cost3/4 have an independent mixed equilibrium
  at activation probability1/4, with positive collision probability.
- Papadimitriou–Roughgarden2008 and Jiang–Leyton-Brown2011 primary optimal-CE
  texts were inspected in Phases15–17. Their compact-game representations,
  separation methods and existing optimal-CE hardness prevent presenting this
  as a novel generic gap between simple payoff evaluation and strategic
  optimization. Their statements do not themselves give the exact marginal
  polytope identity proved here.
- Ahmadinejad et al., AAAI2016 *From Duels to Battlefields*, primary matching-
  duel discussion inspected in Phase17, already places matching-polytope size
  against efficient game optimization. Hence a game-theoretic use of matching
  extension complexity is not new. See phase17-originality.md for exact source.

A particularly close primary framework was newly inspected: Kamisetty, Xing
and Langmead, *Approximating Correlated Equilibria using Relaxations on the
Marginal Polytope*, ICML2011 author PDF
https://www.cs.cmu.edu/~epxing/papers/2011/Kamisetty_Xing_Langmead_ICML11.pdf ,
Section3.1 exact correlated equilibria and its neighborhood-marginal definition.
It already formulates graphical-game CE through globally realizable local
marginals plus linear obedience constraints, then studies outer relaxations.
This is direct prior for G3's augmented-moment viewpoint and strengthens the
judgement that the general representation principle is established. G1/G2's
candidate difference is only the explicit same-own-marginal EF separation.

A very close additional lead is Adkins–Mount–Zhang, *A Game-Theoretic Approach
for Minimizing Delays in Autonomous Intersections*, TGF2017/2019, on CE and
independent-set conflict games. Search results/secondary full-book text exposed
finite-collision CE rows and a theorem allowing collisions at finite positive
activation reward. Those are NOT counted as verified original chapter text:
the actual chapter body has not yet been retrieved from a primary endpoint
in this branch. The primary2016 student report at
https://www.cs.umd.edu/users/mount/Indep/Robert-Adkins/adkins_cmsc499a_final.pdf
was retrieved; it is a DIFFERENT earlier document and is not silently substituted
for the final chapter. This source gap matters for novelty comparison, although
our elementary identities and finite counterexample do not depend on it.

### Originality judgement

The literal main question has a positive answer in recommendation marginals.
But the proof is short: weak-dominance support restriction gives STAB, or a
calibrated best-shot work margin gives an independent-support matching face;
then apply Rothvoss. The ingredient connections are mature. Exact priority
of these scoped EF statements is unresolved, and absence of a matching search
result is not evidence of a major discovery. Treat them as useful constructive
answers and short lower-bound transfers, not a new general theory of strategic
representation complexity. A stronger fixed-payoff, nonbinding-margin or
approximate-description separation would remain a distinct research target.

## Exact tests and record

Seven exact tests pass. They examine every conflict graph through four agents
and pure profiles; verify collision CE/CCE rows and arbitrary independent-
support rational laws; realize a rational cube point with an independent
product law; check best-shot calibrated work rows and strict maximal-set
profiles; identify perfect-matching faces on K4/K6 line graphs; and verify
the smaller-margin collision counterexample. They import no earlier-phase
helpers and implement no CE optimizer or extension-complexity lower-bound
solver. Asymptotic EF hardness is analytic plus the external Rothvoss theorem.
No shared ledgers, manuscript, companion or commits were edited by this branch.
