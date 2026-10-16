import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase19_payoff_geometry import (profiles, symmetrize, payoffs,
    rows, cycle_coordination, xor_utility)

class PayoffGeometryChecks(unittest.TestCase):
    def test_even_parity_masks_exact_row_identity(self):
        for n in range(2,6):
            masks=[(i,(i+1)%n) for i in range(n)]
            for biases in product((0,1),repeat=n):
                u=xor_utility(masks,biases)
                atoms=profiles(n)
                law={a:F(j+1,len(atoms)*(len(atoms)+1)//2)
                     for j,a in enumerate(atoms)}
                v=payoffs(law,u)
                sym=symmetrize(law)
                self.assertEqual(payoffs(sym,u),v)
                for (i,r),g in rows(sym,u).items():
                    self.assertEqual(g,v[i]-F(1,2))

    def test_cycle_raw_vertices_even_disagreements(self):
        for n in range(2,8):
            actual={tuple(cycle_coordination(a,i) for i in range(n))
                    for a in profiles(n)}
            self.assertEqual(actual,{v for v in profiles(n) if (n-sum(v))%2==0})

    def test_nonconstant_ce_payoffs_and_rejection(self):
        u=cycle_coordination
        for law,wanted in [({a:F(1,8) for a in profiles(3)},F(1,2)),
                           ({(0,0,0):F(1)},F(1))]:
            self.assertEqual(payoffs(law,u),(wanted,)*3)
            self.assertTrue(all(g>=0 for g in rows(law,u).values()))
        law={(0,0,1):F(1)}
        self.assertTrue(any(v<F(1,2) for v in payoffs(law,u)))
        self.assertTrue(any(g<0 for g in rows(law,u).values()))

    def test_missing_assumptions_break_identity(self):
        law={(0,0):F(1)}
        u=lambda a,i:F(a[i])
        self.assertNotEqual(payoffs(law,u),payoffs(symmetrize(law),u))
        u=lambda a,i:F(1)
        self.assertNotEqual(rows(law,u)[0,0],payoffs(law,u)[0]-F(1,2))

if __name__=='__main__': unittest.main()
