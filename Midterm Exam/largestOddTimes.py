#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 04:02:34 2017

@author: jcuartas
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    LCount = {}
    largestKey = None
    count = 0
    for i in L:
        count = L.count(i)
        if count%2 == 1:
            LCount[i] = count
    
    
    for key, value in LCount.items():
        if largestKey == None or largestKey < key:
            largestKey = key
    
    return largestKey

print(largest_odd_times([3,9,5,3,5,3]))
print(largest_odd_times([2, 2]))
print(largest_odd_times([2, 2, 4, 4]))
print(largest_odd_times([2, 4, 5, 4, 5, 4, 2, 2]))
print(largest_odd_times([3, 2]))