# Phase 12 — selective audits and voluntary contribution

16 October 2026. Candidate derivations by the verification branch, for Nicholas
Ham's Agent Games programme. Novelty is provisional: the central reduced-form
inequality is close to established costly-verification mechanism design.

## Model and equilibrium scope

Independent finite private costs C_i in (0,B), every supported type positive,
shared benefit B from task success, and utility B*success-C_i*active. A trusted
coordinator commits to a finite direct mechanism: reports, internal randomization,
perfect external cost audits, private action recommendations, voluntary actions.
An audit reveals actual cost, cannot be manipulated, and has no intrinsic cost
to its subject. No transfers/fines. Count audited agents on the honest equilibrium
path (repeated audits never help). Report and action deviations are tested jointly.
Recommendations and role addressing are not charged as communication bits.
The result weakly implements one honest/obedient Bayesian equilibrium, not every
equilibrium or a dominant reporting strategy against arbitrary opponent actions.
On-path allocation rules and their interim workloads are supplied explicitly;
computing them from succinct descriptions is a separate representation problem.

## V12-A: exact audit cost for an arbitrary one-worker allocation

Service succeeds iff at least one agent works. Let f specify, for every reported
type profile, a lottery selecting exactly one worker. Write x_i(c) for that
worker probability conditional on C_i=c and m_i=max_c x_i(c). Among mechanisms
whose honest equilibrium implements f, minimum expected number of audited agents is

    A(f) = sum_i m_i - 1.

If a first audit of agent i has fixed external cost kappa_i>=0, its sharp expected
cost is sum_i kappa_i*(m_i-E[x_i(C_i)]). Both statements allow arbitrary adaptive
auditing in the converse and direct randomized auditing in the construction.

**Lower bound.** Fix i, type c attaining m_i, and report d. Couple the strategy
of type c mimicking type d with the honest d trajectory, including opponents,
randomness and audit answers. Independence supplies the same opponent-type law.
Until i's first audit their histories agree. On paths where i is never audited,
mimicry gives expected utility B-c*a_i, with a_i the honest d final work indicator.
After its first audit the deviator can always volunteer, guaranteeing B-c,
regardless of recommendations or opponents' actions. Against the honest d
benchmark B-c*a_i, this loses at most c if a_i=0 and nothing if a_i=1.
This coupling remains valid if later paths diverge: sample the counterfactual
honest d continuation using the same independent random tape. Therefore joint
incentive compatibility implies

    m_i-x_i(d) <= Pr(i audited AND i unselected | report d).

Average over d with its true marginal probability and sum i. The right sides
are bounded by expected audited-agent counts. Since sum_i E x_i=1, the result
follows, also separately for each fixed agent price. Audits after actions need
special care: the stated model audits before final voluntary action.

**Construction.** First select J using f(reports). For each i != J independently
audit i with probability

    rho_i(d)=(m_i-x_i(d))/(1-x_i(d)),

using zero if denominator is zero. This is in [0,1]. If every audit agrees,
recommend J work and everybody else abstain. If any lie is detected, choose
one detected liar as sole worker and recommend all others abstain. For unilateral
deviations only the deviator can be detected. A false report d then produces
workload x_i(d)+(1-x_i(d))*rho_i(d)=m_i, at least truthful workload x_i(c).
The designated worker strictly obeys B>c, and every other agent strictly abstains.
Thus arbitrary report-and-action deviations cannot gain. Honest expected audits
of i are m_i-E x_i, meeting every lower bound. Truthful reports that maximize
workload require no audit; detected false reports change the allocation only
off the honest path. Off-path assignments need not be efficient.

The theorem extends Phase11's flat-workload obstruction: A(f)=0 iff every
agent's interim workload is constant on its supported types. This exact zero
criterion uses independence, finite positive costs, cost-free perfect audit
subjects, and a one-worker unilateral safety action.

## V12-B: a discontinuity at redundant contribution tasks

For any success technology with NO singleton successful and any prescribed
lottery f over inclusion-minimal successful coalitions, put

    t_i(d) = max_c (c/B)*(x_i(c)-x_i(d)).

This is nonnegative because c=d is included. With arbitrary independent finite
cost distributions in (0,B), the sharp expected audit count is

    A_F(f) = sum_i E[t_i(C_i)].

The same formula weighted by fixed nonnegative agent audit prices is sharp.
This covers every threshold task k>=2 and arbitrary finite types, not only
binary monotone rules. Inclusion-minimality makes each recommended worker
pivotal, so B>cost guarantees honest-path action obedience.

