#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:28:26 2017

@author: jcuartas

Write a Python function that takes in two lists and calculates whether they are permutations
 of each other. The lists can contain both integers and strings. 
 We define a permutation as follows:

the lists have the same number of elements
list elements appear the same number of times in both lists
If the lists are not permutations of each other, the function returns False. 
If they are permutations of each other, the function returns a tuple consisting of the following elements:

the element occuring the most times
how many times that element occurs
the type of the element that occurs the most times
If both lists are empty return the tuple (None, None, None). If more than one 
element occurs the most number of times, you can return any of them.

"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    auxL1 = {}
    auxL2 = {}
    numTimes = 0
    outKey = None
    # Check if the lists are not empty and have the same size
    if not ((L1 == [] and L2 == []) or len(L1) != len(L2)):
        # Count and store elements in dictionaries
        for i in range(len(L1)):
            auxL1[L1[i]] = L1.count(L1[i])
            auxL2[L2[i]] = L2.count(L2[i])
        # Compare dictionaries and get the most occurring element
        for key, value in auxL1.items():
            # If there is a difference, there is no permutation
            if auxL2[key] != value:
                return False
            if numTimes < value:
                numTimes = value
                outKey = key
        return(outKey, numTimes, type(outKey))
    else:
        if L1 == [] and L2 == []:
            return (None, None, None)
        else:
            return False
    
#L1 = [2, 1, 1, 2, "fake", "fake"]
#L2 = [1, 2, 2, 1, "fake", "fake"]

print(is_list_permutation([1, 1], [1]))