import unittest
from fractions import Fraction as F
from itertools import product
from experiments.allocation_information import (
    assignment_rows, contrasts, row_swap_operator, observations, maximizers,
    rank, is_task_sufficient, choose_noisy, regret,
)


class AllocationInformationTests(unittest.TestCase):
    def test_assignment_dimension_and_structural_ranks(self):
        for n in range(2, 6):
            rows = assignment_rows(n)
            b, t = contrasts(rows), row_swap_operator(n)
            self.assertEqual(rank(b), (n-1)**2)
            self.assertEqual(rank(t), n)
            self.assertTrue(is_task_sufficient(rows, b))
        self.assertTrue(is_task_sufficient(assignment_rows(2), row_swap_operator(2)))
        self.assertFalse(is_task_sufficient(assignment_rows(3), row_swap_operator(3)))

    def test_incomparability_on_same_assignment_model(self):
        rows = assignment_rows(3)
        b, t = contrasts(rows), row_swap_operator(3)
        zero, constant_row = [0]*9, [1]*3+[0]*6
        self.assertEqual(observations(b, zero), observations(b, constant_row))
        self.assertNotEqual(observations(t, zero), observations(t, constant_row))
        plus, minus = [0]*6+[1, 0, 0], [0]*6+[-1, 0, 0]
        self.assertEqual(observations(t, plus), observations(t, minus))
        self.assertFalse(maximizers(rows, plus) & maximizers(rows, minus))
        self.assertEqual(rank(b+t), 5)  # 4+3 minus two common contrasts

    def test_rectangle_measurements_recover_all_assignment_contrasts(self):
        n = 3
        rectangles = []
        for i in range(n-1):
            for j in range(n-1):
                row = [0]*(n*n)
                for a, z in ((i*n+j, 1), (i*n+n-1, -1),
                             ((n-1)*n+j, -1), (n*n-1, 1)):
                    row[a] += z
                rectangles.append(tuple(row))
        self.assertTrue(is_task_sufficient(assignment_rows(n), rectangles))
        self.assertEqual(rank(rectangles), 4)

    def test_bounded_noise_regret_and_sharp_binary_tie(self):
        scores = [(0, 0), (2, -1), (-1, 1)]
        eps = F(1, 2)
        # infinity observation norm; dual norm is one-norm
        k = max(sum(abs(x-y) for x, y in zip(a, b))
                for a in scores for b in scores)
        for truth in product((F(-1), F(0), F(1)), repeat=2):
            for e in product((-eps, F(0), eps), repeat=2):
                y = tuple(x+z for x, z in zip(truth, e))
                d = choose_noisy(scores, y)
                self.assertLessEqual(regret(scores, truth, d), eps*k)
        binary = [(0, 0), (2, -1)]
        d = choose_noisy(binary, (0, 0))
        truth = (eps, -eps) if d == 0 else (-eps, eps)
        self.assertEqual(regret(binary, truth, d), 3*eps)

    def test_each_assignment_requires_its_own_message(self):
        for n in range(2, 5):
            rows = assignment_rows(n)
            for i, w in enumerate(rows):
                self.assertEqual(maximizers(rows, w), {i})

    def test_private_report_deviation(self):
        # Other type truthful and uniform; tie gets 1/2.
        def chance(report):
            return sum((F(1) if report > other else F(1, 2)
                        if report == other else F(0)) / 2 for other in (0, 1))
        self.assertEqual(chance(0), F(1, 4))
        self.assertEqual(chance(1), F(3, 4))


if __name__ == '__main__':
    unittest.main()