**Converse.** Type c imitating the entire report-d strategy obtains baseline
utility B-c*x_i(d) until its own audit. After detection it can always obtain at
least zero by abstaining. Each own-audit event can therefore lower payoff by
at most B. Incentive compatibility gives

    c*(x_i(c)-x_i(d)) <= B*Pr(audit i | report d).

Maximize over c, weight by d's marginal prior and sum. As in V12-A, the
coupling allows adaptive audit decisions and joint report/action deviations.
On an audited path on which the counterfactual agent would already work,
the actual loss is at most B-c, so such audits cannot improve this lower bound.

**Construction and why unselected audit capacity always suffices.** First select
f(reports). Audit only unselected agents i with report d, with probability

    rho_i(d)=t_i(d)/(1-x_i(d)),

zero if the denominator vanishes. Since c/B<1 and x_i(c)<=1,
t_i(d)<=1-x_i(d), so these probabilities are feasible even with arbitrarily
many types and a nonmonotone rule. If any lie is detected, recommend all agents
abstain. No singleton can recover service, so all-abstain is a Nash continuation.
Otherwise use the selected inclusion-minimal coalition. A unilateral false
report d then gives best continuation utility

    B-c*x_i(d)-B*t_i(d) <= B-c*x_i(c).

Thus every joint deviation is unprofitable. On an audited/unselected event the
shutdown loss is exactly B; the converse is attained. Auditing selected agents
can never reduce the optimum: its loss capacity is at most B-c, whereas
unselected audits attain B and always have sufficient total probability.
The coordinator must credibly commit to off-path shutdown despite its welfare
loss. This is weak implementation; no selection among multiple continuation
or reporting equilibria is claimed.

For binary costs l_i<h_i with x_i(l_i)>=x_i(h_i), this simplifies to

    A_F(f)=sum_i Pr(h_i)*(l_i/B)*[x_i(l_i)-x_i(h_i)].

Consequently the analogous one-worker formula is false for redundant tasks.
With n=3,k=2,p=1/2,l=1/2,h=3/2,B=2 and efficient uniform ties,
x(l)=11/12,x(h)=5/12. The sharp audit count is 3/16, whereas applying
sum_i max x_i-k would falsely give 3/4. The difference is an endogenous
punishment bound: one worker can secure B-c; no singleton can complete k>=2.
A technology with some singleton feasible requires agent-specific safety
analysis and is left open. Similarly, a prescribed nonminimal coalition may
fail action obedience independently of audit incentives.

## V12-C: exact reliability-sensitive audit characterization

This extension was proposed by root and independently reconstructed in the
verification branch. Keep the no-singleton technology. Now the target rule f(t)
is a lottery over inclusion-minimal successful coalitions OR the empty failure
outcome. Let s_i(d) be its interim success probability and x_i(d) its interim
workload. Then 0<=x_i(d)<=s_i(d)<=1, and truthful utility is

    u_i(c)=B*s_i(c)-c*x_i(c) >= 0.

For each i,d define capacities U=s_i(d)-x_i(d), V=x_i(d), and gains

    g_c = B*(s_i(d)-s_i(c)) + c*(x_i(c)-x_i(d)).

The exact minimum expected audits attributable to report d is the minimum
alpha+beta subject to

    0<=alpha<=U,  0<=beta<=V,
    B*alpha+(B-c)*beta >= g_c       for every supported c.

Consequently the sharp total audit requirement is the sum of these minima
weighted by each report's true marginal probability. Fixed nonnegative
agent-specific audit prices multiply these separate minima. Arbitrary adaptive
finite audit protocols cannot improve it; a direct finite construction attains it.

**Necessity.** Couple a true c type imitating d with the honest d trajectory
until its own first audit. On a counterfactual failure path baseline payoff is
zero, and abstention after detection cannot be worse. On a successful path
with i unselected, baseline payoff is B, so detection can lose at most B. On a
successful path with i selected, baseline payoff is B-c, so detection can lose
at most B-c. Define alpha and beta as the counterfactual probabilities of
first audit intersecting these two successful events. Their capacities and
all displayed IC inequalities follow. Independence and no intrinsic cost to
audit subjects are essential to this argument.

