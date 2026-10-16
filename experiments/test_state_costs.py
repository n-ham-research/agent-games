import unittest
from fractions import Fraction

from state_costs import (minimum_tracking_cost, successful_primary_words,
                         one_state_controllers, two_state_controller,
                         accepted_sequence, split_restricted_cost)


class StateCostTests(unittest.TestCase):
    def test_fixed_actuators_and_checkpoint_timing(self):
        c = Fraction(7, 3)
        for t in range(21):
            self.assertEqual(minimum_tracking_cost(t, (1,), c), (t // 2) * c)
            self.assertEqual(minimum_tracking_cost(t, (3,), c), ((t + 1) // 2) * c)
            self.assertEqual(minimum_tracking_cost(t, (1,), c, checkpoints=False),
                             ((t // 2) % 2) * c)

    def test_complete_primary_word_enumeration(self):
        for t in range(11):
            words = successful_primary_words(t)
            self.assertEqual(words, [tuple(two_state_controller(t))])
            self.assertEqual(minimum_tracking_cost(t, (1, 3)), 0)
        self.assertEqual(one_state_controllers(2), {1: False, 3: False})
        self.assertTrue(accepted_sequence(two_state_controller(100)))

    def test_reverse_actuation_price(self):
        for c in (Fraction(1, 3), Fraction(2), Fraction(7, 2)):
            for d in (Fraction(0), Fraction(1, 2), Fraction(3)):
                for t in range(13):
                    self.assertEqual(minimum_tracking_cost(t, (1, 3), c, {3: d}),
                                     (t // 2) * min(c, d))

    def test_split_extension_still_can_cost(self):
        for t in range(15):
            self.assertEqual(split_restricted_cost(t), t)
        # Both odd C4 lifts fail to have order two; contrast split C2 x C2.
        self.assertEqual({(2 * h) % 4 for h in (1, 3)}, {2})
        self.assertEqual(((1 + 1) % 2, (0 + 0) % 2), (0, 0))

    def test_unreset_failures_and_role_only_observation(self):
        for t in range(25):
            states = [j % 4 for j in range(1, t + 1)]
            failures = sum(x // 2 != 0 for x in states)
            self.assertEqual(failures, 2 * (t // 4) + max(0, t % 4 - 1))
            self.assertTrue(all(x % 2 == j % 2
                                for j, x in enumerate(states, 1)))


if __name__ == '__main__':
    unittest.main()
