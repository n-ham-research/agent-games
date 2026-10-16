# Phase 11 — private-cost coordination and honest implementation

16 October 2026. Author Nicholas Ham; derivations and exact checks assisted by
Codex. These are proved candidate applications of standard incentive methods,
not novelty-cleared results. The volunteer calculation is a bounded calibration
exercise, not the proposed centre of the research programme.

## 1. Timing and resources

There are n≥2 agents. Independent, finite-support, positive private costs C_i
are drawn from known distributions, and each agent sees only its own cost.
An agent choosing a_i∈{0,1} receives

    u_i = B 1[sum a_j≥1] − C_i a_i.

Use one common cardinal money/consequence scale and the externally specified
welfare W=∑u_i. Initially there are no transfers, external cost observations,
verification, or enforced action commitments. A communication device may have
arbitrary type-independent public/private randomness. Reports precede private
recommendations; actions remain voluntary. An equilibrium must resist joint
report-and-action deviations, not merely truthful reports followed by forced
obedience. Costs below B are imposed when claiming that a designated or
cheapest volunteer obeys. All finite types have positive prior probability.

Public-local policies below use only own cost and exogenous public randomness;
labels and distinct local policies are allowed. An informed mediator instead
observes actual costs externally. The difference is a resource assumption.

## 2. P11-M1: the two-type public-local frontier

For n=2, let 0<l<h<B, p=Pr(C_i=l), and costs be iid. Put
cbar=pl+(1−p)h, q=1−p. The exact best expected welfare of every public-local
policy, with no requirement of equilibrium, is

    W_PL = max{2B−cbar, 2B(2p−p²)−2pl}.

The externally informed obedient optimum is

    W_* = 2B − l(2p−p²) − hq².

Thus, for 0<p<1,

    W_*−W_PL = min{pq(h−l), (2B−h)q²+lp²} > 0.

At p=0 or p=1 the gap is zero, as it is for h=l. This is the equality
criterion on the closed parameter domain 0≤p≤1, 0<l≤h<B. The public-local
maximum is an unconstrained team bound; its low-only/low-only maximizer need
not be an equilibrium. The designated-volunteer branch is obedient.

Proof. Conditional on any public seed, expected welfare is multilinear in
four behavioral action probabilities; a deterministic pair of policies attains
the maximum. Each agent has four policies N,L,H,A (never, low only, high only,
always). At a welfare maximum, the team's gain from a player volunteering at
type c is 2B(1−r)−c, where r is the opponent's aggregate volunteering probability.
Thus H (volunteer high but not low) cannot maximize: it would require this
quantity at h to be nonnegative and at l to be nonpositive, impossible when
l<h and both type probabilities are positive. Each policy paired with A is
weakly worse than N paired with A because service is already certain. N paired
with any policy is maximized by A, because 2B−C>0. Only LL and designated A,N
remain, with the stated welfares. At p=0,1 drop null types. At h=l, designation
is pointwise efficient. The displayed gaps follow by subtraction. Exactly one
cheapest volunteer is the pointwise welfare optimum, and obeys ex post because
B>C_i; an abstainer only adds its positive cost by deviating. ∎

Failed shortcut retained: directly replacing H by L need not improve welfare
when p≠1/2, because it changes service probability. The team best-response
threshold argument, rather than this false pointwise dominance, is used above.

## 3. P11-M2: guaranteed-service screening impossibility, arbitrary finite n

Consider any Bayesian equilibrium of a finite communication/recommendation
protocol with independent positive private costs, type-independent auxiliary
randomness and no transfers, verification or type-dependent feasible actions.
Suppose service is provided almost surely at every type profile on its support.
Let x_i(c)=Pr(a_i=1 | C_i=c) under the equilibrium. Then x_i(c) is constant in c.
Consequently

    E W ≤ nB − min_i E C_i.

