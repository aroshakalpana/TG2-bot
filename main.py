import os
import telebot

bot= telebot.TeleBot("API Key Here")

@bot.massag_handler(commands=["satrt"])
def send_welcome(massage):
    bot.reply_to(massage,"Heloo i'm arosha kalpana")


@bot.massage_handler(commands=["How"])
def send_massage(massage):
    bot.send_massage(massage, "https://t.me/slfreefire23")

bot.pooling()



