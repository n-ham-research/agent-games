import unittest
from fractions import Fraction as F
from itertools import product
from functools import reduce
from experiments.phase17_repeated import leaves,repeated,value,lift,valid_gate,gate_tables,marginals,sparse_reconstruct


def trees(labels):
    if len(labels)==1:return (labels[0],)
    return tuple((op,l,r) for k in range(1,len(labels)) for l in trees(labels[:k])
                 for r in trees(labels[k:]) for op in ('and','or'))


def profiles(ids):
    return [frozenset(i for i,b in zip(ids,bits) if b) for bits in product((0,1),repeat=len(ids))]


class RepeatedLift(unittest.TestCase):
    def test_all_small_labelled_formulas(self):
        for length in range(1,5):
            for labels in product(range(3),repeat=length):
                for tree in trees(labels):
                    for active in profiles(sorted(set(labels))):
                        r,states=lift(tree,active)
                        def check(node,addr):
                            if isinstance(node,int):
                                if node not in r:
                                    self.assertEqual(states[addr][-1],value(tree,active|{node})-value(tree,active-{node}))
                                return
                            self.assertTrue(valid_gate(node[0],states[addr],states[addr+(0,)],states[addr+(1,)]))
                            check(node[1],addr+(0,));check(node[2],addr+(1,))
                        check(tree,())
                        for j,i in enumerate(r):
                            self.assertEqual(states[()][0]-states[()][j+1],value(tree,active)-value(tree,active^{i}))

    def test_sparse_reconstruction_and_all_incentive_rows(self):
        tree=('or',('and',0,1),('and',0,('or',2,1)))
        law={a:F(j+1,36) for j,a in enumerate(profiles(range(3)))}
        r,m,u,g=marginals(tree,law)
        rebuilt=sparse_reconstruct(tree,m,u,g)
        self.assertEqual(marginals(tree,rebuilt),(r,m,u,g))
        self.assertEqual(sum(rebuilt.values()),1)
        def rows(law):
            return {(i,bit):sum(p*(value(tree,a)-value(tree,a^{i})+F(i+1,5)*(1-2*bit)-F(1,20))
                for a,p in law.items() if int(i in a)==bit) for i in range(3) for bit in (0,1)}
        self.assertEqual(rows(law),rows(rebuilt))

    def test_gate_table_bound(self):
        for r in range(5):
            for op in ('and','or'):
                table=gate_tables(op,r)
                self.assertEqual(len(table),2**(2*r+3))
                self.assertTrue(all(valid_gate(op,*t) for t in table))

    def test_global_summary_requires_exponentially_many_states(self):
        for m in range(1,8):
            # F=AND_j(probe_j OR selector_j), probes always work.
            tree=reduce(lambda x,y:('and',x,y), (('or',j,m+j) for j in range(m)))
            vectors=set()
            for bits in product((0,1),repeat=m):
                active=frozenset(range(m))|{m+j for j,bit in enumerate(bits) if bit}
                self.assertEqual(value(tree,active),1)
                vectors.add(tuple(value(tree,active)-value(tree,active-{j}) for j in range(m)))
            self.assertEqual(len(vectors),2**m)

    def test_repeated_leaf_sensitivity_is_not_its_worker_effect(self):
        tree=('and',0,0)
        r,states=lift(tree,frozenset())
        self.assertEqual(states[(0,)][-1],0)
        self.assertEqual(states[()][1],1)
        self.assertEqual(r,(0,))


if __name__=='__main__':unittest.main()
