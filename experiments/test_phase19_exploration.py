import unittest
from fractions import Fraction as F
from experiments.phase19_exploration import list_joint,singleton_joint,flags,expand,success,rows,posterior

class Exploration(unittest.TestCase):
    def test_private_adjacent_lists_every_signal_obeys(self):
        n=3;law=list_joint(n,{1:F(4,7),2:F(3,7)})
        for alpha in (F(0),F(1,3),F(3,4),F(1)):
            for kind in ('common','independent'):
                out=expand(law,flags(n,alpha,kind),n)
                self.assertEqual(sum(p for *_,p in out),1)
                self.assertEqual(sum(p for theta,a,f,real,p in out if theta in real),1)
                self.assertTrue(all(v[1]>=0 for v in rows(out,n,F(1),F(3,5),F(1,10)).values()))
    def test_low_success_affine(self):
        n=3;tau=F(7,10);t=F(7,20);law=singleton_joint(n,tau,t)
        self.assertEqual(success(law),t)
        for alpha in (F(0),F(1,3),F(3,4),F(1)):
            for kind in ('common','independent'):
                out=expand(law,flags(n,alpha,kind),n)
                actual=sum(p for theta,a,f,real,p in out if theta in real)
                self.assertEqual(actual,alpha+(1-alpha)*t)
                self.assertTrue(all(v[1]>=0 for v in rows(out,n,F(1),F(3,5),F(1,10)).values()))
    def test_correlated_flags(self):
        n=3;alpha=F(1,3);law=singleton_joint(n,F(7,10),F(7,20))
        out=expand(law,flags(n,alpha,'one'),n)
        self.assertEqual(sum(p for theta,a,f,real,p in out if theta in real),alpha+(1-alpha)*success(law))
        self.assertTrue(all(v[1]>=0 for v in rows(out,n,F(1),F(3,5),F(1,10)).values()))
    def test_uninformed_rows_are_scaled_base(self):
        n=3;law=list_joint(n,{1:F(4,7),2:F(3,7)})
        base=rows(expand(law,flags(n,F(0),'common'),n),n,F(1),F(3,5),F(1,10))
        alpha=F(2,3)
        for kind in ('common','independent'):
            augmented=rows(expand(law,flags(n,alpha,kind),n),n,F(1),F(3,5),F(1,10))
            for key,(mass,slack) in base.items():
                self.assertEqual(augmented[key],((1-alpha)*mass,(1-alpha)*slack))
    def test_uniform_containing_set_posteriors(self):
        law=list_joint(3,{1:F(4,7),2:F(3,7)})
        for _,a in law:
            self.assertEqual(posterior(law,a),{i:F(1,len(a)) for i in a})
    def test_zero_acquisition_private_test_baseline(self):
        # State-independent invitation: nobody invited; only aware capable works.
        law={(theta,frozenset()):F(1,3) for theta in range(3)}
        for alpha in (F(0),F(1,4),F(1)):
            out=expand(law,flags(3,alpha,'independent'),3)
            self.assertEqual(sum(p for theta,a,f,real,p in out if theta in real),alpha)
            self.assertTrue(all(v[1]>=0 for v in rows(out,3,F(1),F(3,5),F(1,10)).values()))
    def test_blindly_skipping_acquisition_fails(self):
        alpha,w=F(3,4),F(1,2)
        no={(theta,frozenset()):F(1,3) for theta in range(3)}
        yes=list_joint(3,{1:F(4,7),2:F(3,7)})
        mixture={key:w*yes.get(key,0)+(1-w)*no.get(key,0) for key in yes.keys()|no.keys()}
        out=expand(mixture,flags(3,alpha,'common'),3)
        actual=sum(p for theta,a,f,real,p in out if theta in real)
        self.assertEqual(actual,alpha+(1-alpha)*w)
        self.assertLess(actual,1)
    def test_nonuniform_heterogeneous_availability_identity(self):
        from itertools import product
        mu=(F(1,2),F(1,3),F(1,6));alpha=(F(1,4),F(1,2),F(3,4))
        hit=(F(1,3),F(1,2),F(2,3));law={}
        for i in range(3):
            law[i,frozenset((i,))]=mu[i]*hit[i]
            law[i,frozenset()]=mu[i]*(1-hit[i])
        fs={}
        for v in product((0,1),repeat=3):
            p=F(1)
            for i,b in enumerate(v):p*=alpha[i] if b else 1-alpha[i]
            fs[v]=p
        out=expand(law,fs,3)
        actual=sum(p for theta,a,f,real,p in out if theta in real)
        self.assertEqual(actual,sum(mu[i]*(alpha[i]+(1-alpha[i])*hit[i]) for i in range(3)))
    def test_literal_invitation_override_is_essential(self):
        law=list_joint(3,{2:F(1)})
        out=expand(law,flags(3,F(1,2),'independent'),3)
        # Some incapable invited worker knows it is incapable and must abstain.
        self.assertTrue(any(i in a and i!=theta and f[i] and i not in real
                            for theta,a,f,real,p in out if p for i in range(3)))

if __name__=='__main__':unittest.main()
