# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:07:14 2021

@author: User
"""

#from funksiyalar import play
#from uzwords import words

#play()
import random as r

taxminlar = 13
harflar = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЪЬЭЮЯҚҒҲ')

def soz_shakli(taxminiy_harflar, words):
    pass

def display_info(taxminiy_harflar, words):
    pass

def taxmin_tekshirish(taxmin, word, taxminiy_harflar):
    pass

def b_m_sh(harflar, words):
    pass


def play_game():
    words = ['абадийлашмоқ', 'микроскоп', 'мушук']
    sirli_soz = r.choice(words)
    soz_uzunligi = len(sirli_soz)
    taxminlangan = []
    print(f"Сиз танлаган сўз {soz_uzunligi}")
    while taxminlar > 0:
        taxmin = input("Сўз киритинг: ")
        taxmin = taxmin.upper()
        taxmin_tekshirish(taxmin, sirli_soz, taxminlangan)
        if b_m_sh(taxminlangan, sirli_soz):
            return print('Сиз ютдингиз!')
        print('Тахминингиз нотўғри чиқди.\nЮтқиздингиз')

def taxmin_tekshirish(taxmin, words, taxminiy_harflar):
    global taxminlar 
    if taxmin in harflar and len(taxmin) == 1 and taxmin not in taxminiy_harflar:
        taxminiy_harflar.append(taxmin)
        if taxmin in words:
            print("Тўғри тахмин!")
        else:
            print('Тахмин хато!')
            taxminlar -= 1
    else:
        if len(taxmin) != 1:
            print("Сиз яна ҳарф киритишингиз керак!")
        elif taxmin.upper() not in harflar:
            print('Сизнинг тахминингиз ҳарф бўлиши керак!')
        elif taxmin in taxminiy_harflar:
            print('Аллақан бу ҳарфни киритгансиз!')
    display_info(taxminiy_harflar, words)
            
def b_m_sh(harflar, words):
    for harf in words:
        if harf not in harflar: 
            return False
    return True
            
def display_info(taxminiy_harflar, words):
    bosh_harflar = ' '.join([
        harf for harf in harflar if harf not in taxminiy_harflar
        ])  
    print(soz_shakli(taxminiy_harflar, words))
    print(f"Таҳмин қолди: {taxminlar}.")
    print(f"Бош ҳарфлар: {bosh_harflar}.")
    
def soz_shakli(taxminiy_harflar, words):
    toldi_matn = ''
    for harf in words:
        if harf in taxminiy_harflar:
            toldi_matn += harf
        else: 
            toldi_matn += '-' 
    return toldi_matn
            
if __name__ == '__main_':
    play_game()
            
            
            
            
            
            
            
            
            
            
            
            
            
            