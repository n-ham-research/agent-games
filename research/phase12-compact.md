# Phase 12 — Compact representations: equilibrium output and certification

16 October 2026. Author Nicholas Ham; candidate development and exact checks
assisted by Codex. All games below are finite, complete information, independent
mixed Nash games. Internal AI review is not external mathematical review.
Novelty is provisional. The main result is a constant-orbit refinement of
Schoenebeck–Vadhan2006 and a stronger obstruction than local AG-H1:
**three supplied action orbits suffice for counting to be recoverable from every
sufficiently precise approximate equilibrium profile.** Cheap pure-payoff
circuits do not imply cheap equilibrium output, even with known exact symmetry.
A tractable sum-product class is recorded as an established-method corollary,
not promoted as a new general algorithm.

## 1. Representation and output convention

Players and their binary actions are explicitly listed. A rational payoff
circuit takes one bit per player and produces that player's exact pure payoff;
its gates comprise Boolean gates, addition and multiplication by explicitly
encoded rational constants. In the reductions below every payoff lies in [0,1],
pure evaluation is polynomial in input length L, and output numerators and
denominators have polynomial length. This restriction excludes unbounded
arithmetic repeated squaring hidden behind an alleged unit-cost evaluator.
Typed generators are explicit permutations of players and bijections of each
player's actions. Their action on profiles follows the repository convention.
The parameter q counts orbits of disjoint player-action pairs under the supplied
subgroup, not necessarily under the full game automorphism group.

An epsilon-Nash output is an explicit list of rational marginal probabilities,
with each player's expected unilateral regret at most epsilon. Accuracy is
binary encoded, so polynomial dependence on log(1/epsilon) is a strong promise.
No value oracle, circuit solving, sampling or obedience is supplied for free.
The theorem also rules out an algorithm restricted to exactly invariant output,
since it applies to every epsilon-equilibrium, invariant or otherwise.

## 2. P12-C1 — Constant-action-orbit equilibrium-output counting obstruction

**Statement.** From a Boolean circuit F on n>=2 inputs and an integer
0<=K<2^n, one can construct in polynomial time a (2n+1)-player binary game,
with rational payoff circuits valued in [0,1], and two explicitly certified
exact typed generators whose group has q=3, such that every epsilon-Nash
profile with

    epsilon <= 1 / [2^(n+1) (8n+8)]

identifies whether #SAT(F)>K simply by testing whether a distinguished player's
action-1 probability exceeds 1/2. Consequently a deterministic algorithm with
runtime f(q) poly(L,log(1/epsilon)) for these circuit inputs would count circuit
satisfying assignments in polynomial time, using O(n) calls. Equivalently this
is a #P-hardness result under polynomial-time Turing reductions for the profile
search oracle, and a single-call counting-threshold reduction. No claim of
constant-epsilon hardness, PPAD membership, or player transitivity is made.

### Construction

Players A_0,...,A_(n-1), B_0,...,B_(n-1), D have binary actions a_j,b_j,d.
The first 2n players play disjoint unit-range matching pennies:

    u_Aj = 1[a_j=b_j],       u_Bj = 1[a_j!=b_j].

Write z=(a,b). Let R rotate both n-tuples by one place. Let T be the typed
quarter-turn acting on profiles as

    T(a,b) = (1-b,a).

In player-action notation, T sends (A_j,c) to (B_j,c) and (B_j,c) to
(A_j,1-c). Thus T^4=1. R and T commute and generate an explicitly described
C_n x C_4 action on paired players. Both fix D and its two actions. Define

    H_F(z) = (1/(4n)) sum_(j=0)^(n-1) sum_(t=0)^3
                       F(first_n_coordinates(R^j T^t z)),
    theta = (K+1/2)/2^n,
    u_D(z,0)=theta,          u_D(z,1)=H_F(z).

