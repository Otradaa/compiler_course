import unittest
from nfa.nfa_builder import build_nfa


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = build_nfa('d*(a|b)bbc')
        a.visualize('test')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
