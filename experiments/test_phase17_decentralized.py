import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase17_decentralized import value,choose,all_sets,pure_ne,ic_table,cost_ratio,coin_protocol

class Decentralized(unittest.TestCase):
    def test_tree_selection_all_profiles(self):
        trees=[('or',0,1),('and',('or',0,1),('or',2,3)),
               ('or',('and',0,1),('and',2,3)),('and',0,('or',1,('and',2,3)))]
        for tree in trees:
            n=2 if tree==trees[0] else 4
            for costs in product((F(1,4),F(1,2),F(3,4)),repeat=n):
                total,active=choose(tree,costs)
                winners=[a for a in all_sets(n) if value(tree,a)]
                self.assertEqual(total,min(sum(costs[i] for i in a) for a in winners))
                self.assertTrue(pure_ne(tree,active,costs))
    def test_successful_ne_equals_minimal(self):
        tree=('and',('or',0,1),('or',2,3));costs=[F(1,2)]*4
        for a in all_sets(4):
            if value(tree,a):
                minimal=all(not value(tree,a-frozenset((i,))) for i in a)
                self.assertEqual(pure_ne(tree,a,costs),minimal)
    def test_all_tiny_ic_tables_constant(self):
        types=(F(1,4),F(3,4));profiles=list(product(types,repeat=2));valid=0
        for vals in product((F(0),F(1,2),F(1)),repeat=4):
            p=dict(zip(profiles,vals))
            if ic_table(p,types):
                valid+=1;self.assertEqual(len(set(vals)),1)
        self.assertEqual(valid,3)
    def test_approximate_ic_endpoint_bound(self):
        l,h=F(1,4),F(3,4);types=(l,h);profiles=list(product(types,repeat=2))
        for vals in product((F(0),F(1,2),F(1)),repeat=4):
            p=dict(zip(profiles,vals));eta=F(0)
            for a,b in profiles:
                for r in types:
                    eta=max(eta,a*(p[a,b]-p[r,b]),b*(p[a,r]-p[a,b]))
            ca=p[l,h]*l+(1-p[l,h])*h
            cb=p[h,l]*h+(1-p[h,l])*l
            self.assertGreaterEqual((ca+cb)/2,(h+l)/2-(h-l)*eta/l)
    def test_cheapest_not_ic(self):
        types=(F(1,4),F(3,4))
        p={(a,b):F(1) if a<=b else F(0) for a,b in product(types,repeat=2)}
        self.assertFalse(ic_table(p,types))
    def test_sharp_minimax(self):
        l,h=F(1,5),F(4,5)
        for p in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            worst=max(cost_ratio(p,a,b) for a,b in product((l,h),repeat=2))
            self.assertEqual(worst,1+(h/l-1)*max(p,1-p))
        self.assertEqual(max(cost_ratio(F(1,2),a,b) for a,b in product((l,h),repeat=2)),(h+l)/(2*l))
    def test_pair_extension_cross_dependence(self):
        l,h=F(1,4),F(3,4);orientations=list(product((0,1),repeat=2))
        totals=[]
        for z0,z1 in orientations:
            c=((l,h) if z0==0 else (h,l))+((l,h) if z1==0 else (h,l))
            # Each pair uses OTHER pair's orientation: ignores both own costs.
            totals.append(c[z1]+c[2+z0])
        self.assertEqual(sum(totals)/len(totals),h+l)
        self.assertGreaterEqual(max(totals),h+l)
    def test_coin_resources_and_manipulation(self):
        B,c=F(1),F(1,2)
        for r in range(1,10):
            stats=coin_protocol(r)
            self.assertEqual(stats['bits'],2*stats['expected_rounds'])
            honest=B*stats['success']-c*stats['work_each']
            deviant=B*stats['success']
            self.assertGreater(deviant,honest)
            self.assertEqual(deviant-honest,c*(1-F(1,2)**r)/2)
    def test_identical_tapes_event(self):
        for bits in range(1,8):
            tapes=list(product((0,1),repeat=bits))
            same=sum(a==b for a in tapes for b in tapes)
            self.assertEqual(F(same,len(tapes)**2),F(1,2)**bits)

if __name__=='__main__': unittest.main()
