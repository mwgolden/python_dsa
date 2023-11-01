import unittest
from fibonacci import fibonacci


class TestFibonacciMethods(unittest.TestCase):
    def test_fib_with_memoization(self):
        fib = fibonacci.fib_with_memoization(6)
        self.assertEqual(fib, 8)  # add assertion here

    def test_fib_with_tabulation(self):
        fib = fibonacci.fib_with_tabulation(6)
        self.assertEqual(fib, 8)

    def test_fib_with_tabulation_constant_space(self):
        fib = fibonacci.fib_with_tabulation_constant_space(6)
        self.assertEqual(fib, 8)


if __name__ == '__main__':
    unittest.main()
