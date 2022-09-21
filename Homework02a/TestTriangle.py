# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    print(classifyTriangle(1,2,3) +'hi')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertNotEqual(classifyTriangle(3,3,5),'Right','Should be isoceles')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 should be equilateral')

    def testScaleneTriangls(self):
        self.assertEqual(classifyTriangle(3,4,7),'Scalene','3,4,7 should be scalene')
        self.assertEqual(classifyTriangle(1,2,3),'Scalene','3,4,7 should be scalene')
        self.assertNotEqual(classifyTriangle(3,4,5),'Scalene','3,4,7 should be right')

    def testTriangles(self):
        self.assertNotEqual(classifyTriangle(3,4,8),'Scalene','Should be NotATriangle')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','10,10,10 should be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

