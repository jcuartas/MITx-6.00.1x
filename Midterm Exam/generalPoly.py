#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:08:39 2017

@author: jcuartas

import math
def make_cylinder_volume_func(r):
    def volume(h):
        return math.pi * r * r * h
    return volume
Use it like this, for example with radius=10 and height=5:

volume_radius_10 = make_cylinder_volume_func(10)
volume_radius_10(5)
=> 1570.7963267948967
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
   
    
    def factorPower(x):
        k = len(L) - 1
        fun = None
        for i in L:
            if fun == None:
                fun = i * x ** k
            else:
                fun += i * x ** k
            k -= 1
        return fun
    
    return factorPower


#print(general_poly([1,2,3,4])(10))
print(general_poly([1, 2, 3, 4, 6])(11))