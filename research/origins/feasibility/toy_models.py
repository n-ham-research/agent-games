"""Exact finite feasibility checks; no LLM calls or external dependencies."""
from fractions import Fraction as F
from itertools import product
import json


def coherence():
    # C4 -> C2; normalized sections have odd lift 1 or 3.
    out = []
    for lift in (1, 3):
        direct = 0
        composed = (2 * lift) % 4
        out.append({"odd_lift": lift, "two_swaps": composed,
                    "direct_identity": direct,
                    "role_equal": composed % 2 == direct % 2,
                    "full_state_equal": composed == direct,
                    "binary_probe_equal": int(composed == 0) == int(direct == 0)})
    assert all(x["role_equal"] and not x["full_state_equal"]
               and not x["binary_probe_equal"] for x in out)
    return out


def observation():
    # Two equiprobable capability states. a matches state => reward one.
    # A truthful identity bit passes a binary symmetric channel, error e.
    out = []
    for e in (F(0), F(1, 4), F(1, 2)):
        values = []
        for policy in product((0, 1), repeat=2):
            v = sum(F(1, 2) * (1-e if y == z else e)
                    * int(policy[y] == z) for z, y in product((0, 1), repeat=2))
            values.append(v)
        best = max(values)
        assert best == 1-e
        out.append({"bit_error": str(e), "optimal_reward": str(best),
                    "blind_reward": "1/2", "value_of_signal": str(best-F(1, 2))})
    return out


def incentives(n=3, benefit=F(3, 2), cost=F(1)):
    profiles = list(product((0, 1), repeat=n))
    def u(s, i):
        return benefit * int(all(s)) - cost * s[i]
    def potential(s):
        return benefit * int(all(s)) - cost * sum(s)
    def welfare(s):
        return sum(u(s, i) for i in range(n))
    equilibria = []
    for s in profiles:
        eq = True
        for i in range(n):
            t = tuple(1-x if j == i else x for j, x in enumerate(s))
            assert u(t, i)-u(s, i) == potential(t)-potential(s)
            eq &= u(s, i) >= u(t, i)
        if eq:
            equilibria.append(s)
    pmax = max(map(potential, profiles))
    wmax = max(map(welfare, profiles))
    assert equilibria == [(0,)*n, (1,)*n]
    assert [s for s in profiles if potential(s) == pmax] == [(0,)*n]
    assert [s for s in profiles if welfare(s) == wmax] == [(1,)*n]
    return {"agents": n, "benefit": str(benefit), "cost": str(cost),
            "pure_equilibria": equilibria,
            "potential_maximizers": [s for s in profiles if potential(s) == pmax],
            "welfare_maximizers": [s for s in profiles if welfare(s) == wmax],
            "optimal_welfare": str(wmax), "worst_equilibrium_welfare": "0"}


if __name__ == "__main__":
    print(json.dumps({"coherence": coherence(), "observation": observation(),
                      "incentives": incentives()}, indent=2))
