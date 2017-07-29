#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    
    author: @jcuartas
    """
    #YOUR CODE HERE
    acum = 1
    inc = 2
    
    if k < 1:
        return False
    elif k == 1:
        return True
    else:
        while acum < k:
            acum += inc
            inc += 1
        if acum == k:
            return True
        else:
            return False

print(is_triangular(105))

