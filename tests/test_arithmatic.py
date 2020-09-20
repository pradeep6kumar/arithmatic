import arithmatic
import unittest

class TestArithmatic(unittest.TestCase):

	def test_addition(self):
		self.assertEqual(arithmatic.add(2, 3), 5)
	
	def test_addition_error(self):
		with self.assertRaises(TypeError) as context:
			arithmatic.add(2, 'a')
			self.assertEqual(str(context.exception), "You have different types of data use valid combinations")
	
	def test_subtraction(self):
		self.assertEqual(arithmatic.sub(2, 3), -1)
	
	def test_subtraction_error(self):
		with self.assertRaises(TypeError) as context:
			arithmatic.sub(2, 'a')
			self.assertEqual(str(context.exception), "You have different types of data use valid combinations")

	def test_multiplication(self):
		self.assertEqual(arithmatic.mul(2, 3), 6)
	
	def test_multiplication_error(self):
		with self.assertRaises(TypeError) as context:
			arithmatic.mul('b', 'a')
			self.assertEqual(str(context.exception), "You have different types of data use valid combinations")

	def test_division(self):
		self.assertEqual(arithmatic.div(10, 5), 2)
		self.assertEqual(round(arithmatic.div(22, 7),2), 3.14)
	
	def test_division_error(self):
		with self.assertRaises(TypeError) as context:
			arithmatic.div(2, 'a')
			self.assertEqual(str(context.exception), "You have different types of data use valid combinations")

		

            
if __name__ == '__main__':
    unittest.main()




