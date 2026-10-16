# Persistent-state reassignment: costs depend on controller access

Status: proved finite-model candidates, novelty provisional. No strategic or
LLM-agent behavior is asserted. All transformations compose right to left.

## Provenance and boundary

Game Fairness P8-C1, source commit
`bcf8bfcbd185962576b78a4ccd729e361231dea9`,
`research/phase8-behavior-and-identification.md`, is canonical for observer-quotient
splitting. The frozen local `research/origins/feasibility/feasibility.md`, Model C,
already uses C4 -> C2. Neither splitting nor that example is new here. The new
question in this note is a completely specified intervention/control problem:
when does the same obstruction cost a positive resource, and when does it cost
nothing? The elementary bounds below are operational specializations, not a new
group-extension theorem or a general communication-complexity result.

## Physical specification, independently of splitting

Two persistent agents occupy two recipient roles. A shared carrier has four
configurations X=Z/4. Role allocation is p(x)=x mod 2. Configurations with the
same role allocation differ in a binary calibration register b(x)=floor(x/2).
This can represent an orientation-sensitive shared tool: the task specification
requires register value zero before each task is performed, whichever agent
occupies which role. Thus the accepted configurations are 0 and 1; task output
is success exactly when b(x)=0. This requirement is an explicit input, not
deduced from a preference for group splitting. The model does not assert that
an actual agent system has this carrier architecture.

Initial state is publicly known x=0. A stream of identical requests swaps the
two roles; one task checkpoint follows each request. There are T requests.
The desired configuration at checkpoint t is r(p_t), with p_t=t mod 2 and
r(0)=0,r(1)=1. Requests cannot be skipped or replaced by direct reassignment.
Time within a request is not itself a task checkpoint.

Physical reversible transports are H=C4 acting by addition on X, projecting by
parity to P=C2. Role-preserving correction k=2 toggles calibration and has cost
c>0. At each request a primary actuator is applied, followed by any corrections,
then the task runs. Identity correction is free. Applying k twice costs 2c,
so an optimal correction uses k at most once. All costs count physical kernel
corrections; a primary actuator's baseline cost is common and omitted. If the
reverse primary actuator is separately priced, the conclusion changes below.

The complete observation o(x)=(p(x),b(x)) distinguishes all four states;
the universally invisible subgroup is trivial. With role-only observation the
invisible subgroup is {0,2}. P8-C1 applies to these normal subgroups. Here the
calibration register is tied to task success rather than merely exposed by an
extra formal probe.

## AG-C1: fixed actuator, sharp correction cost

Suppose the only primary actuator is h=1. A monitor can observe calibration and
apply correction 2. Every checkpoint must succeed. The least total correction
cost is

    c floor(T/2).

Proof. At any successful checkpoint the physical state is forced to equal p_t,
not merely some state with the correct parity. From state 0, actuator 1 reaches
the next required state 1, so no correction is needed. From state 1 it reaches
2 whereas the next required state is 0: an odd number of corrections is
necessary, and exactly one suffices. These cases alternate from initial 0.
Consequently every even request costs at least c, and correcting precisely
there attains the bound. Extra anticipatory corrections cannot improve it
because every preceding checkpoint must still have the prescribed state. QED.

For primary actuator 3 alone the analogous cost is c ceil(T/2). Optimizing a
single fixed actuator selected from {1,3} therefore still gives c floor(T/2).
Without correction, the h=1 implementation has
`2 floor(T/4)+max(0,(T mod 4)-1)` failed checkpoints (times congruent to 2 or 3
modulo 4), each with independently specified task loss L if failures cost L. This loss
count is not a claim about game payoffs or welfare.

Checkpoint timing is essential. If only the final checkpoint matters, repeated
h=1 needs just one correction iff floor(T/2) is odd, otherwise zero. Its cost
is c (floor(T/2) mod 2), not linear in T.

## AG-C2: a state-aware choice eliminates the cost

Now allow both primary actuators 1 and 3 at equal baseline cost, without any
kernel correction. A controller with one bit a storing current role parity
chooses 1 if a=0 and 3 if a=1, then toggles a. Starting at a=0,x=0 gives

    0 -> 1 -> 0 -> 1 -> 0 -> ...

and every checkpoint succeeds at zero correction cost. One controller state
cannot do this for arbitrary T>=2 when its only input is the identical swap
command, no clock, role observation, or external feedback is supplied, and it
must choose one deterministic primary actuator each time. It must repeatedly
choose either 1 or 3; neither gives the required first two transitions.
Thus two controller states are necessary and sufficient in this restricted
no-correction architecture. This is a one-bit memory bound, not a lower bound
on memory in arbitrary controllers. Fresh independent randomization without
memory cannot guarantee success almost surely: first-step success forces
actuator 1 with probability one, while second-step success requires 3.

The same model has two useful sharp alternatives:

* If the actuator reads current role parity, the bit is already observable and
  no additional memory is needed. If it is freshly initialized at each call
  and cannot read parity, a sender knowing parity can send one bit; a one-symbol
  deterministic message alphabet cannot distinguish the two required outputs.
  This is only a single-call, zero-error bound with both parities possible.
  It is not one bit of communication per request for a persistent controller:
  a persistent controller computes parity locally and communicates nothing.
