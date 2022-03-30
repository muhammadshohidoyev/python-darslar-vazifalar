# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:52:50 2022

@author: User
"""

import requests
import googletrans

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()["slip"]["advice"]
print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest="uz")
print(tarjima.text)