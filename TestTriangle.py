# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import math

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Scalene&Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,3,4),'Scalene&Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(5,12,13),'Scalene&Right', '5,12,13 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','Should be equilateral')
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral', 'Should be equilateral')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(10,9,10), 'Isosceles', 'Should be isosceles')
        self.assertEqual(classifyTriangle(4,4,3), 'Isosceles', 'Should be isosceles')

    def testScalene(self):
        self.assertEqual(classifyTriangle(2,7,6), 'Scalene', 'Should be scalene')
        self.assertEqual(classifyTriangle(5,6,8), 'Scalene', 'Should be scalene')

    def testValidInputA(self):
        self.assertEqual(classifyTriangle(209,6,7), 'InvalidInput', 'Invalid input')
        self.assertEqual(classifyTriangle(56,409,7), 'InvalidInput', 'Invalid input')

    def testValidInputB(self):
        self.assertEqual(classifyTriangle('209',6,8.9), 'InvalidInput', 'Invalid input')
        self.assertEqual(classifyTriangle('six',3.6,[10]), 'InvalidInput', 'Invalid input')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,2,1), 'NotATriangle', 'Should not be a triangle')
        self.assertEqual(classifyTriangle(3,3,7), 'NotATriangle', 'Should not be a triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

