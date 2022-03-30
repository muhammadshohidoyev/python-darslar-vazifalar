# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:39:42 2022

@author: User
"""
import requests
from pprint import pprint

# manzil= "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)
country = "Uzbekistan"
url = f"https://restcountries.com/v2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
print(r_json['capital'])