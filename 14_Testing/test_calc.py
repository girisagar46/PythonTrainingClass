import unittest
import calc

class TestCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calc.add(2, 3), 5)
		self.assertEqual(calc.add(1, -1), 0)
		self.assertEqual(calc.add(-1, -1), -2)
		self.assertEqual(calc.add(-2, 3), 1)
	
	def test_subtract(self):
		self.assertEqual(calc.subtract(2, 3), -1)
		self.assertEqual(calc.subtract(1, -1), 2)
		self.assertEqual(calc.subtract(-1, -1), 0)

	def test_multiply(self):
		self.assertEqual(calc.multiply(2, 3), 6)
		self.assertEqual(calc.multiply(1, -1), -1)
		self.assertEqual(calc.multiply(-1, -1), 1)
		self.assertEqual(calc.multiply(-2, 3), -6)

	def test_divide(self):
		self.assertEqual(calc.divide(10, 5), 2)
		self.assertEqual(calc.divide(1, -1), -1)
		self.assertEqual(calc.divide(-1, -1), 1)
		# self.assertRaises(ValueError, calc.divide, 2, 0)
		with self.assertRaises(ValueError):
			calc.divide(10, 0)


if __name__ == '__main__':
	unittest.main()