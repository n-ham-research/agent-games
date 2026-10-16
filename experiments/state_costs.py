"""Exact finite persistent-state tracking; see research/persistent-state-costs.md."""
from fractions import Fraction
from itertools import product


def target(t):
    return t % 2


def minimum_tracking_cost(horizon, actuators=(1,), correction_cost=1,
                          actuator_costs=None, checkpoints=True):
    """Dynamic programming on all four physical states, not the claimed formula.

    One primary odd actuator and optional correction 2 at each step. Costs are
    exact. With checkpoints=False only the last step requires accepted state.
    """
    if horizon < 0 or any(h % 2 != 1 for h in actuators):
        raise ValueError("Need nonnegative horizon and odd primary actuators")
    actuator_costs = actuator_costs or {}
    costs = {0: Fraction(0)}
    for t in range(1, horizon + 1):
        nxt = {}
        for x, past in costs.items():
            for h in actuators:
                for correction in (0, 2):
                    y = (x + h + correction) % 4
                    if (checkpoints or t == horizon) and y != target(t):
                        continue
                    price = past + Fraction(actuator_costs.get(h, 0))
                    price += Fraction(correction_cost) * (correction != 0)
                    nxt[y] = min(nxt.get(y, price), price)
        costs = nxt
    return min(costs.values())


def accepted_sequence(operations):
    x = 0
    for t, h in enumerate(operations, 1):
        x = (x + h) % 4
        if x != target(t):
            return False
    return True


def successful_primary_words(horizon):
    return [word for word in product((1, 3), repeat=horizon)
            if accepted_sequence(word)]


def one_state_controllers(horizon):
    return {h: accepted_sequence((h,) * horizon) for h in (1, 3)}


def two_state_controller(horizon):
    a, operations = 0, []
    for _ in range(horizon):
        operations.append(1 if a == 0 else 3)
        a = 1 - a
    return operations


def split_restricted_cost(horizon):
    """C2 x C2, target (parity,parity), primary (1,0), correction (0,1)."""
    x, corrections = (0, 0), 0
    for t in range(1, horizon + 1):
        x = (1 - x[0], x[1])
        required = (t % 2, t % 2)
        if x != required:
            x = (x[0], 1 - x[1])
            corrections += 1
        assert x == required
    return corrections
