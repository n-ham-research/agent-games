# Phase 15 — mediator channels, safe disclosure and obedience leakage

16 October 2026. Nicholas Ham's Agent Games programme; information-branch
Codex development. This branch gives scoped channel characterizations and
robustness certificates. Most underlying principles are established Blackwell,
Bayes-correlated-equilibrium and likelihood-ratio methods. It does not claim a
new general theory of information design or truthful elicitation.

## 1. Exact model: keep state information and recommendation privacy separate

There is a finite state theta with known full-support prior mu; theta includes
actual costs. Agent i observes its own type t_i(theta), including its cost, and
receives a private literal action recommendation a_i. A coordinator sees a
private signal z from an external experiment Q(z|theta), then uses independent
randomness to generate joint recommendations a and optional public disclosure y.
The coordinator receives NO strategic type reports. The emitted law is a
prescribed kernel J(a,y|theta). Agents observe (t_i,a_i,y), not z, other agents'
recommendations, or the coordinator's random tape. All channels, messages and
state alphabets are finite. Addressing/private communication are explicit
architectural resources, not inferred free from a state-information statistic.

For delta>=0, conditional delta-obedience means the utility advantage over each
alternative action is at least delta, at every positive-probability receiver
information event (t_i,a_i,y). For binary work in a monotone contribution task,

    Delta_i(theta,a)=B*pivotal_i-c_i       if a_i=work,
    Delta_i(theta,a)=c_i-B*repair_i        if a_i=abstain.

The benefit B>0 and costs satisfy 0<c_i<B. Other models can use the general
utility difference; the exact pivotal/repair formulas below use this architecture.

## P15-I1 — information feasibility separates from obedience for a prescribed law

A prescribed J is implementable through PRIVATE experiment Q with the declared
literal recommendations and public y if and only if

1. J(a,y|theta)=sum_z Q(z|theta)D(a,y|z) for a stochastic decoder D;
2. J satisfies the stated conditional delta-obedience inequalities.

Necessity is the Markov factorization of the coordinator's observation/action
architecture plus equilibrium obedience. Sufficiency uses exactly D and sends
only the prescribed private/public messages; no extra seed or z is disclosed.
Thus a fixed law's incentive validity is independent of WHICH factorization
implements it, provided the receiver information remains exactly the declared
information. This applies to correlated types; independence is not needed.

Consequently a Blackwell-more-informative PRIVATE coordinator experiment can
simulate any less informative one, preserving the entire joint outcome law
and all conditional margins. This is a standard simulation/obedience principle,
not an original Blackwell theorem. If z itself must be disclosed to the agents,
the receiver information changes and the conclusion need not hold.

### Minimum information, with the resource meaning explicit

Among arbitrary experiments capable of implementing a prescribed obedient J,
the direct channel theta -> (a,y) is Blackwell-least: every implementing Q
has J as a garbling, and J implements itself by the identity decoder. A least
Blackwell class need not specify a unique signal alphabet or sampling cost.
For deterministic observations of a partition of theta, implementation is
possible exactly when J's rows are constant on every partition cell. The
coarsest such partition groups identical rows of J.

If only the number of private signal values is minimized and experiments may
be randomized, its exact minimum is nonnegative rank of the row-stochastic
matrix J. For rational-only implementations use RATIONAL nonnegative rank;
real and rational minima cannot be identified without proof. This is precisely
Cohen–Rothblum1993 Theorem3.2 applied to the coordinator channel, not a new
rank theorem. For example three states with binary-output probabilities
0,1/2,1 require three deterministic partition cells but only two stochastic
signal values. No efficient minimal-factorization algorithm is asserted.

Mutual information about theta is not a measure of recommendation-privacy or
communication resources. A coordinator with no state information can still need
private correlated messages. Conversely independent action randomness can be
sampled without observing theta. The experiment/decoder model charges neither
sampling nor message bits unless those are added separately.

### Literal recommendations are a substantive restriction

A cost-blind coordinator sending TYPE-CONTINGENT PLANS is more general than
sending literal actions independent of types. With two volunteers, B=2 and iid
costs1/2,3/2 equiprobable, the fixed instruction 'work iff low' is a strict
Bayesian equilibrium: the other's work probability is1/2, so the gain from
work is1-c, positive for low and negative for high. Its actual action kernel
varies with the private type profile although the coordinator observes nothing.
Thus ordinary J=QD factorization cannot be used as a lower bound for arbitrary
local type-dependent coordination. It characterizes the declared literal-action
architecture. General plan-mediated outcomes require local response maps
D_i(a_i|z_i,t_i), and their information/incentive restrictions differ.

