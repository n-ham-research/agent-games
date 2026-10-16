import unittest
from fractions import Fraction as R
from itertools import product
from experiments.phase16_hardness_audit import (
    bit_profiles, succeeds, utility, switch, all_obedience_rows,
    conditional_gains, payoff_vector, preprocess, subset_solutions,
    reduction, audit_law, law_statistics)


class IndependentHardnessAudit(unittest.TestCase):
    def test_preprocessing_preserves_all_small_degenerate_answers(self):
        for length in range(5):
            for items in product(range(1, 5), repeat=length):
                for target in range(8):
                    mapped, threshold = preprocess(items, target)
                    self.assertTrue(mapped)
                    self.assertTrue(all(0 < a < threshold for a in mapped))
                    self.assertEqual(bool(subset_solutions(items, target)),
                                     bool(subset_solutions(mapped, threshold)))

    def test_parity_equivalence_exhaustive_small_instances(self):
        for target in range(2, 6):
            for length in range(1, 4):
                for items in product(range(1, target), repeat=length):
                    weights, q, costs = reduction(items, target)
                    relevant = any(s[0] and succeeds(s, weights, q)
                                   and not succeeds(switch(s, 0), weights, q)
                                   for s in bit_profiles(len(weights)))
                    self.assertEqual(relevant, bool(subset_solutions(items, target)))
                    # Some successful pure NE is always explicitly known.
                    backstop = (0,)*(len(weights)-1)+(1,)
                    self.assertTrue(all(v >= 0 for v in all_obedience_rows(
                        {backstop: R(1)}, weights, q, costs).values()))

    def test_original_two_cost_witness_all_conditional_rows(self):
        for items, target in (((1, 1), 2), ((1, 2, 2), 3), ((2, 3, 4), 5)):
            for solution in subset_solutions(items, target):
                weights, q, costs = reduction(items, target, backstop_cost=R(3, 4))
                law = audit_law(items, target, solution, backstop_cost=R(3, 4))
                self.assertEqual(sum(law.values()), 1)
                self.assertEqual(payoff_vector(law, weights, q, costs)[0], 0)
                self.assertTrue(all(g >= 0 for g in conditional_gains(law, weights, q, costs).values()))

    def test_common_cost_witness_and_positive_conditional_margins(self):
        for items, target in (((1, 1), 2), ((1, 2, 2), 3), ((2, 3, 4), 5)):
            for solution in subset_solutions(items, target):
                weights, q, costs = reduction(items, target)
                for delta in (R(0), R(1, 20), R(1, 4), R(1, 2)):
                    law = audit_law(items, target, solution, delta=delta)
                    self.assertTrue(all(p > 0 for p in law.values()))
                    self.assertEqual(sum(law.values()), 1)
                    self.assertEqual(payoff_vector(law, weights, q, costs)[0], delta)
                    self.assertTrue(all(g >= delta for g in conditional_gains(law, weights, q, costs).values()))
                    self.assertTrue(all(v >= 0 for v in all_obedience_rows(law, weights, q, costs, delta).values()))

    def test_general_backstop_target_cost_law(self):
        items, target, solution = (1, 1), 2, (1, 1)
        for b in (R(1, 10), R(1, 3), R(1, 2), R(3, 4)):
            for c in (1-b, (2-b)/2):
                weights, q, costs = reduction(items, target, c, b)
                law = audit_law(items, target, solution, c, b)
                self.assertEqual(payoff_vector(law, weights, q, costs)[0], 0)
                self.assertTrue(all(v >= 0 for v in all_obedience_rows(law, weights, q, costs).values()))

    def test_no_instance_dual_gap_identity_without_any_ce_assumption(self):
        for items, target in (((2, 2), 3), ((1, 1), 3), ((2, 2, 2), 5)):
            self.assertFalse(subset_solutions(items, target))
            for b in (R(1, 2), R(3, 4)):
                weights, q, costs = reduction(items, target, backstop_cost=b)
                n, r = len(weights), len(weights)-1
                for s in bit_profiles(n):
                    law = {s: R(1)}
                    rows = all_obedience_rows(law, weights, q, costs)
                    self.assertEqual(rows[0, 1], -costs[0]*s[0])
                    self.assertEqual(utility(s, weights, q, costs, 0),
                        1-b+b*s[r]+rows[r, 0]+rows[0, 1])

    def test_positive_margin_no_gap_identity(self):
        weights, q, costs = reduction((2, 2), 3)
        n, r = len(weights), len(weights)-1
        for delta in (R(0), R(1, 4), R(1, 2)):
            for s in bit_profiles(n):
                rows = all_obedience_rows({s: R(1)}, weights, q, costs, delta)
                # NO work recommendations impossible at positive probability:
                self.assertEqual(rows[0, 1], -(R(1, 2)+delta)*s[0])
                if s[0] == 0:
                    self.assertEqual(utility(s, weights, q, costs, 0),
                        R(1, 2)+delta+(R(1, 2)-delta)*s[r]+rows[r, 0])

    def test_gap_constants_approximate_obedience_and_value(self):
        # Homogeneous NO dual certificate gives u >= 1/2 - 2 eta.
        eta, optimization_error = R(1, 32), R(1, 8)
        self.assertGreater(R(1, 2)-2*eta, optimization_error)
        # Strict two-sided value error below one quarter leaves a separator.
        value_error = R(1, 5)
        self.assertLess(value_error, R(1, 2)-value_error)


if __name__ == '__main__':
    unittest.main()
