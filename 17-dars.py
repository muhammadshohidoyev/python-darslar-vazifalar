# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:31:42 2021

@author: User
"""

#ism = input("Ismingiz nima? ")
#print(f'Salom, {ism.title()}')
#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
#yosh = input(savol)

#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
#yosh = input(savol)
#yosh = int(yosh) # yosh ni butun songa o'tkazamiz
#height = input("Bo'yingiz necha metr? ")
#height = float(height) # bo'yni o'nlik songa o'tkazamiz

#son = 1 # son ga 1 qiymatini beramiz
#while son<=5: # toki son 5 dan kichik yoki teng ekan...
    #print(son, end=' ') # son ni konsolga chiqaramiz,
    #son = son+1 # songa 1 qo'shamiz.
    
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#qiymat = ''
#while qiymat != 'exit':
   # qiymat = input(savol)
    #if qiymat != 'exit':
        #print(float(qiymat)**2
        
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#ishora = True
#while ishora:
   # qiymat = input(savol)
   # if qiymat == 'exit':
        #ishora = False
    #else:
        #print(float(qiymat)**2)

#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True: # abadiy tsikl
   # qiymat = input(savol)
   # if qiymat == 'exit':
        #break # tsiklni to'xtatish
   # else:
        #print(float(qiymat)**2)        
        
#sonlar = list(range(1,11))
#for son in sonlar: 
    #if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
       # break
    #print(f"{son} ning kvadrati {son**2} ga teng")        
        
#sonlar = list(range(1,11))
#for son in sonlar:
   # if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
       # continue
   # print(f"{son} ning kvadrati {son**2} ga teng")        
        
#son = 0
#while son<10:
    #son += 1
    #if son%2==0:
        #continue
    #else:
        #print(son)        
# infinite loop
#savol = "Yaxshi ko'rgan kitoblaringiz"
#savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "
#while True:
    #kitob = input(savol)
    #if kitob == 'exit':
        #break
        #print("Rahmat")
#savol = "Yoshingizni kiriting: "    
    
#while True:
    #qiymat = input(savol)
    #if qiymat == 'exit' or qiymat == 'quit':
        #break
    #yosh = int(qiymat)
    
    #if yosh<7:
        #narh = 2000
    #elif 7<=yosh<18:
        #narh = 3000    
   # elif 18<=yosh<65:
        #narh = 10000
    #else: narh = 0
        
    #if narh==0:
        #print("Sizga chipta bepul")
    #else:
       # print(f"Chipta {narh} so'm")
    
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    elif float(qiymat)<0:
        continue
    
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")    