**Attainment.** Draw the target outcome from f(reports). On failure perform no
audits and recommend all abstain. On success audit each unselected i with
probability alpha_i(d)/[s_i(d)-x_i(d)], and each selected i with probability
beta_i(d)/x_i(d), independently; a zero denominator gets rate zero. If any lie
is detected, recommend shutdown. Otherwise use the drawn coalition. Truth-path
workers are pivotal; truthful failures and detected-lie shutdowns are Nash
continuations because no singleton can succeed. A false report d by actual c
has optimal action-stage payoff exactly

    B*s_i(d)-c*x_i(d)-B*alpha_i(d)-(B-c)*beta_i(d).

The IC inequalities make this at most u_i(c). Honest audit use is precisely the
claimed objective. Thus this is a genuine necessary-and-sufficient
resource characterization for the stated implementation model, not merely a
sufficient audit policy or a numerical LP observation.

**Closed form: exhaust success-unselected audits first.** The tiny per-report
LP does not require a solver. Put T=max_c(g_c/B), which is nonnegative because
g_d=0. If T<=U, its optimum is

    alpha=T, beta=0, cost=T.

Otherwise its optimum is

    alpha=U,
    beta=max{0, max_c [(g_c-B*U)/(B-c)]},
    cost=U+beta.

Proof: transferring an equal probability delta from selected to unselected
audits increases every IC left side by c*delta while preserving audit cost.
Thus at any fixed total audit count the choice with greatest feasible alpha
weakly dominates all others. If T<=U, B*(alpha+beta)>=max g_c gives the matching
lower bound T. If T>U, no cost <=U is feasible, and maximizing alpha sets it
to U; the remaining inequalities give the displayed beta. Feasibility is
always guaranteed for valid targets: full successful-path auditing
(alpha,beta)=(U,V) gives left side B*s_i(d)-c*x_i(d), exceeding g_c by u_i(c)>=0.
Selected audits therefore arise only when success-unselected capacity is
exhausted. In the guaranteed-success case T=t_i(d)<=U, recovering V12-B.

**Why reliability alone does not order audit requirements.** For n=3, threshold
k=2, B=2, iid costs {1/2,3/2} with equal probabilities, prescribe success only
when ALL reported costs are low, and uniformly choose two workers then.
For each low report, s=1/4, x=1/6, and the optimum is alpha=1/12,beta=1/6:
every agent is audited on each successful profile. Total expected audits are
3/8. Efficient guaranteed success instead needs only 3/16 (V12-B).
Thus a particular lower-reliability target can require MORE verification.
This does not say that optimizing over targets with a relaxed lower bound on
reliability increases cost; such feasible-set relaxation cannot worsen an optimum.

**Exact finite welfare-resource frontier.** If the finite profile table and
successful coalitions are explicitly listed, choose variables f(t,S) over
minimal S and empty failure, plus all alpha_i(d),beta_i(d). Marginal success,
workload, reliability bounds, the displayed IC/capacity constraints, expected
audits, and expected welfare are all linear in these variables. Thus one LP
exactly characterizes attainable welfare/reliability targets under audit budgets for this
weak-implementation class; each feasible solution has the explicit construction
above and every implementation yields a feasible solution with no more audit
cost. This is a mature finite mechanism-design method applied with a proved
endogenous punishment capacity, not a claim to invent linear-programming
mechanism design. The number of profiles/coalitions can be exponential in a
compressed task description. No succinct-input polynomial algorithm is claimed.
Maximal supported cost<B, credible coordinator commitment, no singleton success,
independent types and voluntary binary work remain substantive restrictions.

## Efficient iid binary tasks, any population

Let 0<p<1, L~Binomial(n,p), common low l<high h<B, and choose uniformly among cheapest
k-worker coalitions. Set M=E[min(L,k)]. Then

    x(l)=M/(n*p),  x(h)=(k-M)/(n*(1-p)).

These are monotone; one proof couples an agent's report from high to low and
holds tie priorities fixed, so its selected indicator cannot decrease.
For k=1 the sharp first-best audit optimum, including over efficient tie rules, is

    A_FB,1=(1-(1-p)^n)/p - 1.

For 2<=k<=n it is

    A_FB,k=(l/B)*(M-k*p)/p.

To see global optimality over tie rules, all efficient rules select min(L,k)
low workers. Thus sum_i x_i(l)=M/p and sum_i x_i(h)=(k-M)/(1-p), irrespective
of ties. In the one-worker case sum_i m_i>=sum_i x_i(l); uniform ties attain
this. In the k>=2 case the lower bound l*D_i need only be used when positive;
summing positive parts is at least summing all D_i, and uniform ties attain the
result. Audit probabilities, report messages and worker selection can all be
exchange-equivariant using independent symmetric coins/uniform ties.

