# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:45:39 2021

@author: User
"""

import pickle

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)
print(talaba2)







