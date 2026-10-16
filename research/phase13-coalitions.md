# Phase 13 — credible punishment, private correlation and coalition purification

16 October2026. Candidate development for Nicholas Ham; verification-branch
Codex proofs and exact checks. This is an exploratory shift from audit formulas
to the geometry of obedient continuation play. Originality is unresolved.

## Model and distinctions

A finite monotone successful-coalition family F is nonempty and excludes empty.
Agents choose binary work simultaneously. At active set A, utility is
B*1[A in F]-c_i*1[i in A], with common benefit B>0 and known costs 0<c_i<B.
A mediator privately recommends each agent only its own action. A correlated
equilibrium (CE) resists each action-contingent unilateral deviation. No reports,
transfers, audits, repetitions or private types are included in these theorems.
A full private-cost auditing mechanism cannot import these conclusions without
checking its continuation information and report incentives separately.

Let S={j:{j} in F} be singleton-capable agents. The rest are R. An agent can
unilaterally guarantee B-c_i if i in S and zero otherwise. This security bound
need not equal the lowest payoff jointly obedient continuations can attain.
With S nonempty literal shutdown is not an equilibrium: a singleton agent
would repair it. Private recommendations can nevertheless conceal failure and
support much harsher continuation payoffs than public lotteries over pure NE.

## P13-P1 — success-preserving deletion preserves CE and improves all utilities

Let pi be any CE. For each realized A choose, possibly randomly, T subset A
with 1[T in F]=1[A in F]. The pushforward law is again CE, has exactly the
same success probability, and weakly increases every agent's expected utility.
This holds for all positive costs, even without c_i<B.

Proof. Use unconditional obedience margins. For a worker i the margin against
abstaining is B*1[i pivotal in A]-c_i. If i remains selected, deleting other
workers without changing success can only increase its pivotality, by monotonicity.
If i is deleted, it was nonpivotal: T subset A\{i} has the same success as A.
Thus the old worker-obedience contribution was -c_i; removing that contribution
increases its worker margin. Its new abstention-obedience contribution is +c_i,
since adding i to T cannot change success (T subset T+i subset A). For an agent
absent from both A and T, the abstention margin is
c_i-B*(1[A+i in F]-1[A in F]); monotonicity and preserved success show that
this margin cannot decrease. Sum these pointwise comparisons. Utilities weakly
increase because success is preserved and work is only removed. QED.

Consequently every CE admits a Pareto-improving CE supported on inclusion-minimal
successful coalitions and empty failure: minimize every successful A and delete
all work on unsuccessful A. This is a structural justification for that support
restriction when optimizing complete-information CE welfare/reliability with
positive work costs. It does NOT justify the restriction when minimizing an
agent's punishment payoff, or when preserving strategic-report incentives.
The deletion rule can require the full coalition/task description; no cheap
compact-input minimization or decentralized implementation is assumed.

## P13-P2 — exact zero-payoff CE criterion for arbitrary monotone tasks

Fix agent i. If S is empty, all-abstain is CE and gives i zero. If i in S, no
CE gives i zero because volunteering secures B-c_i>0. Suppose S nonempty and
i not in S. Define

    t0=1-min_{j in S} c_j/B,
    r0=(B-c_i)*t0/c_i,
    K={j not in S union {i}: {i,j} in F}.

Let M_i be inclusion-minimal successful coalitions containing i. Then i has
payoff zero in some CE if and only if all of the following hold:

1. M_i is nonempty and t0<=c_i/B.
2. For every j in K, B*r0<=c_j.
3. Either M_i contains a coalition of size at least three, OR

       sum_{j in K} [1-B*r0/c_j]/t0 >= 1.

If M_i contains no large coalition, it consists exactly of pairs {i,j}, j in K.
The empty sum cannot meet condition3. These conditions are exact finite
rational inequalities after the relevant minimal-coalition information is known.
They are not a polynomial-time oracle-discovery claim for arbitrary monotone F.

