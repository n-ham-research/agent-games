import unittest
from fractions import Fraction as Q
from itertools import product
from experiments.phase14_complexity import (
    opponent_tuple,observed_inputs,pointed_payoffs,baseline_differences,
    regrets,hidden_expectations,hidden_differences,constant_query_bound_holds,
    inverse_poly_query_bound_holds,direct_expectation,
)


class SymmetryOracleChecks(unittest.TestCase):
    def test_typed_rotation_and_full_group_slice_obstruction(self):
        n=3
        xs=list(product((0,1),repeat=n))
        for table in product((0,1),repeat=2**n):
            F=dict(zip(xs,table)).__getitem__
            for profile in product((0,1),repeat=n+1):
                old=pointed_payoffs(profile,F)
                moved=profile[-1:]+profile[:-1]
                self.assertEqual(pointed_payoffs(moved,F),old[-1:]+old[:-1])
                self.assertTrue(all(0<=v<=1 for row in old for v in row))
            zero=(0,)*(n+1);one=(1,)*(n+1)
            self.assertEqual(pointed_payoffs(zero,F)[0][0],Q(1,2))
            self.assertEqual(pointed_payoffs(one,F)[0][0],Q(1,2))
            self.assertGreater(pointed_payoffs(zero,F)[0][1],pointed_payoffs(one,F)[0][1])

    def test_adversary_preserves_even_all_pointed_pure_answers(self):
        n=5
        queries=[tuple((index>>j)&1 for j in range(n+1)) for index in (0,7,18,43)]
        seen=observed_inputs(queries)
        self.assertLessEqual(len(seen),(n+1)*len(queries))
        for profile in queries:
            self.assertEqual(pointed_payoffs(profile,lambda z:0),
                             pointed_payoffs(profile,lambda z:int(z not in seen)))

    def test_seen_mass_formula_matches_full_product_enumeration(self):
        ps=(Q(2,5),Q(3,7),Q(4,9),Q(5,11))
        seen=observed_inputs(((0,0,1,1),(1,0,1,0)))
        got=hidden_expectations(ps,seen)
        for i in range(len(ps)):
            ordered=tuple(ps[(i+j)%len(ps)] for j in range(1,len(ps)))
            direct=direct_expectation(lambda z:int(z not in seen),ordered)
            self.assertEqual(got[i],direct)

    def test_constant_accuracy_robust_profiles_are_fooled(self):
        eps=Q(1,1024);rho=Q(1,64)
        for n in (12,16,20):
            N=n+1
            possible=(64**n)//(8*N*(41**n))
            queries=[tuple((index*421+117)>>j&1 for j in range(N))
                     for index in range(min(10,possible))]
            self.assertTrue(constant_query_bound_holds(n,len(queries),rho))
            ps=tuple(Q(7,16)+Q((-1)**j,4096) for j in range(N))
            self.assertLessEqual(max(ps)-min(ps),rho)
            self.assertLessEqual(max(regrets(ps,baseline_differences(ps))),eps)
            seen=observed_inputs(queries)
            self.assertTrue(all(e>=Q(7,8) for e in hidden_expectations(ps,seen)))
            Ds=hidden_differences(ps,seen)
            self.assertTrue(all(D>=Q(1,32) for D in Ds))
            self.assertTrue(all(r>eps for r in regrets(ps,Ds)))

    def test_constant_bounds_have_strict_regret_slack(self):
        eps=Q(1,1024)
        for rho in (Q(0),Q(1,128),Q(1,64)):
            self.assertGreater(Q(1,64),eps)
            D=Q(7,64)-Q(1,16)-rho
            self.assertGreaterEqual(D,Q(1,32))
            self.assertGreater((Q(1,2)-rho)*D/2,eps)

    def test_inverse_accuracy_atom_bound_and_hidden_regret(self):
        for n in range(2,64):
            eps=Q(1,256*n);r=Q(1,2)-Q(1,4*n)
            for p in (r-8*eps,r,r+8*eps):
                self.assertLess(p,Q(1,2))
                self.assertLessEqual((1-p)**n,Q(2,2**n))
            self.assertGreater(Q(11,128*n),eps)
            self.assertTrue(inverse_poly_query_bound_holds(n,0))

    def test_inverse_accuracy_actual_query_transcript(self):
        for n in (10,12,16):
            N=n+1;alpha=Q(1,2*n);eps=Q(1,256*n)
            possible=(2**n)//(8*N)
            queries=[tuple((index*119+37)>>j&1 for j in range(N))
                     for index in range(min(possible,12))]
            self.assertTrue(inverse_poly_query_bound_holds(n,len(queries)))
            seen=observed_inputs(queries)
            ps=(Q(1,2)-Q(1,4*n),)*N
            self.assertEqual(max(regrets(ps,baseline_differences(ps,alpha))),0)
            self.assertTrue(all(e>=Q(3,4) for e in hidden_expectations(ps,seen)))
            self.assertTrue(all(v>eps for v in regrets(ps,hidden_differences(ps,seen,alpha))))


if __name__=='__main__':unittest.main()
