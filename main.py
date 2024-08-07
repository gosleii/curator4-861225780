import telebot

bot = telebot.TeleBot("7393160799:AAGxIdjtnlHboZJgzhQR82obmxKOJFozeQc")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     text= 'Привет! Добро пожаловать в наше котокафе "Мур"! Выбери чем ты хочешь заняться?', parse_mode = 'Markdown')

    @bot.message_handler(commands=["pet_cat"])
    def main(message):
        bot.send_message(message.chat.id, text= "Котику очень нравится когда его гладят ❤️", parse_mode = 'Markdown')

@bot.message_handler(commands=["feed_cat"])
def main(message):
        bot.send_message(message.chat.id,
                         text= "Теперь ты бог котиков! Вкусняшки самое лучшее для котиков 😺", parse_mode = 'Markdown')

@bot.message_handler(commands=["play_cat"])
def main(message):
        bot.send_message(message.chat.id, text= " *Играть!!*\n"  
        "Это что - мышка? Надо срочно [поймать] (https://pin.it/1AFqM0IP4)!", parse_mode = 'Markdown')

@bot.message_handler(commands=["tea_with_cookies"])
def main(message):
        bot.send_message(message.chat.id, text= "Как же в котокафе и без чая с печеньками? 🍪", parse_mode = 'Markdown')

        bot.infinity_polling()