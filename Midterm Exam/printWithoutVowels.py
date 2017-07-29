#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 03:44:10 2017

@author: jcuartas

"""
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    sOut = ""
    for i in s:
        if i not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            sOut += i
    print(sOut)

s = "This is great!"
print_without_vowels(s)

s = "a"
print_without_vowels(s)

        