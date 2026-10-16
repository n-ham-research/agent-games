import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase15_succinct import (
    coalitions, threshold_dags, coverage_dags, path_labels, law_to_flows,
    decompose_flows, threshold_gain, coverage_gain, flow_statistics,
    direct_statistics, subset_sum_gadget, zero_witness)


class SuccinctTaskChecks(unittest.TestCase):
    def test_threshold_dags_partition_every_pure_profile(self):
        for weights in product(range(1, 4), repeat=3):
            dags = threshold_dags(weights)
            found = []
            for total, edges in dags.items():
                labels = path_labels(edges, 3, 0)
                self.assertTrue(all(sum(weights[i] for i in a) == total for a in labels))
                found.extend(labels)
            self.assertCountEqual(found, coalitions(3))

    def test_threshold_conditional_coefficients_match_all_toggles(self):
        costs = (F(1, 4), F(1, 2), F(3, 4))
        for weights in product(range(1, 4), repeat=3):
            for quota in range(1, sum(weights)+1):
                wins = lambda a: sum(weights[i] for i in a) >= quota
                for active in coalitions(3):
                    total = sum(weights[i] for i in active)
                    direct = direct_statistics({active: F(1)}, 3, wins, costs, delta=F(1, 20))
                    for i in range(3):
                        bit = int(i in active)
                        self.assertEqual(direct[3][i, bit], threshold_gain(
                            total, i, bit, weights, quota, costs, delta=F(1, 20)))

    def test_threshold_flow_projection_and_exact_reconstruction(self):
        weights, costs, quota = (2, 2, 3, 4), (F(1, 3),)*4, 6
        step = lambda i, s, a: s+a*weights[i]
        law = {a: F(j+1, 136) for j, a in enumerate(coalitions(4))}
        flows = law_to_flows(law, 4, 0, step)
        restored = decompose_flows(flows, 4, 0)
        direct = direct_statistics(law, 4, lambda a: sum(weights[i] for i in a) >= quota, costs)
        compressed = flow_statistics(flows, 4, lambda total: total >= quota,
            lambda total, i, a: threshold_gain(total, i, a, weights, quota, costs), costs)
        self.assertEqual(direct, compressed)
        self.assertEqual(direct, direct_statistics(restored, 4,
            lambda a: sum(weights[i] for i in a) >= quota, costs))
        self.assertLessEqual(len(restored), len(flows))

    def test_coverage_capped_counts_suffice_for_all_toggles(self):
        masks_list = [frozenset(j for j in range(2) if mask >> j & 1) for mask in range(4)]
        costs = (F(1, 4), F(1, 2), F(3, 4))
        for masks in product(masks_list, repeat=3):
            wins = lambda a: set().union(*(masks[i] for i in a)) == {0, 1}
            dags = coverage_dags(masks, 2)
            found = []
            for counts, edges in dags.items():
                for active in path_labels(edges, 3, (0, 0)):
                    found.append(active)
                    direct = direct_statistics({active: F(1)}, 3, wins, costs)
                    for i in range(3):
                        bit = int(i in active)
                        self.assertEqual(direct[3][i, bit], coverage_gain(counts, i, bit, masks, costs))
            self.assertCountEqual(found, coalitions(3))

    def test_coverage_flow_reconstruction(self):
        masks = (frozenset({0}), frozenset({0, 1}), frozenset({1}), frozenset({0}))
        step = lambda i, s, a: tuple(min(2, s[j]+a*int(j in masks[i])) for j in range(2))
        law = {a: F(j+1, 136) for j, a in enumerate(coalitions(4))}
        costs = (F(1, 2),)*4
        flows = law_to_flows(law, 4, (0, 0), step)
        wins = lambda a: set().union(*(masks[i] for i in a)) == {0, 1}
        direct = direct_statistics(law, 4, wins, costs)
        self.assertEqual(direct, flow_statistics(flows, 4, all,
            lambda t, i, a: coverage_gain(t, i, a, masks, costs), costs))
        self.assertEqual(direct, direct_statistics(decompose_flows(flows, 4, (0, 0)), 4, wins, costs))

    def test_subset_sum_gap_gadget_pivotality_and_yes_witnesses(self):
        checked_yes = checked_no = 0
        for target in range(2, 6):
            for length in range(1, 4):
                for items in product(range(1, target), repeat=length):
                    weights, quota, costs = subset_sum_gadget(items, target)
                    n = len(weights)
                    wins = lambda a: sum(weights[i] for i in a) >= quota
                    solutions = [a for a in coalitions(length) if sum(items[i] for i in a) == target]
                    pivotal = [a for a in coalitions(n) if 0 in a and wins(a) and not wins(a-{0})]
                    self.assertEqual(bool(solutions), bool(pivotal))
                    if solutions:
                        checked_yes += 1
                        for selected in solutions:
                            law = zero_witness(items, target, selected)
                            stats = direct_statistics(law, n, wins, costs)
                            self.assertEqual(stats[2][0], 0)
                            self.assertTrue(all(v >= 0 for v in stats[3].values()))
                    else:
                        checked_no += 1
                        # Work margin is always negative; hence x_target=0 in CE.
                        for a in coalitions(n):
                            if 0 in a:
                                self.assertEqual(direct_statistics({a: F(1)}, n, wins, costs)[3][0, 1], -F(1, 2))
        self.assertGreater(checked_yes, 0)
        self.assertGreater(checked_no, 0)

    def test_no_instance_dual_certificate_includes_approximate_obedience(self):
        weights, quota, costs = subset_sum_gadget((2, 2), 3)
        n, r = len(weights), len(weights)-1
        wins = lambda a: sum(weights[i] for i in a) >= quota
        # Identity holds columnwise, hence for every possibly nonobedient law.
        for active in coalitions(n):
            stats = direct_statistics({active: F(1)}, n, wins, costs)
            self.assertEqual(stats[2][0], F(1, 4)+F(3, 4)*int(r in active)
                             + stats[3][r, 0]+stats[3][0, 1])
        eta = F(1, 64)
        self.assertEqual(F(1, 4)-2*eta, F(7, 32))
        self.assertGreater(F(7, 32), F(1, 16))

    def test_binary_weight_boundary_and_singleton_floor_coefficients(self):
        weights, quota, costs = subset_sum_gadget((2, 2), 3)  # NO
        n, singleton = len(weights), len(weights)-1
        for a in coalitions(n):
            # Singleton expected payoff minus its always-work security value.
            u_r = F(int(sum(weights[i] for i in a) >= quota))-costs[singleton]*int(singleton in a)
            self.assertEqual(u_r-F(1, 4),
                (F(3, 4) if sum(weights[i] for i in a) >= quota else -F(1, 4))
                -F(3, 4)*int(singleton in a))
        # A representative NO instance has no target-pivotal profile.
        self.assertFalse(any(0 in a and sum(weights[i] for i in a) >= quota
                             and sum(weights[i] for i in a-{0}) < quota for a in coalitions(n)))


if __name__ == '__main__':
    unittest.main()
