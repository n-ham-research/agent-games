# Phase 13: independent adversarial audit of V12-C

Status: **proof reconstructed within the stated model; novelty substantially
qualified**. This is a fresh internal review of the supplied Phase 12 result,
not a blinded review and not external peer review. The agent read the project
instructions, roadmap, theorem ledger, review log and Phase 12 verification
note before making research changes. No companion repository was modified.

My verdict is that V12-C is mathematically sound for the restricted target
class and weak implementation notion specified below. I found no counterexample
within that scope. The two-category audit allocation and fill-the-more-effective-
category-first principle have explicit prior art in Yunan Li's 2017 thesis,
which was obtained and inspected during this review. The contribution should
be described as a task-specific sharp characterization with an independently
proved voluntary-action punishment bound, not a new verification or LP method.
The published 2020 Li body remains uninspected; access to earlier primary
bodies has improved materially and must not be confused with final-version
access or novelty clearance.

## Exact scope I checked

There are finitely many independent private costs, every supported type has
positive probability, and `0<c<B`. Utility is `B*success-c*work`. Reports are
strategic, verification perfectly reveals actual cost, and the subject incurs
no audit cost. The trusted coordinator can commit to its protocol, including
off-path recommendations. All audits precede final voluntary binary actions.
The target on every supported report profile is a lottery over inclusion-
minimal successful coalitions and the empty failure outcome. In particular
`F(empty)=0` and `F({i})=0` for every player. Recommendations and audit outcomes
may be private. Implementation asks for one truthful/obedient Bayesian Nash
equilibrium against unilateral deviations jointly in reporting and later
actions; it is neither coalition-proof nor full or dominant-strategy
implementation.

The explicit condition `F(empty)=0` is worth retaining: without monotonicity,
no successful singleton alone would not logically imply empty failure. No
upward closure beyond these conditions is needed in the proof: adding an
unselected worker to a successful coalition cannot improve that worker's
utility above the benefit already received, even if the added action could
destroy success.

## Independent necessity proof, including adaptive private audits

Fix agent `i` and a supported report `d`. Run the actual equilibrium protocol
counterfactually with this agent's cost equal to `d`, honest reports/actions,
independent opponents' types, and a full independent random tape. Let `Z`
indicate final task success, `W` this agent's final work, and `H` whether the
agent is ever audited. On that counterfactual path `(Z,W)` is one of
`(0,0),(1,0),(1,1)`. Define

    alpha_d = Pr(H, Z=1, W=0),
    beta_d  = Pr(H, Z=1, W=1).

Thus `alpha_d<=s(d)-x(d)`, `beta_d<=x(d)`, and
`alpha_d+beta_d<=Pr(H)`.

For every other actual cost `c`, let the agent mimic the entire honest cost-
`d` strategy until its first audit, and abstain at the final action after that
audit. Independence gives the same opponents' type law. Until the first own
audit, all observed messages and audit decisions can be coupled to agree.
The event of performing that audit is determined before its actual cost result
is revealed; subsequently the honest-`d` continuation is still a well-defined
counterfactual sampled with the common tape. The actual histories may diverge
after that point, without invalidating the bound.

Without an own audit, the mimic obtains exactly the counterfactual payoff
`B Z-c W`. After its first audit it can secure at least zero by abstaining,
regardless of other actions or subsequent messages. The counterfactual payoff
lost on an audited failure is zero; on audited success it is `B` if unselected
and `B-c` if selected. Consequently its achievable deviation payoff is at least

    B*s(d)-c*x(d)-B*alpha_d-(B-c)*beta_d.

Truthful incentive compatibility therefore requires, simultaneously for all
supported `c`,

    B*alpha_d+(B-c)*beta_d
        >= B*(s(d)-s(c))+c*(x(c)-x(d)).

The same `alpha_d,beta_d` works for every `c`: it is defined on the single
honest-`d` counterfactual distribution, not selected afresh for each inequality.
This point is essential. Averaging over the true marginal of `d` and summing
agents gives the proposed lower bound on honest-path first-audited-agent
counts; fixed nonnegative agent prices can multiply the same inequalities.
Failure-path audits and repeat audits cannot invalidate that bound, but may
waste counted resources. This proves the converse for finite adaptive
protocols with private histories, not merely direct outcome-first mechanisms.

