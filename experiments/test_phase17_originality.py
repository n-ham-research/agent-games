import unittest
from fractions import Fraction as F
from itertools import combinations
from experiments.phase17_originality import (
    graph_workers, covers, perfect_matching, direct_gain, law_coordinates,
    all_subsets, read_twice_occurrences)


class MatchingFaceChecks(unittest.TestCase):
    def test_global_supporting_inequality_for_every_small_coalition(self):
        for vertices in (2, 4, 6):
            edges = graph_workers(vertices)
            m = vertices//2
            for active in all_subsets(len(edges)):
                self.assertGreaterEqual(len(active)-m*int(covers(active, edges, vertices)), 0)

    def test_face_success_and_cardinality_exactly_perfect_matchings(self):
        for vertices in (2, 4, 6, 8):
            edges = graph_workers(vertices)
            count = 0
            for subset in combinations(range(len(edges)), vertices//2):
                active = frozenset(subset)
                self.assertEqual(covers(active, edges, vertices),
                                 perfect_matching(active, edges, vertices))
                if covers(active, edges, vertices):
                    count += 1
            expected = 1
            for j in range(1, vertices, 2):
                expected *= j
            self.assertEqual(count, expected)

    def test_every_face_vertex_has_maximum_conditional_margin(self):
        for vertices in (4, 6):
            edges = graph_workers(vertices)
            for subset in combinations(range(len(edges)), vertices//2):
                active = frozenset(subset)
                if perfect_matching(active, edges, vertices):
                    for i in range(len(edges)):
                        self.assertEqual(direct_gain(active, i, edges, vertices), F(1, 2))

    def test_rational_mixture_affine_recovery_and_no_product_assumption(self):
        vertices, edges = 4, graph_workers(4)
        matchings = [frozenset(a) for a in combinations(range(len(edges)), 2)
                     if perfect_matching(frozenset(a), edges, vertices)]
        law = {a: F(j+1, 6) for j, a in enumerate(matchings)}
        s, x, u = law_coordinates(law, edges, vertices)
        self.assertEqual(s, 1)
        self.assertEqual(sum(x), 2)
        self.assertEqual(x, tuple(2*(1-v) for v in u))
        for i in range(len(edges)):
            for rec in (0, 1):
                mass = sum(p for a, p in law.items() if int(i in a) == rec)
                gain = sum(p*direct_gain(a, i, edges, vertices)
                           for a, p in law.items() if int(i in a) == rec)
                self.assertEqual(gain, mass/2)

    def test_formula_is_read_twice_and_linear_size(self):
        for vertices in range(2, 14, 2):
            edges = graph_workers(vertices)
            clauses = read_twice_occurrences(vertices)
            self.assertEqual(sum(map(len, clauses)), 2*len(edges))
            self.assertTrue(all(sum(i in c for c in clauses) == 2
                                for i in range(len(edges))))
            # Binary OR trees plus binary AND tree: total gates 2N-1.
            gates = sum(len(c)-1 for c in clauses)+len(clauses)-1
            self.assertEqual(gates, 2*len(edges)-1)


if __name__ == '__main__':
    unittest.main()
