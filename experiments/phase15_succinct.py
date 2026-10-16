"""Exact summary-flow identities; invokes no LP optimizer."""
from fractions import Fraction as F
from itertools import product


def coalitions(n):
    return [frozenset(i for i, bit in enumerate(bits) if bit)
            for bits in product((0, 1), repeat=n)]


def summary_dags(n, start, step):
    """One layered deterministic-choice DAG per attainable terminal summary.

    Edge=(layer, previous_state, action, next_state). Retain only edges on a
    start-to-terminal path. Parallel action-labelled edges remain distinct.
    """
    layers = [{start}]
    all_edges = []
    for i in range(n):
        edges = [(i, s, a, step(i, s, a))
                 for s in sorted(layers[-1]) for a in (0, 1)]
        all_edges.append(edges)
        layers.append({e[3] for e in edges})
    result = {}
    for terminal in sorted(layers[-1]):
        good = {terminal}
        retained = []
        for i in reversed(range(n)):
            edges = [e for e in all_edges[i] if e[3] in good]
            retained.extend(edges)
            good = {e[1] for e in edges}
        result[terminal] = tuple(sorted(retained))
    return result


def threshold_dags(weights):
    return summary_dags(len(weights), 0,
                        lambda i, s, a: s+a*weights[i])


def coverage_dags(masks, features):
    return summary_dags(len(masks), (0,)*features,
        lambda i, s, a: tuple(min(2, v+a*int(j in masks[i]))
                             for j, v in enumerate(s)))


def terminal_of(active, n, start, step):
    s = start
    for i in range(n):
        s = step(i, s, int(i in active))
    return s


def path_labels(edges, n, start):
    """Finite test helper, not used by the polynomial construction."""
    frontier = [(start, frozenset())]
    for i in range(n):
        frontier = [(e[3], a | (frozenset({i}) if e[2] else frozenset()))
                    for s, a in frontier for e in edges if e[0] == i and e[1] == s]
    return [a for _, a in frontier]


def law_to_flows(law, n, start, step):
    flows = {}
    for active, mass in law.items():
        terminal = terminal_of(active, n, start, step)
        s = start
        for i in range(n):
            action = int(i in active)
            nxt = step(i, s, action)
            key = terminal, (i, s, action, nxt)
            flows[key] = flows.get(key, F(0))+mass
            s = nxt
    return flows


def decompose_flows(flows, n, start):
    """Exact acyclic-flow path decomposition; may change nonessential correlation."""
    residual = {key: F(value) for key, value in flows.items() if value}
    result = {}
    for terminal in sorted({key[0] for key in residual}):
        while any(key[0] == terminal and key[1][0] == 0 and value > 0
                  for key, value in residual.items()):
            path, s, active = [], start, set()
            for i in range(n):
                options = sorted(key for key, value in residual.items()
                    if key[0] == terminal and key[1][0] == i
                    and key[1][1] == s and value > 0)
                if not options:
                    raise ValueError('nonconserving flow')
                key = options[0]
                path.append(key)
                if key[1][2]:
                    active.add(i)
                s = key[1][3]
            if s != terminal:
                raise ValueError('wrong terminal')
            mass = min(residual[key] for key in path)
            for key in path:
                residual[key] -= mass
            active = frozenset(active)
            result[active] = result.get(active, F(0))+mass
    if any(residual.values()):
        raise ValueError('residual flow without a source')
    return result


def threshold_gain(total, i, action, weights, quota, costs, benefit=F(1), delta=F(0)):
    if action:
        return benefit*int(total >= quota and total-weights[i] < quota)-costs[i]-delta
    return costs[i]-benefit*int(total < quota <= total+weights[i])-delta


def coverage_gain(counts, i, action, masks, costs, benefit=F(1), delta=F(0)):
    succeeds = all(counts)
    if action:
        pivotal = succeeds and any(counts[j] == 1 for j in masks[i])
        return benefit*int(pivotal)-costs[i]-delta
    repairs = not succeeds and all(v or j in masks[i] for j, v in enumerate(counts))
    return costs[i]-benefit*int(repairs)-delta


def flow_statistics(flows, n, success, gain, costs, benefit=F(1)):
    mass = sum(value for (terminal, edge), value in flows.items() if edge[0] == 0)
    s = sum(value*int(success(terminal)) for (terminal, edge), value in flows.items()
            if edge[0] == 0)
    x = [sum(value for (_, edge), value in flows.items()
             if edge[0] == i and edge[2] == 1) for i in range(n)]
    margins = {(i, a): sum(value*gain(terminal, i, a)
                   for (terminal, edge), value in flows.items()
                   if edge[0] == i and edge[2] == a)
               for i in range(n) for a in (0, 1)}
    return mass, s, tuple(benefit*s-costs[i]*x[i] for i in range(n)), margins


def direct_statistics(law, n, wins, costs, benefit=F(1), delta=F(0)):
    mass = sum(law.values())
    s = sum(p*int(wins(a)) for a, p in law.items())
    utilities = tuple(sum(p*(benefit*int(wins(a))-costs[i]*int(i in a))
                          for a, p in law.items()) for i in range(n))
    margins = {(i, bit): sum(p*(benefit*(int(wins(a))-int(wins(a ^ {i})))
                          +costs[i]*(1 if bit == 0 else -1)-delta)
                      for a, p in law.items() if int(i in a) == bit)
               for i in range(n) for bit in (0, 1)}
    return mass, s, utilities, margins


def subset_sum_gadget(items, target):
    """Domain 0<a_j<T (standard preprocessing handles other inputs)."""
    if not target > 1 or not items or not all(0 < a < target for a in items):
        raise ValueError('requires nonempty restricted positive subset sum')
    weights = (1,)+tuple(2*a for a in items)+(2*target+1,)
    costs = (F(1, 2),)*(len(items)+1)+(F(3, 4),)
    return weights, 2*target+1, costs


def zero_witness(items, target, selected):
    if sum(items[j] for j in selected) != target:
        raise ValueError('not a subset-sum witness')
    # Positive integer items: each selected item is indispensable at this quota.
    winner = frozenset({0} | {j+1 for j in selected})
    return {winner: F(1, 4), frozenset({0}): F(1, 4), frozenset(): F(1, 2)}