Duplicating F at most 4n times gives polynomial circuit size. R and T preserve
the whole game: matching becomes mismatching when T swaps the corresponding
roles, and H_F is the group average. Their action on paired player-actions is
transitive: rotations reach all indices; T and T^2 reach the two roles and two
actions. The two D actions are singleton orbits. Hence q=3 exactly for this
supplied group. The game has two player orbits, so this does not assert full
player symmetry.

### Proof for every approximate equilibrium

Let p_j,q_j be the independent action-1 probabilities of A_j,B_j. Put
x=2p_j-1 and y=2q_j-1. Their regrets are exactly

    r_Aj=(|y|-xy)/2,       r_Bj=(|x|+xy)/2,
    r_Aj+r_Bj=|p_j-1/2|+|q_j-1/2|.

If every regret is at most epsilon, summing gives

    sum_j (|p_j-1/2|+|q_j-1/2|) <= 2n epsilon.

Couple each independent Bernoulli marginal to a fair Bernoulli and use a union
bound. The total variation distance of the paired players' product law from
uniform is at most 2n epsilon. Because 0<=H_F<=1,

    | E H_F - #SAT(F)/2^n | <= 2n epsilon.

The equality at the uniform law holds because every transformed first-n-tuple
is itself uniform. Let g=2^(-n-1). The number #SAT(F) is integral, so the fair-law
payoff difference #SAT(F)/2^n-theta has absolute value at least g. Thus its sign
is positive iff #SAT(F)>K, and the actual payoff difference at any approximate
equilibrium has the same sign and absolute value at least g-2n epsilon.
The chosen epsilon ensures

    (g-2n epsilon)/2 > epsilon.

If D assigned probability at least 1/2 to the inferior action, its regret would
exceed epsilon. Therefore its probability of action 1 is strictly greater than
1/2 on a yes instance and strictly less than 1/2 on a no instance. This proves
the extraction claim for all valid outputs, without computing expected payoffs
or checking regret at extraction time. Binary search for #SAT(F) requires
O(n) threshold calls; all have polynomial binary accuracy length. QED.

**Existence and exact structure.** Each pair has the unique fair Nash profile,
so all pairs are fair at every exact NE. The decision player's strict fair-law
payoff comparison forces one pure action. Hence the constructed game actually
has a unique exact independent Nash profile. It is invariant, entirely
rational, and cheap to write; selecting its last bit is hard. This avoids the
Phase11 error of treating value hardness at an already known equilibrium as
profile-search hardness. This construction is neither an equilibrium-output
size lower bound nor an irrationality obstruction.

**What would defeat the reduction?** An expected-payoff arithmetic circuit is a
stronger input than a pure-payoff circuit: the decision player's conditional
expectation at the fair profile already performs the counting. If efficiently
constructible decomposable circuits for these expectations were assumed, the
reduction would no longer be cheap. Low-precision algorithms polynomial in
1/epsilon are compatible with this theorem. An algorithm permitted to return
an opaque symbolic instruction such as “compare E H_F to theta” has not returned
the specified explicit mixed profile.

## 3. P12-C2 — Semantic typed-symmetry checking remains hard

**Statement.** Checking whether a supplied typed permutation is an exact
rational payoff-circuit automorphism is coNP-complete, even on games already
equipped with the two certified generators above and base q=3.

**Proof.** Use the same construction with theta=0 and ask whether V, fixing all
paired players and flipping D's two actions, is an additional automorphism.
The paired utilities ignore D. The condition at D is exactly H_F(z)=0 for
every pure z. Since every summand is nonnegative and the identity transform is
included, this happens iff F is unsatisfiable: if F(a)=1, any b supplies z with
H_F(z)>=1/(4n)>0. Conversely unsatisfiability gives H_F identically zero.
This reduces circuit UNSAT to automorphism checking. Non-automorphism has a
polynomial witness: a player and a pure profile with unequal transported
payoffs, evaluated exactly in polynomial time. QED.

