from fractions import Fraction as F
from itertools import combinations,product
import unittest
from experiments.phase18_projections import complete_matching,projection_mechanism,statistics,threshold_law,edges


class ProjectionTests(unittest.TestCase):
    def test_all_protected_intersections_complete(self):
        for k in range(4):
            protected=tuple((2*j,2*j+1) for j in range(k))
            vertices=2*(k+2)
            for bits in product((0,1),repeat=k):
                chosen=frozenset(e for e,b in zip(protected,bits) if b)
                match=complete_matching(vertices,protected,chosen)
                self.assertEqual(len(match),vertices//2)
                self.assertEqual(len({v for e in match for v in e}),vertices)
                self.assertEqual(match & set(protected),chosen)

    def test_all_grid_targets_and_all_workers_rows(self):
        protected=((0,1),(2,3))
        for cost in (F(1,4),F(1,2),F(3,4)):
            for delta in (F(0),min(cost,1-cost)/2,min(cost,1-cost)):
                for s in (F(0),F(1,4),cost+delta,F(3,4),F(1)):
                    lo=max(s-cost,delta*s/(cost+delta))
                    for targets in product((lo,(lo+s)/2,s),repeat=2):
                        law=projection_mechanism(8,protected,s,dict(zip(protected,targets)),cost,delta)
                        actual,utilities,rows=statistics(8,law,cost,delta)
                        self.assertEqual(sum(law.values()),1)
                        self.assertEqual(actual,s)
                        self.assertEqual(tuple(utilities[i] for i in protected),targets)
                        self.assertTrue(all(v>=0 for v in rows.values()))
                        self.assertLessEqual(len(law),2*len(protected)+2)

    def test_threshold_law_exact_marginals(self):
        probs={'a':F(1,7),'b':F(3,7),'c':F(6,7)}
        law=threshold_law(probs)
        self.assertLessEqual(len(law),4)
        for i,p in probs.items():self.assertEqual(sum(q for a,q in law.items() if i in a),p)

    def test_small_graph_repair_prevents_naive_extension(self):
        # On four vertices an absent disjoint edge repairs failed protected work.
        protected=((0,1),)
        law={frozenset({(0,1),(2,3)}):F(1,2),frozenset({(0,1)}):F(1,2)}
        _,_,rows=statistics(4,law)
        self.assertLess(rows[(2,3),0],0)
        with self.assertRaises(ValueError):projection_mechanism(4,protected,F(1,4),{(0,1):F(0)})

    def test_incident_protected_edges_rejected(self):
        with self.assertRaises(ValueError):projection_mechanism(8,((0,1),(0,2)),F(1,2),{(0,1):F(0),(0,2):F(0)})


if __name__=='__main__':unittest.main()