The argument would require revision if costly effort occurred before the
first audit, audits themselves harmed subjects, external information revealed
cost without an audit, or types were correlated. Those changes can respectively
remove the zero-payoff safety action or the common counterfactual law.

## Independent attainment and full joint-deviation check

For each report `d`, choose a feasible minimizer `(alpha_d,beta_d)`. Draw the
target coalition first. On successful outcomes, audit an unselected agent
with probability `alpha_d/(s(d)-x(d))` and a selected agent with probability
`beta_d/x(d)`; use rate zero when its denominator is zero. Failure draws
receive no audit. The capacity constraints make all rates valid. Independent
per-agent coins are sufficient; no simultaneous-audit constraint is imposed.

If any audit finds a lie, send every agent an abstention recommendation.
Otherwise send the drawn coalition's work recommendations. With one reporting
deviator only that deviator can be caught. In every relevant realized state:

- A selected worker in a non-shutdown minimal coalition strictly prefers
  working: it is pivotal and `B-c>0`.
- An unselected agent in a successful coalition strictly prefers abstaining:
  success already occurs, so working cannot improve benefit and adds cost.
- On empty failure or shutdown, abstention is optimal: no singleton succeeds.

These arguments hold conditional on each private information set. An
abstention recommendation can pool shutdown, empty failure and unselected
success; abstention is optimal in each state separately. An agent need not
observe others' audit statuses or recommendations. A work recommendation
arrives only in a non-shutdown successful coalition, where working is optimal.

Hence a true cost `c` reporting `d` has best possible continuation payoff
exactly

    B*s(d)-c*x(d)-B*alpha_d-(B-c)*beta_d.

This checks arbitrary recommendation- and audit-dependent actions after a
false report, not just a lie followed by obedience. The inequalities make
every such report unprofitable, and random mixtures of reports cannot help.
On the honest path no shutdown occurs and expected audits are exactly the
claimed objective. Private audit information and private action recommendations
therefore do not create an omitted unilateral deviation.

## Closed form, feasibility and finite LP

At fixed audit mass, replacing a selected audit by an available unselected
audit changes every constraint's deterrence by `c*delta>0` without changing
counted cost. Thus unselected capacity should be filled first, with the
Phase 12 two-branch formula. Full successful-path auditing is feasible because
its deterrence equals `B*s(d)-c*x(d)`, while the required gain subtracts the
nonnegative truthful utility. The denominator `B-c` is strictly positive.

No coupling constraint between agents' audit masses is missing: unlimited
parallel audits and shutdown after any detected lie make all the individually
specified rates jointly implementable. If concurrent audit caps, type-dependent
prices, or audit-state-dependent prices are imposed, the separable minimum and
this greedy rule no longer follow automatically.

The explicit profile-table welfare/resource LP is valid within this class:
`f`, interim success/workload and audit capacities are linear variables or
linear expressions, and every feasible solution has the stated construction.
It does not optimize over all possible coalitions or mechanisms once one
removes the minimal-success/empty-failure restriction. Its exponential explicit
representation cost must remain visible.

Two elementary additional consequences help interpret the result, without
creating novelty claims. The sharp audit functional is convex in the target
lottery. It is also positively homogeneous under independent global thinning:
replace the target by itself with probability `lambda` and empty failure
otherwise; all capacities and required gains scale by `lambda`, so the sharp
audit cost scales by exactly `lambda`. The higher-audit/lower-reliability
example therefore concerns type-dependent screening, rather than failure
probability alone. Zero audits are possible exactly when all the ordinary
reporting IC inequalities already hold, since action obedience is automatic
for the restricted outcome class.

## Disproof attempts and substantive boundaries

1. **Selected audits appear dispensable.** Rejected. In the stated three-agent
   all-low-success example, a low report has `s=1/4,x=1/6`, giving
   `alpha=1/12,beta=1/6`. Unselected capacity alone cannot deter the high type.
   The formula yields total audits `3/8` exactly.
