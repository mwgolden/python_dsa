import unittest
from challenges import min_cost_path


class TestMinCostPath(unittest.TestCase):
    def test_min_cost_path(self):
        matrx = [
            [3, 2, 12, 15, 10],
            [6, 19, 7, 11, 17],
            [8, 5, 12, 32, 21],
            [3, 20, 2, 9, 7]
        ]
        min_cost = min_cost_path.min_cost_path(matrx)
        self.assertEqual(min_cost, 52)  # add assertion here

    def test_min_cost_path_with_memoization(self):
        matrx = [
            [3, 2, 12, 15, 10],
            [6, 19, 7, 11, 17],
            [8, 5, 12, 32, 21],
            [3, 20, 2, 9, 7]
        ]
        min_cost = min_cost_path.min_cost_path_with_memoization(matrx)
        self.assertEqual(min_cost, 52)  # add assertion here


if __name__ == '__main__':
    unittest.main()
