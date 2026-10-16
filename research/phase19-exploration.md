# Phase 19: private self-tests and the value of observing information availability

Nicholas Ham; Codex-assisted exploratory branch. This moves away from exact
geometry and the already-known memory line. Finite capability/task/message
models throughout; conditional obedience and acquisition architecture explicit.
No companion edits or new manuscript. Novelty remains provisional.

## 1. Model: private self-awareness is an exogenous information resource

Exactly one of N>=2 workers is capable: theta uniform on{1,...,N}. Success
occurs iff that worker works. Worker i's payoff is B*success-c*work, with
0<c<B. Require conditional obedience margin delta, where
0<=delta<=min(c,B-c). A committed coordinator acquires finite Z from theta,
then sends private addressed messages using Z and fresh independent randomness.
Its acquisition cost is I(theta;Z). No worker reports signals or communicates
with another. Messages, their privacy and addressing are supplied resources;
this cost does NOT count all information in the system.

Before acting, each worker either sees its true capability bit 1[theta=i]
or an erasure symbol U. An exogenous availability flag makes the first event
occur with probability alpha, independent of theta and the coordinator's
experiment/randomness. Flags may be independent across workers or correlated;
the proofs require each own flag to have the same alpha and be independent of
(theta,Z,all message/randomization inputs), not independence across flags.
The coordinator does NOT observe the flags and cannot ask workers to reveal
them. Workers know their own flag. Their own fresh private coins are independent
of theta and all availability flags. There are no state-correlated seeds or
other signals.

An informed capable worker must work, with gain B-c; an informed incapable
worker must abstain, with gain c. For an UNINFORMED worker, the coordinator's
message prescribes an action and must be delta-obedient given that worker's
message AND its erasure signal. Thus an invitation is not an unconditional
literal instruction overriding a verified private incapability. The implemented
policy explicitly allows informed workers to override an invitation. Calling
that whole policy a literal work recommendation would change the model.

Let C_0(t) denote the minimum acquisition cost of the ORIGINAL no-self-test
model at success exactly t, with the same B,c,delta and private action bits.
Set C_0(t)=+infinity for infeasible t. The following theorem is operational:
it reduces the entire augmented mechanism class, not just a proposed symmetric
list experiment, to this base frontier.

## P19-E1: exact reliability rescaling with hidden self-test availability

For0<=alpha<1, the minimum coordinator acquisition cost at success exactly s is

    C_hidden,alpha(s)=C_0((s-alpha)/(1-alpha)),       alpha<=s<=1.     (H)

Success below alpha is impossible under obedience. In particular
C_hidden,alpha(1)=C_0(1) for EVERY alpha<1. At alpha=1 the capable worker always
recognizes itself, everybody acts correctly and success one needs zero
coordinator information. Whenever C_0(1)>0, exact certain-success acquisition
therefore has a discontinuity at full self-awareness. This is a zero-error
architecture effect, not a claim that private information is useless.

### Counterfactual action construction and all-deviation argument

For an arbitrary permitted mechanism define A as the vector of actions workers
would use if their own signal were U, with the same messages/private random
coins. This is a COUNTERFACTUAL uninformed work set, not the realized work set.
It can be sampled from Z and theta-independent coins; hence
I(theta;Z)>=I(theta;A). Since every own erasure event is independent of theta,
messages and private coins, an uninformed worker's conditional belief about
its own capability given its message/action equals the belief in that
counterfactual mechanism.

More importantly, its switching gain is ALWAYS

    work gain = B*Pr(theta=i | own U,message/action)-c.

If theta=i, this worker's action alone changes success; if theta differs,
its action never changes success, regardless of what informed OTHER workers
know or do. Abstention gives the opposite gain. Therefore ALL of the
uninformed message-conditioned obedience constraints are precisely the base
constraints; they are not invalid unconditional averages over informed types.
Coarsening each message to its prescribed action preserves delta-obedience
by conditional averaging. Thus the counterfactual A is a feasible base
recommendation law. No deviation using the richer original message escapes
this converse, since its constraints were imposed before coarsening.

For the actual capable worker, work occurs surely when it is informed and
otherwise exactly when theta belongs to A. Its own flag is independent of
(theta,A), yielding

    actual success = alpha+(1-alpha)*Pr(theta in A).

This gives the converse acquisition lower bound in(H). Conversely take any
base mechanism for t, use the same experiment and messages, and let informed
workers follow their known-capability dominant action while uninformed workers
follow the base bit. Every augmented information event obeys with margin
delta, the displayed reliability identity holds and acquisition cost is
unchanged. This proves both inclusions, including arbitrary finite private
message alphabets and any independent randomized response policies.
If a base infimum rather than a minimum is used, the same equality holds for
infima by approximation; no unattained optimizer is silently assumed.