2. **Shutdown should solve singleton-success tasks too.** False. For the
   two-agent one-worker rule with `B=2`, costs `1/2,3/2`, workloads `3/4,1/4`,
   the V12-C shutdown formula would assign only `1/8` audit mass to a high
   report. A low-cost liar can restore service alone after detection and has a
   profitable joint deviation. The one-worker safety payoff must replace zero.
3. **Minimality is only cosmetic.** False. Recommend all three agents work in
   a two-worker task. Any one saves its cost by abstaining while the others
   still succeed. The constant success/workload reduced forms would misleadingly
   give zero audits; the target is simply not obediently implementable by the
   stated construction. Cost audits do not enforce the final action.
4. **Credibility follows from Nash continuation.** Only for agents. All-abstain
   is a Nash continuation because no individual can restore service, but a
   minimal successful coalition can deviate jointly and make every member
   strictly better off. Shutdown is not coalition-proof. A coordinator free to
   revise recommendations and maximizing total surplus would prefer a
   successful coalition, since every cost is below `B`; commitment is a
   substantive external instrument, not a sequential-rationality conclusion.
5. **One equilibrium means truthful behavior is uniquely selected.** False.
   The minimal-audit all-low-success example leaves the high type indifferent
   between truth and some detected deviations. No strict or full implementation
   conclusion follows from the weak inequalities.

No defect was found after these attacks within the stated model. They do
refute several nearby stronger interpretations.

## Primary-source comparison and novelty decision

The following comparison concerns actual retrieved primary bodies, not title
or abstract inference. No downloaded PDF is tracked. Source-derived summaries
are deliberately limited; the detailed proof above is the independent audit
of the local candidate, rather than a paraphrase of those sources.