## P15-I2 — safe public disclosure: a convex cone with no greatest partition

Fix a private recommendation law K(a|theta) and mu. Write w=(theta,a),
P(w)=mu(theta)K(a|theta), and e_i(w)=(t_i(theta),a_i). A proposed public release
has channel L(y|w). Its statistical availability must separately respect the
coordinator's information; equivalently the JOINT target K(a|theta)L(y|theta,a)
must satisfy P15-I1. Conditional on availability, the exact safety criterion is

    sum_{w:e_i(w)=e} P(w)L(y|w)[Delta_i(w)-delta] >= 0
                                      for every i,e,y.             (S)

The condition is necessary and sufficient, including zero-probability events
without dividing by them. Every channel column lies in the cone cut out by
these inequalities, while columns sum pointwise to one. Therefore safe releases
with a fixed output alphabet form a convex polytope; arbitrary postprocessing
of a safe release remains safe by summing the inequalities. The largest
conditional margin cannot decrease under garbling a disclosure. These are
finite obedience/averaging facts closely related to established BCE orderings.

But individually safe public releases need not be safe when COMBINED, and
there need not be a finest safe deterministic partition. Exact strict example:
four equiprobable states theta=(b1,b2); two singleton-capable volunteers each
have B=1,c=3/4. At state00 recommend empty failure surely. At each other state
choose one volunteer uniformly. Revealing b1 alone is safe; revealing b2 alone
is safe. In either bad-containing cell the work margin is1/4 and abstention
margin is1/12; the other cell has certain success. Thus both releases preserve
any delta<=1/12. Joint disclosure of (b1,b2) reveals certain failure at00,
where either singleton profits by volunteering. It fails even weak obedience.
Any common refinement of the row and column partitions is the full partition,
so no finest safe partition can dominate both. This is an information-design
counterexample, not a claim that unsafe channels become feasible by mixing them.

For fixed coordinator information, public release can shrink feasible outcome
laws by adding receiver incentive constraints. Additional PRIVATE information
can be ignored, but irrevocably PUBLIC information cannot generally be ignored
by rational receivers. These are different interventions, not opposing claims
about one information order. Bergemann–Morris2016 is direct conceptual prior.

## P15-I3 — exact likelihood-ratio budget for robust public disclosure

A quantitative sufficient certificate can avoid enumerating every public
posterior. For each receiver event e=(own cost c,recommended action), suppose
for every positive-probability public y the likelihood L(y|w) over all supported
w with e_i(w)=e has positive minimum and maximum with ratio at most R>=1.
This protects the FULL residual world, including other recommendations; it is
not merely privacy of reported types. State-only releases conditionally
independent of recommendations can satisfy this condition, but arbitrary seed
releases need not.

For an event G of prior conditional probability p, Bayes' rule and the likelihood
ratio give the sharp posterior interval

    p/[p+R(1-p)] <= Pr(G|e,y) <= R*p/[1-p+R*p].           (O)

Proof: conditional likelihood averages on G and its complement have ratio in
[1/R,R]. Substitute them in posterior odds. Equality is attained by a two-world
randomized-response channel with likelihoods1/(1+R),R/(1+R).

Suppose baseline conditional obedience margin is at least delta. On a work
recommendation its pivotal probability is at least (c+delta)/B, so every
posterior work margin is at least

    M_work = B*(c+delta)/[c+delta+R*(B-c-delta)] - c.

On an abstention recommendation the repair probability is at most(c-delta)/B,
so every posterior abstention margin is at least

    M_abstain = c - B*R*(c-delta)/[B-c+delta+R*(c-delta)].

Use each formula only for recommendations of positive probability, for which
0<=delta<=B-c (work) or0<=delta<=c (abstention) is necessary. These are exact
worst-case local bounds given the baseline margin and ratio certificate;
sharpness is statistical/conditional, not an assertion that every local extreme
can be simultaneously embedded in every task and all agents' CE constraints.

If 0<delta<min(c,B-c), weak obedience is guaranteed provided

    R <= (c+delta)*(B-c)/[c*(B-c-delta)]                 for work,
    R <= c*(B-c+delta)/[(B-c)*(c-delta)]                 for abstention.

