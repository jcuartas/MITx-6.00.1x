#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 12:45:38 2017

@author: jcuartas
"""

# coding: utf-8

# In this problem, you'll create a program that guesses a secret number!
# 
# 
# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
# 
# 
# Here is a transcript of an example session:
# 
# 
# Please think of a number between 0 and 100!
# 
# Is your secret number 50?
# 
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# 
# Is your secret number 75?
# 
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# 
# Is your secret number 87?
# 
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
# 
# Is your secret number 81?
# 
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# 
# Is your secret number 84?
# 
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
# 
# Is your secret number 82?
# 
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# 
# Is your secret number 83?
# 
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
# 
# Game over. Your secret number was: 83

# In[2]:

print("Please think of a number between 0 and 100! ")
high=100
low=0
ans=(high+low)//2
print("Is your secret number "+str(ans)+"?")
x=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly"))
while x not in ['h','l','c']:
    print("Sorry, I did not understand your input.")
    print("Is your secret number "+str(ans)+"?")
    x=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly"))
    break
while x in ['h','l']:
    if x=='h':
        high=ans
    else :
        low=ans
    ans=(high+low)//2
    print("Is your secret number "+str(ans)+"?")
    x=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly"))
    while x not in ['h','l','c']:
        print("Sorry, I did not understand your input.")
        print("Is your secret number "+str(ans)+"?")
        x=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly"))
        
while x=='c':
    print("Game over. Your secret number was: "+str(ans))
    break


# Iteration V/S Recurssion

# Write an iterative function iterPower(base, exp) that calculates the exponential baseexp by simply using successive multiplication. For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. Write such a function below.
# 
# This function should take in two values - base can be a float or an integer; exp will be an integer â‰¥ 0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.

# In[123]:

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp==0:
        a=round((float(1)))
    else:
        a=float(base)
    for i in range(1,exp):
         a=float(a*base)
         
    return(round(a,4))


# In[124]:

iterPower(-4.16,1)


# In above Problem, we computed an exponential by iteratively executing successive multiplications. We can use the same idea, but in a recursive function.
# 
# Write a function recurPower(base, exp) which computes baseexp by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.
# 
# This function should take in two values - base can be a float or an integer; exp will be an integer â‰¥0. It should return one numerical value. Your code must be recursive - use of the ** operator or looping constructs is not allowed.

# In[125]:

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp<1:
        return float(1)
    else:
        return base*(recurPower(base,(exp-1)))
        
recurPower(-2.1, 2)       
        


# In[146]:

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)
       
    


# In[147]:

gcdRecur(25,6)


# 
# Implement the function isIn(char, aStr) which implements to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value
#     
#     
#     

# In[100]:

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr[:]=='':
        return False
    elif aStr[int((len(aStr)/2))]==char:
        return True
    elif len(aStr)==1:
        return False
    elif char<aStr[int((len(aStr)/2))]:
        return isIn(char,aStr[:int((len(aStr)/2))])
    else:
        char>aStr[int((len(aStr)/2))]<char
        return isIn(char,aStr[int((len(aStr)/2)):])
    


# In[113]:

isIn('d','abcde fgrsqyz ')


# A regular polygon has n number of sides. Each side has length s.
# 
# The area of a regular polygon is: 0.25âˆ—nâˆ—s2tan(Ï€/n)
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

# In[133]:

from math import *
def polysum(n,s):
    '''
    n: number of sides,a positive integer
    s: length of a side,a positive real number
    
    returns: The sum of the area and the square of the perimter, of the polygon with n sides each of length s
    '''
    Area=(0.25*n*s*s)/tan(pi/n)
    SquareofP=(n*s)**2
    answer=Area+SquareofP
    return(round(answer,4))


# In[135]:

polysum(22,56)


# In[ ]:
