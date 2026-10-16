import unittest
from itertools import product
from experiments.phase16_substitution import observer, synthesize, verify_adapter, index_signatures, index_adapter, index_model

class Substitution(unittest.TestCase):
    @staticmethod
    def replay():
        # First observation distinguishes state; next sparse observation erases it.
        return (0,1),2,lambda t,x:x if t==0 else 'blank',lambda t,x:x,lambda t,x,a:(x,),(0,)
    def test_observer_replay(self):
        layers,bad=observer(*self.replay())
        self.assertIsNone(bad)
        self.assertEqual(set(layers[1].values()),{0,1})
    def test_minimum_mode_synthesis(self):
        args=self.replay()
        self.assertIsNone(synthesize(*args,(0,1,'blank'),1))
        cert=synthesize(*args,(0,1,'blank'),2)
        self.assertIsNotNone(cert)
        self.assertIsNotNone(verify_adapter(*args,cert[0]))
    def test_ambiguous_history_impossible(self):
        args=((0,1),1,lambda t,x:'same',lambda t,x:x,lambda t,x,a:(x,),(0,))
        self.assertIsNotNone(observer(*args)[1])
    def test_all_actions_not_default(self):
        initial=(0,); sparse=lambda t,x:'same';rich=lambda t,x:x
        # Default a=0 hides the failure; deviation a=1 can reach either state.
        succ=lambda t,x,a:(0,) if a==0 else (0,1)
        self.assertIsNone(observer(initial,2,sparse,rich,succ,(0,))[1])
        self.assertIsNotNone(observer(initial,2,sparse,rich,succ,(0,1))[1])
    def test_hidden_context_union(self):
        # No action identifies an unobserved context-generated state.
        args=((0,),2,lambda t,x:'same',lambda t,x:x,lambda t,x,a:(0,1),(0,))
        self.assertIsNotNone(observer(*args)[1])
    def test_index_arena_observer(self):
        for n in range(1,6):
            states,args=index_model(n)
            self.assertEqual(len(states),4*n)
            layers,bad=observer(*args)
            self.assertIsNone(bad)
            terminal_supports={support for support,o in layers[-1]}
            self.assertEqual(len(terminal_supports),2**n)
    def test_binary_index_matching(self):
        for n in range(1,9):
            sig=index_signatures(n)
            self.assertEqual(len(set(sig.values())),2**n)
            for w in sig:
                for j in range(n): self.assertEqual(index_adapter(w,j),w[j])
    def test_index_pair_distinguishability(self):
        for n in range(1,6):
            words=list(product((0,1),repeat=n))
            for w in words:
                for v in words:
                    if w!=v: self.assertTrue(any(w[j]!=v[j] for j in range(n)))
    def test_adapter_preserves_every_tiny_response(self):
        # All Boolean terminal policies, every remembered mode and input word.
        for policy in product((0,1),repeat=4):
            for w in product((0,1),repeat=3):
                for j in range(3):
                    for m in range(2):
                        self.assertEqual(policy[2*m+index_adapter(w,j)],policy[2*m+w[j]])

if __name__=='__main__': unittest.main()
