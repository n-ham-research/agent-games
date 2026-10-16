import unittest
from fractions import Fraction as Q
from itertools import product
from experiments.phase12_compact import (
    bits, rotate, quarter_turn, sym_value, payoff, independent_expectation,
    mp_regrets, epsilon_for_counting, action_orbits, sum_product,
)


class CompactRepresentationChecks(unittest.TestCase):
    def test_typed_generators_exact_and_three_action_orbits(self):
        # All n2 functions, plus asymmetric n3 functions distinguish rotation
        # direction (n2 alone would not). Every pure profile, both generators.
        for n in (2, 3):
            zs = list(bits(n))
            tables = bits(2**n) if n == 2 else ((1,0,0,0,0,0,0,0), (0,1,0,1,1,0,0,0))
            for table in tables:
                truth = dict(zip(zs, table))
                for s in bits(2*n+1):
                    old = payoff(s, truth, Q(3, 8))
                    rs = rotate(s[:-1]) + (s[-1],)
                    ts = quarter_turn(s[:-1]) + (s[-1],)
                    self.assertEqual(payoff(rs, truth, Q(3,8)),
                                     (old[n-1],) + old[:n-1] + (old[2*n-1],) + old[n:2*n-1] + old[-1:])
                    self.assertEqual(payoff(ts, truth, Q(3,8)), old[n:2*n] + old[:n] + old[-1:])
        for n in range(2, 9):
            self.assertEqual(sorted(map(len, action_orbits(n))), [1, 1, 4*n])

    def test_uniform_expectation_equals_count_for_all_small_circuits(self):
        n = 2
        xs = list(bits(n))
        for table in bits(2**n):
            truth = dict(zip(xs, table))
            got = independent_expectation(lambda z: sym_value(z, truth), [Q(1,2)]*(2*n))
            self.assertEqual(got, Q(sum(table), 2**n))

    def test_mp_regret_identity_exact_grid(self):
        for p, q in product((Q(j,16) for j in range(17)), repeat=2):
            ra, rb = mp_regrets(p,q)
            self.assertGreaterEqual(ra, 0)
            self.assertGreaterEqual(rb, 0)
            self.assertEqual(ra+rb, abs(p-Q(1,2))+abs(q-Q(1,2)))

    def test_precision_separates_both_count_directions(self):
        for n in range(2, 32):
            eps = epsilon_for_counting(n)
            gap = Q(1, 2**(n+1))
            payoff_error = 2*n*eps
            # If decision chooses the incorrect side with >=1/2 mass,
            # it violates epsilon-Nash even at maximal permitted input error.
            self.assertGreater((gap-payoff_error)/2, eps)
            self.assertLess(eps/(gap-payoff_error), Q(1,2))

    def test_decision_flip_certificate_iff_unsatisfiable(self):
        n = 2
        for table in bits(2**n):
            truth = dict(zip(bits(n), table))
            is_auto = all(payoff(z+(0,), truth, Q(0)) == payoff(z+(1,), truth, Q(0))
                          for z in bits(2*n))
            self.assertEqual(is_auto, not any(table))

    def test_decomposable_conditional_expectations(self):
        # A global degree-three interaction represented by disjoint products,
        # including signed coefficients and missing scopes at a sum node.
        node = ('sum', (
            ('product', (('leaf',0,(0,Q(-3,2))),
                         ('leaf',1,(1,0)), ('leaf',2,(2,-1)))),
            ('leaf', 1, (Q(1,3), Q(4,3))),
        ))
        ps = [Q(1,4), Q(2,3), Q(3,5)]
        for evidence in ({}, {0:0}, {0:1}, {1:1}):
            def evaluate(z):
                values = dict(enumerate(z))
                values.update(evidence)
                return Q(-3,2)*values[0]*(1-values[1])*(2-3*values[2])+Q(1,3)+values[1]
            exact = independent_expectation(evaluate, ps)
            self.assertEqual(sum_product(node, ps, evidence), exact)

    def test_empty_scope_repeated_squaring_rejected(self):
        node = ('product', (('const', Q(1,2)), ('const', Q(1,2))))
        with self.assertRaises(ValueError):
            sum_product(node, [])

    def test_overlapping_product_substitution_rejected(self):
        # E[X^2]=E[X], whereas multiplying marginal expectations gives p^2.
        node = ('product', (('leaf',0,(0,1)), ('leaf',0,(0,1))))
        with self.assertRaises(ValueError):
            sum_product(node, [Q(1,3)])


if __name__ == '__main__':
    unittest.main()
