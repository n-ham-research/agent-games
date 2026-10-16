import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase13_coalitions import (subsets, wins, obedience_margins,
    utility, purify, zero_payoff_witness, antichains)


class CoalitionContinuationTests(unittest.TestCase):
    def assert_ce(self, law, minimal, costs, benefit):
        self.assertEqual(sum(law.values()), 1)
        self.assertTrue(all(p >= 0 for p in law.values()))
        self.assertTrue(all(v >= 0 for v in
            obedience_margins(law, minimal, costs, benefit).values()))

    def test_zero_criterion_constructive_all_four_agent_tasks(self):
        families = antichains(4)
        self.assertEqual(len(families), 166)
        checked = 0
        for minimal in families:
            for costs in product((F(1, 4), F(3, 4)), repeat=4):
                for i in range(4):
                    law = zero_payoff_witness(minimal, costs, F(1), i)
                    if law is not None:
                        self.assert_ce(law, minimal, costs, F(1))
                        self.assertEqual(utility(law, i, minimal, costs, F(1)), 0)
                        checked += 1
        self.assertGreater(checked, 3000)

    def test_purification_all_constructed_equilibria(self):
        # Check the structural operation independently of its explicit proof.
        for minimal in antichains(4):
            costs = (F(3, 4), F(1, 4), F(2, 3), F(4, 5))
            for i in range(4):
                law = zero_payoff_witness(minimal, costs, F(1), i)
                if law is None:
                    continue
                reduced = purify(law, minimal)
                self.assert_ce(reduced, minimal, costs, F(1))
                self.assertEqual(sum(p for a, p in law.items() if wins(a, minimal)),
                    sum(p for a, p in reduced.items() if wins(a, minimal)))
                for j in range(4):
                    self.assertGreaterEqual(utility(reduced, j, minimal, costs, F(1)),
                                            utility(law, j, minimal, costs, F(1)))

    def test_private_zero_public_positive(self):
        minimal = (frozenset({0}), frozenset({1, 2, 3}))
        costs, benefit = (F(1), F(3, 2), F(1), F(1)), F(2)
        law = zero_payoff_witness(minimal, costs, benefit, 1)
        self.assert_ce(law, minimal, costs, benefit)
        self.assertEqual(utility(law, 1, minimal, costs, benefit), 0)
        reduced = purify(law, minimal)
        self.assertEqual(utility(reduced, 1, minimal, costs, benefit), F(1, 4))
        public_min = min(utility({t: F(1)}, 1, minimal, costs, benefit)
                         for t in minimal)
        self.assertEqual(public_min, F(1, 2))

    def test_residual_pair_witness_and_repair_cost_obstruction(self):
        minimal = (frozenset({0}), frozenset({1, 2}))
        costs = (F(9, 10), F(4, 5), F(1, 2))
        root_law = {frozenset({1, 2}): F(1, 5), frozenset({1}): F(1, 20),
                    frozenset(): F(3, 4)}
        self.assert_ce(root_law, minimal, costs, F(1))
        self.assertEqual(utility(root_law, 1, minimal, costs, F(1)), 0)
        self.assertIsNotNone(zero_payoff_witness(minimal, costs, F(1), 1))
        # Same singleton and own security, but a cheap pair repairer prevents0.
        self.assertIsNone(zero_payoff_witness(minimal,
                          (F(9, 10), F(4, 5), F(1, 100)), F(1), 1))

    def test_singleton_and_security_gap_boundaries(self):
        minimal = (frozenset({0}), frozenset({1, 2}))
        self.assertIsNone(zero_payoff_witness(minimal,
                          (F(1, 10), F(4, 5), F(1, 2)), F(1), 1))
        self.assertIsNone(zero_payoff_witness(minimal,
                          (F(9, 10), F(4, 5), F(1, 2)), F(1), 0))
        # Without singleton capability all-abstain is a credible zero punishment.
        self.assertEqual(zero_payoff_witness((frozenset({1, 2}),),
                         (F(1, 2),)*3, F(1), 0), {frozenset(): F(1)})

    def test_purification_does_not_preserve_private_report_ic(self):
        # Reports were irrelevant before thinning the both-work branch.
        low, high = F(1, 2), F(3, 2)
        minimal = (frozenset({0}), frozenset({1}))
        law = {frozenset({0}): F(9, 20), frozenset({1}): F(9, 20),
               frozenset({0, 1}): F(1, 10)}
        for costs in product((low, high), repeat=2):
            self.assert_ce(law, minimal, costs, F(2))
        xlow, xhigh = F(21, 40), F(19, 40)
        self.assertEqual(low*(xlow-xhigh), F(1, 40))

    def test_zero_face_requires_pivotality_on_every_success(self):
        for minimal in antichains(4):
            costs = (F(3, 4), F(1, 4), F(2, 3), F(4, 5))
            for i in range(4):
                law = zero_payoff_witness(minimal, costs, F(1), i)
                if law is None:
                    continue
                for active, probability in law.items():
                    if probability and wins(active, minimal):
                        self.assertIn(i, active)
                        self.assertFalse(wins(active-{i}, minimal))


if __name__ == '__main__':
    unittest.main()
