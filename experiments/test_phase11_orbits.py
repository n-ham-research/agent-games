from fractions import Fraction as Q
from itertools import product
import unittest

from phase11_orbits import (action_orbits, all_regrets, apply,
    compile_conditional, cycle_instance, direct_conditional, evaluate,
    factor_payoff, lift, orbit_index, orbit_regret_matrix, partition, profiles)


class OrbitTests(unittest.TestCase):
    def test_local_compiler_matches_full_expectations(self):
        for n in (4, 5, 7):
            sizes, rotation, _, factors = cycle_instance(n)
            index = orbit_index(action_orbits(sizes, [rotation]))
            self.assertEqual(len(set(index.values())), 2)
            payoff = lambda i, s: factor_payoff(factors, i, s)
            for p in (Q(0), Q(1, 7), Q(1, 2), Q(1)):
                x = [1 - p, p]
                for i in range(n):
                    for a in range(2):
                        poly = compile_conditional(i, a, factors, sizes, index)
                        self.assertLessEqual(max(map(len, poly)), 1)
                        self.assertEqual(evaluate(poly, x), direct_conditional(
                            i, a, sizes, payoff, [[1 - p, p]] * n))
            self.assertEqual(evaluate(compile_conditional(
                0, 0, factors, sizes, index), [Q(1, 2)] * 2), Q(1, 2))

    def test_asymmetric_local_actions_have_nontrivial_invariant_ne(self):
        sizes, rotation, _, factors = cycle_instance(6)
        for i in range(6):
            scope = (i, (i + 1) % 6)
            factors[i] = [(scope, {(0, 0): 0, (0, 1): 1,
                                  (1, 0): 2, (1, 1): 0})]
        index = orbit_index(action_orbits(sizes, [rotation]))
        x = [Q(1, 3), Q(2, 3)]
        for i in range(6):
            self.assertEqual(evaluate(compile_conditional(
                i, 0, factors, sizes, index), x), Q(2, 3))
            self.assertEqual(evaluate(compile_conditional(
                i, 1, factors, sizes, index), x), Q(2, 3))
        # Neither pure invariant endpoint is Nash; the root is p=2/3.
        p0 = compile_conditional(0, 0, factors, sizes, index)
        p1 = compile_conditional(0, 1, factors, sizes, index)
        self.assertGreater(evaluate(p1, [Q(1), Q(0)]),
                           evaluate(p0, [Q(1), Q(0)]))
        self.assertGreater(evaluate(p0, [Q(0), Q(1)]),
                           evaluate(p1, [Q(0), Q(1)]))

    def test_typed_action_maps_and_automorphism_promise(self):
        sizes, rotation, complement, factors = cycle_instance(4)
        self.assertEqual(len(action_orbits(sizes, [rotation, complement])), 1)
        payoff = lambda i, s: factor_payoff(factors, i, s)
        for g in (rotation, complement):
            for s in profiles(sizes):
                for i in range(4):
                    self.assertEqual(payoff(i, s), payoff(g[0][i], apply(g, s)))
        swap = ((1, 0, 2, 3), ((0, 1),) * 4)
        self.assertTrue(any(payoff(i, s) != payoff(swap[0][i], apply(swap, s))
                            for i in range(4) for s in profiles(sizes)))

    def test_additive_factors_not_individually_invariant(self):
        # Offsetting arbitrary factor pieces cancel; only the sum is invariant.
        sizes, rotation, _, factors = cycle_instance(4)
        for i in range(4):
            factors[i].extend([((i,), {(0,): i, (1,): -i}),
                               ((i,), {(0,): -i, (1,): i})])
        index = orbit_index(action_orbits(sizes, [rotation]))
        for i in range(4):
            self.assertEqual(compile_conditional(i, 0, factors, sizes, index),
                             {(index[0, 0],): Q(1)})

    def test_quotient_ce_constraints_equal_all_constraints(self):
        # Four-player directed cycle, action complement joins deviation orbits.
        sizes, rotation, complement, factors = cycle_instance(4)
        payoff = lambda i, s: factor_payoff(factors, i, s)
        rows, cols, matrix = orbit_regret_matrix(sizes, [rotation, complement], payoff)
        for raw in product(range(3), repeat=len(cols)):
            if not sum(raw):
                continue
            masses = [Q(a, sum(raw)) for a in raw]
            full = all_regrets(sizes, payoff, lift(cols, masses))
            for row, coeffs in zip(rows, matrix):
                compressed = sum((a * b for a, b in zip(coeffs, masses)), Q(0))
                self.assertTrue(all(full[d] == compressed for d in row))
            self.assertEqual(all(v >= 0 for v in full.values()),
                             all(sum(a * b for a, b in zip(row, masses)) >= 0
                                 for row in matrix))

    def test_welfare_orbits_lose_incentives(self):
        sizes, swap = [2, 2], ((1, 0), ((0, 1),) * 2)
        def payoff(i, s):
            a, b = s[i], s[1 - i]
            return b - a
        cols = partition(profiles(sizes), [swap], apply)
        self.assertEqual([sum(payoff(i, s) for i in range(2))
                          for s in profiles(sizes)], [0] * 4)
        rows, cols, plus = orbit_regret_matrix(sizes, [swap], payoff)
        _, _, minus = orbit_regret_matrix(sizes, [swap], lambda i, s: -payoff(i, s))
        self.assertNotEqual(plus, minus)
        for sign, unique in ((1, (0, 0)), (-1, (1, 1))):
            for s in profiles(sizes):
                feasible = all(v >= 0 for v in all_regrets(
                    sizes, lambda i, t: sign * payoff(i, t), {s: Q(1)}).values())
                self.assertEqual(feasible, s == unique)

    def test_profile_orbits_remain_exponential(self):
        for n in (4, 5, 7, 8):
            sizes, rotation, _, _ = cycle_instance(n)
            cols = partition(profiles(sizes), [rotation], apply)
            self.assertGreaterEqual(len(cols) * n, 2 ** n)
            self.assertEqual(len(action_orbits(sizes, [rotation])), 2)
        self.assertEqual(len(cols), 36)  # binary necklaces of length eight

    def test_ce_correlation_not_independent_sampling(self):
        sizes = [2, 2]
        payoff = lambda i, s: int(s[0] != s[1])
        lottery = {(0, 1): Q(1, 2), (1, 0): Q(1, 2)}
        self.assertTrue(all(v >= 0 for v in all_regrets(sizes, payoff, lottery).values()))
        for numerator in range(21):
            p = Q(numerator, 20)
            self.assertLessEqual(2 * p * (1 - p), Q(1, 2))


if __name__ == '__main__':
    unittest.main()
