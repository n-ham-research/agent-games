import unittest
from fractions import Fraction as F
from itertools import product,permutations
from equilibrium_selection import (TYPES,POLICIES,policy_welfare,pure_bne,
    interim_value,mediator,volunteer_payoff,expected_mediator_welfare,
    logit_chain,public_good,potential)

class SelectionTests(unittest.TestCase):
    def test_anti_coordination_pure_mixed_and_lottery(self):
        u=lambda s:int(s[0]!=s[1])
        pure=[s for s in product((0,1),repeat=2)
              if all(u(s)>=u(tuple(1-x if j==i else x for j,x in enumerate(s))) for i in (0,1))]
        self.assertEqual(pure,[(0,1),(1,0)])
        self.assertTrue(all(s[::-1]!=s for s in pure))
        # Both pure deviations against a fair opponent yield 1/2.
        for a in (0,1):self.assertEqual(sum(F(1,2)*u((a,b)) for b in (0,1)),F(1,2))
        self.assertEqual(sum(F(1,2)*u(s) for s in pure),1)
        # Adjacent exact typed labels: exhaust player and local action bijections.
        autos=[]
        for p in permutations(range(2)):
            for flips in product((0,1),repeat=2):
                if all(u(tuple(s[p.index(j)]^flips[p.index(j)] for j in range(2)))==u(s)
                       for s in product((0,1),repeat=2)):
                    autos.append((p,flips))
        self.assertEqual(len(autos),4)

    def test_public_seed_anonymous_bound(self):
        for n in range(17):
            p=F(n,16)
            self.assertEqual(F(1,2)-2*p*(1-p),2*(p-F(1,2))**2)

    def test_bayesian_exact_policy_table_and_equilibria(self):
        expected=[[0,F(7,4),F(5,4),3],[F(7,4),F(5,2),2,F(11,4)],
                  [F(5,4),2,F(3,2),F(9,4)],[3,F(11,4),F(9,4),2]]
        self.assertEqual([[policy_welfare(f,g) for g in POLICIES] for f in POLICIES],expected)
        self.assertEqual(max(policy_welfare(f,g) for f,g in product(POLICIES,repeat=2)),3)
        eq=pure_bne()
        self.assertEqual(set(eq),{((0,0),(1,1)),((1,1),(0,0)),((1,0),(1,0))})
        self.assertEqual(policy_welfare((1,0),(1,0)),F(5,2))
        self.assertEqual(interim_value(((1,0),(1,0)),0,0,1)-
                         interim_value(((1,0),(1,0)),0,0,0),F(1,2))

    def test_anonymous_team_optimum_is_not_bne(self):
        p=(F(1),F(1,4))
        self.assertEqual(policy_welfare(p,p),F(41,16))
        self.assertGreater(interim_value((p,p),0,1,0),interim_value((p,p),0,1,1))
        # Analytical completed-square bound in high-q branch.
        for n in range(8,17):
            q=F(n,16)
            self.assertEqual(F(41,16)-(5*q-4*q*q+1),4*(q-F(5,8))**2)

    def test_informed_mediator_obedience_equivariance_efficiency(self):
        for types in product(TYPES,repeat=2):
            law=mediator(types)
            swapped={s[::-1]:p for s,p in law.items()}
            self.assertEqual(swapped,mediator(types[::-1]))
            best=max(sum(volunteer_payoff(types,s,i) for i in (0,1)) for s in product((0,1),repeat=2))
            for s,pr in law.items():
                self.assertEqual(sum(volunteer_payoff(types,s,i) for i in (0,1)),best)
                for i in (0,1):
                    t=list(s);t[i]=1-t[i]
                    self.assertGreaterEqual(volunteer_payoff(types,s,i),volunteer_payoff(types,t,i))
        self.assertEqual(expected_mediator_welfare(),F(13,4))

    def test_truthful_reporting_counterexample(self):
        actual=(F(1,2),F(3,2))
        value=lambda reports:sum(p*volunteer_payoff(actual,a,0) for a,p in mediator(reports).items())
        self.assertEqual(value((F(3,2),F(3,2)))-value(actual),F(1,4))

    def test_logit_detailed_balance_and_bad_potential_max(self):
        states,P,pi=logit_chain()
        for i,s in enumerate(states):
            self.assertEqual(sum(P[i]),1)
            for j,t in enumerate(states):self.assertEqual(pi[i]*P[i][j],pi[j]*P[j][i])
        for j in range(len(states)):
            self.assertEqual(sum(pi[i]*P[i][j] for i in range(len(states))),pi[j])
        self.assertEqual(max(states,key=potential),(0,0,0))
        self.assertEqual(max(states,key=lambda s:sum(public_good(s,i) for i in range(3))),(1,1,1))

    def test_price_witness_and_rejected_four_player_extension(self):
        eps=F(1,7)
        def receipts(s):return eps if not any(s) else (F(1) if all(s) else F(0))
        def ne(s):
            return all(receipts(s)>=receipts(tuple(1-x if j==i else x for j,x in enumerate(s)))
                       for i in range(len(s)))
        eq=[s for s in product((0,1),repeat=3) if ne(s)]
        self.assertEqual(eq,[(0,0,0),(1,1,1)])
        self.assertEqual(max(receipts(s) for s in eq)/min(receipts(s) for s in eq),7)
        self.assertTrue(ne((0,0,1,1)))
        self.assertEqual(receipts((0,0,1,1)),0)

    def test_simultaneous_best_response_cycle(self):
        s=(0,1);path=[s]
        for _ in range(4):
            s=(s[1],s[0]);path.append(s)
        self.assertEqual(path,[(0,1),(1,0),(0,1),(1,0),(0,1)])

if __name__=='__main__':unittest.main()
