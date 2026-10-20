# Mathematical integrity review — Agent Games

20 October 2026. Reviewed current *Information, Incentives and Symmetric Equilibria in Finite Coordination Games*, compared with baseline d4d34eb and the canonical proof/ledger records. Internal OpenAI Codex review with inherited campaign context and access to previous reviews; not blinded, external peer review or author sign-off. No manuscript mathematics was edited by this reviewer.

## Verdict

Approve the editorial changes and the inspected hypothesis repair as mathematically faithful. The initial probability-domain omission described below has been repaired. The diff changes titles, labels, roadmap, acknowledgements, links and bibliographic metadata; it does not promote later research phases or change the main formulas/proofs. The subsequent explicit probability-domain clarification restores the canonical theorem scope. No new theorem-level defect was introduced by the polish.

The manuscript retains the intended screening, verification and orbit-method scope and its literature qualifications. It is ready for the separate publication-readiness pass; broader originality remains provisional.

## Repaired clarification: nondegenerate query prior

The initially reviewed `paper/sections/07-phase11.tex` introduced p only as the low-cost probability. The coordinating agent has now explicitly stated **0<p<1** before both the binary calibration and query results. This is already an assumption in canonical `research/phase11-information-resources.md`, AG-V1, which separately records degenerate cases.

Without it, R_*=(1-a^(n-1))/p is undefined at p=0, and the assertion that zero-error first best requires worst-case n-1 queries is false at p=0 or p=1: the cost is already known and no query is needed. The strict positivity of the calibration's mediation gap likewise requires the interior regime. The canonical proof is correct; this is an existing omission in the baseline manuscript's compressed assumptions, not a new research task or permission to broaden the theorem. I inspected the adopted repair: the interior assumption is explicit; the gap paragraph distinguishes boundary extensions; the query section states that p=0 or p=1 gives coincident costs almost surely and zero queries suffice. This resolves the identified issue without altering the interior formulas or proving a new result. No mathematical blocker from this review remains.

## Proof and semantic checks

- Allocation contrasts: the kernel necessity uses both t and -t in the unrestricted real linear domain. The manuscript preserves that hypothesis, offsets/domain warnings, fixed linear truthful measurements, and the distinction between measurement rank and message count. This is standard estimability applied to decisions, not a generic information theorem.
- Invariant equilibrium: the fixed product-simplex argument averages best responses at an invariant profile, rather than averaging arbitrary Nash equilibria. Cardinal transport preserves best responses. Pure equilibria, Nash product laws, lotteries over Nash profiles and induced CE laws remain distinct. The anonymous success bound uses conditionally IID actions and identical observations/code; labeled roles are explicitly another resource.
- Private costs: the binary BNE gains, local-policy welfare matrix, designated-worker equilibrium and informed obedient mediator comparison are consistent. Observing true costs is distinct from honest reports. The externally informed mediator is not advertised as a truthful cheap-talk implementation.
- Guaranteed success: the entire-strategy type mimicry requires independence, positive costs, type-independent feasible actions, and success at every supported type profile. These are stated. Flat interim activity gives a minimum-mean-coalition lower bound; a minimum coalition is inclusion-minimal because costs are positive and is therefore an attaining equilibrium. The almost-sure common realized minimizer criterion follows from a nonnegative difference with zero expectation. Weak implementation is distinguished from uniqueness/full implementation.
- Verification: under an interior iid binary prior and no other type-dependent signals, useful inspections each have gain p(1-p)(h-l). Their expected count is bounded by the truncated geometric sum. Mixture with no search attains the expected-budget frontier; capped search gives the hard-cap formula. Addressing, recommendation bits and other implementation resources are explicitly uncharged, not claimed free in every model.
- Local-factor action orbits: exact automorphism validity is a promise; explicit table/scope/coefficient/generator encodings are charged. Conditional payoff degree and complementary Nash equations are correct. Normalization rows can be deduplicated by player orbit to obtain O(q) constraints. Singleton substitution and explicit-table logarithmic arity yield the stated parameter bound. Real-algebraic sampling, coefficient/output bounds and algebraic solution encoding remain external ingredients. The same refinement applies to the prior normal-form method, so no unsupported separation is claimed.
- Succinct circuit boundary: rotations plus global complement act transitively on player-action pairs; the sole invariant product profile is uniform and Nash. Its expected value counts satisfying inputs. This proves exact payoff-evaluation hardness, with no inference of equilibrium-output or constant-precision regret hardness.
- Averaging and resources: an affine invariant objective on a compact convex invariant feasible set admits an invariant optimizer. The nonlinear counterexample, product-law distinction, orbit entropy minimum and integer fair-bit sampling condition are consistent. The three-point rejection sampler has expected cost 8/3 bits and unbounded worst case. None is presented as a generic distributed communication bound.
- Persistent state: checkpoint targets and available actuators, not abstract nonsplitting alone, determine costs. The forced alternating states give c floor(T/2); feedback/inverse actuation gives the stated zero-cost control despite nonsplitting. These are model-dependent finite-control applications.

## Attribution and remaining limits

The Nash invariant-existence baseline, Tewolde action-orbit method, real-algebraic sampling, optional inspection, screening and convex averaging retain their literature qualifications. The source comparison does not establish a new general equilibrium, revelation or search theorem. No later-phase result was silently moved into the foundation paper. Human review, publication-readiness checks and any unresolved originality assessment remain distinct from this internal mathematical review.

## Checks performed in this pass

`python3 -m unittest discover -s experiments`: all 244 tests passed in 5.629 seconds. This is a working-copy check, not fresh-copy, PDF layout or bibliography verification. The separate readiness pass owns those checks.
