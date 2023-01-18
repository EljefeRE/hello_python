# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

text = "Привет абв, как абвый ааафф! ывабвйй"
text = text.split()

text_new = []

for i in range(len(text)):
    if "абв" not in text[i]:
        text_new.append(text[i])

print(' '.join(text_new))


# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале.
# Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
import random

print(
    'Добро пожаловать в игру с конфетами! На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.'
    '\nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.'
    'Все конфеты оппонента достаются сделавшему последний ход.'
)
print()
player1 = input('Игрок 1 введите ваше имя: ')
player2 = input('Игрок 2 введите ваше имя: ')
print()
print(f'Жеребьевка: {player1} = Орел, {player2} = Решка')
print()
coin = random.randint(1, 2)
attempts = 0
orel = 0
reshka = 0

while attempts < 11:
    if coin == 1:
        orel += 1
        attempts += 1
        coin = random.randint(1, 2)
    elif coin == 2:
        reshka += 1
        attempts += 1
        coin = random.randint(1, 2)
    else:
        print('Монетка упала ребром. Неужели такое бывает? Хорошо, перебрасываем.')
        attempts += 1
        coin = random.randint(1, 2)

print('Орёл выпал', orel, 'раз(-а), а решка', reshka, 'раз(-а).')

kon = 221
total_p1 = 0
total_p2 = 0

if orel > reshka:
    f_step = player1
    s_step = player2
    print(f'Игрок {player1} ходит первый. Игрок {player2} ходит второй.')
    print()
else:
    f_step = player2
    s_step = player1
    print(f'Игрок {player2} ходит первый. Игрок {player1} ходит второй.')
    print()

while kon > 0:
    total_p1 += int(input(f'{f_step} возьмите конфеты от 1 до 28: '))
    kon -= total_p1
    print(f'{f_step} взял {total_p1} конфет, осталось {kon}')
    total_p1 = 0
    if kon <= 0:
        print()
        print(f'Поздравляю, {f_step}! Ты победил!')
        break
    total_p2 += int(input(f'{s_step} возьмите конфеты от 1 до 28: '))
    kon -= total_p2
    print(f'{s_step} взял {total_p2} конфет, осталось {kon}')
    total_p2 = 0
    if kon <= 0:
        print()
        print(f'Поздравляю, {s_step}! Ты победил!')
        break

# Задача: 39(2). Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, 
# необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, 
# каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, 
# на которую мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

import random

maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]

victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
             [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def check_victories():
    for i in victories:
        if maps[i[0]] == maps[i[1]] == maps[i[2]]:
            return True
        else:
            return False


def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


print_maps()
name1 = input("Введите имя первого игрока - ")
name2 = input("Введите имя второго игрока - ")

first_turn = random.choice([name1, name2])

print(first_turn)
game_over = False

cur_turn = first_turn

while not game_over:
    if cur_turn == first_turn:
        symbol = "X"
        step = int(input("введи клетку от 1 до 9, куда хочешь походить"))
        if maps[int(step) - 1] == "X" or maps[int(step) - 1] == "0":
            print("Occupied!!! Try Again")
            continue
        maps[step-1] = symbol
    else:
        symbol = "0"
        step = int(input("введи клетку от 1 до 9, куда хочешь походить"))
        if maps[int(step) - 1] == "X" or maps[int(step) - 1] == "0":
            print("Occupied!!! Try Again")
            continue
        maps[step - 1] = symbol
    print_maps()
    if check_victories():
        print(f"победил игрок {cur_turn}")
        game_over = True
    cur_turn = name2 if cur_turn == name1 else name1

# Обязательная:
# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def encode(text):
    result = ''
    prev_char = text[0]
    count = 0
    for char in text:
        if char != prev_char:
            result += f'{count}{prev_char}'
            prev_char = char
            count = 1
        else:
            count += 1
    result += f'{count}{prev_char}'
    return result


def decode(text):
    result = ''
    count = ''
    digit = True
    for char in text:
        if digit:
            count = int(char)
            digit = False
        else:
            result += int(count)*char
            digit = True
    return result


text = 'AAAAAAFDDCCCCCCCA'
print(f'Исходный текст: {text}')
encode_text = encode(text)
print(f'Результат сжатия данных: {encode(text)}')
print(f'Результат восстановления данных: {decode(encode_text)}')
