import unittest

from left_rec.grammar import Grammar
from useless.useless_remover import useless_remover

class MyTestCase(unittest.TestCase):
    def test_useless(self):
        a = Grammar()
        a.load_from_file('../test_grammar')
        b = useless_remover(a)
        b.save_to_file('./results/use0')

    def test_useless1(self):
        a = Grammar()
        a.load_from_file('../test_grammar1')
        b = useless_remover(a)
        b.save_to_file('./results/use1')

    def test_useless2(self):
        a = Grammar()
        a.load_from_file('../test_grammar2')
        b = useless_remover(a)
        b.save_to_file('./results/use2')

if __name__ == '__main__':
    unittest.main()
