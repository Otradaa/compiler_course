from syntax_tree import Tree


class OperatorPrecedenceParsing(object):
    def __init__(self):
        #               0~ 1& 2! 3a 4t 5f 6$
        #               !,f,&,t,~,a,$
        self.symbols = ['!', 'false', '&', 'true', '~', 'a', '$']
        self.matrix = [['1', '<', '1', '<', '<', '<', '>'],
                       ['>', '2', '>', '2', '3', '2', '>'],
                       ['1', '<', '1', '<', '<', '<', '>'],
                       ['>', '2', '>', '2', '3', '2', '>'],
                       ['1', '<', '1', '<', '<', '<', '>'],
                       ['>', '2', '>', '2', '3', '2', '>'],
                       ['<', '<', '<', '<', '<', '<', '=']]
        self.errors_dict = {
            '1': "(1)Неверное расположение логических операторов",
            '2': "(2)Неверное расположение логических значений",
            '3': "(3)Неверное расположение отрицания",
        }
        self.marker = '$'
        self.symbol = []
        self.prn = []

    def ind(self, ch):
        return self.symbols.index(ch)

    def operator_precedence_parsing(self, grammar, string):
        if string[0] == self.marker:
            return True
        s = ['' for _ in range(10)]
        s[0] = self.marker
        t = 0  # for stack
        i = 0  # for string
        n = 0
        prn = []
        ch = string[i]
        f_error = False
        tree_list = []
        while t > 0 or ch != self.marker:
            chose = self.matrix[self.ind(s[t])][self.ind(ch)]
            if chose in ['<', '=']:  # перенос
                tree_list.append(Tree(ch))
                t = t + 1
                s[t] = ch
                i = i + 1
                ch = string[i]
                print(f'Shift: {s[0:t+1]}')
            elif chose == '>':  # свертка
                while True:
                    length = 0
                    prn.append(s[t])
                    for rule in grammar.rules:
                        if s[t] in rule.right_part:
                            length = len(rule.right_part)
                            break
                    tree1 = Tree('S ' + str(n))
                    n = n+1
                    for ind_tr in range(length):
                         tree1.childs.append(tree_list[len(tree_list)-length +ind_tr])
                    for _ in range(length):
                        tree_list.pop()
                    tree_list.append(tree1)

                    t = t - 1
                    print(f'Reduce: {s[0:t+1]}')
                    if self.matrix[self.ind(s[t])][self.ind(s[t+1])] == '<':
                        break
            else:
                f_error = True
                break

        if not f_error:
            print(f'Postfix: {prn}')
            return tree_list[0]
        else:
            print(f'Postfix: {prn}')
            print(self.errors_dict[chose])
            return None

