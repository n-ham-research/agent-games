# Phase 15: memory and communication certificates for substitution

Author: Nicholas Ham; candidate development assisted by Codex. This branch
extends P14-I's resource limitation, not its novelty claims. Finite horizon,
finite rational kernels and explicit interfaces throughout. No companion edits.

## Model and budget

A controller has at most K persistent modes. At round t it receives its current
private observation o and uses a rational kernel C_t(a,m'|m,o). Time t is a free
external clock; remembered observations/actions are NOT free. Fresh independent
randomness is permitted, persistent random seeds count as modes, and a context
cannot read controller memory. Read-only program/transition-table size, working
memory, random bits, actions and messages are separate costs. A single action
from an N-letter alphabet costs ceil(log2 N) output bits if communication is
being charged. The finite-context semantics, retained utility factorization,
joint initial-law matching and absence of hidden side channels are as in P14-I.
M modes require ceil(log2 M) storage bits in an explicit binary encoding.
Thus an exponential mode requirement can mean only linear growth in bits;
R3 below requires k bits, not exponentially many bits. No bound on controller
modes silently gives a bound on program size or CPU.

## P15-R1: finite interface adapters and deviation budgets

Suppose two component interfaces have the same action permissions and output
semantics. For each player a supplied deterministic causal observation adapter
has d_i states and converts each replacement observation stream into an original
observation stream. Its update can use the player's own action and time, but
cannot read others' private information. Assume a finite product-state relation
certifies that, for every joint action and context input, the joint retained
output/decoded-observation/next-related-state kernel agrees exactly, and that
initial laws agree jointly with all context private inputs. This is a P14-I
joint-row certificate on the component-adapter product, not merely equality
under a default controller. Illegal actions must remain illegal both ways.

Every original K_i-mode controller then compiles to a replacement controller
with at most d_i K_i modes, preserving the complete retained law against all
opponents and contexts for which their corresponding adapters are installed.
Proof: store (adapter state, original mode), decode the observation, and run
one original update. The assumed product-row equality gives induction for
every controller profile. It applies anew to every unilateral deviation.
Checking a supplied relation and explicit rational tables is polynomial in
the product-table encoding, which includes the joint action/observation sizes.
Finding a smallest adapter is not claimed efficient.

To infer a bounded-deviation equilibrium guarantee requires a REVERSE adapter.
Let it have e_i modes and the same all-profile certificate. For a transported
baseline profile sigma, every replacement deviation using L_i modes pulls back
to an original deviation using at most e_i L_i modes. Consequently

    Regret_replacement,L_i(transport(sigma))
        <= Regret_original,e_i L_i(sigma).

Here baseline payoffs and the fixed opponents' transported behavior agree;
the reverse adapter is used for the deviator alone, with compatibility of the
mixed original/replacement interface composition included in the certificate.
Equivalently one may require the row certificate separately for each subset
of replaced players. This avoids assuming that a whole-profile correspondence
also handles mixed implementations. Forward compilation bounds baseline
memory by d_i K_i; reverse compilation controls ALL deviations, rather than
only deviations that happen to be forward images. With state-neutral adapters
(d_i=e_i=1) the same mode budgets and exact bounded-regret/NE values are
preserved. For larger adapters the displayed asymmetric budgets are essential;
there is no automatic same-K NE theorem. Resource labels must include any
adapter tool calls/messages; permissions cannot be fabricated by compilation.

The construction is classical transducer composition plus the P14-I all-action
certificate. Its contribution here is an explicit, checkable budget contract
and the reverse-deviation requirement, not a new bisimulation theorem.

## P15-R2: exact one-cut memory characterization

A passive prefix supplies a private finite input x in X, and then disappears.
After a cut no observations correlated with x, no communication and no
persistent randomness outside controller memory are available. A terminal
response y in Y must have conditional channel P(y|x). At the cut there are M
controller modes. The exact minimum possible M is the nonnegative rank of the
row-stochastic matrix P.

Indeed every implementation factors P=ED, where E(m|x) is the distribution
of cut memory and D(y|m) is the terminal stochastic decoder. Conversely every
row-stochastic factorization implements the channel. Any nonnegative
factorization P=UV with M terms can be normalized: discard zero-sum rows of V,
put s_m=sum_y V_my, D_my=V_my/s_m and E_xm=U_xm s_m. Since P has row sum one,
E also has row sum one. Thus the stochastic and nonnegative factorization
minimums agree. This proof applies to real kernels; with rational-only
implementations use rational nonnegative rank instead. A supplied rational
factorization is an exact finite checkable certificate. No polynomial-time
minimal-factorization algorithm or equality of real/rational ranks is assumed.
This is a direct application of classical nonnegative factorization, not a new
matrix-rank theorem. Ordinary rank is a valid weaker lower bound, not generally
an exact substitute.

The distinction from ordinary rank already matters for the rational channel

    P = (1/2) [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]].