**Necessity.** Write s=Pr(success), x_i=Pr(i works), and p_i=Pr(i pivotal).
Work obedience gives B*p_i>=c_i*x_i; pivotality implies p_i<=s. If i's utility
B*s-c_i*x_i is zero, both bounds are equalities. Thus EVERY successful supported
coalition contains pivotal i. In particular all singleton-capable agents always
abstain. Their deviation to always volunteering gives s>=t0. Also x_i=B*s/c_i
<=1, so t0<=c_i/B. Since i works on every success, its failed-work probability
is r=(B-c_i)*s/c_i.

For each pair-repairer j in K, every failed i-work profile omits j, and j could
repair it. Its abstention obedience therefore implies

    B*r <= c_j*(1-x_j).

From each successful profile choose a minimal successful subset containing i;
such a subset must contain i because i was pivotal. Let v_j be the conditional
probability it contains j. Then x_j>=s*v_j. The preceding inequalities yield

    B*(B-c_i)*s/c_i <= c_j*(1-s*v_j).

These constraints only become easier when s decreases to t0. Thus
B*r0<=c_j and v_j<=[1-B*r0/c_j]/t0. A minimal coalition containing a pair-repairer
j must be exactly {i,j}; otherwise that pair is a proper successful subset.
Hence if no large minimal coalition exists, the v_j sum to one and condition3
follows. If a large coalition exists, it contains no pair-repairer. QED necessity.

**Construction.** If a large T in M_i exists, take it with conditional probability
one. Otherwise choose partners j with weights v_j>=0 summing to one, below
the displayed capacities; the conditions guarantee such weights exist. Use
private recommendations with distribution

    minimal T containing i: total probability t0, with chosen conditional law;
    failed coalition {i}: probability r0;
    empty failure: probability 1-t0-r0.

These probabilities are nonnegative by condition1. Agent i's work signal pools
pivotal success with failed work and makes its work obedience an equality;
its utility is exactly zero. Its abstention signal is empty failure, which it
cannot repair alone. A selected partner in a minimal T is pivotal and strictly
obeys. A non-singleton abstainer can repair {i} only if it is a pair-repairer;
its obedience is exactly the capacity inequality. All singleton agents always
abstain, and cannot profit by completing at failure rate 1-t0, by definition of
t0. All other abstainers cannot change failure alone. This proves CE. QED.

**Three-branch consequence.** Continuation punishment is not determined by
unilateral security alone. A non-singleton agent has security zero, but may
or may not admit a zero CE payoff depending on singleton costs, own cost,
pair-repairer costs and available minimal coalition sizes. Complete-information
private correlation, rather than literal shutdown, is the decisive resource.

## Examples and boundaries

Take B=2 and minimal successful coalitions {s} and {i,j,k}. Let c_s=1,
c_i=3/2 and c_j,c_k in (0,2). Recommend {i,j,k} with probability1/2,
{i} with probability1/6, and empty with probability1/3. Agent i has zero CE
payoff. An even simpler alternative uses success probability3/4 and {i} failure
probability1/4, with i always working. In contrast any CE supported only on
minimal successful coalitions or empty failure has

    u_i >= (B-c_i)*s >= (B-c_i)*t0 = 1/4.

Thus P13-P1's Pareto improvement may destroy the punishment we need. Publicly
revealing the entire chosen action profile is different again: every profile
would have to be a pure NE. Since S is nonempty, those profiles are exactly
minimal successful coalitions. The minimum public-lottery payoff for relevant
i is B-c_i=1/2, greater than the private CE payoff zero.

Root independently found the smaller pair example B=1, minimal {s} and {i,k},
c_s=9/10,c_i=4/5,c_k=1/2. Probabilities {i,k}:1/5,{i}:1/20,empty:3/4 form CE
with i payoff zero. P13-P2 also supplies a different zero-payoff witness using
t0=1/10,r0=1/40. If c_s=1/10 instead, t0=9/10>c_i/B: zero punishment is
impossible, despite the same unilateral security value zero and task technology.

**Private-cost report IC does not survive arbitrary purification.** Let n=2,
B=2, iid costs {1/2,3/2} equiprobable, one-worker success. Reports are ignored;
recommend {0} and {1} each with probability9/20 and both with probability1/10.
For every type the work signal has pivotal probability9/11>3/4, so obeying is
optimal; reports cannot affect the outcome. Purify the both-worker event by
keeping the cheapest REPORTED worker, uniformly on ties. Truth-path action
obedience survives, but interim workloads become x(low)=21/40 and
x(high)=19/40. A low type can claim high to save expected cost1/40. Therefore
pointwise success-preserving deletion need not preserve honest implementation.
Purifying independently of reports would preserve this particular report IC,
but cannot be assumed to achieve the desired type-sensitive allocation.

