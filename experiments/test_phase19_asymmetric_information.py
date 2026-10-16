import unittest
from fractions import Fraction as F
from experiments.phase19_asymmetric_information import optimum, law, information, entropy_formula, margins


class AsymmetricInformationTests(unittest.TestCase):
    def test_rational_grid_private_and_public(self):
        for p in (F(1,5), F(1,2), F(4,5)):
            for t1 in (F(1,4), F(1,2), F(3,4), F(1)):
                for t2 in (F(1,4), F(1,2), F(3,4), F(1)):
                    for public in (False, True):
                        a,b = optimum(p,t1,t2,public)
                        joint = law(p,a,b)
                        self.assertEqual(sum(joint.values()),1)
                        self.assertEqual(information(joint,p),entropy_formula(p,a,b))
                        # Choose positive margins delta_i=tau_i/4 and costs=3tau_i/4.
                        costs=(3*t1/4,3*t2/4)
                        for (i,work,size),gain in margins(joint,costs,public=public).items():
                            self.assertGreaterEqual(gain,(t1,t2)[i]/4)
                        if t1+t2 <= 1:
                            self.assertEqual((a,b),optimum(p,t1,t2,False))
                            if a+b:
                                self.assertLessEqual(t1,a/(a+b))
                                self.assertLessEqual(a/(a+b),1-t2)
                        else:
                            if public:
                                self.assertEqual((a,b),(0,0))

    def test_private_cap_rectangle(self):
        p,t1,t2=F(2,7),F(3,5),F(4,5)
        astar,bstar=optimum(p,t1,t2)
        for a in (0,astar/2,astar):
            for b in (0,bstar/2,bstar):
                gains=margins(law(p,a,b),(t1,t2))
                self.assertTrue(all(g>=0 for g in gains.values()))
        self.assertLess(margins(law(p,astar,bstar+F(1,100)),(t1,t2))[(0,True,None)],0)

    def test_strict_gap_and_boundary(self):
        for t1,t2 in ((F(3,5),F(4,5)),(F(1),F(3,4))):
            a,b=optimum(F(1,2),t1,t2)
            self.assertEqual(a>0 and b>0,t1<1 and t2<1)
            if t1==1:
                self.assertEqual(information(law(F(1,2),a,b),F(1,2)),{2:F(1)})
        # Uniform symmetric tau: only singleton messages reveal capability.
        for t in (F(51,100),F(3,5),F(3,4)):
            a,b=optimum(F(1,2),t,t)
            self.assertEqual(a,b)
            self.assertEqual(a+b,(1-t)/t)
            # MI = (1-q)log2 exactly; tends to zero as tau decreases to 1/2.
            self.assertEqual(information(law(F(1,2),a,b),F(1,2)),{2:1-(a+b)})

if __name__ == '__main__':
    unittest.main()
