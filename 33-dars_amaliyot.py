# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 17:38:57 2021

@author: User
"""
import pickle

with open('amaliyot/pi_million_digits.txt') as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace("\n","")
pi = pi.replace(" ","")

bdata ='25022000'
print(bdata in pi)

pi = float(pi)

with open('amaliyot/pi_float.dat','wb') as file:
    pickle.dump(pi,file)