import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation
from MathOperations.nthroot import Nthroot
from MathOperations.log import Log

class MyTestCase(unittest.TestCase):


    def test_MathOperations_Addition(self):
        Addition.sum(1,2)
        self.assertEqual(3, Addition.sum(1,2))

    def test_MathOperations_subtraction(self):
        Subtraction.difference(1,2)
        self.assertEqual(-1, Subtraction.difference(1,2))

    def test_MathOperations_sum_list(self):
        valueList = [1,2,3]
        self.assertEqual(6, Addition.sum(valueList))

    def test_MathOperations_multiplication(self):
        Multiplication.product(1,2)
        self.assertEqual(2, Multiplication.product(1,2))

    def test_MathOperations_division(self):
        Division.quotient(1,2)
        self.assertEqual(0.5, Division.quotient(1,2))

    def test_MathOperations_nthroot(self):
        Nthroot.root(2,4)
        self.assertEqual(2, Nthroot.root(2,4))

    def test_MathOperations_exponentiation(self):
        Exponentiation.power(2,2)
        self.assertEqual(4, Exponentiation.power(2,2))

    def test_MathOperations_log(self):
        Log.logarithm(2, 8)
        self.assertEqual(3, Log.logarithm(2,8))


if __name__ == '__main__':
    unittest.main()