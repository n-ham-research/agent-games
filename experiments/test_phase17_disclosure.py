import unittest
from fractions import Fraction as F
from experiments.phase15_information import margins
from experiments.phase16_disclosure import partitions
from experiments.phase17_disclosure import (guessing, safe, merge_by_guess,
    limited_garble, guessing_lp, multirow_law, factorized)


class MultipleRowDisclosureTests(unittest.TestCase):
    def test_multirow_common_task_all_deterministic_partitions(self):
        joint, costs, rows = multirow_law()
        best = F(0)
        for p in partitions(list(range(4))):
            labels = {state: j for j, block in enumerate(p) for state in block}
            release = {w: {labels[w[0]]: F(1)} for w in joint}
            actual = margins(joint, costs, release,
                             tuple(frozenset({i}) for i in range(3)))
            columns = [tuple(F(i in block, 4) for i in range(4)) for block in p]
            self.assertEqual(min(actual.values()) >= F(1, 10), safe(columns, rows))
            if safe(columns, rows):
                best = max(best, guessing(columns))
        self.assertEqual(best, F(1, 2))

    def test_scalar_aggregation_loses_independent_incentives(self):
        _, _, rows = multirow_law()
        columns = ((F(1, 4), F(0), F(1, 4), F(0)),
                   (F(0), F(1, 4), F(0), F(1, 4)))
        aggregate = tuple(a+b for a, b in zip(rows[0], rows[2]))
        self.assertTrue(safe(columns, (aggregate,)))
        self.assertFalse(safe(columns, rows))
        self.assertEqual(tuple(sum(r[i] for r in rows) for i in range(4)), (0,)*4)

    def test_arbitrary_message_splitting_and_exact_guess_merge(self):
        _, _, rows = multirow_law()
        columns = []
        for block in ((0, 1), (2, 3)):
            for share in (F(1, 7), F(2, 7), F(4, 7)):
                columns.append(tuple(share*F(i in block, 4) for i in range(4)))
        self.assertTrue(safe(columns, rows))
        merged = merge_by_guess(columns)
        self.assertEqual(len(merged), 2)
        self.assertEqual(guessing(columns), guessing(merged.values()))
        self.assertTrue(safe(merged.values(), rows))
        self.assertEqual(guessing(merged.values()), F(1, 2))

    def test_nontight_rows_merge_and_limited_alphabet(self):
        columns = ((F(2, 10), F(1, 10), F(0)),
                   (F(1, 10), F(2, 10), F(0)),
                   (F(0), F(0), F(4, 10)))
        rows = ((F(1), F(1), -F(0)), (F(0), F(0), F(1)))
        self.assertTrue(safe(columns, rows))
        value = guessing(columns)
        for k in (1, 2, 3):
            garbled = limited_garble(columns, k)
            self.assertLessEqual(len(garbled), k)
            self.assertTrue(safe(garbled.values(), rows))
            self.assertGreaterEqual(guessing(garbled.values()), F(k, 3)*value)
            for i in range(3):
                self.assertEqual(sum(c[i] for c in columns),
                                 sum(c[i] for c in garbled.values()))

    def test_lp_export_matches_actual_column_safety(self):
        _, _, rows = multirow_law()
        variables, objective, constraints = guessing_lp((F(1, 4),)*4, rows)
        self.assertEqual(len(variables), 16)
        z = {(i, g): F(0) for i, g in variables}
        for i in (0, 1):
            z[i, 0] = F(1, 4)
        for i in (2, 3):
            z[i, 2] = F(1, 4)
        self.assertEqual(sum(v*z[k] for k, v in objective.items()), F(1, 2))
        for coeff, relation, rhs in constraints:
            actual = sum(v*z[k] for k, v in coeff.items())
            self.assertTrue(actual == rhs if relation == '=' else actual >= rhs)

    def test_joint_redesign_full_disclosure_preserves_unconditional_law(self):
        joint = {}
        costs = {0: (F(1, 2), F(1, 2)), 1: (F(1, 2), F(1, 2))}
        for state, prior in ((0, F(1, 3)), (1, F(2, 3))):
            for worker in (0, 1):
                joint[state, frozenset({worker})] = prior/2
        release = {w: {w[0]: F(1)} for w in joint}
        actual = margins(joint, costs, release, (frozenset({0}), frozenset({1})))
        self.assertEqual(min(actual.values()), F(1, 2))
        self.assertEqual(sum(p for (s, a), p in joint.items() if a == frozenset({0})), F(1, 2))

    def test_independence_joint_feasible_set_is_nonconvex(self):
        first = ((F(1), F(0)), (F(0), F(0)))
        second = ((F(0), F(0)), (F(0), F(1)))
        self.assertTrue(factorized(first))
        self.assertTrue(factorized(second))
        mixed = tuple(tuple((first[i][j]+second[i][j])/2 for j in range(2)) for i in range(2))
        self.assertFalse(factorized(mixed))
        independent = ((F(1, 4), F(1, 4)), (F(1, 4), F(1, 4)))
        self.assertTrue(factorized(independent))
        self.assertEqual(tuple(map(sum, mixed)), tuple(map(sum, independent)))


if __name__ == '__main__':
    unittest.main()
