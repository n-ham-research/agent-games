import unittest
from fractions import Fraction as F
from itertools import combinations
from experiments.phase18_strategic_geometry import (
    profiles, all_graphs, adjacent_vertices, independent, maximal_independent,
    collision_utility, bestshot_utility, switched, rows, marginals,
    independent_product_law, complete_line_graph)


class StrategicGeometryChecks(unittest.TestCase):
    def test_collision_pure_ce_profiles_exactly_independent_sets(self):
        for n in range(1, 5):
            for graph in all_graphs(n):
                for a in profiles(n):
                    feasible = all(v >= 0 for v in rows({a: F(1)}, graph).values())
                    self.assertEqual(feasible, independent(a, graph))

    def test_collision_rows_are_nonpositive_collision_mass_and_cces_agree(self):
        graph = frozenset({(0, 1), (1, 2), (0, 2)})
        law = {a: F(j+1, 36) for j, a in enumerate(profiles(3))}
        matrix = rows(law, graph)
        for i in range(3):
            joint = sum(p*a[i]*sum(a[j] for j in adjacent_vertices(graph, i))
                        for a, p in law.items())
            self.assertEqual(matrix[i, 1], -joint/2)
            coarse_abstain = sum(p*(collision_utility(a, i, graph)
                -collision_utility(a[:i]+(0,)+a[i+1:], i, graph)) for a, p in law.items())
            self.assertEqual(coarse_abstain, matrix[i, 1])
        self.assertTrue(any(v < 0 for v in matrix.values()))

    def test_same_nonstrategic_coordinates_fill_cube(self):
        wanted = (F(0), F(1, 3), F(2, 5), F(1))
        law = independent_product_law(wanted)
        self.assertEqual(sum(law.values()), 1)
        self.assertEqual(marginals(law), wanted)

    def test_arbitrary_independent_support_laws_are_ce_and_all_utilities_one(self):
        for graph in all_graphs(4):
            independent_profiles = [a for a in profiles(4) if independent(a, graph)]
            total = sum(range(1, len(independent_profiles)+1))
            law = {a: F(j+1, total) for j, a in enumerate(independent_profiles)}
            self.assertTrue(all(v >= 0 for v in rows(law, graph).values()))
            for i in range(4):
                self.assertEqual(sum(p*collision_utility(a, i, graph) for a, p in law.items()), 1)

    def test_bestshot_work_margin_is_exact_collision_exclusion(self):
        for graph in all_graphs(4):
            for a in profiles(4):
                matrix = rows({a: F(1)}, graph, bestshot_utility, F(1, 4))
                for i in range(4):
                    collision = a[i] and any(a[j] for j in adjacent_vertices(graph, i))
                    self.assertEqual(matrix[i, 1], -F(int(collision)))
                if maximal_independent(a, graph):
                    self.assertTrue(all(v >= 0 for v in matrix.values()))
                    for i in range(4):
                        gain = bestshot_utility(a, i, graph)-bestshot_utility(switched(a, i), i, graph)
                        self.assertGreaterEqual(gain, F(1, 4))

    def test_line_graph_perfect_matching_face_and_strict_profiles(self):
        for vertices in (4, 6):
            workers, graph = complete_line_graph(vertices)
            m, n = vertices//2, len(workers)
            found = 0
            for active in combinations(range(n), m):
                a = tuple(int(i in active) for i in range(n))
                if independent(a, graph):
                    touched = [v for i in active for v in workers[i]]
                    self.assertCountEqual(touched, range(vertices))
                    self.assertTrue(maximal_independent(a, graph))
                    self.assertTrue(all(v >= 0 for v in rows({a: F(1)}, graph, bestshot_utility, F(1, 4)).values()))
                    found += 1
            self.assertGreater(found, 0)

    def test_lower_margin_can_allow_collisions_no_robust_interval_claim(self):
        graph = frozenset({(0, 1)})
        law = {(1, 0): F(29, 60), (0, 1): F(29, 60), (1, 1): F(1, 30)}
        self.assertEqual(sum(law.values()), 1)
        self.assertTrue(all(v >= 0 for v in rows(law, graph, bestshot_utility, F(1, 8)).values()))
        self.assertLess(rows(law, graph, bestshot_utility, F(1, 4))[0, 1], 0)


if __name__ == '__main__':
    unittest.main()
