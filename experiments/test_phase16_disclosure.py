import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase16_disclosure import (partitions, volunteer_law,
    release_margins, partition_channel, best_balanced_partition,
    greedy_pair_channel, guessing)


class DisclosureTests(unittest.TestCase):
    def test_partition_enumerator(self):
        self.assertEqual([sum(1 for _ in partitions(list(range(n))))
                          for n in range(6)], [1, 1, 2, 5, 15, 52])

    def test_signed_slack_embedding_all_cells(self):
        v = (F(1, 3), F(2, 3), -F(1))
        for p in partitions(list(range(3))):
            actual = release_margins(v, partition_channel(p))
            scalar_safe = all(sum(v[i] for i in block) >= 0 for block in p)
            self.assertEqual(min(actual.values()) >= F(1, 10), scalar_safe)
        law, _ = volunteer_law(v)
        self.assertEqual(sum(law.values()), 1)
        self.assertEqual(min(release_margins(v, partition_channel(((0, 1, 2),))).values()), F(1, 10))

    def test_yes_no_three_partition_instances_exhaustively(self):
        for items, expected in (((4, 4, 5, 5, 6, 6), 2),
                                ((4, 4, 4, 6, 6, 6), 1)):
            v = tuple(F(a, 15) for a in items) + (-F(1),)*2
            best = best_balanced_partition(v)
            self.assertEqual(len(best), expected)
            self.assertGreaterEqual(min(release_margins(v, partition_channel(best)).values()), F(1, 10))
            self.assertEqual(guessing(partition_channel(best), (F(1, 8),)*8), F(expected, 8))

    def test_randomized_three_quarters_same_yes_no_instances(self):
        for items in ((4, 4, 5, 5, 6, 6), (4, 4, 4, 6, 6, 6)):
            v = tuple(F(a, 15) for a in items) + (-F(1),)*2
            channel = greedy_pair_channel(v)
            self.assertTrue(all(sum(row.values()) == 1 for row in channel.values()))
            self.assertEqual(guessing(channel, (F(1, 8),)*8), F(3, 4))
            self.assertGreaterEqual(min(release_margins(v, channel).values()), F(1, 10))
            # Each output has exactly one positive and one negative state.
            for y in {y for row in channel.values() for y in row}:
                support = [i for i in channel if channel[i].get(y, 0)]
                self.assertEqual(len(support), 2)
                self.assertEqual(sum(v[i]*channel[i].get(y, 0) for i in channel), 0)

    def test_nonuniform_transport_and_zero_coordinates(self):
        v = (F(1, 2), -F(1), F(0))
        prior = (F(1, 2), F(1, 4), F(1, 4))
        channel = greedy_pair_channel(v, prior)
        self.assertEqual(guessing(channel, prior), F(3, 4))
        self.assertGreaterEqual(min(release_margins(v, channel, prior).values()), F(1, 10))
        self.assertTrue(all(sum(row.values()) == 1 for row in channel.values()))

    def test_binary_perfect_privacy_equivalence(self):
        v = (F(1, 3), F(2, 3), -F(1))
        channel = greedy_pair_channel(v)
        for y in {y for row in channel.values() for y in row}:
            total = sum(channel[i].get(y, 0) for i in channel)
            posterior_x = sum((F(1, 2)+F(1, 4)*v[i])*channel[i].get(y, 0)
                              for i in channel)/total
            self.assertEqual(posterior_x, F(1, 2))


if __name__ == '__main__':
    unittest.main()
