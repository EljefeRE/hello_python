# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# • 6782 -> 23
# • 0.56 -> 11

num = float(input('Введите число: '))
sum = 0
for i in str(num):
    if i != ".":
        sum += int(i)
print(f"Сумма цифр = {sum}")

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# • пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Введите число: '))
list = []
fact = 1
for i in range(1, num+1):
    fact *= i
    list.append(fact)
print(list)

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# • Для n=4 [1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

num = int(input('Введите число: '))
total = 0
for i in range(1, num + 1):
    total += (1 + 1 / i) ** i    
print(total)

# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

with open('file.txt', 'w') as data:
    data.write('0 \n')
    data.write('3 \n')
    data.write('5 \n')

n = int(input('Введите число: '))
list = []
product = 1
for i in range(-n, n):
    list.append(i)
print(list)

path = 'file.txt'
data = open(path, 'r')
for line in data:
    line = int(line)
    product *= list[line]
print(product)


# 5.Реализуйте алгоритм перемешивания списка.

import random
def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)