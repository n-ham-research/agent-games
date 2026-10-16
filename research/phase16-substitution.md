# Phase 16: synthesizing sequential observation adapters with budgets

Nicholas Ham; Codex-assisted finite candidate analysis. This branch seeks an
operational certificate beyond the one-cut example. The observer and bounded-
synthesis algorithms below are established constructions specialized to strategic
substitution, not new automata theory. Novelty remains provisional.

## Finite model, timing and permitted resources

There is a common finite latent system X, horizon H (explicit/unary), initial
support I, rational transition kernels T_t(x'|x,a,e), finite joint actions a,
and context input e. A context may adapt to its own information. The original
interface gives player i deterministic observation g_i,t(x); the replacement
gives h_i,t(x). All probabilities/initial correlations and physical outputs,
utilities and permissions are unchanged. Each round: observe, choose action,
transition. A controller has K modes and a joint randomized action/mode-update
kernel; current observation and external time are free, remembered history is
not. Random seeds, logs, tools or messages persisting across rounds count as
storage. Complete retained initial law includes context private inputs.

We restrict to observation refinement h_i,t=f_i,t(g_i,t), with a supplied
memoryless f. Thus original policies can simulate replacement policies without
extra modes. An adapter must reconstruct g from the h history and remembered
own actions, for EVERY physically possible path and every joint action/context
input, not merely under a proposed equilibrium. Its d modes and transition
table are explicit; it can read own action only. Raw observation labels are
translated; compared retained outcomes are common task/action/resource records.
If permissions depend on observations, legal menus must agree after decoding;
otherwise the following theorem does not apply. No adapter may add tool rights.

## P16-R1: complete observer synthesis for this interface class

At the start of a round maintain a support B subset X of possible latent states.
On receiving sparse observation o, filter C={x in B:h_t(x)=o}. If nonempty,
all g_t(x) for x in C must coincide; output that value. After own action b,
update B to the union of supports T_t(.|x,a,e) over x in C, all joint a whose
own coordinate is b, and every allowed e. Initial B=I. Only reachable filtered
sets need checking. If any reachable C has two different rich observations,
no deterministic causal adapter exists; if none does, the subset observer is
an adapter with at most 2^|X| modes. Time is external so the tables may differ
by round. Enumeration costs polynomial in the explicit transition/support
encoding times H2^|X|, not polynomial in log H or the succinct arena encoding.

Proof: by induction B is exactly the set of states realizable by some path
with the player's sparse-observation/own-action history. Union over hidden
opponent actions and context choices is essential. If a filtered set has two
rich labels, the SAME available history has two possible required outputs,
so no deterministic adapter can work on both. Conversely monochromaticity
makes the rich observation a well-defined function of available history;
the displayed update computes that function. No numerical posterior is needed
because the requirement is pathwise exact for all positive-support paths.
For arbitrary contexts use a support over the explicit product arena whenever
context restrictions create additional state constraints. Union over all e is
exact for the stated unrestricted-input context class; it may be conservative
for a smaller class. Probability-zero transitions are excluded exactly.

Randomization cannot rescue impossible exact decoding: each compatible path
requires output one with probability one, so two different required labels
at the same history are incompatible. This is zero-error reconstruction,
not approximate statistical filtering or probabilistic bisimulation.

## P16-R2: bounded-memory adapter synthesis is an explicit finite certificate

For a proposed bound d (unary), let m in {0,...,d-1}, fixed initial mode0.
Unknown deterministic tables are lambda_t(m,o) (rich observation) and
Delta_t(m,o,b) (next mode). Introduce Boolean reachability R_t(m,x).
Require:

- R_0(0,x) for every x in I.
- R_t(m,x) implies lambda_t(m,h_t(x))=g_t(x).
- For every positive-support transition x --a,e--> x', R_t(m,x) implies
  R_{t+1}(Delta_t(m,h_t(x),a_i),x').

Use one-hot variables for finite table entries. These are finite propositional
clauses after expansion; their number is polynomial in H,d and explicit arena
and alphabet sizes. Reachability variables may overapproximate actual reachable
pairs; this is harmless because every actual pair is forced by initialization
and closure, and output correctness holds on the superset. Conversely an
actual d-mode adapter supplies exact reachable pairs satisfying the clauses.
Thus the certificate is necessary AND sufficient for deterministic d-mode
pathwise adapters in this model. Guessing its tables and checking reachability
is polynomial; no NP-hardness or polynomial synthesis claim is inferred.
SAT solving, exhaustive table enumeration, or specialized search can find a
certificate; this branch implements enumeration only for tiny tests, not an
industrial SAT solver. Controller rational probabilities are unchanged by
this deterministic compilation. Requiring time-independent tables changes
synthesis constraints and can require additional clock modes.

## Strategic budget consequence, including every deviation

Apply a valid adapter independently for each replaced player. Coupling the
same physical latent path and random action choices proves equality of common
retained outcome laws for every original policy profile compiled through the
adapters. All subsets of replaced players are allowed because reconstruction
holds for all joint actions, independently of the other players' interfaces.
An original K_i-mode baseline controller compiles to at most d_i K_i modes.

For ANY replacement L_i-mode deviation, the rich-interface player can feed its
controller f(g) and implement it with exactly L_i modes. Against fixed compiled
opponents, its physical action/outcome law agrees with that deviation. Hence

    Regret_replacement,L_i(compiled sigma)
        <= Regret_original,L_i(sigma).

The baseline uses d_i K_i modes, but deviation budgets stay L_i. In particular,
an original equilibrium against deviations of budget d_i K_i yields an
equilibrium of the compiled profile under those budgets; an original NE only
against K_i modes does NOT automatically do so. An unrestricted NE transfers
to an unrestricted NE with the displayed finite baseline implementation.
This is an operational asymmetry: refinement gives a state-neutral reverse
compiler, while reconstructing the removed information may cost memory.
It is a specialized realization guarantee, not a new general equilibrium-
preservation theorem under ordinary bisimulation.

The compiled transition table has at most d_i K_i times the input/controller
alphabet factors. Runtime per round is one adapter lookup plus one controller
lookup in an explicit RAM table model. Stored mode bits are at most
ceil(log2 d_i)+ceil(log2 K_i); table storage and random sampling cost are charged
separately. No messages/tool calls are added. An observer that needs access to
another player's action violates the certificate even if a centralized monitor
could reconstruct the rich observation.

## P16-R3: sequential binary-output exponential-mode requirement

Choose n>=1. A hidden context samples index J in {1,...,n} with full support.
Over n input rounds the player receives independent fair bits W_1,...,W_n.
There are no actions or external writes before the terminal round. The latent
state stores only J, the latest input bit, and the bit W_J once encountered;
there are at most 4n states per layer, with time-dependent transition tables.
At the terminal round sparse observation is J and the rich observation is
(J,W_J). Before then rich and sparse both reveal the current input bit.
The only terminal action is a BIT Y, utility 1[Y=W_J]. Thus there is no
exponentially large output alphabet, and the only extra terminal input is
log2 n index bits. The rich optimal controller uses one mode, whereas sparse
requires 2^n modes to attain success one. With perfect recall the information
is identical: the queried bit was observed already.

For distinct input words w,v pick a coordinate j where they differ. At the
cut before J is revealed, their sparse controller-state supports must be
disjoint: any shared mode with positive probability, followed by the common
observation J=j, would need to output both different bits with probability one.
This proves 2^n modes even for stochastic exact controllers with fresh private
randomness. The argument uses that before revealing J the observed bit stream
and all controller randomness are independent of J; every word is compatible
with every J. Storing the whole word attains the bound and the observer
construction finds an adapter. The cut has n-bit storage complexity, NOT
exponentially many bits. Hidden environmental storage is O(log n) bits, so
small arena state alone does not imply a small decoder/controller.

If an external trusted retained message has Q possible values and controller
memory M, the same disjoint-support argument gives MQ>=2^n for exact success;
partitioning the word index into a memory label and a message label attains
this whenever enough pairs exist AND the permitted setup interface can compute
and retain those labels (for example a trusted online store with an explicitly
charged update interface). This is a cut-storage attainability statement, not
a free full-word helper or a proof that every pair encoding can be formed by
an arbitrarily restricted streaming writer. No message from a party retaining the word
may arrive after seeing J unless charged separately. Allowing that request/
response channel changes the problem: sending J then the desired bit uses
only O(log n) communication plus the helper's n-bit persistent storage.
All observations/tool permissions and helper storage are therefore architectural
resources, not invisible aids.

These are classical sequential INDEX/observer/coding arguments. They identify
a sharp failure of same-budget substitution even for terminal binary actions
and an explicitly small time-varying latent arena. They do not prove a new
communication lower bound, bounded-synthesis hardness, or approximate-error
INDEX theorem. No broad new publication claim is supported by this branch.

## Primary comparison, stopping assessment and exact checks

[Schewe–Finkbeiner, Bounded Synthesis (2007), full author PDF](https://intranet.csc.liv.ac.uk/~sven/atva07b.pdf)
was inspected at §§5–6, Theorems 5–8. It already synthesizes bounded finite-state
implementations through finite constraint systems, with locality restrictions
for distributed information. Its setting is substantially broader than our
finite-horizon output-reconstruction safety problem. R2 is a transparent
specialization of established bounded synthesis; neither SAT synthesis nor
local-information consistency is claimed new.

[Klauck, One-way communication complexity and the Nečiporuk lower bound on
formula size, primary author arXiv text](https://arxiv.org/pdf/cs/0111062)
was inspected at §2.2's communication model and §6's INDEX/random-access coding
comparison. Communication/INDEX lower bounds are established prior; R3 uses
the elementary exact distinguishability argument in an explicit sequential
controller arena, without claiming the first random-access storage bound.
The earlier Bose et al. bounded-memory game comparison remains relevant.

The observer method is standard partial-observation state estimation. An
attempt to retrieve the original Purdue immediate-observability PDF failed;
a PMC detectability page returned a challenge page, so neither was treated as
an inspected full source. The primary-author [Yin2019 survey, arXiv1903.11413v1](https://arxiv.org/pdf/1903.11413)
was obtained and inspected at §3: its current-state estimate definition and
subset observer construction are direct prior for R1. This is an inspected
primary-author survey, not a claimed first historical source or an inspected
copy of every original paper it cites.

**Stopping assessment.** This branch now has an implementable certificate,
a complete observer decision method for a restricted sensor-replacement class,
and a matching sequential lower bound with binary terminal actions. These are
useful engineering specifications but largely direct combinations of existing
observer, bounded-synthesis and INDEX methods. There is currently no basis for
a separate original-mathematics manuscript on this branch. The next serious
new question would concern quantitative approximate reconstruction with exact
budgeted deviation transport, or efficient synthesis for a structurally useful
arena class; neither is asserted here. Merely renaming the observer as strategic
bisimulation would add no contribution.

Nine exact tests pass: observer replay, one- versus two-mode exhaustive bounded
synthesis, impossible ambiguous histories, hidden-context support, a default-
action-only false certificate, the explicit 4n-state INDEX arena and its 2^n terminal observer supports,
all residual query signatures and matching bit
implementation through n=8, pairwise distinguishing suffixes, and all tiny
Boolean terminal policies. These are finite corroborations, not a SAT solver
implementation or independent certification of the general theorem.


## Independent review record

The disclosure branch independently reconstructed R1's support induction,
R2's reachability-certificate equivalence, the mixed-interface dK forward/L
reverse regret guarantee, and R3's stochastic disjoint-support argument. No
substantive defect found. It requested precision about forming a trusted
message label; the attainment statement now explicitly requires a permitted
charged setup/update interface and does not assume a free helper retaining
the full word. This is internal AI review, not external certification.

## Reciprocal proof reviews

The resource branch independently reconstructed the homogeneous-cost and
positive-margin extension in `phase16-hardness-audit.md`. The law supported
on M and {i} gives target-work and backstop-abstention gains exactly delta,
while every occurring item recommendation gains 1/2. For every law, the
backstop row gives s>=1/2+delta+(1/2-delta)x_r; hence every target payoff is
at least delta. The YES law attains this minimum. In NO instances parity
makes target work strictly dominated, so x_i=0 and payoff is at least
1/2+delta. The known backstop-only profile ensures feasibility at all margins
through 1/2. Numerical encoding, few-row NP witnesses and approximate-row
slack arguments were separately reconstructed. No defect found. This is a
proof-level review, not an independent novelty clearance or fresh human audit.

Root's `phase16-tractability.md` was also independently attacked. On distinct
read-once leaves, the AND/OR downward sensitivity equations give the actual
unilateral switching indicator. Gate triple scopes form a junction tree,
so separator consistency yields an actual law, retaining all CE/output terms.
Positive-state recursive selection plus subtraction preserves every gate/
unary consistency equation and kills an entry each time; thus sparse rational
reconstruction and the linear-size bound hold. Edge-disjoint supplied
series/parallel decomposition correctly instantiates the formula. The
repeated-worker counterexample identifies why success-only tree structure
does not suffice. No proof defect found; the exact priority of this task-class
application remains unestablished here.

The disclosure branch's P16-D1/D2 was independently reconstructed as well:
its volunteer slack is v/5, baseline tightness forces zero-sum cells, and the
anchor count converts maximal deterministic guessing into 3-PARTITION. Pair-
transport decomposition yields the claimed optimal randomized guessing law;
its privacy/rank-two prior limitation is explicit. No defect found.

The disclosure reviewer independently ran the nine substitution tests using
`python3 -m unittest discover -s experiments -p test_phase16_substitution.py -v`.
All passed. This discovery invocation is the supported test command; the
standalone experiment imports are not packaged for module-style unittest.
