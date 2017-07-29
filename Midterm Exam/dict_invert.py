#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 10:41:29 2017

@author: jcuartas

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}


"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    dInv = {}
    auxList = []
    for key, value in d.items():
        if value not in dInv:
            dInv[value] = [key]
        else:
            auxList = dInv[value] + [key]
            auxList.sort() 
            dInv[value] = auxList
    return dInv

d = {1:10, 2:20, 3:30}
print(dict_invert(d))
d = {1:10, 2:20, 3:30, 4:30}     
print(dict_invert(d))
d = {4:True, 2:True, 0:True}
print(dict_invert(d))    