The question is whether the candidate V is valid, not whether a supplied q=2
group can be assumed valid. On yes instances the enlarged group has q=2; on
no instances V is not a symmetry. This distinction matters in parameterized
promise problems. No general lower bound for graph-automorphism discovery,
explicit local-table certification, or every tractable representation follows.

## 4. A genuine compact positive class, with the actual bound

A **player-decomposable rational sum-product payoff DAG** has univariate
rational leaves f(s_i), rational constant leaves, rational weighted sums, and
products whose children have pairwise disjoint, nonempty syntactic player
scopes. Scope is the union of descendant leaf-player indices, even when a
function is accidentally constant. Constant multiplication is encoded by an
explicit rational sum-edge weight, not an empty-scope repeated-squaring DAG.
All player/action lists, DAG gates, weights and leaf tables count in L.
A supplied group is promised exact or supplied with the sufficient syntactic
certificate below. This class permits global high-arity product interactions
using O(n) leaves, exponentially smaller than one explicit payoff table.

### P12-C3 — Conditional expectation and orbit expansion corollary

For such input, every pointed conditional payoff admits a constructible
arithmetic expectation DAG with O(L) arithmetic work per point (i,a).
After substituting q action-orbit variables, a dense coefficient expansion has
at most binomial(n+q,q) monomials and polynomial coefficient bit length.
Consequently invariant exact Nash computation has an L^{O(q)} bit runtime by
the established orbit-polynomial/real-algebraic method, subject to the exact
algebraic sampling reference qualification below. Rational epsilon-Nash output
adds polynomial dependence on log(1/epsilon). This is **XP in q**, not a proved
FPT(q) theorem. If all payoff scopes have size at most d, it gives
f(q,d) poly(L,log(1/epsilon)); however in this binary-action model table expansion costs at most 2^d per
root and already gives FPT(q,d) by Phase11. Thus this restricted case is
not the substantial new result sought.

**Proof.** To condition on i=a, replace its leaf tables by their entries at a.
For every other leaf f(s_j), substitute sum_b f(b) x_(orbit(j,b)). Expectations
pass through weighted sums by linearity and through products because the
children use disjoint independent players, including after conditioning. This
is the sum-product theorem specialized to strategic independent marginals;
normalizing probabilistic weights is unnecessary for this algebraic identity.
The resulting polynomial has total degree at most n and at most q variables.
Sparse polynomial addition and convolution at each gate constructs its dense
expansion with at most binomial(n+q,q) coefficients, hence L^{O(q)} operations.

To justify bit complexity, unfold a single monomial derivation of a gate.
Products partition nonempty player scopes, so there are at most n terminal
branches, each with at most L gates along it. Any input denominator or
numerator is therefore used at most O(nL) times in one monomial derivation.
A common denominator formed from all explicitly encoded denominators to that
power has polynomial bit length. The number of derivations is at most
L^{O(nL)}, whose logarithm is polynomial in L. Thus summing derivations adds
only polynomially many coefficient bits, including with signed weights.
The same argument bounds rational evaluation bit length when marginal inputs
have prescribed bit length. Apply the Phase11 complementarity system to the
expanded conditional polynomials. Its at most 2q variables, O(q) constraints
and degree at most n+1 yield (qn)^{O(q)} poly(L) real-algebraic complexity,
absorbed into L^{O(q)}. Output rounding uses the existing marginal-l1 argument.
QED.

**Why the nonempty condition is real.** Set c_0=1/2 and c_(t+1)=c_t*c_t using a
DAG. Every product is vacuously decomposable if empty scopes are permitted;
all intermediate values lie in [0,1]; size is O(t). Yet c_t=2^(-2^t) needs an
explicit rational denominator with 2^t+1 bits. Thus linear arithmetic inference
and bounded numeric magnitude do not by themselves prove polynomial bit or
output complexity. Our representation excludes this example. Folding a whole
constant circuit is permitted only when its explicit rational expansion is
charged to L. This caveat is a representation-level counterexample, not a
claim that conventional normalized SPN algorithms are incorrect.