## Significance, prior comparison and remaining uncertainty

P13-P1 and P13-P2 are proved candidates, not novelty-cleared theorems. Their
purpose is a broader information/incentive distinction: private correlation can
use apparently wasteful failed work to make low continuation payoffs credible,
while the same waste is dispensable for Pareto-efficient complete-information
coordination. This identifies precisely why welfare and punishment optimizations
need different support restrictions. It does not yet solve arbitrary private-cost
mechanism design or make the coordinator unnecessary.

Primary sources accessed16October2026:
- Hart and Mas-Colell, *A Simple Adaptive Procedure Leading to Correlated
  Equilibrium*, Econometrica68(5),2000,1127–1150, author text
  https://ma.huji.ac.il/hart/papers/adapt0.pdf , Section2 definition inspected.
  Private recommendation obedience and CE linear inequalities are established;
  no novelty is claimed for them, or for the general fact that CE exceeds public
  lotteries over NE. The present task-specific purification and zero-payoff
  criterion require further targeted comparison.
- Ostroy and Song, *Correlated Equilibrium and the Pricing of Public Goods*,
  Autumn2006 primary working paper https://repository.essex.ac.uk/8905/1/dp616.pdf ,
  introduction and Section3.2/Theorem3 inspected. It studies worst weighted
  CE payoffs through LP duality in general normal-form games, using a public-good
  interpretation of joint outcomes. Thus optimizing low CE payoffs is old; our
  exact monotone-task support/repairer structure is the candidate extra content.
  No claim that its general duality itself yields novelty here.
- Kerman and Tenev, *Information design for weighted voting*, Economic Theory,
  accepted2024, DOI10.1007/s00199-024-01599-0, author-copyright full article
  https://d-nb.info/1350115320/34 , Lemma1 and AppendixC proof PDF pp10,32
  inspected. Their private persuasion problem already reduces recommendation
  support to minimal winning coalitions and empty failure by deleting losing
  recommendations and excess winning votes. This is close geometric prior for
  P13-P1's thinning operation, though their state-dependent voter persuasion and
  our costly-work CE have different obedience constraints. Do not advertise the
  minimal-support simplification itself as an unprecedented principle.
- Cavaliere, *Coordination and the Provision of Discrete Public Goods by
  Correlated Equilibria*, JPET3(3),2001,235–255,
  https://doi.org/10.1111/1097-3923.00065 . Primary publisher issue metadata
  confirmed, but article fetch failed and no full primary copy was located.
  This is an important unresolved direct-prior check. Secondary summaries were
  search leads only, not a basis for claiming its theorem content was read.
- Phase12's Battaglini–Palfrey/Ben-Porath–Dekel–Lipman/Li comparisons remain
  relevant to mechanism incentives. These continuation results do not establish
  a new audit theorem or resolve their remaining source-access gaps.

Further work: characterize positive minimum CE payoffs beyond the zero face;
understand which continuation information structures retain these witnesses
when only the liar's cost is verified; optimize mechanisms with credible private
punishment while checking report AND recommendation deviations; investigate
robustness because the zero-payoff construction makes the punished agent
indifferent. No strict-obedience or approximate-rationality guarantee is claimed.
The singleton-cost threshold shows that properties of the whole continuation,
not just a deviator's security value, are indispensable.

## Exact validation limits

Seven Fraction tests validate the construction on every166 nonconstant
four-agent monotone task and16 rational cost vectors; every returned witness
satisfies all action-contingent CE inequalities and gives the targeted payoff0.
They also check pointwise purification and utility improvements, public/private
witnesses, the pair-repairer obstruction, and the reporting-IC counterexample.
These tests independently check feasibility of positive certificates; no general
CE optimizer or computational necessity oracle was run. Necessity is established
by the pivotality/repairer proof above, not by enumeration alone.
