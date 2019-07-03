from left_rec.grammar import Grammar
from left_rec.rule import Rule
#rec - 92
def get_X(rules, symbols):
    X = set()
    for S in symbols:
        p: Rule
        for p in rules:
            if S == p.left_part:
                X.update(p.right_part)
    if '|' in X: X.remove('|')
    return X

def get_rules(V, rules):
    ret = list()
    for r in rules:
        if r.left_part in V and set(r.right_part).issubset(V.union('|')):
            ret.append(r)
    return ret

def useless_remover(grammar):
    ret = Grammar()
    N = grammar.non_terminals
    T = grammar.terminals
    S = grammar.start
    ret.start = S
    V = [{S}]
    i = 1
    while True:
        X = get_X(grammar.rules, V[i-1])
        Vi1 = V[i-1].copy()
        Vi1.update(X)
        V.append(Vi1)
        if (len(V[i].difference(V[i-1])) != 0):
            i = i + 1
            continue
        else:
            ret.non_terminals = list(set(N).intersection(V[i]))
            ret.terminals = list(set(T).intersection(V[i]))
            ret.rules = get_rules(V[i],grammar.rules)
            break
    return ret















