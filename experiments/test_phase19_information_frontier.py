import unittest
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import isqrt
from experiments.phase18_endogenous_information import (information, statistics,
    conditional_margins, add_log, clean)
from experiments.phase19_information_frontier import (parameters,minimum_success,
    optimal_mean,preferred_success,sizes,q_t,tilted_success,tilt_bracket,tilt_law,
    binary_kl,information_formula,log_nonnegative)


class InformationFrontierTests(unittest.TestCase):
    def test_feasibility_and_geometric_redundancy_parameter_grid(self):
        for n,c,d in product(range(2,7),(F(1,5),F(2,5),F(3,5),F(9,10)),
                              (F(0),F(1,20),F(1,10))):
            tau,sigma=parameters(n,F(1),c,d)
            lower=minimum_success(n,tau,sigma)
            for s in (lower,(lower+1)/2,F(1)):
                m=optimal_mean(n,tau,sigma,s)
                self.assertGreaterEqual(m,s)
                self.assertLessEqual(m,n-1+s)
                self.assertLessEqual(m,n*s)
                self.assertGreaterEqual(s,tau*m)
                self.assertLessEqual(1-s,sigma*(n-m))
                lo,hi=tilt_bracket(n,m,s,20)
                if lo is not None:
                    self.assertLessEqual(tilted_success(n,m,lo),s)
                    self.assertGreaterEqual(tilted_success(n,m,hi),s)
            if lower:
                with self.assertRaises(ValueError):
                    optimal_mean(n,tau,sigma,lower/2)

    def test_rational_tilts_attain_optimal_work_binding_moments(self):
        for n in range(2,7):
            for m in (F(1,2),F(1),F(3,2),F(n)-F(1,2)):
                for a in (F(3,2),F(2),F(4)):
                    s=tilted_success(n,m,a)
                    c=s/m
                    tau,sigma=parameters(n,F(1),c,F(0))
                    self.assertEqual(optimal_mean(n,tau,sigma,s),m)
                    law=tilt_law(n,m,a)
                    self.assertEqual(sum(law.values()),1)
                    self.assertEqual(statistics(law),(s,m))
                    self.assertGreaterEqual(min(conditional_margins(law,n,F(1),c).values()),0)
                    self.assertEqual(information(law,n),information_formula(n,m,a))

    def test_rational_tilts_attain_abstention_binding_low_cost(self):
        for n in range(2,6):
            m=F(n)-F(1,2)
            for a in (F(3,2),F(3)):
                s=tilted_success(n,m,a)
                c=(1-s)/(n-m)
                tau,sigma=parameters(n,F(1),c,F(0))
                self.assertLess(c,F(1,n))
                self.assertEqual(optimal_mean(n,tau,sigma,s),m)
                law=tilt_law(n,m,a)
                self.assertGreaterEqual(min(conditional_margins(law,n,F(1),c).values()),0)
                self.assertEqual(information(law,n),information_formula(n,m,a))

    def test_both_rows_bind_at_preferred_middle_reliability(self):
        for n in range(2,6):
            for m in (F(1,2),F(3,2),F(n)-F(1,2)):
                s=tilted_success(n,m,F(2))
                tau,sigma=s/m,(1-s)/(n-m)
                c,d=(tau+sigma)/2,(tau-sigma)/2
                self.assertEqual(parameters(n,F(1),c,d),(tau,sigma))
                self.assertEqual(preferred_success(n,tau,sigma),s)
                self.assertEqual(optimal_mean(n,tau,sigma,s),m)
                margins=conditional_margins(tilt_law(n,m,F(2)),n,F(1),c)
                self.assertEqual(set(margins.values()),{d})

    def test_conjugate_inequality_exact_prime_log_signs(self):
        for n,t,a,q in product(range(2,5),range(1,4),(F(1),F(2),F(3)),
                                (F(0),F(1,4),F(1,2),F(3,4),F(1))):
            if t >= n:
                continue
            expression=defaultdict(F,binary_kl(q,F(t,n)))
            add_log(expression,a,-q)
            add_log(expression,1+(a-1)*F(t,n),F(1))
            self.assertTrue(log_nonnegative(clean(expression)))
            qt=q_t(n,t,a)
            equal=defaultdict(F,binary_kl(qt,F(t,n)))
            add_log(equal,a,-qt)
            add_log(equal,1+(a-1)*F(t,n),F(1))
            self.assertEqual(clean(equal),{})

    def test_scalar_equation_exact_rational_root_and_bracket(self):
        n,m,a=5,F(5,2),F(2)
        s=tilted_success(n,m,a)
        self.assertEqual(tilt_bracket(n,m,s),(a,a))
        tau,sigma=parameters(5,F(1),F(3,5),F(1,10))
        s=F(4,5)
        m=optimal_mean(5,tau,sigma,s)
        lo,hi=tilt_bracket(5,m,s,80)
        self.assertLessEqual(tilted_success(5,m,lo),s)
        self.assertGreaterEqual(tilted_success(5,m,hi),s)
        self.assertLess(hi-lo,F(1,10**20))
        # The unique positive optimum solves 7a^2-89a-168=0.
        self.assertLessEqual(7*lo*lo-89*lo-168,0)
        self.assertGreaterEqual(7*hi*hi-89*hi-168,0)
        self.assertNotEqual(isqrt(12625)**2,12625)

    def test_endpoint_and_zero_information_regimes(self):
        for n in range(2,6):
            tau,sigma=parameters(n,F(1),F(1,n),F(0))
            for s in (F(0),F(1,3),F(1)):
                m=optimal_mean(n,tau,sigma,s)
                self.assertEqual(m,n*s)
                self.assertEqual(information(tilt_law(n,m,F(1)),n),{})
            tau,sigma=parameters(n,F(1),F(1,5),F(1,5))
            self.assertEqual(minimum_success(n,tau,sigma),1)
            self.assertEqual(preferred_success(n,tau,sigma),F(1))
        tau,sigma=parameters(3,F(1),F(9,10),F(1,10))
        for s in (F(0),F(1,2),F(1)):
            m=optimal_mean(3,tau,sigma,s)
            self.assertEqual(m,s)
            self.assertEqual(tilt_bracket(3,m,s),(F(1),F(1)) if not s else (None,None))


if __name__ == '__main__':
    unittest.main()
