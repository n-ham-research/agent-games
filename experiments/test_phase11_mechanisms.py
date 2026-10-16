import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase11_mechanisms import (
    ACTIONS,TYPES,frontier,public_local_max,cheapest_kernel,designated_kernel,
    joint_incentive_gaps,kernel_statistics,deterministic_kernels,reliability_bound,
    minimum_cost_expectation,procurement_joint_gap,payoff,
    cheapest_mean_coalition,coalition_payoff,
)


class MechanismTests(unittest.TestCase):
    def test_parameterized_frontier_vertices(self):
        for B,l,h,p in product((F(2),F(3)),(F(1,10),F(1,2)),
                               (F(1),F(3,2)),(F(0),F(1,5),F(1,2),F(4,5),F(1))):
            public,informed,gap=frontier(B,l,h,p)
            self.assertEqual(public_local_max(B,l,h,p),public)
            self.assertEqual(informed-public,gap)
            self.assertGreater(gap,0) if 0<p<1 else self.assertEqual(gap,0)
        self.assertEqual(frontier(F(2),F(1,2),F(3,2),F(1,2)),(F(3),F(13,4),F(1,4)))
        self.assertEqual(frontier(F(2),F(1,10),F(19,10),F(4,5))[0],F(92,25))

    def test_cheapest_ex_post_obedient_but_not_truthful(self):
        for B,l,h,p in ((F(2),F(1,2),F(3,2),F(1,2)),
                        (F(3),F(1,3),F(5,2),F(4,5))):
            kernel=cheapest_kernel()
            for t in TYPES:
                costs=tuple((l,h)[z] for z in t)
                for a in kernel[t]:
                    self.assertEqual(sum(a),1)
                    for i in (0,1):
                        deviation=list(a);deviation[i]=1-deviation[i]
                        self.assertGreaterEqual(payoff(B,costs,a,i),payoff(B,costs,deviation,i))
            gaps=joint_incentive_gaps(B,l,h,p,kernel)
            self.assertLess(min(gaps.values()),0)
            self.assertEqual(kernel_statistics(B,l,h,p,kernel)[1],frontier(B,l,h,p)[1])
            self.assertGreaterEqual(min(joint_incentive_gaps(B,l,h,p,designated_kernel()).values()),0)

    def test_all_deterministic_direct_mechanisms(self):
        B,l,h,p=F(2),F(1,2),F(3,2),F(1,2)
        feasible=0
        for kernel in deterministic_kernels():
            if min(joint_incentive_gaps(B,l,h,p,kernel).values())<0:
                continue
            feasible+=1
            service,welfare=kernel_statistics(B,l,h,p,kernel)
            self.assertLessEqual(welfare,reliability_bound(B,l,h,p,2,service))
            if service==1:
                self.assertLessEqual(welfare,F(3))
        self.assertGreater(feasible,0)

    def test_n_agent_screening_gap(self):
        costs=(F(1,4),F(3,4),F(5,4)); probs=(F(1,5),F(1,2),F(3,10))
        mean=sum(c*p for c,p in zip(costs,probs))
        for n in range(2,6):
            self.assertLess(minimum_cost_expectation(costs,probs,n),mean)
        for n in (2,3,7):
            p=F(2,3);l=F(1,3);h=F(4,3)
            self.assertEqual(minimum_cost_expectation((l,h),(p,1-p),n),l+(h-l)*(1-p)**n)

    def test_correlated_type_boundary(self):
        # Exactly one low cost: each own type identifies the other's type.
        B,l,h=F(2),F(1,2),F(3,2)
        for costs in ((l,h),(h,l)):
            a=tuple(int(c==l) for c in costs)
            self.assertEqual(sum(a),1)
            for i in (0,1):
                deviation=list(a);deviation[i]=1-deviation[i]
                self.assertGreater(payoff(B,costs,a,i),payoff(B,costs,deviation,i))
        self.assertGreater(2*B-l,2*B-(l+h)/2)

    def test_general_successful_coalitions(self):
        # Threshold-two and C4 vertex-cover production technologies.
        n=4;B=F(2);all_actions=tuple(product((0,1),repeat=n))
        threshold={a for a in all_actions if sum(a)>=2}
        cycle={a for a in all_actions if all(a[i] or a[(i+1)%n] for i in range(n))}
        means=(F(1,2),F(3,4),F(4,5),F(5,4))
        for successful in (threshold,cycle):
            chosen=cheapest_mean_coalition(means,successful)
            self.assertIn(chosen,successful)
            for costs in product((F(1,4),F(7,4)),repeat=n):
                for i in range(n):
                    deviation=list(chosen);deviation[i]=1-deviation[i]
                    self.assertGreater(coalition_payoff(B,costs,chosen,successful,i),
                                       coalition_payoff(B,costs,deviation,successful,i))
        self.assertEqual(sum(c*x for c,x in zip(means,cheapest_mean_coalition(means,threshold))),
                         sum(sorted(means)[:2]))

    def test_procurement_reporting_not_dominant_with_disobedient_opponent(self):
        # Agent1 reports low but abstains even when selected. Agent0 is high.
        B=F(2);actual=(F(3,2),F(1,2))
        truthful_best=max(payoff(B,actual,(a,0),0) for a in (0,1))
        # False low report wins least-index tie; completion earns price 1/2.
        false_best=max(payoff(B,actual,(a,0),0)+F(1,2)*a for a in (0,1))
        self.assertEqual(truthful_best,F(1,2))
        self.assertEqual(false_best,F(1))
        self.assertGreater(false_best,truthful_best)

    def test_procurement_ex_post_joint_reports_actions(self):
        costs=(F(1,3),F(2,3),F(4,3));B=F(2)
        for n in (2,3,4):
            for actual in product(costs,repeat=n):
                for i,report,act in product(range(n),costs,(0,1)):
                    self.assertGreaterEqual(procurement_joint_gap(B,actual,i,report,act),0)


if __name__=='__main__':
    unittest.main()
