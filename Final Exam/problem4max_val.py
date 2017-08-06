#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:53:49 2017

@author: jcuartas
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
    tList = []
    for i in range(len(t)):
        if type(t[i]) == int:
            tList.append(t[i])
        else:
            tList.append(max_val(t[i]))
    return max(tList)
    
print(max_val([8, (9, 5)]))
print(max_val((5, (1,2), [[1],[2]])))
print(max_val((5, (1,2), [[1],[9, (1, 2, 16, 1)]])))