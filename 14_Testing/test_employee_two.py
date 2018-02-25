import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):


	# Classmethod run at first setup and teardown after class execute completes
	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass


	# setUp and tearDown executes everytime after test.
	def setUp(self):
		self.emp_1 = Employee("Sagar", "Giri", 50000)
		self.emp_2 = Employee("Ram", "Prasad", 60000)


	def tearDown(self):
		pass

	def test_email(self):

		self.assertEqual(self.emp_1.email, "Sagar.Giri@gmail.com")
		self.assertEqual(self.emp_2.email, "Ram.Prasad@gmail.com")

		self.emp_1.first = "John"
		self.emp_2.first = "Jane"

		self.assertEqual(self.emp_1.email, "John.Giri@gmail.com")
		self.assertEqual(self.emp_2.email, "Jane.Prasad@gmail.com")

	def test_fullname(self):

		self.assertEqual(self.emp_1.fullname, "Sagar Giri")
		self.assertEqual(self.emp_2.fullname, "Ram Prasad")

		self.emp_1.first = "John"
		self.emp_2.first = "Jane"

		self.assertEqual(self.emp_1.fullname, "John Giri")
		self.assertEqual(self.emp_2.fullname, "Jane Prasad")

	def test_apply_raise(self):
		self.emp_1 = Employee("Sagar", "Giri", 50000)
		self.emp_2 = Employee("Ram", "Prasad", 60000)

		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 52500)
		self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
	unittest.main()
