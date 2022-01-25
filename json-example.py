# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:18:36 2021

@author: User
"""

import json
import googlemaps 
from apikey import APIKEY

#GoogleMaps
gmaps = googlemaps.Client(key=APIKEY)

data = gmaps.geocode('Olmazor, Tashkent, Uzbekistan')
# print(geocode_result)

g = json.dump(data[0], indent = 4, sort_keys=True)
print(g)
