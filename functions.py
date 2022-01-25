# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:16:19 2021

@author: User
"""

import random
from countries_list import l_of_countries

def get_country():
    country = random.choice(l_of_countries)
    while "-" in country or ' ' in country:
        country = random.choice(l_of_countries)
    return country.upper()

def display(user_letters_c, country):
    display_c_l =""
    for letter in country:
        if letter in user_letters_c.upper():
            display_c_l += letter
        else: 
            display_c_l += "-"
        return display_c_l
    
def play():
    country = get_country()
    #Country letters
    country_letters = set(country)
    #User inserted letters
    user_letters_c =' '
    print(f"I thought of a {len(country)} digit number.  Can you find it?")
    #print(country)
    while len(country_letters)>0:
        print(display(user_letters_c, country))
        if len(user_letters_c)>0:
            print(f"Enter your letters so far: {user_letters_c}")
            
        letter = input("Enter your letters: ").upper()
        if letter in user_letters_c:
            print("You entered this letter earlier. Enter another letter.")
            continue 
        elif letter in country:
            country_letters.remove(letter)
            print(f"{letter} is right.")
        else:
            print("This letter is not exist.")
        user_letters_c += letter
    print(f"Congratulations! You found the country name {country} in {len(user_letters_c)} attempts.")