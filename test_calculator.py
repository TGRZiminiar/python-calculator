import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_2(self):
        self.assertEqual(self.calc.add(-5, 8), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-10, 20), -30)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(0, 1), -1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 1), 3)

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(0, 11), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4,2), 2)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(-10, 0), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(6,2), 0)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(3,2), 1)

if __name__ == '__main__':
    unittest.main()