# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 11:03:12 2022

@author: User
"""

def get_full_name(ism, familiya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()

#print(get_full_name('alijon','valiyev'))









