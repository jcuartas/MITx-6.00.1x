#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 12:18:09 2017

@author: jcuartas - Juan Manuel Cuartas Bernal
    Inputs
        n integer
        s integer
    Output
        polysum float
    
"""

from math import *
def polysum(n, s):
    # Calculate area of the polygon
    area = (0.25*n*s**2)/(tan(pi/n))
    # Calculate perimeter
    perimeter = n * s
    # Polysum is the sum of the area plus squared perimeter
    return round(area + perimeter**2, 4)