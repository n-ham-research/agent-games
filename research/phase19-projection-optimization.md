# Phase 19 — optimizing the small protected projection

P19-P is a direct algorithmic corollary of P18-P, not a new polyhedral theorem.
Retain its exact hypotheses: edge-cover task on K_(2m), k pairwise disjoint
protected edge-workers, m>=k+2, benefit1, 0<c<1 and
0<=delta<=min(c,1-c). The retained region is

    0<=s<=1, max(s-c,delta*s/(c+delta))<=u_i<=s.

To maximize beta*s+sum_i w_i*u_i, choose u_i=s for w_i>=0 and the lower
endpoint otherwise. The resulting function of s is affine on each of the two
intervals split at s=c+delta: these are exactly where the two lower-bound
lines cross. Evaluate only s=0,c+delta,1 and select the largest objective.
This takes O(k) rational arithmetic operations; for rational input all
intermediate bit lengths are polynomial. Feed that target into P18's threshold
coupling/matching completion to recover an obedient central law with at most
2k+2 profiles in polynomial time. No generic LP oracle, vertex enumeration,
full-region representation or approximate-hardness assertion is needed.

The attached exact test compares all candidates against a rational success
and endpoint grid over signed objectives, then reconstructs and checks EVERY
worker's obedience rows. These checks supplement the piecewise-affine proof.
This solves linear optimization for this particular protected projection;
incident roles, insufficient graph slack and generic fixed-dimensional
projections remain separate unresolved problems. The older P18 note's sentence
'No LP optimizer is implemented' describes that phase; this is a new specialized
optimizer, not a general LP implementation. No new matching theorem or general
fixed-dimension algorithm is claimed.