Its ordinary rank is three, but four cut modes are necessary. In a nonnegative
rank-one summand the support is a rectangle. No such rectangle contained in
P's support can include two diagonal entries: for every distinct i,j, at least
one cross entry P_ij or P_ji is zero. All four positive diagonal entries need
separate summands. Four row-selector modes attain the bound. This is the
classical support/fooling-set argument, not a new rank separation.

The cut theorem characterizes a terminal response CHANNEL, not all interactive
strategies. A factorization of one on-policy channel does not prove strategic
substitution. R1 still requires all-action row certificates and reverse
compilation. Terminal output generation needs fresh randomness but no memory
beyond a selected cut mode; representing a long sequential output may require
additional modes and is not included without a separate construction.

## P15-R3: sharp exponential memory/communication separation

Let X be uniform on N=2^k strings. A context retains X. At a passive setup
round both interfaces privately reveal X to the player, with NO action or
external write available. At a later terminal decision the rich interface
reveals X again, while the sparse interface emits a blank. The only action is
a response Y in X; utility is 1[Y=X]. There are no intervening actions or
signals, and all randomization after the cut is independent of X conditional
on the stored mode. The compared retained task record is (X,Y), not the unequal raw private
observation streams; adapters translate those streams. Both interfaces have
exactly the same perfect-recall information: rich repeats information already received. Nevertheless the
rich interface has a one-mode optimal controller; sparse requires N modes
for exact optimality. The identity response matrix has ordinary rank N,
so R2 proves the exact lower bound. Storing X attains it.

More sharply, a sparse M-mode controller has success at most min(1,M/N), even
with stochastic encoding and decoding. Its success is

    (1/N) sum_m sum_x E(m|x) D(x|m)
       <= (1/N) sum_m max_x E(m|x) <= M/N.

For M<=N assign M-1 inputs distinct modes and send all remaining inputs to
the last mode; decode one representative per mode. Exactly M inputs succeed,
so the bound is attained. It is also the best retained-record TV approximation
to the rich law (X,Y=X): conditional on X, TV from the point mass is the
conditional error, hence total TV is one minus success. Exact strategic
preservation at equal mode budgets therefore fails despite perfect-recall
strategic equivalence. A one-player K-bounded optimum is a K-bounded NE, but
for K<=N its payoff changes from 1 to K/N; unrestricted regret of the sparse
K-mode optimum is 1-K/N (with both quantities saturating when K>=N). This is not a claim that every transported poor controller
has a profitable K-mode deviation: restricted equilibrium and unrestricted
regret differ.

If a trusted setup helper may retain a message with Q possible values outside
the controller and reveal it only at the terminal decision, replace M by MQ:
condition on the pair (mode,message). Success is at most min(1,MQ/N).
Conversely label min(N,MQ) selected inputs by distinct pairs, send/store their
labels, and decode those representatives. Thus the exact resource frontier is
MQ>=N, or log2 M+log2 Q>=k. Communication can replace memory only because the
helper retains information; a message that vanishes before the cut contributes
nothing. No later communication with a party remembering X is allowed. Setup
receives k input bits and terminal output costs k bits in BOTH interfaces;
the comparison isolates persistent storage, not total communication or CPU.
Rich rereading is itself a resource and must be permissioned/charged if a
system counts repeated private read access. We make that architectural trade
explicit, rather than treating observations as a free universal service.

## Scope, failures and comparison targets

A behavioral/perfect-recall equivalence certificate is insufficient for equal
finite-memory budgets. Nor does recording effort labels bound actual runtime.
A huge response alphabet is explicitly charged; the lower bound survives
stochastic controllers, but this example is a one-cut information storage
problem, not a new finite-state synthesis complexity result. For sequential
bit responses with free visible past outputs, the terminal decoder can use
those outputs as external memory, so the proof's no-external-write condition
cannot be dropped. Similarly correlated initial seeds carrying X are an
unmodeled storage channel unless counted.

R1 makes resource preservation constructive but sufficient only. R2 gives an
exact resource characterization for a restricted useful cut architecture.
R3 shows that logarithmic-bit context information can require exponentially
many controller modes after substitution and supplies the exact compensating
communication frontier. The substantive deliverable is a precise separation
and budget contract; originality remains provisional and the elementary coding
and automata ingredients are established.

