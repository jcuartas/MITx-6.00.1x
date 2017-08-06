#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:32:32 2017

@author: jcuartas
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    sumD = 0
    dCount = 0
    for i in s:
        try:
            sumD += int(i)
            dCount += 1
        except:
            continue
    if dCount == 0:
        raise ValueError
    return sumD

print(sum_digits("a;d"))
