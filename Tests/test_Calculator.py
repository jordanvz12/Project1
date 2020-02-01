import unittest

from Calculator.Calculator import Calculator
class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_calculator_addition(self):
        calculator = Calculator()
        result = calculator.addition(1,2)
        self.assertEqual(3, result)

    def test_calculator_subtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(1,2)
        self.assertEquals(-1, result)

    def test_calculator_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(1,2)
        self.assertEquals(2, result)

    def test_calculator_divide(self):
        calculator = Calculator()
        result = calculator.divide(1,2)
        self.assertEqual(0.5, result)

    def test_calculator_squareRoot(self):
        calculator = Calculator()
        result = calculator.squareRoot(4)
        self.assertEquals(2, result)

    def test_calculator_square(self):
        calculator = Calculator()
        result = calculator.square(2)
        self.assertEquals(4, result)

if __name__ == '__main__':
    unittest.main()