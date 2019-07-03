import unittest
from left_rec.grammar import Grammar
from left_rec.left_recursion import left_rec


class GrammarCreationCase(unittest.TestCase):
    def test_rec(self):
        a = Grammar()
        a.load_from_file('../test_rec')
        left_rec(a)
        a.save_to_file('./results/rec0')

    def test_rec1(self):
        a = Grammar()
        a.load_from_file('../test_rec1')
        left_rec(a)
        a.save_to_file('./results/rec1')

    def test_rec2(self):
        a = Grammar()
        a.load_from_file('../test_rec2')
        left_rec(a)
        a.save_to_file('./results/rec2')


if __name__ == '__main__':
    unittest.main()
