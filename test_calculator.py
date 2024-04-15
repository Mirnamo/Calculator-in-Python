"""
test all functions with simple tests
"""
import unittest
from Api_calculator import *
import math

class simple_functions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(3,5), 8)
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(-1,2), 1)
        self.assertEqual(add(-2,2), 0)
        self.assertEqual(add(-5,3), -2)

    def test_substract(self):
        self.assertEqual(substraction(1,2), -1)
        self.assertEqual(substraction(3,5), -2)
        self.assertEqual(substraction(0,0), 0)
        self.assertEqual(substraction(-1,2), -3)
        self.assertEqual(substraction(-2,2), -4)
        self.assertEqual(substraction(5,3), 2)
    
    def test_division(self):
        self.assertEqual(division(1,2), 0.5)
        self.assertEqual(division(3,5), 3/5)
        self.assertEqual(division(-1,2), -1/2)
        self.assertEqual(division(-2,2), -1)
        self.assertEqual(division(-5,3), -5/3)
    
    def test_multiplication(self):
        self.assertEqual(multiplication(1,2), 2)
        self.assertEqual(multiplication(3,5), 15)
        self.assertEqual(multiplication(0,0), 0)
        self.assertEqual(multiplication(-1,2), -2)
        self.assertEqual(multiplication(-2,2), -4)
        self.assertEqual(multiplication(-5,3), -15)
    
    def test_pow(self):
        self.assertEqual(pow(1,2), 1)
        self.assertEqual(pow(3,5), math.pow(3,5))
        self.assertEqual(pow(0,0), 1)
        self.assertEqual(pow(-1,2), math.pow(-1,2))
        self.assertEqual(pow(-2,2), math.pow(-2,2))
        self.assertEqual(pow(-5,3), math.pow(-5,3))
    
    def test_root(self):
        self.assertEqual(root(1,2), math.pow(1,1/2))
        self.assertEqual(root(3,5), math.pow(3,1/5))
        self.assertEqual(root(2,1/2), 4)
        self.assertEqual(round(root(2,-2)), round(math.pow(2,-1/2)))
        

    def test_abs(self):
        self.assertEqual(absolute(1), 1)
        self.assertEqual(absolute(0),0)
        self.assertEqual(absolute(-1),1)
    
    def test_roundup(self):
        self.assertEqual(roundup(2.00000), round(2.00000))
        self.assertEqual(roundup(3.2747474), round(3.2747474))

    
    
# class scientific_tests(unittest.TestCase):

#     def test_sin(self):
#       #test sin, inverse_sin and cosc

#     def test_cos(self):
#       #test cos, inverse_cos and sec

#     def test_tan(self):
#       #test tan. inverse_tan and cotg

#     def test_log(self):

#     def test_ln(self):

#     def test_remainder(self):


if __name__ == '__main__':
    unittest.main()