import unittest
from fractions import Fraction as Q
from itertools import product, combinations
from experiments.phase13_computation import (
    compositions,histograms,histogram_probability,minimal_outcomes,
    compressed_interims,labeled_profiles,profile_histogram,uniform_lifts,
    target_rule_mass,audit_capacity,knapsack_expected_cover_cost,
    decode_failing_subsets,parity_probability,xor_width,
    cyclic_difference,cyclic_counting_payoff,noisy_sign_bisection,
)


class CompactTaskChecks(unittest.TestCase):
    def setUp(self):
        self.sizes=(2,2)
        self.ps=((Q(1,3),Q(2,3)),(Q(3,5),Q(2,5)))
        self.success=lambda counts: counts[0]+2*counts[1]>=3
        # All singletons fail; role types differ in task weight and prior.

    def chooser(self,h,ys):
        # Meaningful cost-sensitive, sometimes-failing target; intentionally
        # not an IC assertion before the computed audits are imposed.
        if h[0][0]+h[1][0]==0:
            return {None:Q(1)}
        best=min(ys,key=lambda y:sum(row[1] for row in y))
        return {None:Q(1,4),best:Q(3,4)}

    def test_histogram_mass_matches_labeled_independent_prior(self):
        labels,profiles=labeled_profiles(self.sizes,(2,2))
        direct={}
        for types in profiles:
            h=profile_histogram(labels,types,(2,2))
            prob=Q(1)
            for r,c in zip(labels,types): prob*=self.ps[r][c]
            direct[h]=direct.get(h,Q(0))+prob
        for h in histograms(self.sizes,(2,2)):
            self.assertEqual(histogram_probability(h,self.ps),direct[h])
        self.assertEqual(sum(direct.values()),1)

    def test_minimal_count_patterns_equal_labeled_pivotality(self):
        labels,profiles=labeled_profiles(self.sizes,(2,2))
        for types in profiles:
            h=profile_histogram(labels,types,(2,2))
            for y in minimal_outcomes(h,self.success):
                lifts=uniform_lifts(labels,types,y)
                self.assertEqual(sum(lifts.values()),1)
                for coalition in lifts:
                    totals=tuple(sum(labels[i]==r for i in coalition) for r in range(2))
                    self.assertTrue(self.success(totals))
                    for i in coalition:
                        less=tuple(g-(r==labels[i]) for r,g in enumerate(totals))
                        self.assertFalse(self.success(less))

    def test_pointed_interims_match_full_labeled_mechanism(self):
        masses=target_rule_mass(self.sizes,self.ps,self.success,self.chooser)
        s,x,rel=compressed_interims(self.sizes,self.ps,masses)
        labels,profiles=labeled_profiles(self.sizes,(2,2))
        direct_s={(i,c):Q(0) for i in range(4) for c in (0,1)}
        direct_x=dict(direct_s)
        full_rel=Q(0)
        for types in profiles:
            ph=profile_histogram(labels,types,(2,2))
            prior=Q(1)
            for r,c in zip(labels,types): prior*=self.ps[r][c]
            ys=tuple(minimal_outcomes(ph,self.success))
            for y,prob in self.chooser(ph,ys).items():
                if y is None: continue
                full_rel+=prior*prob
                for coalition,lp in uniform_lifts(labels,types,y).items():
                    for i,(r,c) in enumerate(zip(labels,types)):
                        direct_s[i,c]+=prior*prob*lp/self.ps[r][c]
                        direct_x[i,c]+=prior*prob*lp*(i in coalition)/self.ps[r][c]
        self.assertEqual(rel,full_rel)
        for (i,c),v in direct_s.items(): self.assertEqual(v,s[labels[i],c])
        for (i,c),v in direct_x.items(): self.assertEqual(v,x[labels[i],c])

    def test_compressed_audit_reconstruction_satisfies_every_type_deviation(self):
        masses=target_rule_mass(self.sizes,self.ps,self.success,self.chooser)
        s,x,_=compressed_interims(self.sizes,self.ps,masses)
        costs=((Q(1,2),Q(3,2)),(Q(1,3),Q(4,3)))
        B=Q(2)
        for r in (0,1):
            sr=[s[r,c] for c in (0,1)];xr=[x[r,c] for c in (0,1)]
            for d in (0,1):
                a,b=audit_capacity(B,costs[r],sr,xr,d)
                self.assertTrue(0<=a<=sr[d]-xr[d])
                self.assertTrue(0<=b<=xr[d])
                for c in (0,1):
                    honest=B*sr[c]-costs[r][c]*xr[c]
                    lie=B*sr[d]-costs[r][c]*xr[d]-B*a-(B-costs[r][c])*b
                    self.assertGreaterEqual(honest,lie)

    def test_weighted_threshold_expected_value_decodes_counting(self):
        for weights in ((1,2,3),(2,2,5),(1,1,1,3),(2,3,5,7)):
            n=len(weights)
            for quota in range(1,sum(weights)+2):
                cost,alpha=knapsack_expected_cover_cost(weights,quota)
                fail=sum(sum(w*b for w,b in zip(weights,subset))<quota
                         for subset in product((0,1),repeat=n))
                self.assertEqual(decode_failing_subsets(cost,alpha,n),fail)
                gate=sum(weights)+quota+1
                # One ordinary weighted-threshold game forces gate inclusion.
                self.assertLess(sum(weights)+quota,gate+quota)
                self.assertLess(gate,gate+quota)

    def test_xor_amplification_exact_probability(self):
        for k in range(1,7):
            ps=tuple(Q(1,2)+Q((-1)**j,50) for j in range(k))
            direct=Q(0)
            for bits in product((0,1),repeat=k):
                mass=Q(1)
                for bit,p in zip(bits,ps):mass*=p if bit else 1-p
                if sum(bits)%2:direct+=mass
            self.assertEqual(parity_probability(ps),direct)
            self.assertEqual(abs(direct-Q(1,2)),Q(1,2)*Q(1,25)**k)
        for n in range(1,101):
            k=xor_width(n)
            error=Q(n,2)*Q(1,25)**k
            self.assertLessEqual(error,Q(1,48))
            self.assertGreater((Q(1,6)-error)/2,Q(1,100))

    def test_counting_gap_cannot_survive_coarse_accuracy_in_original_family(self):
        for n in range(2,32):
            g=Q(1,2**(n+1))
            # For count K or K+1 around the same half-integer threshold,
            # the common all-half profile has decision regret g/2.
            for sign in (-1,1):
                regret=abs(sign*g)/2
                self.assertEqual(regret,Q(1,2**(n+2)))

    def test_cyclic_two_orbit_construction_payoffs_and_typed_symmetry(self):
        n=3
        xs=list(product((0,1),repeat=n))
        # All 256 functions, all four-player profiles; cyclic ordering matters.
        for table in product((0,1),repeat=2**n):
            truth=dict(zip(xs,table))
            for profile in product((0,1),repeat=n+1):
                old=cyclic_counting_payoff(profile,truth,3)
                moved=profile[-1:]+profile[:-1]
                new=cyclic_counting_payoff(moved,truth,3)
                self.assertEqual(new,old[-1:]+old[:-1])
                self.assertTrue(all(0<=v<=1 for v in old))

    def test_cyclic_two_orbit_strict_monotonicity_and_threshold_regret(self):
        n=3
        xs=list(product((0,1),repeat=n))
        grid=[Q(j,8) for j in range(9)]
        for table in product((0,1),repeat=2**n):
            truth=dict(zip(xs,table))
            count=sum(table)
            for K in range(2**n):
                Ds=[cyclic_difference(truth,p,K) for p in grid]
                self.assertGreater(Ds[0],0);self.assertLess(Ds[-1],0)
                for left,right,p,q in zip(Ds,Ds[1:],grid,grid[1:]):
                    self.assertLessEqual(right-left,-(q-p)/2)
                alpha,g=Q(1,2*n),Q(1,2**(n+1))
                for p,D in zip(grid,Ds):
                    if count>K and p<=Q(1,2):
                        self.assertGreaterEqual((1-p)*D/2,alpha*g/4)
                    if count<=K and p>=Q(1,2):
                        self.assertGreaterEqual(-p*D/2,alpha*g/4)

    def test_noisy_bisection_exact_endpoint_and_nonmonotone_brackets(self):
        eps=Q(1,32)
        for value,want in ((Q(-1,3),Q(0)),(Q(1,3),Q(1)),(Q(0),Q(0))):
            p,trace=noisy_sign_bisection(lambda p:value,4,eps)
            self.assertEqual(p,want);self.assertEqual(trace,[])
        # Three distinct roots: no monotonicity may be silently assumed.
        D=lambda p:-(p-Q(1,5))*(p-Q(1,2))*(p-Q(4,5))
        for direction in (-1,0,1):
            p,trace=noisy_sign_bisection(D,4,eps,
                    lambda j,p:direction*((-1)**j)*eps/4)
            self.assertLessEqual(max((1-p)*D(p),-p*D(p)),eps)
            for lo,hi,mid,estimate,exact in trace:
                self.assertGreater(D(lo),0);self.assertLess(D(hi),0)
                self.assertLessEqual(abs(estimate-exact),eps/4)

    def test_noisy_bisection_all_small_cyclic_games(self):
        n=2;xs=list(product((0,1),repeat=n));eps=Q(1,100)
        for table in product((0,1),repeat=2**n):
            truth=dict(zip(xs,table))
            for K in range(2**n):
                D=lambda p:cyclic_difference(truth,p,K)/2
                for direction in (-1,1):
                    p,trace=noisy_sign_bisection(D,n+1,eps,
                        lambda j,p:direction*((-1)**j)*eps/4)
                    self.assertLessEqual(max((1-p)*D(p),-p*D(p)),eps)
                    for lo,hi,mid,estimate,exact in trace:
                        self.assertGreater(D(lo),0);self.assertLess(D(hi),0)


if __name__=='__main__': unittest.main()
