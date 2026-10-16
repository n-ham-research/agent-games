import unittest
from fractions import Fraction as F
from experiments.phase18_endogenous_information import (full_success_law,
    low_success_law, conditional_margins, statistics, information,
    full_formula, low_formula)


class EndogenousInformationTests(unittest.TestCase):
    def test_full_success_exact_family_and_information_identity(self):
        for n in range(2, 8):
            for cost, delta in ((F(3,5),F(1,10)), (F(1,3),F(1,6)),
                                (F(2,5),F(0)), (F(1,10),F(1,20))):
                law, r = full_success_law(n, F(1), cost, delta)
                self.assertEqual(sum(law.values()), 1)
                self.assertEqual(statistics(law), (F(1),r))
                self.assertGreaterEqual(min(conditional_margins(law,n,F(1),cost).values()), delta)
                self.assertEqual(information(law,n), full_formula(n,r))
                for theta in range(n):
                    self.assertEqual(sum(p for (t,a),p in law.items() if t == theta), F(1,n))

    def test_public_cardinality_optimal_fixed_size(self):
        for n in range(2,7):
            law,r = full_success_law(n,F(1),F(3,5),F(1,10),True)
            self.assertEqual(statistics(law), (F(1),F(1)))
            self.assertGreaterEqual(min(conditional_margins(law,n,F(1),F(3,5),True).values()), F(1,10))
            self.assertEqual(information(law,n), full_formula(n,r,True))

    def test_private_pooling_and_unsafe_size_disclosure_exact_numbers(self):
        law,r = full_success_law(3,F(1),F(3,5),F(1,10))
        self.assertEqual(r,F(10,7))
        self.assertEqual(sum(p for (_,a),p in law.items() if len(a)==1),F(4,7))
        self.assertEqual(information(law,3),{3:F(1),2:-F(3,7)})
        private = conditional_margins(law,3,F(1),F(3,5))
        self.assertEqual({v for (_,work,_),v in private.items() if work},{F(1,10)})
        public = conditional_margins(law,3,F(1),F(3,5),True)
        self.assertEqual({v for (_,work,k),v in public.items() if work and k==2},{-F(1,10)})

    def test_low_success_segment_exact_kl_identity(self):
        for n in range(2,7):
            cost,delta=F(3,5),F(1,20)
            tau=cost+delta
            for success in (F(0),tau/4,tau/2,tau):
                law=low_success_law(n,tau,success)
                self.assertEqual(sum(law.values()),1)
                self.assertEqual(statistics(law),(success,success/tau))
                self.assertGreaterEqual(min(conditional_margins(law,n,F(1),cost).values()),delta)
                self.assertEqual(information(law,n),low_formula(n,tau,success))

    def test_low_success_tau_one_endpoint(self):
        for success in (F(0),F(1,4),F(1)):
            law=low_success_law(3,F(1),success)
            self.assertEqual(statistics(law),(success,success))
            self.assertEqual(information(law,3),low_formula(3,F(1),success))
            self.assertGreaterEqual(min(conditional_margins(law,3,F(1),F(9,10)).values()),F(1,10))

    def test_zero_information_all_work_when_incentives_allow(self):
        law,r=full_success_law(4,F(1),F(1,10),F(1,20))
        self.assertEqual(r,4)
        self.assertEqual(information(law,4),{})
        self.assertEqual({a for (_,a) in law},{frozenset(range(4))})
        self.assertEqual(set(conditional_margins(law,4,F(1),F(1,10)).values()),{F(3,20)})

    def test_blind_full_success_fails_high_cost_obedience(self):
        law={(theta,frozenset(range(3))):F(1,3) for theta in range(3)}
        self.assertEqual(statistics(law)[0],1)
        self.assertEqual(information(law,3),{})
        self.assertEqual(set(conditional_margins(law,3,F(1),F(3,5)).values()),{-F(4,15)})

    def test_fixed_size_public_set_is_also_obedient(self):
        law,r=full_success_law(5,F(1),F(2,5),F(0),True)
        self.assertEqual(statistics(law),(F(1),F(2)))
        self.assertGreaterEqual(min(conditional_margins(law,5,F(1),F(2,5),public_set=True).values()),0)


if __name__ == '__main__':
    unittest.main()
