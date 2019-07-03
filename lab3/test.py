import unittest
from recursive_descent_parser.grammar import Grammar
from recursive_descent_parser.left_recursion import remove_left_recursion
from syntax_tree import show_tree


class MyTestCase(unittest.TestCase):

    def test_get_true_grammar(self):
        a = Grammar()
        a.load_from_file('grammar')
        remove_left_recursion(a)
        a.save_to_file('no_leftrec_grammar')

    def test_check_string(self):
        a = Grammar()
        a.load_from_file('no_leftrec_grammar')
        test_string = 'a = true ! ~ false & a'
        res, tree = a.check_string(test_string)
        self.assertEqual(True, res)
        show_tree(tree)

    def test_wrong(self):
        a = Grammar()
        a.load_from_file('no_leftrec_grammar')
        test_string = 'a = a ! ~ c a & false'
        res, _ = a.check_string(test_string)
        self.assertEqual(False, res)


if __name__ == '__main__':
    unittest.main()
