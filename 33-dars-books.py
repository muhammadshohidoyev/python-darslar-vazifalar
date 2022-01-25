# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 10:46:24 2021

@author: User
"""

while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book: break
    with open('books.txt','a') as file:
        file.write(book+'\n')