#ismlar = []

#print("Hamkasblaringizni ismini kiritamiz")
#h=1 #ismlarni sanash uchun o'zgaruvchi
#while True:
    #savol = f"{h}-hamkasbingiz ismini kiriting:"
    #ism = input(savol)
    #ismlar.append(ism)
    #javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    #if javob == 'ha':
        #h+=1
        #continue
   # else:
       # break
#print("Hamkasblaringiz ro'yxati:")
#for ism in ismlar:
    #print(ism.title())
#print("Hamkasblaringiz yoshini saqlaymiz")
#hamkasblar = {}
#ishora = True
#while ishora:
    #ism = input("Hamkasblaringiz ismini kiriting: ")
    #yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    #hamkasblar[ism] = int(yosh)
    #javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q) ")
    #if javob == "yo'q":
        #ishora = False
#for ism, yosh in hamkasblar.items():
    #print(f"{ism.title()} {yosh} yoshda")
#clubs = ['ajax','psv','barcelona','chelsea','psv','psg',
         #'rb zalsburg','psv']
#while 'psv' in clubs:
    #clubs.remove('psv')
#print(clubs)
#shirinliklar = ['napoleon','pahlava','kruasan','keks','tort']
#narxlangan_shirinliklar = {}
#while shirinliklar:
    #shirinlik = shirinliklar.pop()
    #narx = input(f"{shirinlik.title()}ning narxini kiriting: ")
    #print(f"{shirinlik.title()} narxlandi")
    #narxlangan_shirinliklar[shirinlik] = narx
#def salom_ber():
    #"""Salom beruvchi funksiya"""
    #print("Assalomu alaykum!")
    
#salom_ber()
#def salom_ber(ism):
    #"""Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    #print(f"Assalomu alaykum, hurmatli {ism.title()}!")
    
#salom_ber('hasan')
#salom_ber('olim')
#def toliq_ism(ism, familiya):
    #"""Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    #print(f"Foydalanuvchi ismi: {ism.title()}\n"
          #f"Foydalanuvchi familiyasi: {familiya.title()}")
#toliq_ism(familiya='hakimov',ism='olim')    
#toliq_ism('olim','hakimov')    
#def yosh_hisobla(ism, tugilgan_yil):
    #"""Foydalanuvchi yoshini hisoblaydigan dastur"""
    #print(f"{ism.title()} {2020-tugilgan_yil} yoshda")
    
#yosh_hisobla('olim', 1997)
#yosh_hisobla(tugilgan_yil=1997, ism='olim')

#def yosh_hisobla(tugilgan_yil, joriy_yil=2021): # joriy yil uchun st.qiymat 2020
    #"""Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    #print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

#yosh_hisobla(1995,2021)
#yosh_hisobla(1993)
#def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
    #"""Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    #print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
#tyil = int(input("Tug'ilgan yilingizni kiriting: "))
#yosh_hisobla(tyil)

#def yosh_hisobla(tugilgan_yil, joriy_yil=2021):
    #"""Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    #print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

#yosh_hisobla(1993)
#def salom_ber(ism):
    #"""Salom beruvchi funksiya"""
    #print(f"Assalomu alaykum! {ism.title()}")

#salom_ber('hasan')
#def toliq_ism(ism, familiya):
    #"""Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
   # print(f"Foydalanuvchi ismi: {ism.title()}\n"
          #f"Foydalanuvchi familiyasi: {familiya.title()}")
 
#toliq_ism('olim','hakimov')
#toliq_ism(familiya='hakimov',ism='Olim')
#def tyil_hisobla(ism, yosh):
    #"""Foydalanuvchi tug'ilgan yilini hisoblaydigan dastur"""
    #print(f"{ism.title()} {2021-yosh}-yilda tug'ilgan")
#tyil_hisobla('muhammad',22)
#def kv_kb(son):
    #"""Sonning kvadrati VA kubini hisoblaydigan dastur"""
    #print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")
#kv_kb(18)
#def juftmi(son):
    #"""Sonning juft yoki toqligini chiqaruvchi dastur"""
    #if son % 2:
        #print(f"{son} toq son")
    #else:
        #print(f"{son} juft son")
        
#juftmi(64)
#juftmi(25)

#def solishtiruv(x, y):
    #"""Sonlarni solishtiruvchi dastur"""
    #if x>y:
        #print(f"{x}>{y}")
    #elif x<y:
        #print(f"{x}<{y}")
    #else:
        #print(f"{x}={y}")
        
#solishtiruv(23,27)
#solishtiruv(33,33)
#solishtiruv(25**3,25**2)
#def daraja(x, y=2):
    #print(f"{x} ning {y}-darajasi {x**y} ga teng")
    
#daraja(7,3)
#daraja(5,5)
#daraja(15,25)
#daraja(50)

def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son % n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
        
bolinish_alomatlari(70)

