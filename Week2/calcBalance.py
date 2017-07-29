#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:06:30 2017

@author: jcuartas
"""

def calcBalance(balance, annualInterestRate, monthlyPaymentRate, month=0):
    # Calculate unpaid balance
    unpaidBalance = balance - (balance * monthlyPaymentRate)
    
    newBalance = unpaidBalance + (annualInterestRate/12) * unpaidBalance
    
    if month == 11:
        print("Remaining balance:", round(newBalance, 2))
    else:
        return calcBalance(newBalance, annualInterestRate, monthlyPaymentRate, month+1)
        
#bal = calcBalance(42, 0.2, 0.04)
#bal2 = calcBalance(484, 0.2, 0.04)

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
for i in range(12):
    unpaidBalance = balance - (balance * monthlyPaymentRate)
    
    balance = unpaidBalance + (annualInterestRate/12) * unpaidBalance
    
print("Remaining balance:", round(balance, 2))