# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 10:43:28 2022

@author: User
"""

# yosh = input("Yoshingizni kiriting: ")

# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Siz butun son kiritmadingiz")
# else:
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz")
    
# print("Dastur davom etayapti")   
# print("Dastur tugadi") 
    
# ZeroDivisionError
    
# x,y=5,10
# try:
    
#     y/(x-5)    
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")
    
# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[4])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}

# key="tel"
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")

# print(user['username'])    
    
# filename = "data.txt" # bunday fayl mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()    
# except FileNotFoundError:    
#     print(f"{filename} mavjud emas")
    
#import json
#files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
#for filename in files:
    #try:
        #with open(filename) as f:
            #talaba = json.load(f)        
    #except FileNotFoundError:
        #print(f"{filename} mavjud emas")
        #pass
    #else:
        #print(talaba['ism'])
        # fayl ustida turli amallar     
    
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")    
    
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break        

print(f"Siz {2021-yosh} yilda tug'ilgansiz")    
    
    
    
    
    
    
    
    