#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:25:35 2017

@author: jcuartas
"""

s = 'azcbobobegghakl'

def countVowels(s):
    counter = 0
    for i in range(len(s)):
        if s[i] in ["a", "e", "i", "o", "u"]:
            counter += 1
    print("Number of vowels:", counter)
    
countVowels(s)
            