### Sufficient symmetry certificate

For each typed generator supply a permutation of all DAG nodes taking each
player's root to the image player's root. It must preserve gate kind, ordered
or unordered product incidence as specified, weighted sum incidence with exact
rational weights, and map every leaf table f(s_i) to its typed transport on the
image player's actions. Checking these conditions and player/action bijections
is polynomial in L. Induction from leaves proves semantic payoff equivariance;
then generator validity proves validity of the generated group. Node-map
existence/discovery is not assumed free. This certificate is sufficient, not
complete: semantically equal but syntactically different DAGs may have no such
node permutation. Cancellation-based symmetries such as Phase11 offsetting
factors need not be certified by it. P12-C2 explains why a universal semantic
fallback for arbitrary circuits is unrealistic without complexity collapse.

### What remains open

Compact conditional expectations avoid the general-circuit obstruction, but
the polynomial degree can grow with player count and naive monomial expansion
costs L^{O(q)}. We have not proved f(q) poly(L,log(1/epsilon)) for these global
sum-product inputs. We have not established that bounded graphical width alone
restores that bound. Polynomial-time inference is insufficient to assert cheap
real-algebraic solution without controlling degree and output. An exact
parameterized classification of structured expectation DAGs, perhaps by
interaction width plus orbit multiplicities, is the substantive next question;
merely announcing the leaf-substitution algorithm would repackage prior art.

## 5. Primary-source comparison and exact access record

Sources actually accessed on 16 October 2026:

