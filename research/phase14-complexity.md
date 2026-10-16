# Phase 14 — symmetry, ordinary accuracy, and the price of zero error

16 October2026. Candidate development and exact checks for Nicholas Ham,
assisted by Codex. This branch sought a consequential accuracy boundary rather
than another orbit-polynomial corollary. The result below is a **pure-payoff
oracle separation**, not a stronger explicit-circuit complexity theorem.

The strongest candidate is P14-Q: even at constant Nash accuracy and constant
tolerance for violating symmetry, deterministic and zero-error oracle algorithms
need exponentially many queries in player-transitive binary games with just
two action orbits. Monte Carlo algorithms need only polynomially many. This
refines a classical query adversary to the highly symmetric class; the general
necessity of randomization in payoff-query equilibrium problems is established
prior, and novelty of this restriction remains provisional.

## 1. Exact model and the distinctions it protects

There are N=n+1 binary-action players indexed cyclically, n>=2. The algorithm
is given N, the common action labels, and the exact rotation generator
R:i->i+1 mod N, preserving labels. It accesses the game through a pure-profile
payoff oracle, with no circuit description or expectation oracle. Arbitrary
adaptive queries and unlimited computation between queries are allowed.
A query may return the **entire** utility vector, or even the stronger pointed
answer (u_i(0,s_-i),u_i(1,s_-i)) for every i at the queried profile. Proving the
bound for this stronger oracle also proves it for ordinary utility-vector queries.

Output is an explicit independent mixed profile with action-1 probabilities
p_0,...,p_n. Ordinary additive Nash regret must be at most epsilon for every
player. Define its orbit diameter

    diam(p)=max_i p_i-min_i p_i.

Exact cyclic invariance means diam=0. Requiring diam<=rho permits symmetry
error rho in the maximum absolute action-probability difference over **all**
cyclic group elements. This is not the same as error rho under the one supplied
generator: neighboring errors can accumulate over the cycle. In marginal-l1
norm the corresponding error has an extra factor2.

The two games in an indistinguishable transcript have the same supplied exact
cyclic subgroup and the same actual full action-orbit count2. We do **not**
supply a complete generator list for the full automorphism group, which can
differ between those games. No automorphism recognition is free.

All oracle answers in the construction are rational, have O(log N) bits, and
lie in [0,1]. There is no hidden infinite-precision information in an answer.
The hidden Boolean function is arbitrary: its complete table can be exponential.
The theorem concerns oracle query complexity as a function of N, not polynomial
runtime in the length of an explicit circuit that the algorithm can inspect.

## 2. P14-Q — constant-accuracy, robust-invariance query lower bound

**Theorem.** Fix epsilon=1/1024 and any 0<=rho<=1/64. Every deterministic
algorithm guaranteed to return an epsilon-Nash independent profile with
orbit diameter at most rho in every game of the following class must make
more than

    [1/(8N)] * [1/(5/8+rho)]^n

pure-profile queries on one fixed baseline game, up to integer rounding.
In particular rho=1/64 gives Omega((64/41)^n/N), and exact invariance gives
Omega((8/5)^n/N). The supplied group is player transitive; the actual full
typed automorphism group has exactly two action orbits.

The same lower bound holds for the expected query count of any randomized
**zero-error** algorithm that terminates almost surely on every input in the
class. In contrast, the Phase13 sampled-bisection benchmark returns an exactly
invariant epsilon-Nash profile with probability at least1-delta using a number
of pure queries polynomial in N,1/epsilon and log(1/delta).

### Game class and symmetry certificate

For each Boolean function F:{0,1}^n->{0,1}, write
z_i=(s_(i+1),...,s_(i+n)), and set

    alpha=1/8,       theta=1/2,
    D_i^F(z_i)=1/2 -(1/n)sum_j z_ij +alpha(F(z_i)-theta),
    u_i(0,z_i)=1/2,       u_i(1,z_i)=(1+D_i^F(z_i))/2.

Thus the actual conditional payoff advantage of action1 is D_i^F/2.
The original labels and the cyclic opponent ordering make rotation exactly
preserve utilities, with one action orbit for each label. Each action0 utility
slice is constant, whereas an action1 slice is not: its values on opponent
all-zero and all-one profiles differ by at least(1-alpha)/2>0. Every exact
typed automorphism therefore preserves action labels. Cyclic transitivity then
implies that even the full group's action-orbit count is exactly2. Utilities
are bounded because |D_i^F|<=1/2+alpha, and their rational lengths are logarithmic.

### Deterministic transcript adversary

Run the algorithm against F0 identically zero. Let S be all distinct n-bit
opponent tuples z_i that occur in its Q queried profiles, including all focal
players even if their actual action was0. Then |S|<=NQ. Set

    F1(z)=0 if z in S;   F1(z)=1 otherwise.

