# Phase 18 — a compact protected projection of the hard coverage family

16 October2026. Nicholas Ham; root Codex proof and exact implementation.
Complete candidate, originality provisional. This is a full closed-form
projection for a specified natural family, not inherited lower-bound reasoning.

## P18-P0: one payoff alone cannot have a large existential LP

For any finite game with a nonempty CE or conditional-margin polytope, its
projection onto ONE expected utility coordinate is a closed interval. It has
a two-inequality exact description. Thus a superpolynomial extension-complexity
lower bound is impossible in that output contract. The interval ENDPOINTS may
still be computationally hard to determine: P16-H already makes the lower
endpoint constant-gap NP-hard on binary-weight threshold inputs. Existence of
a small formulation is not efficient construction of its coefficients. This
is elementary convexity, not a new theorem; it prevents conflating size and
optimization in the fixed-projection question. Retaining success as a second
coordinate, or two worker utilities, changes the dimension and this argument
no longer supplies a uniform bound.

## P18-P: O(k) inequalities and O(k) support despite the full-region lower bound

Take the edge-cover task on K_(2m): an edge-worker covers its two endpoints;
success means all vertices covered. Give every worker benefit1 and cost
c in(0,1). Let J consist of k PAIRWISE DISJOINT protected edges, and suppose
m>=k+2. Fix0<=delta<=min(c,1-c). Private recommendations must be conditionally
delta-obedient. Write s for success and u_i for protected utility.

The EXACT projected region on the SAME retained coordinates (s,u_J) is

    0<=s<=1,
    max{s-c, delta*s/(c+delta)} <= u_i <= s    for every i in J.       (P)

Thus an O(k)-inequality direct rational formulation suffices. Every feasible
point has an explicitly recoverable law on at most2k+2 profiles, with polynomial
arithmetic, encoding and construction time in graph size, k and rational input
length. No LP solver or minimal-cover enumeration is needed for reconstruction.
Linear optimization and membership follow from the displayed compact LP.
At c1/2 the full-region extension-complexity bound P17-X applies simultaneously
for every delta<=1/2. A fixed matching of one or two protected edges therefore
loses that hard full geometry completely. The statement even permits k to grow
subject to m>=k+2. It does not address arbitrary incident protected sets.

### Necessity, independently of the task family

Let x_i be work probability. Work obedience gives

    (c+delta)x_i <= Pr(i works and is pivotal) <= s.

Also x_i<=1 and u_i=s-c x_i, while x_i>=0. Consequently
u_i>=s-c, u_i>=delta*s/(c+delta), and u_i<=s, proving (P).
These inequalities are the established positive-margin bound plus probability
bounds. The task-specific theorem is simultaneous sharpness and reconstruction,
not a new general inequality or a universal fixed-k representation theorem.

### Matching completion with a prescribed protected intersection

For any C subset J, there is a perfect matching M_C with M_C intersection J=C.
Remove the endpoints of C. At least four vertices remain since m>=k+2.
The forbidden remaining edges J\C form a matching. Start with any perfect
matching on remaining vertices. If it uses a forbidden edge (a,b), choose a
second matched edge (d,e) and replace both by (a,d),(b,e). Neither replacement
is forbidden, because each endpoint has at most its original paired endpoint
as a forbidden neighbor. This eliminates at least one forbidden edge without
introducing another. Repeat, then restore C. This is polynomial and explicit.
The vertex-disjointness of J is essential to this completion argument.

### Constructive simultaneous sufficiency

For any (P) point define x_i=(s-u_i)/c, so
0<=x_i<=min(1,s/(c+delta)). Let y_i=min(x_i,s).
Conditional on success, choose protected subset C with marginals y_i/s and
work exactly M_C. Conditional on failure, work only protected subset C with
marginals (x_i-y_i)/(1-s). Omit the branch when its probability is zero.
Both conditional marginal vectors lie in[0,1]^k.

Any vector of k subset marginals has a law on at most k+1 subsets: draw a
common uniform threshold U, include i iff U<=p_i, and use the rational intervals
between distinct p_i as the finite support. Thus the two branches together
use at most2k+2 profiles. Private recommendation hides the success/failure
branch and C; they are not additional public observations.

Every successful worker is pivotal because its coalition is a perfect matching.
Every failed coalition has at most k edges; adding ANY one edge covers at most
2k+2 vertices, strictly fewer than2m. Thus no abstainer can repair failure.
Every abstention signal therefore has conditional gain c>=delta. Unprotected
workers work only on successful matching profiles, with gain1-c>=delta.
For protected i, pivotal work mass is y_i and total work mass x_i, so its row
is y_i-(c+delta)x_i>=0: if x_i<=s this follows from c+delta<=1; otherwise it
follows from x_i<=s/(c+delta). This verifies EVERY worker and recommendation,
including zero-probability signals, and produces exactly s,u_J.

All probabilities are rational formulas in target data and c, with polynomial
bit length. Threshold decomposition, matching swaps and at most2k+2 profile
outputs are polynomial. A central sampler can use rational rejection; private
message delivery is an implementation resource. This is not a decentralized
protocol or a bound on arbitrary sampler circuits.

## Scope and counterexample to the naive small-graph extension

The size/slack assumption cannot simply be omitted from THIS construction.
On K4, protect edge(0,1) and mix the matching{(0,1),(2,3)} with failed{(0,1)},
each with probability1/2, at c1/2,delta0. The target payoff is0 at s1/2,
but edge(2,3)'s abstention signal reveals certain repairable failure and its
unconditional gain is-1/4. The proposed law is not CE. This is a concrete
failure of the construction outside its hypothesis, not a proof that no
alternative law can achieve every such target on that graph. An initially
tried1/4-success/1/4-failed/1/2-empty witness did NOT violate that row; the
exact check rejected it and the valid half/half witness is retained instead.

Incident protected edges need a different success-coupling argument: a perfect
matching cannot contain both. The experiment explicitly rejects them rather
than claiming an unproved extension. The full-region lower bound does not
pass automatically to any fixed-dimensional projection; (P) is direct evidence
of its collapse for specified retained roles, not a universal low-dimensional
compression theorem. Constant dimension alone gives no such theorem for
arbitrary rational polytopes.

## Comparison and independent checks

The work-obedience inequality already appears in P13-R/P16 robustness work.
Matching completion and threshold coupling are elementary established tools;
no new matching, convexity or sampling principle is asserted. The candidate
increment is the exact simultaneous projected region and small explicit-law
recovery on the SAME natural full-region-hard family. Exact priority remains
unresolved; it is a task-specific structural theorem rather than a new universal
fixed-projection classification. Primary matching-face source and Rothvoss
version are recorded in phase17-originality.md.

Five exact tests cover every protected subset through k3, matching completion,
all workers' rows and prescribed utilities on a rational success/cost/margin
and TWO-target grid, support bound, threshold marginals, the repair witness
and rejection of incident protection. No LP optimizer is implemented. These
finite checks supplement the constructive general proof, not establish novelty.
