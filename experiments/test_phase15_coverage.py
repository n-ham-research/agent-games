from fractions import Fraction as F
from itertools import combinations, product
import unittest
from experiments.phase15_coverage import path, coefficients, encode_law, evaluate_flow, decompose


class CoverageFlowTests(unittest.TestCase):
    def test_all_small_deviation_coefficients(self):
        # Every ordered triple of subsets of a two-element universe; all profiles.
        subsets = [frozenset(e for e in range(2) if mask >> e & 1) for mask in range(4)]
        for sets in product(subsets, repeat=3):
            for bits in product((0, 1), repeat=3):
                active = frozenset(i for i, a in enumerate(bits) if a)
                final, _ = path(sets, active, 2)
                def win(a):
                    return set().union(*(sets[i] for i in a)) == {0, 1}
                for i, a in enumerate(bits):
                    cost, benefit, delta = F(i+1, 5), F(2), F(1, 7)
                    actual = benefit*win(active)-cost*a
                    other = benefit*win(active ^ {i})-cost*(1-a)
                    self.assertEqual(coefficients(final, sets[i], a, cost, benefit, delta),
                                     (actual, actual-other-delta))

    def test_exact_flow_decomposition_preserves_statistics(self):
        sets = ({0}, {1}, {0, 1}, set())
        costs = (F(1, 3), F(1, 2), F(2, 3), F(1, 4))
        law = {frozenset(i for i in range(4) if mask >> i & 1): F(mask+1, 136)
               for mask in range(16)}
        mass, flow = encode_law(sets, law, 2)
        rebuilt = decompose(sets, mass, flow, 2)
        m2, f2 = encode_law(sets, rebuilt, 2)
        self.assertEqual(evaluate_flow(sets, costs, F(1), mass, flow, F(1, 10)),
                         evaluate_flow(sets, costs, F(1), m2, f2, F(1, 10)))
        self.assertEqual(sum(rebuilt.values()), 1)

    def test_exponential_minimal_winners(self):
        d = 5
        sets = tuple({e} for e in range(d) for _ in range(2))
        winners = []
        for chosen in combinations(range(2*d), d):
            final, _ = path(sets, frozenset(chosen), d)
            if all(x == 1 for x in final):
                winners.append(chosen)
        self.assertEqual(len(winners), 2**d)

    def test_coverage_mask_alone_loses_pivotality(self):
        sets = ({0}, {0})
        one, _ = path(sets, frozenset({0}), 1)
        both, _ = path(sets, frozenset({0, 1}), 1)
        self.assertTrue(all(one) and all(both))
        self.assertNotEqual(coefficients(one, sets[0], 1, F(1, 2), F(1)),
                            coefficients(both, sets[0], 1, F(1, 2), F(1)))


if __name__ == '__main__':
    unittest.main()
