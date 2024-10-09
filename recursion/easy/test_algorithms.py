import unittest
from basic_sum import Solution as BasicSum
from factorial import Solution as FactorialSolution


class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.basic_sum = BasicSum()
        self.factorial = FactorialSolution()

    def test_basic_sum(self):
        self.assertEqual(self.basic_sum.calculateSum(5), 15)
        self.assertEqual(self.basic_sum.calculateSum(0), 0)
        self.assertEqual(self.basic_sum.calculateSum(1), 1)
        self.assertEqual(self.basic_sum.calculateSum(10), 55)

    def test_factorial(self):
        self.assertEqual(self.factorial.calculateFactorial(5), 120)
        self.assertEqual(self.factorial.calculateFactorial(0), 1)
        self.assertEqual(self.factorial.calculateFactorial(1), 1)
        self.assertEqual(self.factorial.calculateFactorial(3), 6)
        self.assertEqual(self.factorial.calculateFactorial(10), 3628800)

    def test_factorial_large_number(self):
        # This test might take longer to run
        self.assertEqual(self.factorial.calculateFactorial(
            20), 2432902008176640000)

    def test_factorial_negative_number(self):
        with self.assertRaises(RecursionError):
            self.factorial.calculateFactorial(-1)


if __name__ == '__main__':
    unittest.main()
