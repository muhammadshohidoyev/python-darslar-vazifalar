# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 18:12:09 2021

Кирилл-Lotin Trlrgram bot
@author: User
"""

# from transliterate import to_cyrillic, to_latin
# import telebot


# TOKEN ='2129265229:AAEkf0zpomPdp5_aLYeZ3wSaxubOguyZalA'
# bot = telebot.Telebot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
# #print(to_latin('дастур'))
# # matn = input("Matn kiriting:")
# # if matn.isascii():
# #     print(to_cyrillic(matn))
# # else: 
# #     print(to_latin(matn))

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.reply_to(message, "Assalomu alaykum, Xush kelibsiz!")


# bot.polling()
import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "2129265229:AAEkf0zpomPdp5_aLYeZ3wSaxubOguyZalA"  # <-- Tokeningizni shu yerga yozing
bot = telebot.TeleBot(token=TOKEN)

# \start komandasi uchun mas'ul funksiya
@bot.message_handler(commands=["start"])
def send_welcome(message):
    username = (
        message.from_user.username
    )  # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f"Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring."
    bot.reply_to(message, xabar)


# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()