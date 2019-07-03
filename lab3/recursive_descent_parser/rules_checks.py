from syntax_tree import Tree


def add_child(tree, name):
    child = Tree(cargo=name)
    tree.childs.append(child)


def operator(string, i, tree):
    if len(string) <= i.val():
        return False
    mine = i.val()
    child = Tree(cargo='a')
    tree.childs.append(child)
    if string[i.val()] == 'a':
        i.inc()
        child = Tree(cargo='=')
        tree.childs.append(child)
        if string[i.val()] == '=':
            i.inc()
            child = Tree(cargo='expression')
            tree.childs.append(child)
            if expression(string, i, child):
                print(f'({i.val()})op -> a = exp')
                return True
            else: print(f'Position {i.val()} It`s not expression')
        else: print(f'Position {i.val()} It`s not `=`')
    else: print(f'Position {i.val()} It`s not `a`')
    return False


def expression(string, i, tree):
    mine = i.val()
    if len(string) <= i.val():
        return False
    child = Tree(cargo='logic expression')
    tree.childs.append(child)
    if logic_expression(string,i, child):
        print(f'({i.val()})exp -> log exp')
        return True
    else: print(f'Position {i.val()} It`s not logic_expression')
    return False


def logic_expression(string, i, tree):
    mine = i.val()
    if len(string) <= i.val():
        return False
    child = Tree(cargo='logic monomial')
    tree.childs.append(child)
    if logic_monomial(string,i, child):
        i.inc()
        child = Tree(cargo='logic expression 1')
        tree.childs.append(child)
        if logic_expression1(string,i, child):
            print(f'({i.val()})log exp -> log mon    log exp 1')
            return True
        else:
            tree.childs.remove(child)
            print(f'!({i.val()})log exp -> log mon')
            i.dec()
            return True
    else: print(f'Position {i.val()} It`s not logic monomial')
    return False


def logic_monomial(string,i, tree):
    if len(string) <= i.val():
        return False
    mine = i.val()
    child = Tree(cargo='second logic expression')
    tree.childs.append(child)
    if second_logic_expression(string,i, child):
        i.inc()
        child = Tree(cargo='logic monomial 1')
        tree.childs.append(child)
        if logic_monomial1(string,i, child):
            print(f'({i.val()})log mon -> sec log exp    log mon 1')
            return True
        else:
            tree.childs.remove(child)
            print(f'!({i.val()})log mon -> sec log exp')
            i.dec()
            return True
    else: print(f'Position {i.val()} It`s not second logic expression')
    return False


def logic_expression1(string, i, tree):
    mine = i.val()
    if len(string) <= i.val():
        return False
    child = Tree(cargo='!')
    tree.childs.append(child)
    if string[i.val()] == '!':
        i.inc()
        child = Tree(cargo='logic monomial')
        tree.childs.append(child)
        if logic_monomial(string,i, child):
            i.inc()
            child = Tree(cargo='logic expression 1')
            tree.childs.append(child)
            if logic_expression1(string,i, child):
                print(f'({i.val()})log exp 1 -> ! log mon    log exp 1')
                return True
            else:
                tree.childs.remove(child)
                i.dec()
                print(f'({i.val()})log exp 1 -> ! log mon')
                return True
        else: print(f'Position {i.val()} It`s not logic monomial')
    else: print(f'Position {i.val()} It`s not `!`')
    return False


def second_logic_expression(string,i, tree):
    mine = i.val()
    if len(string) <= i.val():
        return False
    child = Tree(cargo='~')
    tree.childs.append(child)
    if string[i.val()] == '~':
        i.inc()
        child = Tree(cargo='first logic expression')
        tree.childs.append(child)
        if first_logic_expression(string,i, child):
            print(f'({i.val()})sec log exp -> ~ fir log exp')
            return True
        else: print(f'Position {i.val()} It`s not first logic expression')
    else:
        tree.childs.remove(child)
        child = Tree(cargo='first logic expression')
        tree.childs.append(child)
        if first_logic_expression(string,i, child): # ###################################
            print(f'({i.val()})sec log exp -> fir log exp')
            return True
    print(f'Position {i.val()} It`s not first logic expression')
    return False


def logic_monomial1(string,i, tree):
    mine = i.val()
    if len(string) <= i.val():
        return False
    child = Tree(cargo='&')
    tree.childs.append(child)
    if string[i.val()] == '&':
        i.inc()
        child = Tree(cargo='second logic expression')
        tree.childs.append(child)
        if second_logic_expression(string,i, child):
            i.inc()
            child = Tree(cargo='logic monomial 1')
            tree.childs.append(child)
            if logic_monomial1(string,i, child):
                print(f'({i.val()})log mon -> & sec log exp   log mon')
                return True
            else:
                tree.childs.remove(child)
                print(f'!({i.val()})log mon -> & sec log exp')
                i.dec()
                return True
        else: print(f'Position {i.val()} It`s not second logic expression')
    else: print(f'Position {i.val()} It`s not `&`')
    return False


def first_logic_expression(string,i, tree):
    mine = i.val()
    child = Tree(cargo=string[i.val()])
    tree.childs.append(child)
    if string[i.val()] in ['a', 'true', 'false']:
        print(f'({i.val()})fir log exp -> a true false')
        return True
    else:
        print(f'Position {i.val()} It`s not `a` or logic value')