For first-best welfare, equal costs can be treated as one supported type and
audits omitted; requiring the old low/high priority rule even on payoff-identical
labels would instead be a different fixed-allocation implementation question.
The audit costs are independent of h-l in the distinct-cost binary model. Even a tiny positive
cost gap creates the same report incentive after scaling utility by the deviator's
cost. If l=h the types coincide and no audit is necessary; the discontinuity is
about distinct private reports and exact first-best allocation, not approximate
welfare. This suggests approximate-efficiency and audit-resource optimization,
not extrapolation to general utility functions.

## Relation to Phase11's no-report inspection frontier

V12-A allows cheap strategic reports plus costly verification, whereas AG-V1
explicitly excludes type-dependent messages. For n=2,p=1/2, first-best inspection
without reports costs one query; selective report verification costs 1/2 expected
audits. This is not a contradiction: report incentives are enforced by assigning
a detected liar as the pivotal sole worker. Audits exploit a different resource
architecture. For redundant tasks shutdown makes truthful implementation cheaper
again. Gross welfare and verification expenditures must use a common cardinal
objective before claiming economic superiority.

## Prior art and novelty limits

Primary texts actually inspected 16 October2026:

- Ben-Porath, Dekel and Lipman, *Optimal Allocation with Costly Verification*,
  AER104(12),2014,3779–3813, author PDF
  https://sites.bu.edu/blipman/files/2021/10/allocation_verification.pdf .
  Printed3782–84 set independent private information, perfect external checks,
  no transfers and direct reduced forms. Their IC compares an interim allocation
  probability to another type's probability minus its checking probability.
  The corresponding inequality here uses NONWORKER probabilities, so the core
  audit formula is a close reduced-form adaptation, not a new incentive principle.
  Their one positively valued object and our voluntary contribution game have
  different feasibility constraints; our safety-action proof is needed to justify
  the effective punishment bound. Their main favored-agent optimum is not
  claimed to transfer to this shared-success workload environment.
- Li, *Mechanism design with costly verification and limited punishments*,
  JET186(2020),105000, DOI10.1016/j.jet.2020.105000, publisher abstract and introduction via indexed primary-page text
  https://www.sciencedirect.com/science/article/pii/S0022053120300089 .
  A direct full-page fetch returned403; the Penn2017 working-paper PDF and
  Penn thesis fetch also failed. Full model equations and proofs were NOT
  inspected. The available introduction states: limited destruction of an allocated
  object's surplus changes optimal verification and allocation. This is close
  conceptual prior for our endogenous punishment-capacity distinction. It does
  not by itself establish novelty or nonnovelty of these exact task formulas.
- Battaglini–Palfrey2024, as inspected and recorded in
  phase11-volunteer-mechanisms.md, supplies the private-report/action honest-
  obedient baseline. Unlike Phase11's externally informed mediator, verification
  here is deliberately combined with strategic reports. No new claim is made
  for ordinary joint-deviation incentive testing.

No claim of novelty clearance. The broad exact audit functional and safety-action
versus shutdown distinction merit independent checking, but the surrounding
verification literature is mature. Finite exact tests below verify all binary
profiles and joint report/action deviations for supplied examples; they do not
establish uniqueness, full implementation, coalition-proofness, or efficient
computation from compressed inputs. No coverage theorem beyond the stated
no-singleton, minimal-coalition subclass has been proved.

## Independent internal review

The compact-representations branch independently reconstructed V12-A's
first-own-audit coupling and safety guarantee, then V12-B including the arbitrary
finite-type extension. It found no defect. Its endpoint and payoff-identical
label qualifications were incorporated above. This is same-family AI review,
not external peer review or originality clearance. Nine exact tests pass,
including asymmetric multitype and nonmonotone redundant-task rules, exact
reliability IC checks against a rational audit grid, and the lower-reliability
higher-audit witness. V12-C was root-proposed and independently reconstructed
here; a separate review is still needed before manuscript promotion.

Phase13 update: the separate reconstruction in phase13-verification-audit.md
found no defect within the model and retrieved Li2017's primary thesis, whose
allocated/unallocated audit LP is closer prior than recorded above. Its2020
final full body remains uninspected. No generic two-category novelty is claimed.
