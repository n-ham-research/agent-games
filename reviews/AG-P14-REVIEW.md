# Phase 14 — actual independent reconstruction and repairs

16 October2026. Three separate same-family instances developed continuation,
complexity and contextual-interchangeability branches. They reciprocally attacked
proofs after initial separate development. Root read all three notes, reconstructed
the protected-region/endpoint, adversarial-query and coupling arguments, checked
examples, retrieved primary Cavaliere text and integrated the research decision.
This is internal AI review, not external peer review or author sign-off.

## Main proofs and actual review

* **P14-A/B:** complexity and interchangeability branches independently checked
  deletion margins, protected-payoff equality, canonical columns, restoration
  constraints, FPT(k) construction, endpoint IC, monotonic envelope and attaining
  laws. The later algorithmic corollary received an additional explicit review.
  Root confirmed the projection claim preserves reliability and protected
  utilities, not the complete utility vector or arbitrary welfare objectives.
* **P14-Q:** both other branches reconstructed the adaptive transcript adversary,
  constants, max-atom estimate, approximate orbit diameter, finite-family random-
  tape intersection and inverse-accuracy scaling. No defect found. Exactly which
  oracle answers are available, and the absence of a circuit description, are
  part of the theorem. The claim is not an unrestricted randomized lower bound.
* **P14-I:** continuation independently reconstructed joint-label lumpability,
  seed-posterior realization and TV-to-regret conversion; root separately
  checked all-deviation quantifiers, observation histories and resource scope.
  Two assumption clarifications were necessary, as described below.

## Corrections and nearby false strengthenings

The interchangeability reviewer found that utilities were not explicitly required
to factor through retained records; this is now a hypothesis. Root required
matching the full initial joint law with context state/private inputs, preserving
correlations; equal component marginals alone would be insufficient. Both repairs
are in the statement and proof. These are material modeling assumptions, not
claims that ordinary bisimulation automatically supplies a strategy transport.

The continuation proof retains a delta-versus-deleted-cost bound. Its necessity
is demonstrated by a previously always-working redundant worker who acquires
an insufficient-margin abstention signal after deletion. The private-information
example defeats a cellwise use of a global singleton-success bound. Neither
counterexample invalidates the final scoped statements.

Cavaliere's February2000 primary text was actually found and inspected by root
and continuation reviewer, including rendered equations. Printed claims in that
working text are not imported wholesale: an exact two-player calculation
contradicts its count-only characterization as written, and unsuccessful pure
NE must be excluded from an efficiency assertion. Final2001 text was not
retrieved, so no assertion about its corrected claims or equations is made.
See phase14-literature.md, including the version SHA256.

## Finite checks and completeness limits

111 exact standard-library tests pass:82 retained +10 continuation +7 complexity
+9 interchangeability +3 root source/initialization checks.

Continuation checks exercise all166 nonconstant four-agent monotone tasks on
supplied payoff laws/protected subsets, endpoint/margin families and the canonical
LP constructor's rows. They do not enumerate every continuous CE or independently
solve every projected LP. The normal-form proof establishes the general equality.
No generic LP optimizer was executed; standard rational LP is the invoked
algorithmic ingredient in the FPT theorem, with explicit construction costs.

Complexity tests validate rational oracle answers/transcripts, small hidden
functions and algebraic probability/regret inequalities. They do not empirically
prove an exponential asymptotic lower bound; the adversary proof does. The
zero-error extension is a finite-family measure-one argument, not inferred from
random experimental runs.

Interchangeability checks include128 pure profile/context pairs in one two-round
two-player model, all its unilateral pure deviations, independent private seeds
against pure/mixed opponents, genuine four-state-to-two-state aggregation, and
information, permissions, memory and sharp TV/regret examples. They are not
exhaustive over all state machines or contexts. Root's initialization example
shows why joint, not marginal, initialization is required.

## Novelty and scope decision

Closest-source comparisons narrow the candidate increments. P14-A's structural
protected projection/FPT consequence is strongest; P14-B and the restricted
oracle separation merit further overlap review. Contextual preservation is an
established-method synthesis, not a new universal interchangeability theorem.
No Phase14 result is promoted into the manuscript. No companion changes,
external contact, new repository or submission. Final clean-copy/build/provenance
and repository checks are recorded in the handover.
