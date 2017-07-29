 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:26:49 2017

@author: jcuartas
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    def __len__(self):
        return len(self.vals)
    
    def intersect(self, other):
        x = intSet()
        for i in range(self.__len__()):
            print(self.vals[i])
            if other.member(self.vals[i]):
                x.insert(self.vals[i])
        return x

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

s = intSet()
s.insert(1)
s.insert(2)
s.insert(3)
s2 = intSet()
s2.insert(1)
s2.insert(3)
s2.insert(5)
s3 = s.intersect(s2)
print(len(s3))
print(s3)
print(type(s3))