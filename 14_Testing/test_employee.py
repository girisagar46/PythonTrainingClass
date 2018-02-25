import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def test_email(self):
		emp_1 = Employee("Sagar", "Giri", 50000)
		emp_2 = Employee("Ram", "Prasad", 60000)

		self.assertEqual(emp_1.email, "Sagar.Giri@gmail.com")
		self.assertEqual(emp_2.email, "Ram.Prasad@gmail.com")

		emp_1.first = "John"
		emp_2.first = "Jane"

		self.assertEqual(emp_1.email, "John.Giri@gmail.com")
		self.assertEqual(emp_2.email, "Jane.Prasad@gmail.com")

	def test_fullname(self):
		emp_1 = Employee("Sagar", "Giri", 50000)
		emp_2 = Employee("Ram", "Prasad", 60000)

		self.assertEqual(emp_1.fullname, "Sagar Giri")
		self.assertEqual(emp_2.fullname, "Ram Prasad")

		emp_1.first = "John"
		emp_2.first = "Jane"

		self.assertEqual(emp_1.fullname, "John Giri")
		self.assertEqual(emp_2.fullname, "Jane Prasad")

	def test_apply_raise(self):
		emp_1 = Employee("Sagar", "Giri", 50000)
		emp_2 = Employee("Ram", "Prasad", 60000)

		emp_1.apply_raise()
		emp_2.apply_raise()

		self.assertEqual(emp_1.pay, 52500)
		self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
	unittest.main()
