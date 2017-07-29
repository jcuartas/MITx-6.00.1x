#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:43:40 2017

@author: jcuartas
"""
balance = 320000
annualInterestRate = 0.2

from math import *

monthlyInterestRate = annualInterestRate / 12
altBalance = balance
minMonthlyPayment = balance / 12
maxMonthlyPayment = (balance * (1 + monthlyInterestRate)**12)/12

while abs(altBalance) > 0.001:
    # Restart altBalance
    altBalance = balance
    # Calculate medMonthlyPayment
    medMonthlyPayment = (maxMonthlyPayment + minMonthlyPayment)/2
    
    for i in range(12):
        
            unpaidBalance = altBalance - medMonthlyPayment
    
            altBalance = unpaidBalance + (annualInterestRate/12) * unpaidBalance
    
    if altBalance > 0:
        # I need to increment monthly payments min = med max = max
        minMonthlyPayment = medMonthlyPayment
    else:
        # I need to decrement monthly payments min = min max = med
        maxMonthlyPayment = medMonthlyPayment
        
print("Lowest Payment:", round(medMonthlyPayment, 2))   
    
#print("altBalance=", altBalance)
#print(minMonthlyPayment)

#print(maxMonthlyPayment)