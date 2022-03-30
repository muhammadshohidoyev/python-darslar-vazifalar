# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:11:48 2022

@author: User
"""

import requests
from bs4 import BeautifulSoup


sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
# pprint(r.text)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
news = soup.find_all(class_="news-title")
print(news[0].text)