
"""
Created on Fri Oct  1 15:23:36 2021

@author: User
"""

#car_0 = {'model':'ferrari','rang':'qizil'}
#print(car_0['model'])
#print(car_0['rang'])
#talaba_0 = {'ism':'murod olimov','yosh':21,'t_yil':2000}
#print(f"{talaba_0['ism'].title()},\
 #{talaba_0['t_yil']}-yilda tu'gilgan,\
# {talaba_0['yosh']} yoshda")
#talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
#talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika'
#talaba_1 = {}
##talaba_1['ism'] = 'qobil rasulov'
#talaba_1['kurs'] = 3
#talaba_1['yosh'] = 21
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#talaba_1['kurs'] = 4 # 'kurs' ni 4 ga o'zgartiramiz.
##print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#talaba_0 = {'ism':'murod olimov','yosh':21,'t_yil':2000}
#print(talaba_0)
#del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
#print(talaba_0)
#telefonlar = {
  #  'ali':'iphone x',
  #  'vali':'galaxy s9',
  #  'olim':'mi 10 pro',
  #  'orif':'nokia 3310'
  #$  }
#phone = telefonlar['ali']
#print(f"Alining telefoni {phone}")
#phone = telefonlar['hasan']
#print(f"Hasanning telefoni {phone}")
#phone = telefonlar.get('hasan', 'Bunday ism mavjud emas')
#print(phone)
#phone = telefonlar.get('hasan')
#print(phone)
#ukam = {'ismi':'nodir','tyil':2000,'shahar':'toshkent'}
#tyil = ukam['tyil']
#shah = ukam['shahar']
#print(f"Ukamning ismi {ukam['ismi'].title()}, {tyil}-yilda, {shah.title()} shahrida tug'ilgan")
#taomlar = {
   # 'nodir':'osh',
   # 'ziyoda':'kabob',
   # 'vasila':'dolma',
   # 'iroda':'spagetti',
  #  'muhammad':'lavash'
    #}
#taom = taomlar['nodir']
#print(f"Nodirning sevimli taomi {taom}")
#taom = taomlar['ziyoda']
#taom = taomlar['iroda']
#print(f"Irodaning sevimli taomi {taom}")
python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas Ro'yxat",
    'print':"Konsolga chiqaruvchi",
    'input':"Foydalanuvchi bilan muloqot",
    'for':"Takrorlanish operatori",
    'if':"Agar",
    'else':"Yoki"
    }
#kalit = input("Kalit so'zni kiriting:").lower()
#print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))

kalit = input("Kalit so'zni kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
   print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
         
   