* **Closest prior:** Schoenebeck and Vadhan, [*The Computational Complexity of
  Nash Equilibria in Concisely Represented Games*](https://people.seas.harvard.edu/~salil/research/nash-ec.pdf),
  EC2006, Theorem7.5 and proof on PDF p9; also [49-page author version](https://schoeneb.people.si.umich.edu/papers/ConciseNash.pdf),
  Theorem7.11, PDF pp33–34. They already prove counting-oracle hardness of
  exponentially accurate binary circuit-game equilibrium output, using
  matching-pennies input players and a decision player comparing a circuit
  with a constant. Thus the counting-to-profile mechanism is established
  prior, not an invention here. P12-C1 adds the explicit 4n-term group
  symmetrization and quarter-turn certificate forcing **q=3** while retaining
  extraction from every ordinary epsilon-NE. The paper sections inspected
  do not supply this orbit-count refinement; that is a limited comparison,
  not proof that it is new anywhere in the literature. The explicit
  arbitrary-threshold and perturbation bounds here are local proofs.
* Daskalakis, Fabrikant and Papadimitriou, [*The Game World is Flat: The
  Complexity of Nash Equilibria in Succinct Games*](https://people.csail.mit.edu/costis/papers/dfp06.pdf),
  12-page author manuscript, Sections2–3, Theorems1–2. Its reduction assumes a
  polynomial-length bounded division-free straight-line program for EXPECTED
  UTILITY, not just a polynomial pure-profile evaluator. This is the closest
  conceptual prior to the distinction used here. No claim is made that our
  circuit class automatically satisfies that hypothesis. Its displayed
  approximation definition is well-supported, whereas our proof uses ordinary
  additive expected regret; the latter is explicitly proved above.
* Friesen and Domingos, [*The Sum-Product Theorem: A Foundation for Learning
  Tractable Models*](https://proceedings.mlr.press/v48/friesen16.pdf), ICML2016,
  Definition3 and Theorem1, PDF p2. Disjoint-scope product decomposability gives
  linear arithmetic summation. P12-C3's conditional inference is a direct
  specialization; the bit-height restriction and orbit expansion are explicit
  representation bookkeeping, not a new inference theorem.
* Poon and Domingos, [*Sum-Product Networks: A New Deep Architecture*](https://homes.cs.washington.edu/~pedrod/papers/uai11a.pdf),
  UAI2011, Definition4/Theorems1–2 on PDF pp3–4, inspected. Compact tractable
  inference predates this programme; we use the cleaner decomposable version
  above and do not equate arbitrary payoff circuits with valid SPNs.
* Tewolde et al., AAAI2025, action-orbit Theorem9, as read in Phase11. Our
  constant-q lower bound requires general pure-payoff circuit input; it does
  not contradict their explicit normal-form algorithm or its precision bound.
* Goldberg and Papadimitriou, *Reducibility Among Equilibrium Problems*, direct
  author PDF fetch failed; ECCC TR05-090 landing page was accessible. We do not
  count its full body as inspected. Matching-pennies probability gadgets and
  succinct Nash reductions are long-established; the small supplied orbit count
  of the present reduction requires further targeted novelty checking.

**Original real-algebraic source: partial progress, no false closure.**
Renegar, *On the Computational Complexity and Geometry of the First-order
Theory of the Reals, Part I*, JSC13 (1992)255–299, DOI
[10.1016/S0747-7171(10)80003-3](https://doi.org/10.1016/S0747-7171(10)80003-3),
was actually inspected through its [public full-text article OCR](https://www.researchgate.net/publication/200018947_On_the_computational_complexity_and_geometry_of_the_first-order_theory_of_the_reals_Part_I_Introduction_Preliminaries_The_geometry_of_semi-algebraic_sets_The_decision_problem_for_the_existential_theor),
printed pp260–264, Theorems1.1–1.2 and the approximation paragraph. Decision
and quantifier-elimination bit bounds are stated there; OCR garbles some
exponents. The approximation paragraph refers to a separate Renegar1992a.
This Part-I access does not independently verify exact sample-output encoding.
Subsequently root located the BPR original-book text on a third-party mirror;
see phase12-source-audit.md for the updated exact-output/bit-complexity audit.
This branch separately inspected the stated output and encoding locations.
Mirror access is distinguished from publisher or author-host access.
The [Cornell Part-I record](https://ecommons.cornell.edu/entities/publication/b88c9a71-4b84-4649-a83a-f28a2f6f2c08)
explicitly says its original TR853 is missing. Author-hosted BPR book links
again failed. No missing body is counted as read; P12-C1/C2 and the
representation identities do not depend on this sampling black box.

## 6. Checks and contribution classification

Eight exact Fraction/integer checks in experiments/test_phase12_compact.py
verify: every Boolean truth table on n2 and asymmetric n3 functions under
every pure profile and both typed generators; q3 orbit sizes for n2,...,8; uniform expectation/count equality;
matching-pennies regret identity on a rational grid; worst-case precision
inequalities through n31; the candidate action-flip equivalence to UNSAT on all
n2 truth tables; signed decomposable conditional inference against explicit
enumeration; rejection of overlapping products and empty-scope products.
Enumeration is validation, not a general Nash solver or empirical asymptotic
complexity proof. The supplied local tests are finite exact consistency checks;
the polynomial-time circuit construction, counting reduction, and bit bounds
are proved above.

Classifications: P12-C1 is a proved constant-orbit refinement of the
Schoenebeck–Vadhan counting-output construction, strengthening local AG-H1 from
value to actual profile output; novelty of the q3 refinement is provisional. P12-C2 is a straightforward
semantic-circuit-equivalence specialization, not claimed novel. P12-C3 is an
established inference/orbit-method corollary with explicit limits. The empty-
scope bit-height example is elementary. No broad tractability theorem beyond
these assumptions, deployed agent behavior, or decentralized mechanism is
claimed.

Independent internal review: the verification branch reconstructed C1/C2 and
C3's scope/bit-height reasoning and found no mathematical defect. It specifically
checked quarter-turn typed utility preservation, the linear regret identity and
TV precision extraction, UNSAT averaging, and nonempty-scope parse-tree bounds.
This is same-family AI adversarial checking, not external peer review. The root
review and source comparison are separate.