Both games return exactly the same answer at every queried profile, even under
the stronger oracle returning all action-deviation payoffs. Because the algorithm
is deterministic and the queries adaptive, induction on the identical transcript
shows that it chooses the same queries, stopping point, and output on F1.
This defines a single valid game F1 after the baseline transcript; the oracle
has not changed its answers inconsistently during execution.

The baseline has conditional D values

    D_i^0(p)=r -(1/n)sum_(j!=i)p_j,       r=7/16.

If all p_i<=3/8, then every D_i^0>=1/16 and every player's regret from not
switching to action1 is at least

    (1-p_i)D_i^0/2 >=1/64 >epsilon.

If all p_i>=1/2, every D_i^0<=-1/16 and regret toward action0 is at least
1/64>epsilon. Therefore any correct baseline output satisfies

    max p_i>3/8,       min p_i<1/2.

Combining these inequalities with diam(p)<=rho gives, for every player,

    3/8-rho <p_i<1/2+rho.

Any n-bit opponent profile consequently has probability at most
b^n under the independent output, where b=5/8+rho. This estimate applies to
each focal player's cyclicly ordered opponent law, even when the output is
only approximately invariant. If Q<=b^(-n)/(8N), then

    Pr(z_i in S)<=|S|b^n<=1/8,
    E F1(z_i)>=7/8             for every i.

For this same output in game F1,

    D_i^1(p)=D_i^0(p)+alpha E F1(z_i)
        > -1/16-rho +7/64
        = 3/64-rho >=1/32.

Every player's regret toward action1 is therefore greater than

    (1/2-rho)(3/64-rho)/2
        >=31/4096 >1/1024.

The identical output is invalid in F1, contradicting correctness. Hence a
correct deterministic algorithm cannot stop on F0 within the displayed query
budget. This proof makes no computational-complexity conjecture. QED.

### Zero-error randomized algorithms

For fixed n the family of Boolean F is finite. For each F a zero-error,
almost-surely terminating algorithm has a probability-one event of random tapes
on which it terminates and is correct. Intersect those events over all F; the
intersection still has probability one. Each tape in that event specifies a
deterministic algorithm correct and terminating on every F, so the preceding
baseline lower bound applies to it. Thus on F0 the randomized algorithm uses
more than the bound almost surely, and its expected query count is at least
that bound. The finite-family argument is what justifies this claim; merely
choosing an adversarial game after observing one random execution would not
prove a Monte Carlo lower bound.

### Interpretation

The comparison is **Monte Carlo versus zero error**, not an impossibility of
ordinary approximate equilibrium computation with randomness. The randomized
upper algorithm may fail with probability delta and samples fresh pure profiles;
it returns exactly invariant output on every execution. The lower bound allows
constant approximate invariance and proves that a universally correct stopping
certificate cannot generally be cheap in the oracle model.

The one-orbit case is immediately writable without any payoff queries: a
supplied exact action-transitive group forces uniform marginals, and exact
payoff transport makes every action a best response at that profile. Thus q2
is again the first possible action-orbit count for this separation. The theorem
does not say that every q2 game is difficult.

## 3. A near-full-table bound at inverse-polynomial accuracy

A related scaling gives a larger exponential base, with exactly invariant
output. It is retained as a precision check, not a second research programme.
Set alpha=1/(2n), theta=1/2 and epsilon_n=1/(256n) in the same cyclic game
class. Any deterministic algorithm correct on the class must make more than

    2^n/(8N)

queries on the F0 baseline. The zero-error extension holds as above; Monte
Carlo inverse-accuracy approximation still uses polynomially many queries.

**Proof.** The baseline invariant output has common probability p, its D is
r-p, and r=1/2-1/(4n). Correctness first forces p in(1/4,3/4): outside that
interval the regret is bounded below by a positive constant exceeding epsilon_n.
Within it, regret is at least |p-r|/8, so

    |p-r|<=8epsilon_n=1/(32n),
    1/2-9/(32n)<=p<=1/2-7/(32n)<1/2.

Consequently every opponent atom has probability at most

    (1-p)^n <=2^(-n)(1+9/(16n))^n
             <=2^(-n)exp(9/16)<2*2^(-n).

For Q<=2^n/(8N), the same F1 adversary has E_p F1>=3/4. Hence

    D^1(p)>=-1/(32n)+3/(8n)=11/(32n),
    regret >= D^1(p)/4 >=11/(128n)>epsilon_n.

The two transcripts are identical, giving the contradiction. QED.

## 4. What this does not establish