**Ben-Porath–Dekel–Lipman 2014, published AER PDF.** The complete 35-page
[author-hosted published body](https://sites.bu.edu/blipman/files/2021/10/allocation_verification.pdf)
was retrieved. I inspected §I pp3782–3784, the reduced-form optimization in
§V, the punishment/disclosure extensions in §VI pp3800–3803, and the relevant
appendix statements. Their allocation/checking variables satisfy `q<=p` and
IC `p_i(c)>=p_i(d)-q_i(d)`. The fixed-allocation minimum-checking principle
is already present. Their one-object feasibility and no voluntary action
stage differ from the task model; their favored-agent optimum is not a
characterization of V12-C. The generic checking-probability IC reduction and
minimum checking technique are prior, not a novel principle here.

**Li 2017 working paper and thesis; 2020 final access boundary.** The full
82-page [September 28 working paper](https://economics.sas.upenn.edu/sites/default/files/filevault/SSRN%2016_009%20third%20version.pdf)
was retrieved; §2 pp7–9 gives benefit `b_i(c)`, allocated-only punishment
`h_i(c)`, and IC `P_i(c)b_i(c)>=P_i(d)[b_i(c)-Q_i(d)h_i(c)]`.
The [2017 Penn thesis](https://repository.upenn.edu/bitstreams/2683cbe4-3633-4813-b6cf-05e0866b994c/download)
was also retrieved. Crucially, chapter2 §2.5.2, printed p32 equation(2.21),
already minimizes two-category audit cost subject to expected punishment and
fills the category with better punishment per audit first. Allocated and
unallocated audits are explicit there. This is close prior for the V12-C
capacity LP and greedy step, although that single-object model does not
supply the local theorem's endogenous losses `B,B-c,0`, shared success,
all-type constraints, or voluntary shutdown implementation. The published
[2020 paper](https://www.sciencedirect.com/science/article/pii/S0022053120300089)
PDF returned403 and its public API request406. Its full body and final-version
equation numbering remain uninspected; neither earlier body is represented
as the final article.

**Battaglini–Palfrey 2024 author manuscript.** The complete 80-page
[July 26 manuscript](https://www.its.caltech.edu/~trp/Olson_27July2024%20wiith%20appendix.pdf)
was retrieved. §2.1–2.2, printed pp8–11, specifies the same success-minus-
activity-cost structure and private recommendation mechanisms. Their (HO)
constraint explicitly combines a false report and an arbitrary action map;
(IC) alone is not enough. Their reduced forms `p(c),a(c)` already separate
success from workload, and §5 optimizes honest/obedient mechanisms. They do
not introduce the external cost-audit instrument used in V12-C. The
communication-equilibrium baseline and joint-deviation requirement are prior.

**Decision.** V12-C is not a literal specialization of any one of those three
papers' displayed main theorems: the allocation-feasibility constraints,
private costs entering workloads, and endogenous credible punishment differ.
But calling it a new general verification method would be misleading. The
reduced-form IC method, two audit classes, effective-punishment ordering and
LP optimization all have inspected primary precedent. The defensible candidate
increment is the sharp identification and attainability of the three task-
continuation losses, giving a closed-form audit functional for arbitrary finite
independent types and the specified coalition/failure targets. This is a
potentially useful task-specific extension or synthesis; its publication
novelty and importance are not established by this review. The full published
Li comparison remains an explicit source gap, rather than an excuse to infer
originality from inaccessible text.

## Reproduction, provenance and limits

`experiments/test_phase13_audit.py` imports no Phase 12 implementation. It
solves the two-variable LP by exact rational vertex enumeration and compares
it with the proposed formula on 648 three-type interim problems, including
nonmonotone tables and endpoints. Three other tests check selected-audit
necessity and the singleton/nonminimal-coalition failed strengthenings.
All four tests pass in approximately0.13 seconds. These finite tests do not
replace the adaptive-history coupling proof or certify arbitrary protocol
semantics by enumeration.

Retrieved PDF SHA256 values, for version identification only:

- BDL published PDF: `57c353e34cef257be27e66aacd17d168169d59b21881601da9967f5265f40551`.
- BP July2024 manuscript: `b66816601a7e46e196466931e0a92ffde9756469d041bdd51951ab4fe0385783`.
- Li September2017 working paper: `f6b9f0ad8d4d577e5f8dd8cab7e405f00b68f84da6954149e5efd59300978819`.
- Li2017 thesis: `53315afe36dc91da51c26e18b341533b366f2a674bfa1e2ff59487de1fb8f14c`.

The public university links succeeded on an authorized read-only network
retry after ordinary tool fetches failed; this does not authenticate the
published final version. I inspected the relevant full-body model and proof
passages, not merely indexed abstracts. I did not perform a line-by-line audit
of every unrelated threshold theorem or appendix proof in the lengthy source
papers. There was no external contact, submission, manuscript edit, ledger
change, companion edit or commit by this review agent.

## Additional supplied-proof cross-review: punishment robustness

The coordinating agent subsequently supplied the following corollary for
independent attack. Let a complete-information monotone binary-work game have
a correlated equilibrium, common success probability `s`, work probability
`x_i`, and probability `p_i` that player `i` works and is pivotal. If following
its work recommendation has conditional obedience margin at least `eta>0`,
then its unconditional obedience inequality is

    B*p_i-c_i*x_i >= eta*x_i.

Since `p_i<=s`, it follows that

    x_i <= B*s/(c_i+eta),
    u_i=B*s-c_i*x_i >= B*eta*s/(c_i+eta).

If there is a successful singleton, each such agent `j` can guarantee
`B-c_j` by always working. The correlated-equilibrium deviation inequality
and `u_j<=B*s` therefore imply

    s >= t0 := max_(successful singleton j)(1-c_j/B).

With positive costs below `B`, this is a strictly positive number. The target
player's payoff is consequently at least `B*eta*t0/(c_i+eta)>0`. A zero-payoff
CE punishment in this setting cannot have a positive work-recommendation
obedience margin for that target player. This is a direct inequality
corollary, not a new general CE result or priority claim.

The proof survives the attack. Monotonicity is needed for the stated pivotal-
probability identity and for a singleton's success guarantee despite other
workers. If `x_i=0`, the conditional margin is undefined; use the displayed
unconditional inequality, which is then vacuous and still yields the stated
payoff bound. The premise concerns only this target's work recommendation,
not every recommendation or a globally strict CE. With no successful singleton,
there is no positive `t0` lower bound; all-abstain can have zero success and
zero utility. No positive robustness floor for that case is established.

## Additional supplied-proof cross-review: binary q2 approximation

The compact-computation agent separately supplied a one-dimensional randomized
approximation benchmark. For a promised exact player-transitive binary group
with two player-strategy action orbits, each fibre has exactly one action in
each orbit. Label by those two orbits. The invariant mixed profiles are then
precisely the profiles with one common probability `p`, and all players have
the same representative expected advantage `D(p)`.

With pure payoffs in `[0,1]`, coupling the `N-1` opponent Bernoulli variables
gives `|D(p)-D(q)|<=2(N-1)|p-q|`. Exact pure endpoint comparisons either
produce a pure invariant NE or a positive/negative sign bracket. Fresh Monte
Carlo estimates at adaptive dyadic midpoints, each with error at most
`epsilon/4`, preserve a root bracket whenever the estimate's absolute value
exceeds `epsilon/2`. Otherwise the current profile has advantage at most
`3 epsilon/4` and hence is an epsilon-NE.

For `N>=2`, after
`T=ceil(log2(4(N-1)/epsilon))` bracket reductions, the final midpoint is
within half the bracket width of a zero. The Lipschitz bound then gives
`|D|<=epsilon/4`. No monotonicity of `D` is used. Conditional Hoeffding bounds
remain valid for adaptively chosen midpoints with fresh samples; a union bound
over at most `T` stages works. For differences in `[-1,1]`,
`32 epsilon^-2 log(2T/delta)` samples per stage suffice. Dyadic Bernoulli
sampling and explicit labeled output have the claimed polynomial expected
cost when pure-payoff evaluations and their bit costs are charged.

I found no defect. The `N=1` case needs its separate exact two-payoff comparison;
assume `0<epsilon<=1` and `0<delta<1` for the displayed iteration formula.
A supplied group is promised to consist of true game symmetries: the result
does not efficiently verify semantic circuit symmetries. This is a standard
bisection/concentration application with a useful symmetry-induced one-
dimensional search space, not a new general stochastic-equilibrium algorithm.

I also checked the supplied q2 precise-counting construction: its own-action-0
slice is constant while its own-action-1 slice is nonconstant. Hence no exact
typed automorphism can flip a local action. The rotation subgroup is player-
transitive, so even the full actual group has exactly two action orbits and
the same invariant profile locus. This does not produce generators of the
entire semantic automorphism group if an algorithm's input format requires
those complete generators; that input-model distinction was sent to the
construction's author.

## Read-only cross-review of the continuation branch

After its derivation was supplied in `phase13-coalitions.md`, I independently
checked P13-P1 and P13-P2. Success-preserving deletion raises retained workers'
pivotality, removes a negative work-obedience term for each deleted nonpivotal
worker, adds a positive abstention term for that player, and cannot make an
existing abstainer more able to repair failure. The two CE deviation inequalities
therefore both survive, with success unchanged and every utility weakly higher.
This is specific to monotone complete-information work games.

For P13-P2, zero utility together with work obedience forces the target to be
pivotal on every successful profile. All singleton-capable agents must then
always abstain, yielding the stated success lower bound `t0`. A pair-repairer
can repair every failed target-work profile, giving precisely its displayed
abstention-capacity inequality. Lowering success to `t0` relaxes every such
inequality. A large minimal coalition containing the target contains no
pair-repairer; otherwise all candidate minimal coalitions are pairs and the
sum of the partner capacities is the exact feasibility condition. In the
proposed attaining distribution the only failures are the target alone and
empty, so there are no additional omitted repair opportunities. Selected
partners are pivotal, singleton abstention is checked against the full failure
probability, and the target's work constraint binds as required.

No proof defect was found. This was supplied-proof cross-review after the
candidate was written, not blind discovery, a new source audit of that branch,
or an extension to private-cost reporting mechanisms. Its successful
punishments deliberately use failed work and target indifference; the
minimal-success/empty restriction and positive-margin conclusions must not
be interchanged with it.