The counterfactual construction relies on the erasure signal revealing NO
state information. No analogous rescaling is asserted for noisy signals with
state-dependent error rates, correlated signal flags and capability, workers
communicating their flags, or the coordinator observing flags. These are
meaningful different architectures.

### Scope beyond symmetry

The counterfactual equivalence does not require a uniform prior, equal costs
or equal margins: replace the base problem by any fixed prior and worker costs
c_i/margins delta_i with delta_i<=min(c_i,B-c_i). With a COMMON alpha, exactly
(H) still holds because the reliability identity and each worker's gain are
unchanged. This is a theorem about the architecture, not permutation symmetry.
If own erasure rates differ, with every alpha_i<1 and each flag independent of
state/messages, the same construction gives an exact reduction retaining
statewise base hit rates t_i=Pr(i in A|theta=i):

    actual success=sum_i mu_i[alpha_i+(1-alpha_i)t_i].

Thus the correct base objective is weighted statewise success, not the scalar
uniform frontier. No closed-form nonuniform optimization theorem follows
from this observation. If some alpha_i=1 its uninformed information events
vanish and that worker's counterfactual base constraints cannot be inferred;
that boundary must be handled separately.

## P19-E2: availability information without capability information has value

For a sharp comparison use a COMMON availability flag R, independent of theta:
R=1 with probability alpha means EVERY worker privately knows its own capability;
R=0 means every worker sees U. First hide R from the coordinator, giving(H).
Now allow the coordinator to observe R before acquiring an experiment. It
need not learn theta from R: I(theta;R)=0. Charge I(theta;R,Z), counting all
coordinator information. At success one the exact optimum becomes

    C_visible,alpha(1)=(1-alpha)*C_0(1).                         (V)

Proof: conditional on R=0 full success and obedience require a base mechanism,
so I(theta;Z|R=0)>=C_0(1). The R=1 information term is nonnegative; I(theta;R)=0.
Conversely acquire the optimal base experiment only when R=0 and acquire
nothing when R=1. Workers can tell which case they are in from their own
self-test status, and every prescribed action remains obedient. Thus(V) is
sharp. This construction makes no cost reports and needs no truthful reporting
argument; R is an observed exogenous sensor-availability bit.

Whenever C_0(1)>0 and0<alpha<1, knowing a flag that is STATISTICALLY INDEPENDENT
of capability strictly reduces optimal acquisition cost. It identifies when
other participants already possess useful information. This is complementary
information about the information architecture, not a contradiction of data
processing: the experiment can now be adapted to R. If R is hidden, blindly
mixing 'acquire' and 'do not acquire' fails exact success whenever an uninformed
capable worker receives the latter branch.

### Exact quantitative specialization and limits

Phase18's certain-success frontier gives, with
r=min(N,B/(c+delta)) and L the linear interpolation of log at integer sizes,

    C_0(1)=log N-L(r).

Hidden availability retains this cost; visible common availability multiplies
it by1-alpha. For instance N3,B1,c3/5,delta1/10 gives r10/7 and
C_0(1)=log3-(3/7)log2>0. This is not a new entropy inequality: the substantive
step is the exact COUNTERFACTUAL-mechanism equivalence and adaptive-availability
comparison. If c+delta<=B/N, C_0(1)=0 and there is no strict gap.

When c-B/N>=delta, workers without invitations can all abstain while informed
capable workers work. Hence zero coordinator information already attains
success alpha. The low-success Phase18 segment transforms to

 C_hidden,alpha(s)=((s-alpha)/((1-alpha)*tau))*D_Ber(tau||1/N),
 alpha<=s<=alpha+(1-alpha)*tau,  tau=(c+delta)/B,

under the full original domain1/N<tau<=1 and delta<=c-B/N. This is an exact
corollary of(H), not an independently new reliability frontier. It illustrates
why the old lower bound stated in terms of ACTUAL work/success can be wrong
when workers have uncharged private self-information. The effective original
reliability is(s-alpha)/(1-alpha), not s. No claim is made about information
obtained by workers themselves being physically free or available in practice.

## Opportunity and implementation implications

Workers can have identical ex-ante capability opportunities and yet differ in
whether their current information access is known to the coordinator. That
knowledge changes acquisition efficiency without changing the prior chance of
being capable. We do not identify opportunity equivalence with welfare or
fairness, compare uncalibrated utility magnitudes, or infer a canonical Game
Fairness theorem. The connection is a question about explicitly specified
information access, suitable for a separate companion handoff only if further
canonical mathematics is needed; no companion edits are proposed here.

The same symmetry of workers used in base optimal list mechanisms does not
remove the need for information. The coordinator still needs private addressed
channels and a committed experiment. No decentralized implementation, truthful
signal reporting or learning convergence follows from(H)/(V). Observing R
requires an availability/monitoring channel; it is not synthesized by the model.
This gives a concrete resource question beyond the previous memory examples:
which participant information-status signals can be safely verified and used
for adaptive sensing without revealing the capability itself?

