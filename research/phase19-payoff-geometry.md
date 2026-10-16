# Phase 19 — ordinary-CE payoff geometry: a closure and a stopped lead

Status: proved elementary compact-lifting observation; no positive natural payoff-space separation established. AI derivation and exact checks, not external review or novelty clearance. No manuscript promotion. The target is the SAME expected-utility coordinates before and after ordinary CE obedience, not recommendation probabilities renamed as extra players' payoffs.

## P19-G: payoff-preserving complement closure

Consider any finite binary-action N-player game with utilities in [0,1]. Write bar(a) for simultaneous complementation of every action and a^i for flipping only i. Assume, for every pure profile and player,

1. u_i(bar(a)) = u_i(a);
2. u_i(a^i) = 1-u_i(a).

Let P=conv{u(a):a in {0,1}^N} be the nonstrategic expected-payoff polytope. Then the ordinary correlated-equilibrium payoff region is exactly

    CEP = P intersect {v: v_i >= 1/2 for all i}.

**Proof.** For an arbitrary law lambda define the unnormalized CE row G_i,r as the expectation of 1[a_i=r](u_i(a)-u_i(a^i)). The second hypothesis gives G_i,0+G_i,1=2v_i-1. Thus every CE has v_i>=1/2. Conversely take any law realizing v in P with these lower bounds. Average lambda with its pushforward under simultaneous complementation. Hypothesis 1 preserves every payoff. Complementation exchanges the two action events and preserves the own-switch gain (both terms are globally complement invariant). Consequently both rows of the averaged law equal half their sum, namely v_i-1/2>=0. This law is CE and realizes v. QED.

If P admits an extended formulation with q inequalities, CEP admits one with at most q+N inequalities, in the identical payoff coordinates. Equations are not counted. Given a finite-support realizing law, implementation merely adds its complemented profiles, at most doubling support. The statement is existential if only an existential EF of P is available; it does not supply a polynomial algorithm for recovering an arbitrary original realizing law from an unspecified projection.

This rules out a superpolynomial causal exact-EF gap whenever the baseline is compact and the two hypotheses hold. It does not assert all binary games have the closure, nor any approximate hardness, computational lower bound, or positive-margin version. Both assumptions matter: u_i=a_i has the own-flip identity but complement averaging changes payoffs; constant utility1 has global symmetry but does not have the own-flip identity.

### Natural nonconstant example: directed-cycle coordination

For N>=2 put u_i(a)=1[a_i=a_(i+1 mod N)]. These utilities satisfy both hypotheses and are genuinely nonconstant on CE: independent fair bits give all payoffs1/2, whereas pure consensus gives all payoffs1. Pure payoff vectors are exactly the 0/1 vectors with an even number of zero entries. Necessity follows by traversing the cycle; sufficiency follows by fixing a_1 and propagating equality/inequality labels, with even parity ensuring closure.

This parity polytope has an O(N)-size flow lift: run a two-state parity automaton through N labels, start and finish at parity0, and put a unit nonnegative flow on its layered acyclic graph. At step i, a disagreement label toggles parity; project to v_i equal to the flow using agreement labels. Flow decomposition proves exactness. Adding v_i>=1/2 gives an O(N)-size CE payoff lift. For N=2 the repeated equality yields the corresponding diagonal segment, also covered by this construction. No claim that parity-flow lifts or group averaging are new.

The closure also covers even-cardinality local XOR payoff tests containing the player's own action. Such a class can have a complicated baseline, so the theorem alone does not prove all XOR games easy.

## Primary comparison and originality gate

Lehrer, Solan and Viossat, *Equilibrium payoffs of finite games*, J. Math. Econ.47 (2011),48–53, Proposition1, already proves arbitrary polytopes can occur as CE payoff sets. Actually inspected the author-hosted corrected proofs, pp1–2, including the bimatrix construction; the n-player construction is deferred by the paper to Appendix A and was not reconstructed here. [Primary corrected proofs](https://www.ceremade.dauphine.fr/~viossat/PDFs/LSV-correctedproofs.pdf). Their two-player construction indexes actions by listed extreme points. This universality does not supply the representation contract needed here: compact game description AND compact unconstrained region in the same coordinates with a much larger CE EF. One cannot transfer an exponential-EF target through vertex enumeration and silently keep the input polynomial.

Kamisetty, Xing and Langmead's ICML2011 marginal-polytope formulation already gives the larger general lesson that obedience rows constrain a suitable joint-moment lift. [Primary paper](https://www.cs.cmu.edu/~epxing/papers/2011/Kamisetty_Xing_Langmead_ICML11.pdf), sections3.1 and3.3, inspected in Phase18. P19-G is a short payoff-preserving averaging specialization, classified as a straightforward corollary of standard CE linearity and symmetry averaging, not a substantive originality candidate.

## Rejected constructions and stopping decision

Adding opponents-only externalities to the P18 collision game preserves its incentive differences and can make equilibrium utilities nonconstant. But the unconstrained payoff map then still contains collision products. No compact same-payoff baseline was proved: a small utility circuit is not a compact payoff-polytope EF. Thus this attempt supplies no valid separation.

Adding passive observers whose utilities copy original players' actions would embed the old recommendation-marginal theorem into payoff coordinates. Giving observers a strictly dominated extra action does not cure that substantive issue. This is coordinate encoding through extra players, not the natural economic example sought; it is rejected rather than promoted. Full baseline geometry would still need checking if all player payoffs were retained.

The natural parity/coordination lead is closed by P19-G. No further perturbation or gadget branch is recommended without an independently motivated game class and a separately proved compact baseline. Prioritize endogenous information rather than another matching-face encoding. Ordinary-CE payoff separation remains open in the requested natural nondegenerate regime; this note is not an impossibility theorem beyond its explicit hypotheses.

## Exact verification and scope

Four unittest methods pass: exact rational action-row identities across biased parity games for N2–5; cycle payoff vertex parity for N2–7; distinct nonconstant CE payoff laws and a rejected payoff vector; and missing-assumption counterchecks. These finite checks supplement the proof and do not establish unbounded claims experimentally. Files: experiments/phase19_payoff_geometry.py and experiments/test_phase19_payoff_geometry.py. Independent adversarial reconstruction requested from the parent team.
