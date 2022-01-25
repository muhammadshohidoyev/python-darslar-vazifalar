# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:33:13 2021

@author: User
"""

#talaba_0 = {
 #   'ism':'alijon',
 ##   'familiya':'shamshiyev',
 #   'yosh':22,
  #  'fakultet':'matematika',
  #  'kurs':4
#    }

#print(talaba_0.items())
#for kalit, qiymat in talaba_0.items():
 #   print(f"Kalit: {kalit}")
 #   print(f"Qiymat: {qiymat} \n")
#telefonlar = {
    #'ali':'iphone x',
   # 'vali':'galaxy s9',
   # 'olim':'mi 10 pro',
   # 'orif':'nokia 3310'
  #  }

#for k, q in telefonlar.items():
  #  print(f"{k.title()}ning telefoni {q}")
#mahsulotlar = { # Do'kondagi mahsulotlar
#    'olma':10000,
#    'anor':20000,
   # 'uzum':40000,
  #  'anjir':25000,
  #  'shaftoli':30000
 #   }

#print(mahsulotlar.keys())
#print('Do\'kondagi mahsulotlar:')
#for mahsulot in mahsulotlar.keys():
    #print(mahsulot.title())
    
#bozorlik = ['anor','uzum','non','baliq']
#for mahsulot in mahsulotlar:
  #  if mahsulot in bozorlik:
  #      print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
#for buyum in bozorlik:
  #  if buyum not in mahsulotlar:
      #  print(f"Iltimos, do'koningizga {buyum} ham olib keling")        
        
#print("Do'konimizdagi mahsulotlar:")    
#for mahsulot in sorted(mahsulotlar):
  ##  print(mahsulot.title())        
#print(telefonlar.values())
#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
   # print(tel)
#9telefonlar = {
  #  'ali':'iphone x',
    #'vali':'galaxy s9',
  #  'olim':'mi 10 pro',
  #  'orif':'nokia 3310',
  #  'hamida':'galaxy s9',
  #  'maryam':'huawei p30',
 #   'tohir':'iphone x',
 #   'umar':'iphone x'    
 #   }

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
  #  print(tel)
    
#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in set(telefonlar.values()):
   # print(tel)    
#toys = {"ball", "car", "lamp", "ball"} 
#python_izohli_lugati = {
   # 'boolean':"Mantiqiy son",
   # 'float':"O'nlik son",
   # 'for':"Biror amalni qayta-qayta bajarish tsikli",
    #'if':"Shartlarni tekshirish operatori",
    #'integer':"Butun son"
   # } 

#for key, value in sorted(python_izohli_lugati.items()):
 #   print(f"{key.title()} - {value}")
    
#davlatlar = {
  #  'aqsh':"vashington",
   # 'o\'zbekiston':"toshkent",
  #  'qirg\'iziston':"bishkek",
  #  'rossiya':"moskva",
    #'tojikiston':"dushanbe",
   # 'qozog\'iston':"nursulton",
   # 'italiya':"rim",
  #  'malayziya':"Kuala-Lumpur",
   # 'ispaniya':"madrid"
  #  }
    
#print("Dunyo davlatlari:")
#for davlat in sorted(davlatlar):
 #   print(davlat.upper())

#print('\nDavlatlarning poytaxtlari')    
#for poytaxt in sorted(davlatlar.values()):
   # print(poytaxt.title())
#country = input("Qaysi davlatlar poytaxtlarini bilishni istaysiz?").lower()
#capital = davlatlar.get(country)
#if capital==None:
   # print('Kechirasiz, bizda bunday ma\'lumot mavjud emas')
#else:
   # print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
#world_clubs = {
#    'real madrid':"madrid",
   # 'barcelona':"catalonia",
   ## 'borussia dortmund':"dortmund",
   # 'ajax':"amsterdam",
   # 'manchester united':"manchester",
   # 'zenit':"sant-petersburg",
   # 'galatasaray':"stanbul",
   # 'psg':"paris",
   # 'pakhtakor':"tashkent"
  # }

#print("World clubs:")
#for club in sorted(world_clubs):
   # print(club.upper())
    
#print("\nCities of world clubs")
#for city in sorted(world_clubs.values()):
   # print(city.title())

#teams = input('which team do you want to know?').lower()
#group = world_clubs.get(teams)
#if group==None:
   # print("Sorry, we do not have such information")
#else:
    #print(f"this club {teams.upper()} is {group.title()}s club")
#menu = {
       # 'osh':20000,
       # 'norin':25000,
       # 'xonim':15000,
     #   'kabob':10000,
      #  'somsa':5000,
      # 'sho\'rva':18000,
       # 'manti':6000,
       # 'pizza':19000,
      #  'mastava':13000,
      #  'non':4000
      #  }
#print("3 ta taom buyurtma bering.")
#buyurtmalar = []
#for n in range(3):
   # buyurtmalar.append(input(f"{n+1}-taom:").lower())

#for buyurtma in buyurtmalar:
  #  if buyurtma in menu:
       # print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
   # else:
      #  print(f"Kechirasiz, bizda {buyurtma} yo'q")
shokoladlar = {
    'snickers':6000,
    'milkway':5000,
    'alpengold':7000,
    'roshen':10000,
    'millenium':15000,
    'bounty':8000,
    'kitkat':7.500,
    'amilov':4.500,
    'nesquick':5.500,
    'twiks':9000
    }
print('5 ta shokoladga buyurtma bering.')
sweets = []
for m in range(5):
    sweets.append(input(f"{m+1}-shokolad:").lower())

for sweet in sweets:
    if sweet in shokoladlar:
        print(f"{sweet.title()} {shokoladlar[sweet]} so'm")
    else:
        print(f"Bu {sweet} mavjud emas")






