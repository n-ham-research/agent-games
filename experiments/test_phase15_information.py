import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase15_information import (compose, row_partition, margins,
    odds_interval, worst_margins, safe_ratios, rr_posterior)

EMPTY = frozenset()
SINGLETONS = (frozenset({0}), frozenset({1}))


class InformationTests(unittest.TestCase):
    def test_random_signals_and_deterministic_partitions_differ(self):
        q = ((F(1), F(0)), (F(1, 2), F(1, 2)), (F(0), F(1)))
        decoder = ((F(1), F(0)), (F(0), F(1)))
        self.assertEqual(compose(q, decoder), q)
        self.assertEqual(row_partition(q), ((0,), (1,), (2,)))
        # A strict private refinement simulates exactly the same law.
        identity = tuple(tuple(F(i == j) for j in range(3)) for i in range(3))
        self.assertEqual(compose(identity, q), q)

    def test_safe_positive_margin_disclosures_do_not_join(self):
        joint, costs = {}, {}
        for state in product((0, 1), repeat=2):
            costs[state] = (F(3, 4), F(3, 4))
            if state == (0, 0):
                joint[state, EMPTY] = F(1, 4)
            else:
                for a in SINGLETONS:
                    joint[state, a] = F(1, 8)
        for bit in (0, 1):
            release = {w: {w[0][bit]: F(1)} for w in joint}
            self.assertEqual(min(margins(joint, costs, release, SINGLETONS).values()), F(1, 12))
        joined = {w: {w[0]: F(1)} for w in joint}
        self.assertEqual(min(margins(joint, costs, joined, SINGLETONS).values()), -F(1, 4))
        hidden = {w: {None: F(1)} for w in joint}
        self.assertGreaterEqual(min(margins(joint, costs, hidden, SINGLETONS).values()), F(1, 12))

    def test_safe_channel_convexity_and_postprocessing(self):
        joint = {(0, EMPTY): F(1, 5), (0, SINGLETONS[0]): F(2, 5),
                 (0, SINGLETONS[1]): F(2, 5)}
        costs = {0: (F(1, 2), F(1, 2))}
        # Independent disclosures, including an impossible output, cannot change obedience.
        release = {w: {'a': F(1, 3), 'b': F(2, 3), 'zero': F(0)} for w in joint}
        self.assertEqual(min(margins(joint, costs, release, SINGLETONS).values()), F(1, 6))
        self.assertTrue(all(k[-1] != 'zero' for k in margins(joint, costs, release, SINGLETONS)))

    def test_odds_endpoints_attained_by_full_randomized_response(self):
        for p, ratio in product((F(1, 5), F(1, 2), F(4, 5)),
                                (F(1), F(3, 2), F(2), F(4))):
            lower, upper = odds_interval(p, ratio)
            self.assertEqual(rr_posterior(p, ratio), lower)
            self.assertEqual(rr_posterior(p, ratio, True), upper)

    def test_local_obedience_thresholds_exact(self):
        for c in (F(1, 4), F(1, 2), F(3, 4)):
            delta = F(1, 20)
            rw, ra = safe_ratios(c, delta)
            self.assertEqual(worst_margins(c, delta, rw)[0], 0)
            self.assertEqual(worst_margins(c, delta, ra)[1], 0)
            self.assertLess(worst_margins(c, delta, rw+F(1, 10))[0], 0)
            self.assertLess(worst_margins(c, delta, ra+F(1, 10))[1], 0)
            self.assertEqual(worst_margins(c, delta, F(1)), (delta, delta))

    def test_sequential_likelihood_ratios_multiply(self):
        for p, ratio in product((F(1, 4), F(3, 5)), (F(3, 2), F(3))):
            twice = rr_posterior(rr_posterior(p, ratio), ratio)
            self.assertEqual(twice, odds_interval(p, ratio*ratio)[0])

    def test_type_privacy_does_not_hide_recommendation_randomness(self):
        joint = {(0, EMPTY): F(1, 5), (0, SINGLETONS[0]): F(2, 5),
                 (0, SINGLETONS[1]): F(2, 5)}
        costs = {0: (F(1, 2), F(1, 2))}
        hidden = {w: {None: F(1)} for w in joint}
        revealed = {w: {w[1]: F(1)} for w in joint}
        self.assertEqual(min(margins(joint, costs, hidden, SINGLETONS).values()), F(1, 6))
        self.assertEqual(min(margins(joint, costs, revealed, SINGLETONS).values()), -F(1, 2))
        # There is only one type-state, so every disclosure is type-private.
        self.assertEqual(len({w[0] for w in joint}), 1)

    def test_local_type_contingent_plan_exceeds_literal_blind_architecture(self):
        # Other agent works with probability 1/2 under its low-cost-only plan.
        B = F(2)
        low_gain, high_gain = B*F(1, 2)-F(1, 2), B*F(1, 2)-F(3, 2)
        self.assertGreater(low_gain, 0)
        self.assertLess(high_gain, 0)
        actual_kernel = ((F(1), F(0)), (F(0), F(1)))
        self.assertEqual(len(row_partition(actual_kernel)), 2)
        blind = ((F(1),), (F(1),))
        for prob in (F(0), F(1, 3), F(1)):
            emitted = compose(blind, ((prob, 1-prob),))
            self.assertEqual(emitted[0], emitted[1])


if __name__ == '__main__':
    unittest.main()
