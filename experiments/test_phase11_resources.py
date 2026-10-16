"""Exact finite checks; proofs of unrestricted statements remain in research."""
import unittest
from fractions import Fraction as F
from itertools import product

class ResourceTests(unittest.TestCase):
    def test_verification_frontier(self):
        for n,p in product(range(2,7),(F(1,5),F(1,2),F(4,5))):
            a=1-p; lo=F(1,2); hi=F(3,2); B=F(2)
            for m in range(n):
                cost=F(0); queries=F(0)
                for types in product((lo,hi),repeat=n):
                    prob=p**types.count(lo)*a**types.count(hi)
                    seen=[]
                    for i in range(m):
                        seen.append(types[i])
                        if types[i]==lo: break
                    chosen=lo if lo in seen else types[len(seen)]
                    cost+=prob*chosen;queries+=prob*len(seen)
                self.assertEqual(cost,lo+(hi-lo)*a**(m+1))
                self.assertEqual(queries,sum(a**j for j in range(m)))
                self.assertEqual(n*B-cost,n*B-(p*lo+a*hi)+p*a*(hi-lo)*queries)

    def test_all_three_input_circuits_as_truth_tables(self):
        n=3;profiles=list(product((0,1),repeat=n))
        for table in product((0,1),repeat=8):
            truth=dict(zip(profiles,table))
            def u(s):
                return sum(truth[s[j:]+s[:j]]+truth[tuple(1-x for x in s[j:]+s[:j])] for j in range(n))*F(1,2*n)
            for s in profiles:
                self.assertEqual(u(s),u(s[1:]+s[:1]))
                self.assertEqual(u(s),u(tuple(1-x for x in s)))
            self.assertEqual(sum(map(u,profiles))*F(1,8),F(sum(table),8))
            for i in range(n):
                self.assertEqual(sum(u(s) for s in profiles if s[i]==0),sum(u(s) for s in profiles if s[i]==1))

    def test_affine_hypothesis_is_necessary(self):
        self.assertGreater(F(1)**2+F(0)**2,2*F(1,2)**2)

    def test_uniform_seed_divisibility(self):
        self.assertTrue(all(2**b%3 for b in range(30)))
        self.assertEqual(F(2,1)/(1-F(1,4)),F(8,3))

    def test_product_exactly_one_requires_designation(self):
        for probs in product((F(0),F(1,3),F(1,2),F(1)),repeat=3):
            success=sum(probs[i]*__import__('math').prod(1-probs[j] for j in range(3) if j!=i) for i in range(3))
            if success==1:
                self.assertEqual(sorted(probs),[0,0,1])