At delta=0 either threshold is1: weak obedience alone gives no uniform tolerance
for likelihood-ratio leakage. To retain a desired positive margin delta', use
M_work,M_abstain>=delta'. Endpoint cases use the displayed margin formulas
rather than undefined divisions. Sequential releases whose conditional
likelihood ratios are bounded by R1,R2,... have joint ratio at most their
product, even when later kernels depend on earlier public outputs, so the
same certificate composes multiplicatively. Conditional independence across
releases is unnecessary when the per-history bounds are supplied.

This is a task-specific exact posterior-odds application, not a new differential-
privacy theorem. As a coarser comparison, posterior TV at most eta loses at
most B*eta in a binary work/abstention margin, since its range width is B.
A likelihood ratio R yields the standard posterior-TV bound
(sqrt(R)-1)/(sqrt(R)+1); the exact cost-dependent formulas can be stronger.

### Why type privacy alone fails

One payoff state, two volunteers, B=1,c=1/2. Recommend empty with probability1/5
and each singleton with probability2/5. The private law has work margin1/2
and abstention margin1/6, hence is1/10-obedient. Publish the sampled coalition
itself: failure becomes public and singleton deviation is profitable. Since
there is only one type/state, the release is trivially perfectly private ABOUT
TYPES. It is not private about the residual recommendation randomness. Thus
neither type mutual information nor a type-only privacy guarantee suffices to
certify preservation of correlated obedience. Joint/private-message information
belongs in the privacy hypothesis; no claim of a new privacy paradox is made.

## Assessment and primary comparison

This branch's strongest deliverable is a precise separation of three resources:
coordinator state information, receiver information, and private correlated
recommendation randomness. It supplies exact feasibility/safety checks, a
nonlattice disclosure counterexample and sharp local leakage-margin bounds.
These are useful extensions of the prior cost-blind examples, but substantially
established methods; no independent algorithms paper is justified by them alone.

Primary sources actually inspected16October2026:
- Bergemann–Morris2016, *Bayes correlated equilibrium and the comparison of
  information structures in games*, author-hosted full text
  https://economics.mit.edu/sites/default/files/publications/paper_79_bce.pdf .
  Definition of obedience, Theorem2 and its proof pp502–504, Section5.4 inspected.
  Its individual-sufficiency ordering already characterizes more receiver
  information as stronger incentive restrictions. Private simulation and public
  garbling arguments here are scoped applications, not a new general ordering.
- Cohen–Rothblum1993, *Nonnegative ranks, decompositions, and factorizations of
  nonnegative matrices*, primary author full text
  https://lab.rockefeller.edu/cohenje/PDFs/211CohenRothblumLAA1993.pdf , Theorem3.2
  and normalization proof printed156 inspected. It is the exact algebraic prior
  for minimum stochastic channel alphabet. Rational-field caveat follows the
  resource branch's separately inspected irrationality literature.
- McSherry–Talwar2007, *Mechanism Design via Differential Privacy*, primary
  author PDF https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/mdviadp.pdf ,
  Section2/printed fourth PDF page likelihood-ratio utility argument inspected.
  Privacy/incentive links and compositional reasoning are established. Its
  approximate truthful-report mechanism is different from preserving a fixed
  correlated action law under public disclosure; our no-report model does not
  claim its truthful-elicitation conclusion.

No source establishes novelty of the examples or exact conditional formulas.
Any future novelty claim needs targeted comparison beyond these major priors.
No external contact, companion edit or manuscript promotion occurred.

## Validation and independent proof review

`python3 -m unittest experiments.test_phase15_information -v` passes eight
exact-rational tests. These check private-channel simulation and the distinct
deterministic partition requirement; positive-margin disclosure noncomposition;
postprocessing/independent disclosure; sharp randomized-response posterior
endpoints and local obedience thresholds; sequential ratio multiplication; and
both architecture counterexamples. No rank optimizer or claim of exhaustive
channel search is included.

The compact-computation branch independently reconstructed P15-I1--I3, including
the 1/12 margin and both likelihood thresholds, and found no proof defect. The
review emphasized the essential literal-action architecture restriction, the
positive full-residual-world likelihood condition, and the field qualification
for nonnegative rank. Root independently checked the posterior and margin
algebra.
