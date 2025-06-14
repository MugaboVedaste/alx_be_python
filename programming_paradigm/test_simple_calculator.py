import unittest
from simple_calculator import SimpleCalculator # type: ignore

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(7, 3), 21)
        self.assertEqual(self.calc.multiply(8, 0), 0)
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(8, 0), "Error: Cannot divide by zero.")

if __name__ == '__main__':
    unittest.main()