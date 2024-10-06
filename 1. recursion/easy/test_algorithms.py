import unittest

from basic_sum import Solution as BasicSum


class TestAlgorithms(unittest.TestCase):
    def test_basic_sum(self):
        solution = BasicSum()
        self.assertEqual(solution.calculateSum(5), 15)
        self.assertEqual(solution.calculateSum(0), 0)
        self.assertEqual(solution.calculateSum(1), 1)


if __name__ == '__main__':
    unittest.main()
