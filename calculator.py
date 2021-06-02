# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 09:37:53 2021

@author: Teja Kalidindi
"""
import math as mt

class Calculator:
    def _init_(self):
        print("calculator initialized")
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b
    
    
class scientific(Calculator):
    def _init_(self):
        super()._init_()
    def sin(self, c):
        return mt.sin(c)
    
    def cos(self, c):
        return mt.cos(c)
        
    def tan(self, c):
        return mt.tan(c)

if __name__ == '__main__':
    my_cl = scientific()
#my_cl = Calculator()
#a = 1
#b = 1
#c=0
#print(my_cl.divide(a,b))
#print(my_cl.sin(c))
#print(my_cl.cos(c))
#print(my_cl.add(my_cl.tan(my_cl.subtract(a,b)),my_cl.tan(c)))

