# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:34:37 2022

@author: User
"""

#from datetime import date

# d1 = date(2022, 3, 10)
# print(d1)
# d2 = date(2022, 3, 24)
# print(d2)
# d3 = date(2022, 4, 7)
# print(d3)
# d4 = date(2022, 4, 21)
# print(d4)
# d5 = date(2022, 5, 5)
# print(d5)
# d6 = date(2022, 5, 19)
# print(d6)
# d7 = date(2022, 6, 2)
# print(d7)
# d8 = date(2022, 6, 16)
# print(d8)
# d9 = date(2022, 6, 30)
# print(d9)
# d10 = date(2022, 7, 14)
# print(d10)

# import datetime as dt 

# bugun = dt.date.today()
# ramazon = dt.date(2022, 4, 3)
# farq = ramazon-bugun
# print(farq)
# print(f"Ramazonga {farq.days} kun qoldi")

# bugun = dt.date.today()
# qurbon_hayit = dt.date(2022, 7, 10)
# farq = qurbon_hayit-bugun
# print(farq)
# print(f"Qurbon hayitga {farq.days} kun qoldi")

# from datetime import date
# import datetime

# def calculateAge(birthDate):
#     today = date.today()
#     age = today.year - birthDate.year - ((today.month, today.day) < 
#         (birthDate.month, birthDate.day))
    
#     return age

# print(calculateAge(date(1999, 7, 23)), "years")


# end_date = datetime.datetime(2022,3,14)
# start_date = datetime.datetime(1999, 7, 23)

# num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
# print(num_months, "months")
# def months(d1, d2):
#     return d2.month - d1.month + 12 *(d2.year - d1.year)

# d2 = datetime.datetime(2022, 3, 15)
# d1 = datetime.datetime(1999, 7, 23)

# print(months(d1, d2), "months")

# def numOfDays(date1, date2):
#     return (date2-date1).days

# date1 = date(1999, 7, 23)
# date2 = date(2022, 3, 15)
# print(numOfDays(date1, date2), "days")

import re

# model = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

# msg = "Telefon raqamingizni kiriting:"


# while True: 
#     number = input(msg)
#     if re.match(model, number):
#         print("Siz kiritgan raqam qabul qilindi!")
#         break
#     else:
#         print("Siz noto'g'ri raqamni kiritdingiz!")

model = '(https.*)'
#model = '((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'

text = "Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"


url = re.findall(model,text)
print(url)























































