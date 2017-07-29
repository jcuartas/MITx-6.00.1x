#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:00:59 2017

@author: jcuartas
"""

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    import string
    total = string.ascii_lowercase
    available = ""
    for i in total:
        if i not in lettersGuessed:
            available += i
    
    return available
print(getAvailableLetters(lettersGuessed))