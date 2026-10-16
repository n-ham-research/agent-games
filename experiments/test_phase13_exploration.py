"""Exact benchmarks for broader exploration; no originality claim."""
import unittest
from fractions import Fraction as F
from itertools import product

class ExplorationChecks(unittest.TestCase):
    def test_strategic_equivalence_does_not_fix_calibrated_roles(self):
        def u(a): return a[0], a[1]
        def v(a): return a[0]+10*a[1], a[1]
        for a in product((0,1), repeat=2):
            for i in range(2):
                b=list(a);b[i]=1-b[i]
                self.assertEqual(u(tuple(b))[i]-u(a)[i],v(tuple(b))[i]-v(a)[i])
        self.assertEqual(u((1,1)),(1,1))
        self.assertEqual(v((1,1)),(11,1))
        self.assertEqual(len({v(a)[0] for a in product((0,1),repeat=2)}),4)
        self.assertEqual(len({v(a)[1] for a in product((0,1),repeat=2)}),2)

    def test_robust_work_margin_sharp_example(self):
        B,c,eta=F(2),F(3,2),F(1,4)
        success,failed_work,empty=F(1,2),F(1,14),F(3,7)
        self.assertEqual(success+failed_work+empty,1)
        work=success+failed_work
        utility=B*success-c*work
        self.assertEqual((B*success-c*work)/work,eta)
        self.assertEqual(utility,B*eta*success/(c+eta))
        self.assertEqual(utility,F(1,7))
        # No-singleton collaborators cannot repair either failed profile;
        # singleton cost1 is indifferent to repairing total failure1/2.
        self.assertEqual(B*(1-success)-F(1),0)
