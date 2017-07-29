#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:00:59 2017

@author: jcuartas
"""

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    sW_copy = list(secretWord[:])
    
    for e in lettersGuessed:
        if e in secretWord:
            for i in range(sW_copy.count(e)):
                sW_copy.remove(e)
    return len(sW_copy) == 0
#print(isWordGuessed(secretWord, lettersGuessed))