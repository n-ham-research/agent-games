"""Exact challenges of stochastic/strategic substitution certificates."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import unittest
import phase14_interchangeability as m


class InterchangeabilityTests(unittest.TestCase):
    def test_nonisomorphic_hidden_state_rows_really_lump(self):
        for c,actions,e in product(range(2),m.ACTIONS,range(2)):
            aggregate=[]
            for bit in range(2):
                row=defaultdict(Q)
                for state,obs,reward,resource,p in m.kernel(True,(c,bit),actions,e):
                    row[(state[0],obs,reward,resource)]+=p
                aggregate.append(dict(row))
            abstract=defaultdict(Q)
            for state,obs,reward,resource,p in m.kernel(False,c,actions,e):
                abstract[(state,obs,reward,resource)]+=p
            self.assertEqual(aggregate[0],aggregate[1])
            self.assertEqual(aggregate[0],dict(abstract))
        self.assertNotEqual(list(m.kernel(True,(0,0),(0,0),0)),
                            list(m.kernel(True,(0,1),(0,0),0)))

    def test_all_profiles_all_deviations_two_contexts(self):
        for context in (m.zero_context,m.adaptive_context):
            fine_values={};abstract_values={}
            for plans in product(m.PLANS,repeat=2):
                profiles=tuple(map(m.pure_policy,plans))
                a=m.outcome_law(True,profiles,context)
                b=m.outcome_law(False,profiles,context)
                self.assertEqual(a,b)
                self.assertEqual(sum(a.values()),1)
                fine_values[plans]=tuple(m.expected_utility(a,i) for i in range(2))
                abstract_values[plans]=tuple(m.expected_utility(b,i) for i in range(2))
            # Every pure profile/deviation pair already occurs in this complete
            # matrix. Check its exact utility and best-response suprema too.
            for plans in product(m.PLANS,repeat=2):
                for i in range(2):
                    fine_best=max(fine_values[plans[:i]+(d,)+plans[i+1:]][i]
                                  for d in m.PLANS)
                    abstract_best=max(abstract_values[plans[:i]+(d,)+plans[i+1:]][i]
                                      for d in m.PLANS)
                    self.assertEqual(fine_best-fine_values[plans][i],
                                     abstract_best-abstract_values[plans][i])

    def test_seed_posterior_transport_against_many_opponents(self):
        weights={plan:Q(k+1,36) for k,plan in enumerate(m.PLANS)}
        other={plan:Q(8-k,36) for k,plan in enumerate(m.PLANS)}
        for context in (m.zero_context,m.adaptive_context):
            for opposing in [other]+[{plan:Q(1)} for plan in m.PLANS]:
                seeded=m.mixed_plan_law(True,(weights,opposing),context)
                behavioral=m.outcome_law(False,
                        (m.posterior_policy(weights),m.posterior_policy(opposing)),context)
                self.assertEqual(seeded,behavioral)

    def test_private_information_breaks_open_loop_equivalence(self):
        # Every fixed guess has Bernoulli(1/2) reward in either system.
        for guess in range(2):
            self.assertEqual(sum(Q(1,2)*(guess==bit) for bit in range(2)),Q(1,2))
        blind_best=Q(1,2);informed_copy=Q(1)
        self.assertEqual(informed_copy-blind_best,Q(1,2))

    def test_joint_private_signal_not_just_marginals(self):
        self.assertEqual(m.signal_copy_game(False),(Q(1,2),Q(0)))
        self.assertEqual(m.signal_copy_game(True),(Q(0),Q(1)))

    def test_same_default_action_omits_an_exploit(self):
        old={0:Q(0)};new={0:Q(0),1:Q(1)}
        self.assertEqual(old[0],new[0])
        self.assertEqual(max(old.values())-old[0],0)
        self.assertEqual(max(new.values())-new[0],1)

    def test_persistent_seed_is_not_memoryless_fresh_randomness(self):
        persistent={(0,0):Q(1,2),(1,1):Q(1,2)}
        memoryless={acts:Q(1,4) for acts in m.ACTIONS}
        self.assertEqual(m.tv(persistent,memoryless),Q(1,2))
        # Perfect recall implementation: fair first action, repeat it later.
        recall={(a,a):Q(1,2) for a in range(2)}
        self.assertEqual(recall,persistent)

    def test_approximate_regret_factor_two_is_attained(self):
        error=Q(1,10)
        old=(Q(1,2),Q(1,2));new=(Q(1,2)-error,Q(1,2)+error)
        for x,y in zip(old,new):
            self.assertEqual(m.tv({0:1-x,1:x},{0:1-y,1:y}),error)
        self.assertEqual(max(old)-old[0],0)
        self.assertEqual(max(new)-new[0],2*error)

    def test_row_error_accumulates_over_an_entire_record(self):
        error=Q(1,10);horizon=3
        exact={(0,)*horizon:Q(1)}
        perturbed={bits:((1-error)**bits.count(0))*error**bits.count(1)
                   for bits in product(range(2),repeat=horizon)}
        self.assertEqual(m.tv(exact,perturbed),1-(1-error)**horizon)
        self.assertLessEqual(m.tv(exact,perturbed),horizon*error)


if __name__=='__main__':unittest.main()
