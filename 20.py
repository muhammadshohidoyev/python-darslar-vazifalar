# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:27:10 2021

@author: User
"""

#def toliq_ism_yasa(ism, familiya):
    #"""Toliq isma qaytaruvchi funksiya"""
   # toliq_ism = f"{ism} {familiya}"
   # return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz

#talaba1 = toliq_ism_yasa('olim','hakimov')
#talaba2 = toliq_ism_yasa('hakim','olimov')

#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

#def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
   # """Toliq isma qaytaruvchi funksiya"""
   # if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
       # toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    #else:
       # toliq_ism = f"{ism} {familiya}"
    #return toliq_ism.title()

#talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
#talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
##print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

#def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    #avto = {
        #'kompaniya':kompaniya,
            #'model':model,
            #'rang':rangi,
            #'korobka':korobka,
            #'yil':yili,
            #'narh':narhi#
            #}
    #return avto

#avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
#avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
#avtolar = [avto1, avto2]
#print('Onlayn bozordagi mavjud avtomashinalar:')
#for avto in avtolar:
    #if avto['narh']:
        #narh = avto['narh']
   # else:
        #narh = "Noma'lum"
    #print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

#def oraliq(min,max,qadam):
    #sonlar = [] # bo'sh ro'yxat
    #while min<max:
        #sonlar.append(min)
        #min += 2
    #return sonlar

#print(oraliq(0,10))
#print(oraliq(10,21))

#print(oraliq(0,21,2)) # 0 dan 21 gacha 2 qadam bilan

#print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
#avtolar = [] # salondagi avtolar uchun bo'sh ro'yxat
#while True:
   # print("\nQuyidagi ma'lumotlarni kiriting",end=" ")
   # kompaniya = input("Ishlab chiqaruvchi: ")
   # model = input("Modeli: ")
   # rangi = input("Rangi: ")
   # korobka = input("Korobka: ")
   # yili = input("Ishlab chiqarilgan yili: ")
    #narhi = input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    #avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    #javob = input("Yana avto qo'shasizmi? (yes/no): ")
    #if javob == 'no':
       # break

#print("\nSalonimizdagi avtolar: ")
#for avto in avtolar:
    #if avto["narh"]:
        #narh = avto["narh"]
    #else:
        #narh = "Noma'lum"
    #print(
       # f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. narhi: {narh}"
        #)


# def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {
#         "ism": ism,
#         "familiya": familiya,
#         "tyil": tyil,
#         "yoshi": 2020 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#     }
#     return mijoz


# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar = []
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob != "ha":
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(
#         f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#         f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
#     )
    
# def kattasi(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z 
#     return max

# print(kattasi(3,2,5))
    
# def aylana_info(radius, pi=3.14159):
#     aylana = {
#         "radius": radius,
#         "diametr": 2 * radius,
#         "perimetr": 2 * radius * pi,
#         "yuza": pi * radius ** 2,
#     }
#     return aylana    
    
# aylana_info(4)

# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar
# def welcome():
#     """Kutib olish funksiyasi"""
#     print("Xush kelibsiz!")
# welcome()
# def welcome(shaxs):
#     print(f"Welcome to my home, my friend {shaxs.title()}")
    
# welcome('Alex')
# welcome('Joseph')
# def malumot_ber(davlat, poytaxt):
#     """Davlat poytaxti haqida ma'lumot beruvchi funksiya"""
    
#     print(f"Davlat nomi: {davlat.title()}\n"
#           f"Poytax nomi: {poytaxt.title()}")
    
# malumot_ber("o'zbekiston",'toshkent')
# def nom_ber_shart(club, country, club_capital=''):
#     """Jamoa haqida ma'lumot beruvchi funksiya"""
    #print(f"{club} {country}")
#nom_ber("shakhtar donetsk","Ukraine")
    # if club_capital:
    #     jamoa_keltir = f"{club} {club_capital} {country}"
    # else:
    #     jamoa_keltir = f"{club} {country}"
    # return jamoa_keltir.title()
    
#team = nom_ber_shart('shakhtar donetsk','Ukraine')
# team_1 = nom_ber_shart('chelsea','england','london')
# team_2 = nom_ber_shart('ajax','netherland')
# print(f"chempionlar ligasida qatnashgan jamoalar: {team_1} va {team_2}")
# print(f"{team_2} bugun yutqazdi")
def user_info(name, l_name, date_of_birth,job, earnings=None):
    user = {'name':name,
            'l_name':l_name,
            'date_of_birth':date_of_birth,
            'job':job,
            'earnings': earnings}
    return user

# user1 = user_info('John','Johnson',1989,'enginer')
# user2 = user_info('Alex','Smith',1998,'programmer',25000)
# user3 = user_info('Abigal','Roberts',1993,'architect',30000) 
# users = [user1, user2, user3]  
# print("Informations about users:")   
# for user in users:
#     if user['earnings']:
#         earnings = user['earnings']
#     else:
#         earnings = "Unknown"
#     print(f"{user['name']} {user['l_name']}.\
#  Date of birth: {user['date_of_birth']}.\
#  Job:{user['job']}. Monthly earnings:{earnings}")
print("Odamlar haqida ma'lumot ro'yxatini shakllantiramiz.")
userss = []
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    name = input("Name: ")
    l_name = input("Last name: ")
    date_of_birth = input("Date of birth: ")
    job = input("Job: ")
    earnings = input("Earnings: ")
    
    userss.append(user_info(name, l_name, date_of_birth, job, earnings ))

    answers = input("Odamlar haqida ma'lumot qo'shasizmi? (yes/no): ")    
    if answers=='no':
        break

print("\nBizdagi ma'lumotlar: ")
for user in userss:
    if user['earnings']:
        earnings = user['earnings']
    else:
        earnings = "Unknown"
    print(f"{user['name'].title()} {user['l_name'].title()},\
 Birth of date: {date_of_birth}. Job: {job}. Maosh: {earnings}")
















