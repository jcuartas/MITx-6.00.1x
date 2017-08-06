#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:29:20 2017

@author: jcuartas
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    key_code = {}
    decoded = ""
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    
    for j in code:
        decoded += key_code[j]

    return (key_code, decoded)

print(cipher("abcd", "dcba", "dab"))