# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 18:12:09 2021

Кирилл-Lotin Trlrgram bot
@author: User
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN ='2129265229:AAEkf0zpomPdp5_aLYeZ3wSaxubOguyZalA'
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
#print(to_latin('дастур'))
# matn = input("Matn kiriting:")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else: 
#     print(to_latin(matn))

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, Xush kelibsiz!")


bot.polling()
