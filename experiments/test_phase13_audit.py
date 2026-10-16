"""Independent exact checks of the V12-C two-capacity characterization.

No phase12 implementation imports. Rational vertex enumeration is independent
of the proposed success-unselected-first formula. These finite checks are not
an adaptive-protocol lower-bound proof.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import unittest


def lp_vertex_minimum(B,costs,success,work,report):
    s=success[report];x=work[report]
    # A*a+C*b <= rhs; vertices of the bounded two-dimensional polytope.
    planes=[(-1,0,0),(0,-1,0),(1,0,s-x),(0,1,x)]
    for j,c in enumerate(costs):
        gain=B*(s-success[j])+c*(work[j]-x)
        planes.append((-B,-(B-c),-gain))
    planes=[tuple(Q(value) for value in row) for row in planes]
    vals=[]
    for (a,b,r),(d,e,t) in combinations(planes,2):
        det=a*e-b*d
        if not det:continue
        alpha=(r*e-b*t)/det;beta=(a*t-r*d)/det
        if all(A*alpha+C*beta<=rhs for A,C,rhs in planes):
            vals.append(alpha+beta)
    if not vals:raise AssertionError('valid target must have a feasible audit LP')
    return min(vals)


def proposed_formula(B,costs,success,work,report):
    s=success[report];x=work[report];U=s-x
    gain=[B*(s-t)+c*(y-x) for c,t,y in zip(costs,success,work)]
    T=max(gain)/B
    if T<=U:return T,Q(0)
    beta=max(Q(0),max((g-B*U)/(B-c) for g,c in zip(gain,costs)))
    return U,beta


class IndependentAuditChecks(unittest.TestCase):
    def test_rational_vertex_challenge_all_small_three_type_interims(self):
        B=Q(1);costs=(Q(1,4),Q(1,2),Q(3,4))
        valid=[(s,x) for s in (Q(0),Q(1,2),Q(1))
               for x in (Q(0),Q(1,2),Q(1)) if x<=s]
        count=0
        for rows in product(valid,repeat=3):
            success,work=zip(*rows)
            for report in range(3):
                a,b=proposed_formula(B,costs,success,work,report)
                self.assertEqual(a+b,lp_vertex_minimum(B,costs,success,work,report))
                self.assertTrue(0<=a<=success[report]-work[report])
                self.assertTrue(0<=b<=work[report])
                count+=1
        self.assertEqual(count,648)

    def test_selected_audits_are_necessary_for_the_failure_target(self):
        B=Q(2);costs=(Q(1,2),Q(3,2))
        success=(Q(1,4),Q(0));work=(Q(1,6),Q(0))
        a,b=proposed_formula(B,costs,success,work,0)
        self.assertEqual((a,b),(Q(1,12),Q(1,6)))
        # Actual high type falsely reporting low must get zero after shutdown.
        utility=B*success[0]-costs[1]*work[0]-B*a-(B-costs[1])*b
        self.assertEqual(utility,0)
        self.assertEqual(3*Q(1,2)*(a+b),Q(3,8))

    def test_no_singleton_assumption_is_substantive(self):
        # For a one-worker task, a caught low-cost liar can restore success.
        # Applying the shutdown formula would wrongly predict only1/8 audits.
        B=Q(2);low=Q(1,2);high=Q(3,2)
        success=(Q(1),Q(1));work=(Q(3,4),Q(1,4))
        a,b=proposed_formula(B,(low,high),success,work,1)
        self.assertEqual((a,b),(Q(1,8),Q(0)))
        saved_cost=low*(work[0]-work[1])
        feasible_punishment=low*a
        self.assertGreater(saved_cost-feasible_punishment,0)

    def test_nonminimal_coalition_fails_action_obedience(self):
        B=Q(2);c=Q(1,2)
        # All three recommended to work in a two-worker threshold task:
        # dropping one action preserves success and strictly improves payoff.
        obey=B-c;drop=B
        self.assertGreater(drop,obey)
        # Constant success/work reduced forms alone would give zero audits.
        self.assertEqual(proposed_formula(B,(c,),(Q(1),),(Q(1),),0),(Q(0),Q(0)))


if __name__=='__main__':unittest.main()