* If reverse actuation 3 has extra cost d>=0 while actuation 1 is free, then
  exact successful checkpoints cost floor(T/2) min(c,d): every 1->0 transition
  uses either 3, costing d, or 1 followed by correction 2, costing c. Every
  0->1 transition can use free actuator 1. No other allowed operations exist.

The extension still does not split: every odd element of C4 squares to 2.
The zero-cost controller is not a homomorphic lift chosen once for each role
permutation. Its operation depends on current allocation. Indeed for any
section r and current allocation a, the transport

    h(p,a) = r(pa) r(a)^(-1)

has the requested projection and telescopes along a history. Thus *arbitrary
available lifts with current-allocation feedback* can track the chosen section
even when no homomorphic section exists. This elementary state-feedback
identity explains why nonsplitting alone never proves positive operating cost.

## AG-C3: fixed checkpoint tracking gives a finite cost formula

The preceding argument extends without claiming algorithmic novelty. Let H be
a finite implementation group acting regularly on its configurations, with
projection q:H->P and K=ker(q). Choose a normalized section r:P->H as the
physical task's target configurations. At checkpoint a the state must be r(a).
A request p changes the role allocation to pa. Primary operations available
for that request form a nonempty A_p subset of q^(-1)(p), each with cost
alpha(h)>=0. Following it, any k in K may be applied at effective cost
gamma(k)>=0. Effective cost includes the least price of any allowed sequence
implementing k; gamma(1)=0. Both the task targets and these prices are specified
independently. They need not be conjugation invariant.

For a disclosed request word p_1,...,p_T with a_0=1,a_t=p_t a_(t-1), minimal
total cost of exact checkpoint tracking is the sum over t of

    min_{h in A_(p_t)} [ alpha(h)
       + gamma(r(a_t) r(a_(t-1))^(-1) h^(-1)) ].

Proof. The unique post-primary correction satisfying
k h r(a_(t-1))=r(a_t) is
k=r(a_t) r(a_(t-1))^(-1) h^(-1). Its projection is identity, so it lies in K.
All checkpoints fix the intervening states, leaving no cross-time optimization;
each summand is an independent attained minimum over a finite set. Choosing
minimizers attains the sum, and any successful protocol incurs at least each
summand. QED. This statement does not require splitting, and is a direct finite
control calculation. If costed corrections do not implement all K, allow
gamma=+infinity, with infinite value meaning infeasibility. If the state action
is not regular, equality of states can admit multiple corrections and the
formula needs a stabilizer minimization; do not apply this form unchanged.

## What destroys the positive cost

Three independently natural changes suffice: omit calibration from task
consequences and permit no reset; supply both primary directions with current
role feedback; or allow a free destructive normalization R(x)=x mod 2 after
each request. The last is a noninvertible operation outside H and erases the
calibration register. It is legitimate only if erasing this state does not
destroy another task-relevant datum. If reset costs rho>0, the fixed-primary
model instead costs floor(T/2) min(c,rho). These changes prove that neither an
algebraic defect nor a larger invisible subgroup is an intrinsic welfare claim.

Conversely a split extension does not ensure that an arbitrary target section
and restricted physical actuators have zero cost. Even in H=C2 x C2 with q the
first coordinate, choose target r(0)=(0,0),r(1)=(1,1), only primary actuator
(1,0), and costed correction (0,1). The extension splits, but every swap needs
one correction. This is a counterexample to any claim that positive operational
cost characterizes nonsplitting. Targets, actuators, feedback and prices matter.

## Source comparison and limits (16 October 2026)

Primary body inspected: Makdesi, Girard and Fribourg, *Data-Driven Abstraction of
Monotone Systems*, L4DC/PMLR144 (2021),
<https://proceedings.mlr.press/v144/makdesi21a/makdesi21a.pdf>, introduction and
Sections 2--3. Their system is a possibly set-valued ordered-state controlled
dynamics learned from observed transitions. Proposition 5 gives its minimal
monotone simulating map; finite abstraction supports controller synthesis.
Our system is known, finite and reversible before reset, has prescribed exact
checkpoints and resource prices, and needs neither learning nor monotonicity.
This comparison establishes substantial symbolic-control prior art, not novelty
of the cost formula. A full comparison with feedback refinement and weighted
automata remains open.

Targeted recent MAS lead: *Memory-Based Resilient Control Against
Non-cooperation in Multi-agent Flocking*, AAMAS2024,
<https://www.ifaamas.org/Proceedings/aamas2024/pdfs/p2075.pdf>. Search-indexed
metadata identified a memory-based controller, but both full-PDF retrieval
attempts failed. No theorem comparison or non-overlap claim is made from that
metadata. This is a recorded access gap, not an examined proof.

The present results are deliberately small and likely application-level. A
stronger publishable direction would optimize a family of independently
motivated task targets under realistic partial state observation and shared
actuator constraints, rather than present AG-C1--C3 as a general theory of MAS.
No task-success requirement is called fairness and no software-agent welfare
interest is assumed. Exact checks enumerate actuator choices and corrective
paths independently of the closed-form expressions.

Reproduce: `python3 -m unittest discover -s experiments -p 'test_state_costs.py'`.