* **No new explicit-circuit constant-accuracy hardness.** In the oracle theorem,
  F1 can have a large table. A circuit detecting membership in S has size
  O(n|S|), which can itself be exponential when the query lower bound is
  saturated. Supplying its description would reveal information unavailable
  to the black-box algorithm. For polynomially many queried inputs, the
  adversary does yield a polynomial-size membership circuit, but that alone
  does not prove a lower bound against algorithms permitted to inspect circuits.
* **No unrestricted Nash or CE lower bound for this symmetric subclass.** The
  output requirement includes approximate interchangeability. Heterogeneous
  pure equilibria of the baseline do exist and are excluded by that requirement.
  Arbitrary correlated lotteries are not independent mixed profiles.
* **No lower bound with expected-payoff queries.** A single query at an invariant
  mixed profile can integrate many hidden Boolean values, defeating the counting
  of at most N exposed inputs per pure query.
* **No sparse-graph or bounded-arity circuit-free claim.** The arbitrary F term
  can depend on all cyclicly ordered opponents. Known explicit-factor orbit
  algorithms remain compatible with these results.
* **No generic near-symmetry discovery claim.** All tested games have exact
  certified rotation symmetry. The relaxed quantity concerns output strategy
  invariance, not approximation error in utilities or inferred automorphisms.

The failed extrapolation “Phase13 shows constant-accuracy counting hardness”
remains rejected. This phase changes the information model and establishes an
unconditional query separation instead. Those are different kinds of results.

## 5. Primary comparisons and novelty assessment

Sources actually accessed16October2026:

* Hart and Nisan, [*The Query Complexity of Correlated Equilibria*](https://math.huji.ac.il/~hart/papers/corr-com.pdf),
  author manuscript dated17May2013, TheoremsA/B, Section2 query model,
  Section3, and footnotes4–5 on PDF p3. Exponential deterministic approximate
  CE query lower bounds, the distinction from randomized approximation, and
  unqueried-payoff adversaries for Nash verification are already established.
  Their zero-error remark also predates this programme. P14-Q does not claim
  that general randomization separation or its transcript method is new; its
  candidate restriction is player transitivity, full action-orbit count2, and
  constant tolerance for orbit-diameter error. Its solution/output class differs
  from their arbitrary correlated output. The current construction uses a
  simpler sampling adversary precisely because invariant independent marginals
  retain mass on hidden inputs.
* Goldberg and Turchetta, [*Query Complexity of Approximate Equilibria in
  Anonymous Games*](https://arxiv.org/pdf/1412.6455), 31-page author version,
  Section2 query models and Section4/Proposition4.1 inspected, alongside its
  [13-page WINE2015 version](https://www.cs.ox.ac.uk/people/paul.goldberg/papers/WINE2015-anon-games.pdf).
  Their fully anonymous/symmetric utility representations permit querying by
  aggregate action counts; two-strategy symmetric games have logarithmic-query
  pure-equilibrium algorithms. Cyclic transitivity with arbitrary ordered
  Boolean dependence is not that full anonymity. Nor is their unrestricted
  pure equilibrium output the invariant mixed-output problem here. We do not
  claim their algorithms are contradicted by a q2 label.
* Schoenebeck–Vadhan and Tewolde et al. remain the primary explicit-circuit and
  action-orbit comparisons recorded in phases12–13. The old fine-precision
  counting reduction is not silently reused as a proof in this oracle model.

Targeted searches for player-transitive/symmetric payoff-query Nash results did
not locate this exact restricted separation. This is not novelty clearance.
The underlying oracle mean-estimation adversary is classical; contribution
significance depends on whether the symmetry/output restriction supplies a
useful boundary beyond the known general theory. At present this is a rigorous
and relevant supporting theorem, potentially a natural continuation of P13-Q,
not sufficient evidence for a separate algorithms manuscript.

A serious follow-up would ask whether comparable zero-error lower bounds survive
under a natural succinct structural promise that permits **using** the structure,
or whether specified distributed observations make orbit-diameter constraints
operationally necessary. Another orbit count alone will not settle either.

## 6. Exact evidence and remaining verification

Seven exact rational/integer checks in experiments/test_phase14_complexity.py
pass. They verify rotation equivariance and the constant-slice obstruction for
every three-input Boolean function; transcript equality even for the stronger
pointed oracle; the seen-input mass formula against full product enumeration;
constant-accuracy approximately invariant output profiles with valid transcript
budgets; strict slack in the robust constants; inverse-accuracy atom bounds;
and actual inverse-accuracy transcripts. The examples include asymmetric
marginals, not just an exactly symmetric output.

Finite checks validate identities and boundary arithmetic. They do not prove
an asymptotic decision-tree lower bound by enumeration or demonstrate a
stochastic success guarantee experimentally. The adaptive transcript and
zero-error arguments are the mathematical proofs above. No sampling algorithm
or general Nash solver is newly implemented in this branch.
