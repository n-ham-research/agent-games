import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase19_projection_optimization import optimize
from experiments.phase18_projections import statistics


class ProjectionOptimizationTests(unittest.TestCase):
    def test_three_breakpoints_dominate_exact_grid(self):
        roles=((0,1),(2,3))
        for cost,delta in ((F(1,2),F(0)),(F(2,5),F(1,5)),(F(3,4),F(1,4))):
            for ws in product((-2,0,3),repeat=3):
                weights=dict(zip(roles,ws[:2]))
                value,s,u,law=optimize(8,weights,F(ws[2]),cost,delta)
                actual,utilities,rows=statistics(8,law,cost,delta)
                self.assertEqual(actual,s)
                self.assertEqual({i:utilities[i] for i in roles},u)
                self.assertTrue(all(row>=0 for row in rows.values()))
                self.assertLessEqual(len(law),6)
                for target in (F(j,20) for j in range(21)):
                    lower=max(target-cost,delta*target/(cost+delta))
                    for us in product((lower,target),repeat=2):
                        self.assertLessEqual(ws[2]*target+sum(w*x for w,x in zip(ws,us)),value)

if __name__ == '__main__':
    unittest.main()
