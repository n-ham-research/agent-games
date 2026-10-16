import unittest
from fractions import Fraction as F
from phase15_resources import channel, normalize, rank, optimal_code, success, deterministic_optimum, replay_adapter

class Resources(unittest.TestCase):
    def test_normalization(self):
        u=[[F(1,4),F(1,2)],[F(1,2),F(0)]]
        v=[[F(1),F(1)],[F(1),F(0)]]
        e,d=normalize(u,v)
        self.assertEqual(channel(e,d),[[F(3,4),F(1,4)],[F(1,2),F(1,2)]])
    def test_identity_lower_bound(self):
        for n in range(1,10):
            a=[[F(i==j) for j in range(n)] for i in range(n)]
            self.assertEqual(rank(a),n)
    def test_rank_is_not_memory(self):
        p=[[F(1,2),F(1,2),F(0),F(0)],
           [F(0),F(1,2),F(1,2),F(0)],
           [F(0),F(0),F(1,2),F(1,2)],
           [F(1,2),F(0),F(0),F(1,2)]]
        self.assertEqual(rank(p),3)
        for i in range(4):
            for j in range(i): self.assertEqual(p[i][j]*p[j][i],0)
        identity=[[F(i==j) for j in range(4)] for i in range(4)]
        self.assertEqual(channel(identity,p),p)
    def test_exact_frontier(self):
        for n in range(1,13):
            for m in range(1,8):
                for q in range(1,5):
                    p=channel(*optimal_code(n,m,q))
                    self.assertEqual(success(p),min(F(1),F(m*q,n)))
                    tv=sum(1-p[x][x] for x in range(n))/n
                    self.assertEqual(tv,1-success(p))
    def test_exhaustive_small_codes(self):
        for n,m in [(2,1),(2,2),(3,1),(3,2),(4,2),(3,3)]:
            self.assertEqual(deterministic_optimum(n,m),min(F(1),F(m,n)))
    def test_stochastic_encoder_bound(self):
        # Enumerate all binary-input/two-mode encoders and decoders on half grid.
        from itertools import product
        rows=[[F(t,2),1-F(t,2)] for t in range(3)]
        for erows in product(rows,repeat=3):
            # decoder distributions on 3 outputs on the same half grid
            ds=[[F(a,2),F(b,2),F(2-a-b,2)] for a in range(3) for b in range(3-a)]
            for drows in product(ds,repeat=2):
                self.assertLessEqual(success(channel(list(erows),list(drows))),F(2,3))
    def test_adapter_product(self):
        # All two-mode deterministic response controllers across 3 decoded inputs.
        from itertools import product
        for policy in product(range(2),repeat=6):
            for x in range(3):
                for mode in range(2):
                    decoded=replay_adapter(x,3)
                    self.assertEqual([policy[2*z+mode] for z in decoded],[policy[2*x+mode]]*3)
    def test_channel_certificate_rejects(self):
        with self.assertRaises(ValueError): channel([[F(1)]],[[F(1,2)]])
        with self.assertRaises(ValueError): normalize([[F(1)]],[[F(2)]])

if __name__=='__main__': unittest.main()
