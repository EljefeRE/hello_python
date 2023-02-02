import telebot 
from telebot import types
import random

bot = telebot.TeleBot('5930058117:AAEg7J5j9V5m7G08nlfARSWrbcG99elvv3E')

sweets = 50
max_sweet = 15
user_turn = 0
bot_turn = 0
flag = ''


@bot.message_handler(commands = ['start'])
def play(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Правила игры')
    but2 = types.KeyboardButton('Играть')
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, 'Выбери нижe', reply_markup = markup)

@bot.message_handler(content_types = 'text')
def menu(message):
    global flag
    if message.text == 'Играть':
        bot.send_message(message.chat.id, "Приветствую Вас в игре!")
        bot.send_message(message.chat.id, f"Всего {sweets} конфет в игре!")
        flag = random.choice(['user', 'bot'])
        if flag == 'user':
            bot.send_message(message.chat.id, "Первым ходите Вы")
            controller(message)
        else:
            bot.send_message(message.chat.id, "Первым ходит бот")
            controller(message)
     
    elif message.text == 'Правила игры':
        bot.send_message(message.chat.id, f'На столе лежат 50 конфет, вам по очереди с ботом надо брать конфеты со стола от 1 '
                                           'до 15. Первый ход определяется рандомно. Побеждает тот, чей ход будет последним')
        play(message)

def controller(message):
    global flag, sweets
    if sweets > 0:
        if flag == 'user':
            bot.send_message(message.chat.id, f'Введите количество конфет от 1 до {max_sweet}')
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)
    else:
        flag = 'user' if flag == 'bot' else 'bot'
        bot.send_message(message.chat.id, f'Победил {flag}!')
        sweets = 50

def bot_input(message):
    global sweets, bot_turn , flag
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        sweets % max_sweet - 1 == 0
        if bot_turn == 0:
            bot_turn = 1

    sweets -= bot_turn
    bot.send_message(message.chat.id, f'Бот взял {bot_turn} конфет')
    bot.send_message(message.chat.id, f'Осталось {sweets} конфет')
    flag = 'user' if flag == 'bot' else 'bot'
    controller(message)

def user_input(message):
    global sweets, user_turn, flag
    user_turn = int(message.text)
    sweets -= user_turn
    bot.send_message(message.chat.id, f'Осталось {sweets} конфет')
    flag = 'user' if flag == 'bot' else 'bot'
    controller(message)
    

bot.infinity_polling()
