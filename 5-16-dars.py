# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:44:51 2021

@author: User
"""

#ism = "Umar"
#print("Mening ismim " + ism)
#familiya = "Umarov"
#print(ism + familiya)
#print(ism + ' ' + familiya)
#ism_sharif = f"{ism} {familiya}"
#print(ism_sharif)
#name = "Homer"
#surname = "Simpson"
#print(f"My name is {surname}. {name} {surname}!")
#name2 = "Bart"
#surname2 = "Simpson"
#name2_surname2 = f"{name2} {surname2}"
#print(name2_surname2.title())
#fruit = " peach "
#print("I love " + fruit.lstrip() + " it is delicious")
#print("I like " + fruit.rstrip() + " it is delicious")
#print("I like " + fruit.strip() + " it is delicious")
#print("I like " + fruit + " it is delicious")
#name = input("What is your name?")
#print("Hello, " + name)
#name = input("What is your name?\n>>>")
#print("Hello, " + name.title())
#stadium = "Anfield"
#club = "Liverpool"
#nickname = "The Reds"
#head_coach = "Jurgen Klopp"
#captain = "Jordan Henderson"
#league = "Premier League"

#print(stadium + " stadium, " + club + " club, " + \
     # nickname + " nickname, " + head_coach + " headcoach, " + \
     # captain + " captain, " + league + " league ")
#print(" Please enter the following information:")
#stadium = input("Your stadium is:")
#club = input("Your club is:")
#nickname = input("Your nicknamer is:")
#head_coach = input("Your head coach is:")
#captain = input("Your captain is:")
#league = input("Your league is:")

#print(stadium + " stadium,\n " + club + " club,\n " + \
   #   nickname + " nickname,\n " + head_coach + " head coach,\n " + \
   #   captain + " captain,\n " + league + " league\n ")
    
#manzil = f"{stadium} stadium, \
#{club} club, {nickname} nickname, \
#{head_coach} head coach, {captain} captain, \
#{league}" 
#print(manzil)   

#print(manzil.upper())
#print(manzil.lower())
#print(manzil.title())    
#print(manzil.capitalize())    
#ism = 'Rustam' 
#yosh = 24
#xabar = ism + ' ' + str(yosh) + " yoshda"  
#print(xabar)
#tyil =  int(input("Tug'ilgan yilingizni kiriting: ")) 
#yosh = 2020 - tyil
#print("Siz " + str(yosh) + " yoshda ekansiz")   
#tyil = input("Tug'ilgan yilingizni kiriting:")#tlug'ilgan yilni kiritishni so'rayman    
#tyil = int(tyil)#tyil ni int ga aylantiraman
#yosh = 2021 - tyil#foydalanuvchi yoshini hisoblayman
#print("Siz " + str(yosh) + " yoshda ekansiz")   
#istalgan son kiritilishini so'rayman
#x = int(input("Istalgan son kiriting: "))
#print(x, "ning kvadrati", x**2, "ga teng")
#print(x, "ning kubi", x**3, "ga teng")
#yosh1 = int(input("Yoshingiz nechida?\n>>>"))
#tyil1 = 2021-yosh1
#print("Siz ", tyil1, " da tug'ilgansiz")
#a = float(input("Birinchi sonni kiriting: "))
#b = float(input("Ikkinchi sonni kiriting: "))
#print(f"{a}+{b}=", a+b)
#print(f"{a}-{b}=", a-b)
#print(f"{a}*{b}=", a*b)
#print(f"{a}/{b}=", a/b)

#clubs = ['barcelona', 'real madrid', 'chelsea', 'tottenham', 'juventus']
#my_clubs = clubs[2:]
#print(my_clubs) 
#print(clubs[2:4])
#print("First club:", clubs[0].title())
#print("Third club:", clubs[2].upper())
#print("Fourth club:", clubs[-1]. lower ())
#clubs.append("juventus")
#del clubs[3]
#print(clubs)

#prices = [12000, 5000, 200, 60000, 10000, 50, 7000]
#prices[2] = 15000
#prices[4] = 9000
#prices[5] = prices[5]+50000
#brands = []
#brands.append("nike")
#brands.append("puma")
#brands.append("adidas")
#brands.append("joma")
#0brands = ['nike', 'puma', 'adidas', 'kappa', 'joma', 'nike']
#brands.remove('nike')
#print(brands)
#brands.insert(3, "kappa")
#print(brands)
#colors = ["red", "yellow", "pink", "black", "white"]
#color = colors.pop(2)
#print("I have " + color + "color")
#print("The colors I don't have: ", colors)
#footballers = ['G.Buffon', 'L.Messi', 'C.Ronaldo', 'G.Bale', 'Neymar Jr.', 
               #'S.Ramos', 'J.Boateng', 'E.Holland']
#footballers.sort()
#footballers.sort(reverse=True)
#print(footballers)
#print("sorted() return list:", sorted(footballers))
#print("The original list remained unchange:", footballers)
#print(sorted(footballers, reverse=True))
#ages = [3, 7, 10, 50, 1, 8, 4, 2, 11, 0]
#ages.sort()
#print(ages)
#print(sorted(ages, reverse=True))
#characters = ['Homer','Bart','Lisa','Maggie','Marge']
#characters.reverse()
#print(characters)
#print("Elements number:", len(characters))
#numbers = list(range(0,10))
#print(numbers)
#even_numbers = list(range(0,20,2))
#odd_numbers = list(range(1,20,2))
#print("Even numbers: ", even_numbers)
#print("Odd numbers: ", odd_numbers)
#costs = [3000, 1000, 7000, 100, 4000, 10000, 2000, 500]
#cheap = min(costs)
#expensive = max(costs)
#overall = sum(costs)
#print("Cheapest value", cheap, ". Most expensive", expensive, ". Overall", overall)
#numbers_0 = [1, 2, 3, 4, 5, 6, 7]
#numbers_1 = numbers_0[:]
#numbers_1.append(8)
#numbers_1.append(9)
#print("Those numbers list:", numbers_0)
#print("Those numbers list:", numbers_1)
#directions = (20, 25, 50, 75.5)
#print(directions)
#flags = ('spain', 'germany', 'russia', 'albania', 'usa', 'poland', 'japan')
#print(flags[1])
#print(flags[-1])
#print(flags[2:5])
#flags = list(flags)
#flags.append("estonia")
#flags.remove('poland')
#flags[5] = 'italy'
#flags = tuple(flags)
#print(flags)
#friends = ['Alex','Joseph','James','David','Zach']
#for friend in friends:
    #print(friend)
    #print(f"Hurmatli {friend}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")   
   # print("Hurmat bilan, Palonchiyevlar oilasi")
#print(friends)

#friends_0 = []
#print("who are your five best friends?")
#for f in range(5):
 #   friends_0.append(input(f"{f+5}-enter your friend's name: "))
#print(friends_0)
#automobiles = ['bmw', 'toyota', 'tesla', 'audi', 'mazda', 'mitsubishi']
#for automobile in automobiles:
   # if automobile =='bmw':
        #print(automobile.upper())
    #else:
        #print(automobile.title())
#name1 = input("What is your name?\n>>>")
#if name1.lower() != 'alex':
   # print(f"Sorry, {name1.title()} we are waiting for Alex.")
#else:
    #print("Hello, Alex")
#answer = float(input("13×7 is equal to what?>>"))
#if answer !=91:
    #print("Answer is fault!")
#age = int(input("How old are you?>>>"))
#if age >=18:
    #print("Welcome!")
#else:
    #print("Can not be accessed!")
#login = input("Select new login: ")
#if len(login)<=5:
    #print("Login must be more than 5 letters!")

#year = int(input("Enter your year of birth: "))
#if 2021-year<18:
   # print(f"Your age {2021-year} years old.")
    #print("Can't be accessed!")
#else:
    #print ("Welcome!")

#yosh = int(input('Yoshingiz nechchida? '))
#if yosh<=4:
    #qiymat = 0
   # print("Sizga kirish bepul.")
#elif yosh<=12:
    #qiymat = 5000
    #print("Sizga kirish 5000 so'm")
#elif yosh<65:
    #qiymat = 10000
#elif yosh>=65:#else:
   # qiymat = 8000
    #qiymat = 10000
   # print("Sizga kirish 10000 so'm")
#print(f"Sizga kirish {qiymat} so'm")    
#day = input("What day is it today?>>>")
#temperature = float(input("What is the air temperature"))
#if day.lower()=="sunday" and temperature>=30:
    #print("Let's go for a swim!")
#elif day.lower()=="sunday" and temperature<30:
    #print("We rest at home!")
    #print("Today is a day off.") 
#else:
    #print("Today is bussines day")
#price = 17000
#tea = True
#salad = False
#bread = True
#juice = False
#assorted = True

#if tea:
   # print("The customer bought a tea.")
    ##price = price + 4000

#if salad:
    #print("The customer bought a salad.")
    #price = price + 7000
    
#if bread:
    #print("The customer bought a bread.")
   # price = price + 3000
    
#if juice:
    #print("The customer bought a juice.")
    #price = price + 2000

#if assorted:
    #print("The customer bought assorted")
    #price = price + 25000
#if tea and salad: 
   # price = price + 10000
#elif tea or salad:
    #price = price + 7000
    
#print(f"Total {price} sum")
#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#'manti' in menu # menu da manti bormi?
#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#'osh' not in menu
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() not in menu:
    #print('Buyurtma qabul qilindi.')
#else:
    #print('Afsuski bizda bunday ovqat yo\'q')

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti", "shashlik"]

#if buyurtmalar:
    #for taom in buyurtmalar:
        #if taom in menu:
            #print(f"Menuda {taom} bor")
        #else:
            #print(f"Kechirasiz, menuda {taom} yo'q")
#else:
    #print("Savatchangiz bo'sh")
#talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
#print(f"{talaba_0['ism'].title()},\
 #{talaba_0['t_yil']}-yilda tu'gilgan,\
 #{talaba_0['yosh']} yoshda")
#talaba_1 = {}
#talaba_1['ism'] = 'qobil rasulov'
#talaba_1['kurs'] = 3
#talaba_1['yosh'] = 20
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#talaba_1['kurs'] = 4 # 'kurs' ni 4 ga o'zgartiramiz.
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

#talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
#print(talaba_0)
#del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
#print(talaba_0)
#telefonlar = {
    #'ali':'iphone x',
    #'vali':'galaxy s9',
    #'olim':'mi 10 pro',
    #'orif':'nokia 3310'
    #}

#print(telefonlar.values())

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
    #print(tel)
#phone = telefonlar['ali']
#print(f"Alining telefoni {phone}")
#phone = telefonlar['hasan']
#print(f"Hasanning telefoni {phone}")
#phone = telefonlar.get('hasan','Bunday ism mavjud emas')
#print(phone)
#phone = telefonlar.get('hasan')
#print(phone)
#talaba_0 = {
    #'ism':'alijon',
   # 'familiya':'shamshiyev',
    #'yosh':22,
    #'fakultet':'matematika',
    #'kurs':4
    #}

#print(talaba_0.items())

#for kalit, qiymat in talaba_0.items():
   # print(f"Kalit: {kalit}")
   # print(f"Qiymat: {qiymat} \n")
#telefonlar = {
   # 'ali':'iphone x',
   # 'vali':'galaxy s9',
   # 'olim':'mi 10 pro',
   # 'orif':'nokia 3310'
   # }

#for k, q in telefonlar.items():
   # print(f"{k.title()}ning telefoni {q}")

#mahsulotlar = { # Do'kondagi mahsulotlar
    #'olma':10000,
   # 'anor':20000,
   # 'uzum':40000,
   # 'anjir':25000,
   # 'shaftoli':30000
    #}

#print(mahsulotlar.keys())

#print('Do\'kondagi mahsulotlar:')
#for mahsulot in mahsulotlar.keys():
   # print(mahsulot.title())
#bozorlik = ['anor','uzum','non','baliq']
#for mahsulot in mahsulotlar:
    #if mahsulot in bozorlik:
        #print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
#for buyum in bozorlik:
   # if buyum not in mahsulotlar:
        #print(f"Iltimos, do'koningizga {buyum} ham olib keling")

#print("Do'konimizdagi mahsulotlar:")    
#for mahsulot in sorted(mahsulotlar):
    #print(mahsulot.title())
#telefonlar = {
    #'ali':'iphone x',
    #'vali':'galaxy s9',
    #'olim':'mi 10 pro',
    #'orif':'nokia 3310',
    #'hamida':'galaxy s9',
    #'maryam':'huawei p30',
    #'tohir':'iphone x',
    #'umar':'iphone x'    
    #}
#
#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
    #print(tel)
#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in set(telefonlar.values()):
    #print(tel)

#car0 = {
        #'model':'lacetti',
        #'rang':'oq',
        #'yil':2018,
        #'narh':13000,
        #'km':50000,
        #'korobka':'avtomat'
        #}

#car1 = {
        #'model':'nexia 3',
        #'rang':'qora',
        #'yil':2015,
        #'narh':9000,
        #'km':89000,
        #'korobka':'mexanika'
        #}

#car2 = {
        #'model':'gentra',
        #'rang':'qizil',
        #'yil':2019,
        #'narh':15000,
        #'km':20000,
        #'korobka':'mexanika'
        #}

#car = car0
#print(f"{car['model'].title()},\
  #{car['rang']} rang,\
  #{car['yil']}-yil, {car['narh']}$")

#car = car1
#print(f"{car['model'].title()},\
  #{car['rang']} rang,\
  #{car['yil']}-yil, {car['narh']}$")

#car = car2
#print(f"{car['model'].title()},\
  #{car['rang']} rang,\
  #{car['yil']}-yil, {car['narh']}$")  
#cars = [car0, car1, car2]
#for car in cars:
    #print(f"{car['model'].title()}, "
          #f"{car['rang']} rang, "
          #f"{car['yil']}-yil, {car['narh']}$")
#malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
#for n in range(10):
    #new_car = { # har bir yangi mashina uchun lug'at yaratamiz
        #'model':'malibu',
        #'rang':None, # rangi noaniq
        #'yil':2020,
        #'narh':None, # narhi belgilanmagan
        #'km':0,
        #'korobka':'avto'
        #}
   # malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
    
#for malibu in malibus[:3]:
   # malibu['rang']='qizil'    
    
#for malibu in malibus[3:6]:
    #malibu['rang']='qora'    
    
#for malibu in malibus[6:]: # ohirgi 4 ta mashinani
    #malibu['rang']='qora'  # rangi qora
    #malibu['korobka']='mexanika' # korobkasi mexanika
    
#for malibu in malibus:
    #if malibu['korobka']=='avto':
       # malibu['narh']=40000
    #else:
       # malibu['narh']=35000    
    
    
#dasturchilar = {
    #'ali':['python','c++'],
    #'vali':['html','css','js'],
    #'hasan':['php','sql'],
    #'husan':['python','php'],
    #'maryam':['c++','c#']
    #}

#for ism, tillar in dasturchilar.items():
   # print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    #for til in tillar:
        #print(til.upper())    
    
#for ism, tillar in dasturchilar.items():
    #print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    #for til in tillar:
        #print(f'{til.upper()} ', end='')    

hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())




















    
    
    
    
    
    
    