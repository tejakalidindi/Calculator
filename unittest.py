# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:26:50 2021

@author: Teja Kalidindi
"""

import unittest
from Calculator import scientific
class TestSum(unittest.TestCase):
    def test_add(self):
        a = 1
        b = 1
        result = scientific.add(self,a,b)
        self.assertEqual(result, 2)
    def test_subtract(self):
        a = 1
        b = 1
        result = scientific.subtract(self,a,b)
        self.assertEqual(result, 0)
    def test_multiply(self):
        a = 1
        b = 1
        result = scientific.multiply(self,a,b)
        self.assertEqual(result, 1)
    def test_divide(self):
        a = 1
        b = 1
        result = scientific.divide(self,a,b)
        self.assertEqual(result, 1)
    def test_sin(self):
        c = 0
        result = scientific.sin(self,c)
        self.assertEqual(result, 0)
    def test_cos(self):
        c = 0
        result = scientific.cos(self,c)
        self.assertEqual(result, 1)
    def test_tan(self):
        c = 0
        result = scientific.tan(self,c)
        self.assertEqual(result, 0)
    def test_complex(self):
        a = 1
        b = 1
        c = 0
        result = scientific.add(self,scientific.tan(self,scientific.subtract(self,a,b)),scientific.tan(self,c))
        self.assertEqual(result, 0)        

if __name__ == '__main__':
    unittest.main()
