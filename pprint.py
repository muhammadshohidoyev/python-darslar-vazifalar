# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 20:22:09 2022

@author: User
"""

from pprint import pprint
# import json

# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)

#print(bemor)
#pprint(bemor)

import requests 
r = requests.get('https://api.github.com')
pprint(r.json())