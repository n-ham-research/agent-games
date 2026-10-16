"""Exact repeated-worker counterfactual lift; no LP optimizer."""
from fractions import Fraction as F
from itertools import product
from collections import Counter


def leaves(tree):
    return (tree,) if isinstance(tree, int) else leaves(tree[1])+leaves(tree[2])


def repeated(tree):
    return tuple(sorted(i for i, count in Counter(leaves(tree)).items() if count > 1))


def value(tree, active):
    if isinstance(tree, int):
        return int(tree in active)
    a, b = value(tree[1], active), value(tree[2], active)
    return a & b if tree[0] == 'and' else a | b


def lift(tree, active):
    """Node state=(actual value, each repeated-worker-flip value, sensitivity)."""
    r = repeated(tree)
    worlds = (frozenset(active),)+tuple(frozenset(active) ^ {i} for i in r)
    states = {}
    def visit(node, address, sensitivity):
        vals = tuple(value(node, world) for world in worlds)
        states[address] = vals+(sensitivity,)
        if isinstance(node, int):
            return
        op, left, right = node
        a, b = value(left, active), value(right, active)
        visit(left, address+(0,), sensitivity*(b if op=='and' else 1-b))
        visit(right, address+(1,), sensitivity*(a if op=='and' else 1-a))
    visit(tree, (), 1)
    return r, states


def valid_gate(op, parent, left, right):
    vals = tuple(a & b if op=='and' else a | b for a,b in zip(left[:-1],right[:-1]))
    return (parent[:-1] == vals and
            left[-1] == parent[-1]*(right[0] if op=='and' else 1-right[0]) and
            right[-1] == parent[-1]*(left[0] if op=='and' else 1-left[0]))


def gate_tables(op, r):
    """Enumerate O(4^r) supported gate tuples, without enumerating all D³."""
    vectors = tuple(product((0, 1), repeat=r+1))
    out = []
    for lv, rv, p in product(vectors, vectors, (0, 1)):
        pv = tuple(a & b if op=='and' else a | b for a,b in zip(lv, rv))
        ls = lv+(p*(rv[0] if op=='and' else 1-rv[0]),)
        rs = rv+(p*(lv[0] if op=='and' else 1-lv[0]),)
        out.append((pv+(p,), ls, rs))
    return tuple(out)


def marginals(tree, law):
    r = repeated(tree)
    unary, gates, mass = {}, {}, {}
    for active, prob in law.items():
        b = tuple(int(i in active) for i in r)
        mass[b] = mass.get(b,F(0))+prob
        _, states = lift(tree, active)
        def visit(node, address):
            key = b,address,states[address]
            unary[key] = unary.get(key,F(0))+prob
            if isinstance(node,int): return
            key = b,address,(states[address],states[address+(0,)],states[address+(1,)])
            gates[key] = gates.get(key,F(0))+prob
            visit(node[1],address+(0,));visit(node[2],address+(1,))
        visit(tree,())
    return r,mass,unary,gates


def sparse_reconstruct(tree, mass, unary, gates):
    r = repeated(tree)
    u,g = dict(unary),dict(gates)
    result = {}
    for b, total in mass.items():
        left = total
        while left:
            root = next(state for (bits,addr,state),p in u.items() if bits==b and addr==() and p>0)
            uk,gk,active = [],[],{i for i,bit in zip(r,b) if bit}
            def visit(node,address,state):
                uk.append((b,address,state))
                if isinstance(node,int):
                    if node not in r and state[0]: active.add(node)
                    return
                triple = next(t for (bits,addr,t),p in g.items()
                              if bits==b and addr==address and t[0]==state and p>0)
                gk.append((b,address,triple))
                visit(node[1],address+(0,),triple[1]);visit(node[2],address+(1,),triple[2])
            visit(tree,(),root)
            p = min([u[key] for key in uk]+[g[key] for key in gk])
            for key in uk:u[key]-=p
            for key in gk:g[key]-=p
            a=frozenset(active);result[a]=result.get(a,F(0))+p
            left-=p
    if any(u.values()) or any(g.values()):raise ValueError('residual inconsistent marginals')
    return result
