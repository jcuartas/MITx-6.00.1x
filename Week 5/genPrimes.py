#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:13:45 2017

@author: jcuartas
"""

def genPrimes():
    numb = 1
    primes = []
    
    while True:
        numb += 1
        for i in primes:
            if numb % i == 0:
                break
        else:
            primes.append(numb)
            yield numb