## Primary-source comparison and verification

[Cohen–Rothblum (1993), author-hosted full 20-page article](https://lab.rockefeller.edu/cohenje/PDFs/211CohenRothblumLAA1993.pdf)
defines nonnegative rank and investigates nonnegative factorizations. Its
Theorem 3.2 states exactly that a stochastic matrix has nonnegative rank q
iff it factors through q states with stochastic factors, using the same row
normalization proof. Thus the algebraic content of R2 is explicitly PRIOR;
only its one-cut agent-budget interpretation is supplied here. The real/rational distinction is substantive:
[Chistikov et al., Nonnegative Matrix Factorization Requires Irrationality,
primary arXiv text](https://arxiv.org/pdf/1605.06848) gives a rational matrix
whose minimum real factorization cannot be attained with rational factors.
Thus this branch does not erase the field restriction when charging a rational
implementation. No result here solves nonnegative-factorization synthesis.

[Bose–Ibsen-Jensen–Totzke, Bounded-Memory Strategies in Partial-Information
Games, 2024 author-hosted full text](https://cgi.csc.liv.ac.uk/~patrick/assets/pdf/BIT2024.pdf)
was inspected at its strategy definitions and bounded-equilibrium results.
It explicitly treats private memory modes, bounded strategies and bounded
Nash deviations in partial-information stochastic games; Section 8.2 also
warns that exposing encoded arena state changes required strategic memory.
Its infinite-duration algorithmic results are not claimed here. Our finite
one-cut example isolates an observation-access/storage trade rather than
establishing the first importance of memory to equilibrium. P14's primary
Gutierrez et al. and Alur et al. comparisons continue to apply to R1: strategic
semantics and alternating/bisimulation certificates are established prior.

Eight exact tests check normalization, a rank-three channel needing four modes, identity rank through N=9, the whole
M,Q frontier on small grids, exhaustive small deterministic encoders/decoders,
all three-input/two-mode half-grid stochastic encoders/decoders, adapter action
transport for all tiny deterministic response policies, and rejection of
invalid channel certificates. The tiny adapter check does not certify every
context: the general statement is the product-state proof above. Tests do not
establish novelty. No independent external review has occurred.

## Reciprocal review record

The resource branch independently reconstructed root's P15-S3-C coverage flow
proof. Conditioning on the final capped count vector (rather than only the
covered set) makes each worker's pivotal and repair events recoverable from
its action and that vector. Source-terminal flow decomposition restores an
actual joint recommendation distribution. The 3^d final vectors times 3^d
prefix states give the stated O(n9^d) size, and no protected-thinning margin
restriction is needed because actions are not deleted. No defect found; this
was proof reconstruction, not an independent implementation or novelty review.

The information branch independently reconstructed R1–R3 and found no
substantive defect under the reverse/mixed-interface certificate, rational
factor restriction and no-external-storage cut architecture. It caught one
minor saturation omission: the prose K/N payoff and 1-K/N regret now explicitly
restrict K<=N; the formulas and code already used min(1,K/N). Its review also
checked the four-cycle support argument. This is internal AI proof review, not
external verification or a novelty certification.

The succinct branch's weighted-threshold SUBSETSUM conversion was separately
attacked from its complete reduction description. Even item weights and an
odd quota make the protected weight-one worker pivotal exactly at a subset
sum equal to the target. The supplied three-coalition YES recommendation law
satisfies every obedience row, including the singleton worker's tight abstain
row. In NO instances the protected work row and singleton abstain row give
the stated exact payoff identity and constant gap, including the two-row
unconditional approximation loss. No defect found in this reduction; this
review does not certify novelty or the separate weighted-flow construction.

After the complete `phase15-succinct.md` draft became available, this branch
also independently reconstructed P15-S1–S4. The terminal-conditioned summary
DAG preserves labelled parallel action edges; finite path decomposition yields
an actual joint law with exactly the displayed utility/success/obedience
statistics. Its O(nM^2) size, rational-support reconstruction and expected
sampling-cost claims are justified in the explicit generated LP encoding.
Weighted-threshold coefficients correctly use total-minus-own-weight for work
and total-plus-own-weight for abstention. The zero-payoff NP certificate uses
only O(n) supported profiles, with polynomial rational bit length from the
few-row full-profile LP. The constant-gap and approximate-output precision
statements distinguish optimization from finding an arbitrary CE. No defect
found in these proofs; no additional source priority claim was independently
established by this reciprocal review.