If every possible cost is below B, this bound is attained by publicly
designating an agent minimizing its mean cost. For iid costs it is attained
by an exchange-invariant public lottery over designated agents. This is an
implementation bound, independent of protocol length or public/private message
alphabet; it does not say that arbitrary posterior distributions coincide.

Proof. A type c can imitate the full randomized communication/action strategy
of another possible type d, including any responses to received messages.
Independence ensures that the law of opponents' types is unchanged. The
resulting service/workload law is exactly that of type d in the original
equilibrium, hence its expected payoff is B−c x_i(d). Equilibrium implies
B−c x_i(c)≥B−c x_i(d), so x_i(c)≤x_i(d), since c>0. Reversing c,d gives equality.
Write the constant as x_i. Expected total cost is ∑E[C_i]x_i, whereas guaranteed
service gives ∑x_i=E[∑a_i]≥1. Positivity implies ∑E[C_i]x_i≥min_i E C_i.
Designating the minimum-mean agent provides service and costs exactly its
mean; the designated agent strictly prefers volunteering when C_i<B and all
other agents strictly prefer abstaining. Public correlation is disclosed
before acting and is not an independent mixed Bayesian equilibrium. ∎

Direct truthful mechanisms are included: mimicking d is false reporting d
followed by the d-type action strategy. Testing only report-and-follow
incentives is already necessary for the bound, but is insufficient for an
implementation claim. Conversely the designated construction resists every
joint report/action deviation because reports are unused and play is ex-post
obedient.

### P11-M3: exact efficient-implementation criterion

Assume every possible cost is below B. The first best is

    W_FB = nB−E[min_i C_i].

A no-transfer Bayesian communication equilibrium attains this welfare if and
only if there is an index j with C_j≤C_i almost surely for every i. In that
case fixed designation of j attains it. In particular, iid nondegenerate
positive costs cannot attain first best for n≥2, regardless of communication.

Proof. At each profile the unique efficient kind of action is exactly one
minimum-cost volunteer; its identity may tie. Therefore welfare efficiency
forces guaranteed service. M2 gives E[min C_i]=min_i E C_i as a necessary
condition. Choose j attaining the minimum mean. The nonnegative random
variable C_j−min C_i has expectation zero, so vanishes almost surely. Conversely
an almost surely cheapest j can be designated. For iid nondegenerate costs,
there are two values l<h with positive probabilities. The event C_j=h and
some other C_i=l has positive probability for every j. ∎

This criterion is for weak implementation of one equilibrium. It does not
establish unique equilibrium or full implementation. Correlated costs,
observable verifiable types, payments, effort-dependent benefits, report costs,
repeated reputational stakes and type-dependent feasible actions can invalidate
the mimic proof. No claim is made about LLM agents' actual behavior.

## 4. P11-M4: an explicit reliability–screening bound

For iid binary costs 0<l<h<B with 0<p<1, n≥2, any such Bayesian equilibrium
(allowing failure) has service probability S and satisfies

    E W ≤ (nB−cbar) S + [npB(h−l)/l](1−S).

This is an upper bound, not a sharp frontier. It yields a nontrivial whole-class
regime: if npB(h−l)/l≤nB−cbar, even arbitrary failure-contingent communication
cannot improve on the designated-volunteer welfare. At equality this does not
claim uniqueness of its maximizers.

Proof. Let s_i(c) and x_i(c) be conditional service and participation
probabilities. Mimicking the two type strategies yields, with
Δs=s_i(l)−s_i(h) and Δx=x_i(l)−x_i(h),

    l Δx ≤ B Δs ≤ h Δx.

Thus Δx≥0, Δs≥0, and Δx≤BΔs/l. Since
S=p s_i(l)+(1−p)s_i(h), Δs≤(1−S)/(1−p). The cost identity is

    E[C_i a_i]=cbar E[a_i]−p(1−p)(h−l)Δx.

Sum over i, use E∑a_i≥S, and substitute the bounds. ∎

