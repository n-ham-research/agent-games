import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase18_sequential import prefix_schedule,workload_prefix,periodic_workload,balance_polynomial,evaluate,stage_gain

class Sequential(unittest.TestCase):
    def test_residual_invariant(self):
        for beta in (F(1,2),F(3,5),F(2,3),F(3,4),F(9,10)):
            bits,rs=prefix_schedule(beta,60)
            for t,r in enumerate(rs):
                self.assertTrue(0<=r<=1)
                self.assertEqual(workload_prefix(beta,bits[:t])+beta**t*r,F(1,2))
                self.assertLessEqual(abs(workload_prefix(beta,bits[:t])-F(1,2)),beta**t)
    def test_half_discount_finite_implementation(self):
        self.assertEqual(periodic_workload(F(1,2),(1,),(0,)),F(1,2))
        bits,_=prefix_schedule(F(1,2),6)
        self.assertEqual(bits,[0,1,1,1,1,1])
        self.assertEqual(periodic_workload(F(1,2),(0,),(1,)),F(1,2))
    def test_periodic_polynomial_identity(self):
        for L in range(3):
            for P in range(1,5):
                for digits in product((0,1),repeat=L+P):
                    a,b=digits[:L],digits[L:];q=balance_polynomial(a,b)
                    self.assertIn(q[0],(-1,1))
                    for beta in (F(1,2),F(2,3),F(3,4)):
                        lhs=evaluate(q,beta)
                        rhs=(1-beta**P)*(2*periodic_workload(beta,a,b)-1)
                        self.assertEqual(lhs,rhs)
    def test_no_small_eventual_period_rational(self):
        for beta in (F(2,3),F(3,4),F(3,5),F(4,5)):
            for L in range(3):
                for P in range(1,5):
                    for digits in product((0,1),repeat=L+P):
                        self.assertNotEqual(periodic_workload(beta,digits[:L],digits[L:]),F(1,2))
    def test_alternating_role_distinction(self):
        for beta in (F(1,2),F(2,3),F(9,10)):
            a=periodic_workload(beta,(),(1,0));b=periodic_workload(beta,(),(0,1))
            self.assertEqual(a,1/(1+beta));self.assertEqual(b,beta/(1+beta))
            self.assertEqual((a+b)/2,F(1,2));self.assertNotEqual(a,b)
    def test_every_stage_deviation_loses(self):
        for cost in (F(1,10),F(1,2),F(9,10)):
            for assigned in (False,True): self.assertGreater(stage_gain(cost,assigned),0)
    def test_persistent_type_mimic(self):
        types=(F(1,4),F(3,4));profiles=list(product(types,repeat=2))
        for loads in product((F(0),F(1,2),F(1)),repeat=4):
            d=dict(zip(profiles,loads));ic=True
            for a,b in profiles:
                for r in types:
                    ic &= 1-a*d[a,b]>=1-a*d[r,b]
                    ic &= 1-b*(1-d[a,b])>=1-b*(1-d[a,r])
            if ic:self.assertEqual(len(set(loads)),1)
    def test_reject_unsupported_discount(self):
        with self.assertRaises(ValueError):prefix_schedule(F(1,3),5)

if __name__=='__main__':unittest.main()
