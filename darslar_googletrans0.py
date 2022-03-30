# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:58:55 2022

@author: User
"""

from googletrans import Translator
tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
tarjima = tarjimon.translate(matn_uz)
# print(tarjima.origin)
# print(tarjima.text)
# print(tarjima.src)
tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
#print(tarjima_ru.text)

matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = tarjimon.translate(matn_en, dest='uz')
print(tarjima_uz.text)