These are ordinary pairwise incentive inequalities; they should not be
presented as a new general screening principle.

## 5. P11-M5: the general successful-coalition characterization

Let F⊆2^I be a known nonempty upward-closed family, with ∅∉F. Service occurs
exactly when the set of active agents lies in F. Costs remain independent,
positive, finite-support and individually below B. All agents obtain the same
benefit B from success and active agents pay their private cost. The communication
resources and equilibrium notion are those in M2. Then the sharp optimum over
all guaranteed-service Bayesian communication equilibria is

    W_G = nB − min_{S∈F} ∑_{i∈S} E C_i.

There is a first-best efficient Bayesian communication equilibrium if and only if
one fixed feasible coalition S is minimum-cost almost surely:

    ∑_{i∈S} C_i = min_{T∈F} ∑_{i∈T} C_i    almost surely.

Proof. M2's mimic argument depends only on success being certain, not on the
production technology, so E[C_i a_i]=E C_i E a_i. Realized active sets are in F;
therefore their expected mean-cost sum is at least the displayed deterministic
minimum. Choose S minimizing mean cost. Strictly positive means make it
inclusion-minimal: no proper subset is successful. Designating S independently
of actual types is ex-post obedient, since removing an active agent makes
service fail, costing it B rather than C_i, while an inactive agent's extra
activation only wastes its positive cost. This attains the bound, and reports
are unused. At each realized profile the first best succeeds (all costs<B
implies every feasible total cost<nB) using a cheapest successful coalition.
Hence first-best welfare is nB−E[min_{T∈F}∑_{i∈T}C_i]. Equality with the bound
holds exactly when a mean-cost-minimizing fixed S attains this realized minimum
almost surely, by expectation zero of the nonnegative difference. ∎

This covers threshold tasks, coverage systems and redundant worker coalitions,
with F explicitly specifying the task technology. For a threshold m, the bound
subtracts the sum of the m smallest means. For iid nondegenerate costs and
1≤m<n, no fixed m-set is always cheapest: for any such set there is positive
probability of a high cost inside and a low cost outside. For a symmetry group
preserving F and the prior, a public uniform lottery on the orbit of a chosen
minimum-mean coalition has the same optimum, is exchange-invariant under that
group, and remains an ex-post obedient lottery of designated coalitions. This
averaging statement does not reduce the information needed for the first best.

Do not overinterpret F: heterogeneous task labels, action-dependent quality,
sequential completion, correlated costs and type-dependent capabilities require
new models. This is a shared-success private-workload architecture, not a
general characterization of decentralized coordination.

## 6. Resource changes: verification and transfers

Externally observing costs restores the cheapest-agent rule, with ex-post
obedience if all costs<B. This is not truthful elicitation. With transfers
funded by an external sponsor, truthful cheapest selection is implemented by
a second-price procurement rule: choose a minimum reported cost (fixed tie
priority), pay the selected agent the second-smallest report ONLY on verified
completion, and pay others zero. True costs and reports lie in the disclosed
finite positive domain below B. Truthful reports followed by obedience form an ex-post honest-and-obedient
equilibrium: fixing opponents to their truthful reports and prescribed obedient
continuations, a selected agent finds completion better than abstention, and
its gain over losing is second price minus actual cost. An agent with cost above that price cannot profit by winning;
an agent below it cannot profit by losing. Nonselected extra volunteering only
adds cost. The transfer is not budget-balanced; completion verification is a
new primitive. No claim of minimal audit complexity follows.

