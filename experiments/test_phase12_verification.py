import unittest
from fractions import Fraction as F
from experiments.phase12_verification import (efficient_rule, interim, audit_rates,
    expected_audits, deviating_utility, iid_frontier, reliability_audits,
    reliability_deviation)


class SelectiveAuditTests(unittest.TestCase):
    def check_joint_incentives(self, priors, rule, benefit, k):
        x, rates = audit_rates(priors, rule, benefit, k)
        for row in rates:
            self.assertTrue(all(0 <= r <= 1 for r in row.values()))
        for i, prior in enumerate(priors):
            for true_cost in prior:
                honest = benefit - true_cost*x[i][true_cost]
                for report in prior:
                    actual = deviating_utility(priors, rule, benefit, rates,
                                               i, true_cost, report, k)
                    self.assertLessEqual(actual, honest)
        return x, rates

    def test_binary_first_best_all_thresholds(self):
        for n in range(2, 6):
            for k in range(1, n+1):
                for p in (F(1, 4), F(1, 2), F(3, 4)):
                    low, high, benefit = F(1, 2), F(3, 2), F(2)
                    priors = [{low: p, high: 1-p} for _ in range(n)]
                    rule = lambda t: efficient_rule(t, k)
                    _, rates = self.check_joint_incentives(priors, rule, benefit, k)
                    self.assertEqual(expected_audits(priors, rule, rates),
                        iid_frontier(n, k, p, low, benefit))

    def test_asymmetric_multitype_one_worker(self):
        priors = [{F(1, 3): F(1, 4), F(2, 3): F(1, 2), F(4, 3): F(1, 4)},
                  {F(1, 2): F(1, 3), F(3, 2): F(2, 3)},
                  {F(3, 4): F(1, 2), F(5, 4): F(1, 2)}]
        x, rates = self.check_joint_incentives(priors, efficient_rule, F(2), 1)
        self.assertEqual(expected_audits(priors, efficient_rule, rates),
                         sum(max(row.values()) for row in x)-1)

    def test_multitype_redundant_task(self):
        priors = [{F(1, 3): F(1, 4), F(2, 3): F(1, 2), F(4, 3): F(1, 4)},
                  {F(1, 2): F(1, 3), F(3, 2): F(2, 3)},
                  {F(3, 4): F(1, 2), F(5, 4): F(1, 2)}]
        for rule in (lambda t: efficient_rule(t, 2),
                     lambda t: {tuple(j for j in range(3)
                       if j != (sum(int(c*12) for c in t) % 3)): F(1)}):
            x, rates = self.check_joint_incentives(priors, rule, F(2), 2)
            target = sum(priors[i][d] * max(c/F(2)*(v-values[d])
                          for c, v in values.items())
                         for i, values in enumerate(x) for d in values)
            self.assertEqual(expected_audits(priors, rule, rates), target)

    def test_nonmonotone_target_rule(self):
        priors = [{F(1, 2): F(1, 3), F(3, 2): F(2, 3)}]*3
        rule = lambda t: {((sum(int(c*2) for c in t)//2) % 3,): F(1)}
        x, rates = self.check_joint_incentives(priors, rule, F(2), 1)
        self.assertEqual(expected_audits(priors, rule, rates),
                         sum(max(row.values()) for row in x)-1)

    def test_threshold_shutdown_counterexample(self):
        low, high = F(1, 2), F(3, 2)
        priors = [{low: F(1, 2), high: F(1, 2)}]*3
        rule = lambda t: efficient_rule(t, 2)
        x, rates = self.check_joint_incentives(priors, rule, F(2), 2)
        self.assertEqual(x[0], {low: F(11, 12), high: F(5, 12)})
        self.assertEqual(rates[0][high], F(3, 14))
        self.assertEqual(expected_audits(priors, rule, rates), F(3, 16))
        self.assertEqual(sum(max(row.values()) for row in x)-2, F(3, 4))

    def test_designation_requires_no_audit(self):
        priors = [{F(1, 2): F(1, 2), F(3, 2): F(1, 2)}]*3
        rule = lambda t: {(0,): F(1)}
        _, rates = self.check_joint_incentives(priors, rule, F(2), 1)
        self.assertEqual(expected_audits(priors, rule, rates), 0)

    def test_reliability_selective_audit_closed_form(self):
        low, high, benefit = F(1, 2), F(3, 2), F(2)
        priors = [{low: F(1, 2), high: F(1, 2)}]*3
        # Mix arbitrary report-dependent success probabilities with efficient
        # or deliberately inefficient minimal coalitions; all arithmetic exact.
        for variant in range(5):
            def rule(t):
                chance = F((sum(int(c*2) for c in t)+variant) % 5, 4)
                base = efficient_rule(t, 2) if variant % 2 else {(0, 1): F(1)}
                return {**{coalition: chance*p for coalition, p in base.items()},
                        (): 1-chance}
            s, x, audit = reliability_audits(priors, rule, benefit)
            for i, prior in enumerate(priors):
                for c in prior:
                    honest = benefit*s[i][c]-c*x[i][c]
                    for d in prior:
                        self.assertLessEqual(reliability_deviation(priors, rule,
                            benefit, s, x, audit, i, c, d), honest)
                        alpha, beta = audit[i][d]
                        gain = benefit*(s[i][d]-s[i][c])+c*(x[i][c]-x[i][d])
                        self.assertGreaterEqual(benefit*alpha+(benefit-c)*beta, gain)
                        # Exhaust a rational grid of feasible alternative audit
                        # pairs: none can improve the closed-form objective.
                        for numerator_u in range(9):
                            u = F(numerator_u, 8)*(s[i][d]-x[i][d])
                            for numerator_v in range(9):
                                v = F(numerator_v, 8)*x[i][d]
                                feasible = all(benefit*u+(benefit-e)*v >=
                                    benefit*(s[i][d]-s[i][e])+e*(x[i][e]-x[i][d])
                                    for e in prior)
                                if feasible:
                                    self.assertGreaterEqual(u+v, alpha+beta)

    def test_lower_reliability_can_require_more_audits(self):
        low, high, benefit = F(1, 2), F(3, 2), F(2)
        priors = [{low: F(1, 2), high: F(1, 2)}]*3
        rule = lambda t: efficient_rule(t, 2) if all(c == low for c in t) else {(): F(1)}
        s, x, audit = reliability_audits(priors, rule, benefit)
        audit_count = sum(priors[i][d]*sum(pair)
                          for i, row in enumerate(audit) for d, pair in row.items())
        self.assertEqual(audit_count, F(3, 8))
        self.assertEqual(audit[0][low], (F(1, 12), F(1, 6)))
        self.assertGreater(audit_count,
            iid_frontier(3, 2, F(1, 2), low, benefit))
        for i in range(3):
            for c in priors[i]:
                for d in priors[i]:
                    self.assertLessEqual(reliability_deviation(priors, rule,
                        benefit, s, x, audit, i, c, d), benefit*s[i][c]-c*x[i][c])

    def test_reports_reduce_external_inspections(self):
        self.assertEqual(iid_frontier(2, 1, F(1, 2), F(1, 2), F(2)), F(1, 2))


if __name__ == '__main__':
    unittest.main()
