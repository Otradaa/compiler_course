import unittest
from syntax_analyzer.grammar import Grammar
from syntax_tree import show_tree


class MyTestCase(unittest.TestCase):

    def test_op(self):
        a = Grammar()
        a.load_file('new_grammar')
        test_string = 'true ! ~ false & a $'
        tree = a.grammar_parsing(test_string)
        show_tree(tree)

    def test_op_wrong_operators(self):
        a = Grammar()
        a.load_file('new_grammar')
        test_string = 'a & ! a $'
        _ = a.grammar_parsing(test_string)

    def test_op_wrong_values(self):
        a = Grammar()
        a.load_file('new_grammar')
        test_string = 'a a a $'
        _ = a.grammar_parsing(test_string)

    def test_op_wrong_not(self):
        a = Grammar()
        a.load_file('new_grammar')
        test_string = 'a & a ~ $'
        _ = a.grammar_parsing(test_string)


if __name__ == '__main__':
    unittest.main()
