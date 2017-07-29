#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:00:59 2017

@author: jcuartas
"""

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'a', 'l']

def getGuessedWord(secretWord, lettersGuessed):
    sW_copy = []
    secW_clone = secretWord[:]
    
    for e in lettersGuessed:
        if e in secretWord:
            sW_copy.append(e)
    
    for i in secretWord:
        
        if i not in sW_copy:
            secW_clone = secW_clone.replace(i, ' _ ')
            
    return secW_clone
print(getGuessedWord(secretWord, lettersGuessed))