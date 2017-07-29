#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:27:43 2017

@author: jcuartas
"""

balance = 3926
annualInterestRate = 0.2
altBalance = balance
monthlyPayment = 0

while altBalance >= 0:
    altBalance = balance
    monthlyPayment += 10
    for i in range(12):
        
        unpaidBalance = altBalance - monthlyPayment
    
        altBalance = unpaidBalance + (annualInterestRate/12) * unpaidBalance

print("Lowest Payment:", monthlyPayment)
    