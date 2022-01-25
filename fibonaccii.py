# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 11:45:59 2022

@author: User
"""

def fibonacci(n):
    fibona=[]
    for x in range(n):
        if x==0 or x==1:
            fibona.append(1)
        else:
            fibona.append(fibona[x-1]+fibona[x-2])
        return fibona



                                                                        