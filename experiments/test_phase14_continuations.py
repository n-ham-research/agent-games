import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase13_coalitions import (antichains, subsets, utility, wins,
    zero_payoff_witness)
from experiments.phase14_continuations import (anchored_thinning,
    conditional_margin_slacks, blind_endpoint_slacks, blind_frontier,
    frontier_payoff, bayesian_margin_slacks, canonical_region_lp)


class ContinuationRegionTests(unittest.TestCase):
    def test_protected_payoff_projection_all_four_agent_tasks(self):
        costs, benefit = (F(3, 4), F(1, 4), F(2, 3), F(4, 5)), F(1)
        for minimal in antichains(4):
            for target in range(4):
                law = zero_payoff_witness(minimal, costs, benefit, target)
                if law is None:
                    continue
                for protected in subsets(4):
                    new = anchored_thinning(law, minimal, protected)
                    self.assertTrue(all(v >= 0 for v in conditional_margin_slacks(
                        new, minimal, costs, benefit).values()))
                    for i in protected:
                        self.assertEqual(utility(new, i, minimal, costs, benefit),
                                         utility(law, i, minimal, costs, benefit))
                    for a in new:
                        if wins(a, minimal):
                            for j in a-protected:
                                self.assertFalse(wins(a-{j}, minimal))
                        else:
                            self.assertTrue(a <= protected)

    def test_blind_robust_envelope_parameter_family(self):
        minimal = (frozenset({0}), frozenset({1, 2, 3}))
        lower = (F(4, 5), F(1, 5), F(1, 3), F(1, 4))
        upper = (F(9, 10), F(4, 5), F(2, 3), F(3, 4))
        for delta in (F(0), F(1, 20), F(1, 10), F(1, 5)):
            law, s, x = blind_frontier(minimal, lower, upper, F(1), 1,
                                       frozenset({1, 2, 3}), delta)
            self.assertEqual(sum(law.values()), 1)
            self.assertTrue(all(p >= 0 for p in law.values()))
            self.assertTrue(all(v >= 0 for v in blind_endpoint_slacks(
                law, minimal, lower, upper, F(1), delta).values()))
            # Check every endpoint type profile directly, rather than only
            # reusing the endpoint-reduction implementation.
            for costs in product(*zip(lower, upper)):
                self.assertTrue(all(v >= 0 for v in conditional_margin_slacks(
                    law, minimal, costs, F(1), delta).values()))
                self.assertEqual(utility(law, 1, minimal, costs, F(1)),
                                  frontier_payoff(s, x, costs[1], F(1)))

    def test_information_gap_and_positive_margin_numbers(self):
        minimal = (frozenset({0}), frozenset({1, 2, 3}))
        lower = (F(9, 10), F(1, 5), F(1, 2), F(1, 2))
        upper = (F(9, 10), F(4, 5), F(1, 2), F(1, 2))
        for delta, expected in ((F(0), (F(3, 40), F(0))),
                                (F(1, 20), (F(39, 340), F(3, 340)))):
            law, s, x = blind_frontier(minimal, lower, upper, F(1), 1,
                                       frozenset({1, 2, 3}), delta)
            self.assertEqual(tuple(frontier_payoff(s, x, c, F(1))
                                   for c in (lower[1], upper[1])), expected)
        informed = zero_payoff_witness(minimal, lower, F(1), 1)
        self.assertIsNotNone(informed)
        self.assertEqual(utility(informed, 1, minimal, lower, F(1)), 0)

    def test_robust_anchored_thinning(self):
        minimal = (frozenset({0}), frozenset({1, 2, 3}))
        costs = (F(9, 10), F(4, 5), F(1, 2), F(1, 2))
        delta = F(1, 20)
        law, _, _ = blind_frontier(minimal, costs, costs, F(1), 1,
                                  frozenset({1, 2, 3}), delta)
        for protected in subsets(4):
            new = anchored_thinning(law, minimal, protected)
            self.assertTrue(all(v >= 0 for v in conditional_margin_slacks(
                new, minimal, costs, F(1), delta).values()))
            for i in protected:
                self.assertEqual(utility(new, i, minimal, costs, F(1)),
                                 utility(law, i, minimal, costs, F(1)))

    def test_blind_endpoint_ignorance_is_substantive(self):
        minimal = (frozenset({0}), frozenset({1, 2, 3}))
        low = (F(9, 10), F(1, 5), F(1, 2), F(1, 2))
        high = (F(9, 10), F(4, 5), F(1, 2), F(1, 2))
        informed_low = zero_payoff_witness(minimal, low, F(1), 1)
        # Reusing low-cost-informed recommendations for a possible high type
        # violates its worker obedience; a mean-cost substitution is not free.
        self.assertLess(conditional_margin_slacks(informed_low, minimal, high,
                                                  F(1))[1, 1], 0)

    def test_thinning_margin_cost_bound_is_necessary_in_general(self):
        minimal = (frozenset({0, 1}), frozenset({2, 3}))
        costs = (F(1, 10), F(2, 5), F(2, 5), F(2, 5))
        law = {frozenset({0, 1}): F(1, 2),
               frozenset({0, 2, 3}): F(1, 2)}
        delta = F(1, 5)
        self.assertTrue(all(v >= 0 for v in conditional_margin_slacks(
            law, minimal, costs, F(1), delta).values()))
        reduced = anchored_thinning(law, minimal, frozenset())
        self.assertLess(conditional_margin_slacks(reduced, minimal, costs,
                                                 F(1), delta)[0, 0], 0)

    def test_private_type_pooling_invalidates_cellwise_singleton_floor(self):
        minimal = (frozenset({0}), frozenset({1, 2, 3}))
        low = (F(9, 10), F(1, 5), F(1, 2), F(1, 2))
        high = (F(9, 10), F(4, 5), F(1, 2), F(1, 2))
        kernel = {low: {frozenset(): F(1)},
                  high: {frozenset({1, 2, 3}): F(1, 5),
                         frozenset({1}): F(1, 20), frozenset(): F(3, 4)}}
        prior = {low: F(1, 2), high: F(1, 2)}
        self.assertTrue(all(v >= 0 for v in bayesian_margin_slacks(
            kernel, prior, minimal, F(1)).values()))
        for costs in (low, high):
            self.assertEqual(utility(kernel[costs], 1, minimal, costs, F(1)), 0)
        # Publicly revealing the low state makes the singleton repair shutdown.
        self.assertLess(conditional_margin_slacks(kernel[low], minimal, low,
                                                  F(1))[0, 0], 0)

    def test_projected_region_lp_columns_and_coefficients(self):
        costs, benefit = (F(3, 4), F(1, 4), F(2, 3), F(4, 5)), F(1)
        for minimal in antichains(4):
            for protected in (frozenset({0}), frozenset({0, 2})):
                lp = canonical_region_lp(minimal, costs, benefit, protected)
                self.assertLessEqual(len(lp['columns']),
                                     (len(minimal)+1)*(2**len(protected)))
                # Every full action-table column normalizes into the generated
                # extended formulation; no original coalition is assumed feasible.
                for a in subsets(4):
                    image = anchored_thinning({a: F(1)}, minimal, protected)
                    self.assertTrue(set(image) <= set(lp['columns']))
                for target in protected:
                    law = zero_payoff_witness(minimal, costs, benefit, target)
                    if law is None:
                        continue
                    law = anchored_thinning(law, minimal, protected)
                    vector = tuple(law.get(a, F(0)) for a in lp['columns'])
                    for key, row in lp['obedience_rows'].items():
                        self.assertEqual(sum(x*y for x, y in zip(vector, row)),
                            conditional_margin_slacks(law, minimal, costs, benefit)[key])
                    self.assertEqual(sum(x*y for x, y in zip(vector,
                        lp['protected_payoffs'][target])),
                        utility(law, target, minimal, costs, benefit))

    def test_simultaneous_security_minima_can_coincide(self):
        minimal = (frozenset({0}), frozenset({1}))
        costs = (F(1, 2), F(1, 2))
        law = {a: F(1, 4) for a in subsets(2)}
        self.assertTrue(all(v >= 0 for v in conditional_margin_slacks(
            law, minimal, costs, F(1)).values()))
        self.assertEqual([utility(law, i, minimal, costs, F(1)) for i in range(2)],
                         [F(1, 2), F(1, 2)])

    def test_upper_cost_saturation_branch(self):
        minimal = (frozenset({0}), frozenset({1, 2, 3}))
        costs = (F(1, 10), F(1, 5), F(1, 2), F(1, 2))
        law, s, x = blind_frontier(minimal, costs, costs, F(1), 1,
                                   frozenset({1, 2, 3}))
        self.assertEqual((s, x), (F(9, 10), F(1)))
        self.assertEqual(utility(law, 1, minimal, costs, F(1)), F(7, 10))


if __name__ == '__main__':
    unittest.main()
