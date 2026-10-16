"""Independent exact source/version and information-boundary checks."""
import unittest
from fractions import Fraction as F
from itertools import product

class SourceAndInitializationChecks(unittest.TestCase):
    def test_symmetric_threshold_lottery_not_count_only_cost_half(self):
        # Cavaliere2000 printed Prop1 specializes to c=1/2 at M2,w1.
        # Direct recommendation inequalities permit every0<c<1 instead.
        count_only_left=count_only_right=F(1,2)
        self.assertEqual(count_only_left,count_only_right)
        for cost in (F(1,4),F(3,4)):
            law={(1,0):F(1,2),(0,1):F(1,2)}
            for i,rec in product(range(2),range(2)):
                margin=F(0)
                for actions,prob in law.items():
                    if actions[i]!=rec: continue
                    other=list(actions);other[i]=1-rec
                    u=int(any(actions))-cost*actions[i]
                    v=int(any(other))-cost*other[i]
                    margin+=prob*(u-v)
                self.assertGreater(margin,0)
            self.assertNotEqual(cost,count_only_left)

    def test_failure_pure_ne_mixture_not_necessarily_efficient(self):
        # Threshold2: no individual can repair all-abstain.
        B,c=F(1),F(1,2)
        def u(actions,i): return B*int(sum(actions)>=2)-c*actions[i]
        self.assertEqual(u((0,0),0),0)
        self.assertLess(u((1,0),0),u((0,0),0))
        self.assertGreater(sum(u((1,1),i) for i in range(2)),0)

    def test_matching_component_marginal_does_not_fix_context_correlation(self):
        correlated={(0,0):F(1,2),(1,1):F(1,2)}
        independent={(b,z):F(1,4) for b,z in product(range(2),repeat=2)}
        for bit in range(2):
            self.assertEqual(sum(p for (b,z),p in correlated.items() if b==bit),
                             sum(p for (b,z),p in independent.items() if b==bit))
        # Context exposes z; guessing it is value1 or1/2 despite same marginalb.
        self.assertEqual(sum(p*(b==z) for (b,z),p in correlated.items()),1)
        self.assertEqual(sum(p*(b==z) for (b,z),p in independent.items()),F(1,2))
