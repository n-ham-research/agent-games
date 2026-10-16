import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase16_formulas import evaluate, lift, gate_tables, marginals, reconstruct, sparse_reconstruct


def trees(labels):
    if len(labels) == 1:
        return (labels[0],)
    return tuple((op, left, right) for k in range(1, len(labels))
        for left in trees(labels[:k]) for right in trees(labels[k:]) for op in ('and', 'or'))


def profiles(n):
    return [frozenset(i for i in range(n) if mask>>i & 1) for mask in range(2**n)]


class FormulaLiftTests(unittest.TestCase):
    def test_every_read_once_shape_through_five_leaves(self):
        for n in range(1, 6):
            for formula in trees(tuple(range(n))):
                for active in profiles(n):
                    states = lift(formula, active)
                    def check(tree, address):
                        if isinstance(tree, int):
                            actual = evaluate(formula, active | {tree})-evaluate(formula, active-{tree})
                            self.assertEqual(states[address][1], actual)
                        else:
                            triple = states[address], states[address+(0,)], states[address+(1,)]
                            self.assertIn(triple, gate_tables(tree)[()])
                            check(tree[1], address+(0,)); check(tree[2], address+(1,))
                    check(formula, ())

    def test_junction_reconstruction_all_rows(self):
        formula = ('and', ('or', 0, 1), ('or', 2, 3))
        law = {a: F(j+1, 136) for j, a in enumerate(profiles(4))}
        unary, gates = marginals(formula, law)
        rebuilt = sparse_reconstruct(formula, unary, gates)
        self.assertLessEqual(len(rebuilt), len(unary)+len(gates))
        self.assertEqual(sum(rebuilt.values()), 1)
        self.assertEqual(marginals(formula, rebuilt), (unary, gates))
        def stats(distribution):
            s = sum(p*evaluate(formula, a) for a,p in distribution.items())
            rows = {}
            for i in range(4):
                c, delta = F(i+1, 6), F(1, 20)
                for bit in (0, 1):
                    rows[i,bit] = sum(p*(evaluate(formula,a)-evaluate(formula,a^{i})
                        +c*(1-2*bit)-delta) for a,p in distribution.items() if int(i in a)==bit)
            return s, rows
        self.assertEqual(stats(law), stats(rebuilt))

    def test_repeated_variable_invalidates_local_sensitivity(self):
        formula = ('and', 0, 0)
        state = lift(formula, frozenset())
        self.assertEqual(state[(0,)][1], 0)
        self.assertEqual(evaluate(formula,{0})-evaluate(formula,set()), 1)

    def test_zero_marginal_branches_and_single_leaf(self):
        for formula in (0, ('or', 0, 1)):
            law = {frozenset(): F(1)}
            unary, gates = marginals(formula, law)
            self.assertEqual(reconstruct(formula, unary, gates), law)


if __name__ == '__main__':
    unittest.main()
