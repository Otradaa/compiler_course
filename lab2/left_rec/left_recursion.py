def left_rec(grammar):
    A = grammar.non_terminals
    for i in range(len(A)):
        for j in range(i):
            # Ai->Ajy
            aij_rules = []
            for rule in grammar.rules:
                if rule.left_part == A[i] and A[j] == rule.right_part[0]:
                    aij_rules.append(rule)
            for rule in aij_rules:
                aj = rule.right_part[0]
                aj_rules = []
                for r in grammar.rules:
                    if r.left_part == aj:
                        aj_rules.append(r)
                grammar.rules.remove(rule)
                for r in aj_rules:
                    # Ai->xiy
                    right_part = r.right_part.copy()
                    right_part.extend(rule.right_part[1:])
                    grammar.add_rule(rule.left_part, ' '.join(right_part))
        # непосредственная
        recursive_rules = {
            'rec': [],
            'nonrec': [],
        }
        for rule in grammar.rules:
            if rule.left_part == A[i]:
                if rule.right_part[0] == A[i]:
                    recursive_rules['rec'].append(rule)
                else:
                    recursive_rules['nonrec'].append(rule)

        if len(recursive_rules['rec']) > 0:
            new_non_literal = f'{A[i]}1'
            grammar.add_non_terminal(new_non_literal)
            # левую заменяем на правую: к нерекурсивным добавляем новый нетерминал + нерекурсивные
            for rule in recursive_rules['nonrec']:
                # grammar.rules.remove(rule)
                if rule.right_part[0] != grammar.eps:
                    grammar.add_rule(A[i],
                                     ' '.join(rule.right_part) + ' ' + new_non_literal)
                else:
                    grammar.add_rule(A[i], new_non_literal)
                    grammar.add_rule(new_non_literal, 'eps')

            #добавляем правила с новым нетерминалом и правой рекурсии рекурсивынх + нерекурсивная часть рекурсивных
            for rule in recursive_rules['rec']:
                grammar.rules.remove(rule)
                grammar.add_rule(new_non_literal,
                                 ' '.join(rule.right_part[1:]) + ' ' + new_non_literal)
                grammar.add_rule(new_non_literal,
                                 ' '.join(rule.right_part[1:]))