## Primary comparison and originality assessment

[Bergemann–Morris2016, Bayes correlated equilibrium and the comparison of
information structures in games, final primary journal text](https://economics.mit.edu/sites/default/files/publications/paper_79_bce.pdf)
was actually inspected at its introduction's outcome characterization and
information/incentive ordering. It explicitly requires obedience conditional
on own type and recommendation and treats receivers with prior information.
These are established foundations, not discoveries of this branch. An
unrestricted BCE decision rule can depend on the full type/signal profile;
our hidden-availability coordinator cannot do so. Its experiment and messages
must remain independent of availability flags conditional on capability.
Dropping that architecture would invalidate(H); the hidden/visible comparison
is precisely about that extra availability channel. No general new information
ordering or BCE characterization is claimed.

[Kolotilin–Mylovanov–Zapechelnyuk–Li, Persuasion of a Privately Informed
Receiver, primary author manuscript dated19November2016](https://www.gla.ac.uk/media/Media_500913_smxx.pdf)
was inspected at its model and implementation-equivalence introduction. It
already studies binary actions, private receiver types and persuasion
mechanisms versus experiments. Its private preference type is independent of
the payoff state, whereas our self-test signal directly concerns own capability
and our coordinator is not allowed to elicit a report. Their equivalence cannot
be cited as a proof of(H), but it rules out any broad originality claim for
incorporating private receiver information or distinguishing mechanisms from
experiments. The accessed manuscript version, not an assumed final publication
body, is the source actually read. A separate Hu–Weng robust-private-receiver
PDF endpoint failed and is not counted as inspected.

The proofs here use elementary counterfactual coupling, type-conditioned
obedience, data processing and conditioning on an independent availability
flag. They identify a technically distinct architecture reduction, potentially
useful for adaptive sensing, but do not establish a new general information-
design principle. The certain-success discontinuity and the value of an
availability bit should be presented with the free-self-test and zero-error
restrictions; they are not claims of universal information complementarity.
Exact priority of the unique-capability specialization remains unresolved.
A larger literature review on private receiver experiments, complementary
information and adaptive sensing would be required before publication claims.

**Next worthwhile question.** If a self-test has false positives/negatives,
its result generally changes beliefs even on the non-reveal event. The
counterfactual base equivalence then fails, and joint recommendations must
satisfy different posterior thresholds by signal type. Finding a sharp
non-erasure characterization, or a useful verified availability protocol,
would be more significant than merely substituting an existing base frontier
into(H). No such stronger noisy-signal theorem was proved in this pass.

## Exact verification and actual reviews

Nine exact tests pass under
`python3 -m unittest discover -s experiments -p test_phase19_exploration.py`.
They enumerate capability, private invitations and independent/common/
exactly-one-aware flag patterns; verify every augmented information-event
margin and the exact reliability transform; check erased-type rows equal
scaled base rows; test uniform containing-list posteriors; demonstrate zero
coordinator-acquisition self-test success and the failure of blindly skipping
acquisition; verify nonuniform heterogeneous-availability reliability; and
check that informed incapable workers must override literal invitations.
They do not solve arbitrary information-design programs numerically, compute
logarithmic values by floating approximation, or establish novelty.

The information branch independently reconstructed E1/E2 without finding a
defect. It specifically checked that no all-erased JOINT flag event needs
positive probability: the counterfactual action set is a product of response
policies and each worker's OWN erasure event suffices. Correlation of flags
therefore does not invalidate the result. It also checked rich-message
coarsening and visible-R chain-rule optimality. The actual lower feasible
success may exceed alpha when the base s_min is positive; C_0=+infinity already
encodes this, so the theorem does not assert every s>=alpha is feasible.
This is internal AI proof review, not external peer review.

This branch reciprocally reconstructed the complete I1–I3 frontier in
`phase19-information-frontier.md`. Both obedience moment bounds and all
feasibility endpoints were checked. The KL-conjugate log-partition is concave
in integer cardinality; adjacent interpolation makes Jensen tight, and the
common tilt realizes the required success. Its monotonicity in mean justifies
U(s). Convexity along the two rays gives the preferred reliability and the
exact/at-least distinction, including sigma0, tau1 and the critical zero-margin
case. No defect found; real/algebraic-probability implementation limits remain
essential. This is proof reconstruction, not an independent priority finding.

The complement-closure theorem in `phase19-payoff-geometry.md` was also
independently reconstructed. Payoff-preserving complementation exchanges the
two action rows, and own-flip complementarity fixes their sum, yielding the
exact clipped payoff polytope. The cycle parity-flow application is valid.
No positive payoff-space separation follows from that stopped lead. No defect
found in the stated theorem, and no manuscript or companion edits made.
