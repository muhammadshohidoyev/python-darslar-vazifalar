# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:34:47 2021

@author: User
"""

import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs':2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs':1}

with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)












