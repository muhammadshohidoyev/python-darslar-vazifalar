# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:15:47 2022

@author: User
"""

from math import sqrt
def even(r):
    evens = []
    for x in r:
        if x%2 == 0:
            evens.append(x)
    return evens