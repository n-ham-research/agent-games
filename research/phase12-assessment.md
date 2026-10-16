# Phase 12 — contribution assessment and next decision

16 October 2026. Author Nicholas Ham. Full proofs are in phase12-compact.md and
phase12-verification.md; actual internal review is in ../reviews/AG-P12-REVIEW.md.
No candidate has originality clearance or external mathematical review.

## What survived the ambition filter

**Algorithm programme:** P12-C1 strengthens the Phase11 value-only obstruction
into an explicit-profile-output lower bound. Binary games with three supplied
action orbits, unit-range pure-payoff circuits and a unique rational exact Nash
profile encode counting in every sufficiently precise approximate equilibrium.
The precision length is polynomial, but epsilon itself is exponentially small.
The closest known counting-output reduction is Schoenebeck–Vadhan2006;
constant-orbit symmetrization is the candidate refinement, not the underlying
hardness mechanism. P12-C2 supplies a separate coNP semantic-certification
barrier. Neither asserts constant-epsilon hardness or bounded-local-width
hardness. A decomposable sum-product positive class gives only an XP(q)
corollary; bounded-degree FPT already follows from prior explicit-factor work.
We did not find a substantively new tractable class and stopped promoting this
positive branch. Polynomial conditional inference is useful, but insufficient
by itself to give a new fixed-parameter equilibrium algorithm.

**Verification programme:** V12-C is the strongest complete characterization.
For independent finite positive costs below B, no singleton success and a target
lottery over minimal successful coalitions or failure, two audit-event capacities
exactly characterize honest/obedient implementability. The per-report minimum
has a closed form: audit successful unselected agents first, then selected agents
when necessary. A constructive shutdown continuation attains every bound.
This yields the exact audit/welfare/reliability frontier by an explicit-table LP
for that architecture. V12-A gives the distinct arbitrary one-worker formula;
V12-B handles arbitrary finite types and guaranteed-success minimal coalitions.
These are audit frontiers without transfers; no general payments frontier was
proved. The main contribution is task-dependent endogenous punishment capacity,
with broad fixed-target necessity and a matching voluntary-action implementation.

## Closest prior and what might be additional

* Schoenebeck–Vadhan, EC2006 Theorem7.5 (long2005 Theorem7.11), already proves
  exponential-precision Boolean-circuit FindNash counting hardness with random
  input gadgets. The constant-q symmetrization must be compared further before
  novelty can be asserted. See compact note for primary URLs and locations.
* Ben-Porath–Dekel–Lipman2014 explicitly has reduced-form audit IC. One-worker
  V12-A is a close adaptation after proving its voluntary-action safety bound.
  Battaglini–Palfrey2024 supplies honest/obedient collective action. Li2020 is
  close conceptual limited-punishment prior; its full proof was NOT read.
  The exact no-singleton voluntary-action/reliability specialization merits
  comparison, but generic verification or mechanism LP ideas are not new.
* Friesen–Domingos2016 and Tewolde2025 make the conditional-inference/orbit
  positive route a method corollary. It is retained as a boundary, not a new
  theorem campaign. The real-algebraic source check is documented separately.

## Disproved or abandoned candidate extrapolations

1. Value-evaluation hardness automatically implies equilibrium-output hardness:
   false in Phase11; P12-C1 now has a valid independent extraction proof.
2. One-worker audit functional extends unchanged to redundant tasks: false;
   n3 threshold2 requires3/16 rather than the wrongly extrapolated3/4.
3. A lower-reliability prescribed target necessarily needs less auditing: false;
   success only on all-low types needs3/8, above guaranteed efficiency's3/16.
   Relaxing a constraint while optimizing over all targets still cannot worsen
   the optimum. The counterexample concerns two prescribed targets.
4. Linear arithmetic inference with bounded numerical values ensures polynomial
   rational bit output: false; an empty-scope repeated-squaring DAG produces
   2^(-2^L). Nonempty product scopes or an explicit bit-height promise matter.
5. Bounded-degree decomposable inference plus orbit polynomials supplies a major
   new FPT class: not established; explicit-table expansion already covers it.

## Applications with exact guarantees

* A coordinator handling a finite redundant-computation or coverage task can
  compute a minimal-coalition/failure target and a minimum-audit implementation
  from explicit cost/coalition tables. Agents can strategically report and
  refuse work. It requires independent known priors, all costs<B, perfect
  audits, private addressed recommendations, a trusted committed coordinator,
  and permissible shutdown after detected lying. It guarantees one honest/
  obedient equilibrium, not truthful behavior in every equilibrium.
* A circuit representation of a large interacting task system may be cheap at
  pure profiles yet computationally unsuitable for precise Nash calculation,
  even when its exact symmetry is certified. The lower bound rules out a
  uniform f(q)poly(L,log1/epsilon) algorithm unless circuit counting becomes
  polynomial; it does not predict ordinary-precision deployed-agent performance.
* The audit construction can be averaged over exact task/type relabelings when
  all constraints and audit prices are invariant. Central private addressing,
  random seeds and reports are implementation resources. No bounded-message
  decentralized realization or new communication lower bound was established.

## Next decision and publication structure

The verification programme produced the stronger positive result this phase:
a sharp necessary-and-sufficient characterization including failure. Its next
important gap is a naturally succinct task class admitting efficient frontier
optimization, or a theorem for unrestricted recommended active sets without
minimality. Allowing correlated types, noisy verification, no credible shutdown
or bounded payments may fundamentally change the answer. Do not pile on each
variation unless it changes the theorem or proves a barrier.

For algorithms, prioritize a genuinely new structured expected-payoff class
with both low orbit complexity and controllable algebraic degree; otherwise
pursue sharp symmetry-constrained lower bounds instead of routine new encodings.
Approximate symmetry and equilibrium selection remain in the Phase11 question
list; neither was disproved or abandoned.

Keep one conservative foundation manuscript for now, unchanged in length.
If further overlap review validates a substantial audit theorem, a dedicated
mechanism paper would be the more coherent first publication. A separate
algorithm paper needs more than the current constant-orbit refinement and XP
corollary. No new manuscript or repository is created, and no publication
readiness claim is made.