A stronger dominant-strategy assertion for the unrestricted voluntary-action
extensive game is false. Take n=2, B=2, report/cost domain {1/2,3/2}, and
least-index tie priority. Agent0 has actual cost3/2 and agent1 cost1/2. Suppose
agent1 reports truthfully but always abstains, even when selected. A truthful
report by agent0 loses; its best subsequent action is unpaid volunteering,
with utility1/2. A false low report wins the tie, and completing earns
utility2−3/2+1/2=1. Thus truthful reporting is not dominant against arbitrary
opponents’ off-equilibrium action strategies. The valid statement above is an
ex-post equilibrium against obedient continuations, not dominant-strategy
implementation of the unrestricted extensive game. This correction was
identified in root adversarial review; classical second-price report DSIC
assumes a different allocation/enforcement model.

In an agent-delegation application, M2 says cheap talk alone cannot assign an
always-completed one-worker task to the least private-cost worker when all
workers prefer a lower chance of workload and task success benefits everyone.
The protocol must relax completion guarantees or change incentives/information.
It guarantees neither task quality nor rational behavior in an actual LLM system.

## 7. Primary-source comparison and research priority

Sources accessed 16 October 2026; source content was read via primary-host PDF
text, not inferred from titles. No third-party PDFs were added to the repo.

- [Battaglini–Palfrey, July 26 2024 author manuscript](https://www.its.caltech.edu/~trp/Olson_27July2024%20wiith%20appendix.pdf),
  *Organizing for Collective Action: Olson Revisited*, published JPE132(9),
  2881–2936, DOI10.1086/729580. This is close prior art: §2.2 defines
  private-report honest/obedient communication mechanisms. Printed p11 (HO)
  explicitly includes joint report/action deviations; its (IC) makes the
  flat-success⇒flat-activity argument immediate. Printed p10 footnote12 already
  gives symmetry averaging preserving honesty, obedience and surplus. §3.2
  contrasts enforceable recommendations; §5 studies optimization, and Lemma1
  concerns flattening interim success/activity probabilities as population grows.
  Its threshold technology and continuous iid costs include costs above the
  benefit; our finite costs below B serve a different limited regime. The
  guaranteed-service/no-screening criterion is a direct incentive specialization,
  not a replacement for that characterization.
- [Battaglini–Palfrey, March27 2025 author manuscript](https://static1.squarespace.com/static/54ae5756e4b08953398803ea/t/67e81203be874132bcbbda88/1743262211219/VolunteerDilemma_25Mar2025.pdf),
  *Welfare in the Volunteer’s Dilemma*, §2.1 equation1 gives the private-cost
  cutoff BNE; §2.2 studies welfare and its group-size asymptotics; first-best
  welfare is given before equation4. It studies equilibrium welfare, not our
  exact no-communication architecture bound.
- [Bergemann–Morris2016, Theoretical Economics11](https://economics.mit.edu/sites/default/files/publications/paper_79_bce.pdf),
  Theorem1, printed p495: Bayes correlated decision rules correspond to BNE
  under information expansions. This validates the informed-mediator vocabulary,
  but external information expansions do not solve endogenous truthful reports.

All are prior work; no novelty asserted for procurement, mimic deviations,
multilinear extrema, lowest-cost efficiency or honest/obedient distinctions.
The strongest next question is a class-wide resource-constrained implementation
criterion combining verifiable task-relevant contrasts with strategic reports,
not another volunteer formula. Symmetry can average an admissible mechanism
but cannot repair violated incentive inequalities or replace information.

## 8. Verification

`experiments/phase11_mechanisms.py` uses Fractions to enumerate all sixteen
public-local policy vertices, all types/actions in cheapest selection, interim
mimic gains, arbitrary binary direct recommendation kernels, and payment
joint deviations. Tests compare exact parameter families, including an LL
optimal regime and designated optimum, and retain a correlated-type witness
to the independence boundary. Computational checks support the proofs and do
not replace them. Independent read-only reconstruction by the orbit-algorithms agent found no
defect in M2/M3/M5; its endpoint qualification for M4 was incorporated explicitly.
Root reconstructed M1–M5 without a proof defect and corrected the separate
procurement implementation claim as recorded above. Shared-model AI review is
not external peer review.
