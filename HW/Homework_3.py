# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import *

n = int(input('Введите длинну списка: '))
list = []
for i in range(n):
    list.append(randint(1,10))
print(list)

sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum += list[i]

print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import *

n = int(input('Введите длинну списка: '))
list = []
for i in range(n):
    list.append(randint(1, 5))
print(list)

product = []

if len(list) % 2 == 0:
    for i in range(len(list) // 2):
        if i == 0:
            product.append(list[i] * list[-1])
        else:
            product.append(list[i] * list[- i - 1])
else:
    for i in range((len(list) + 1) // 2):
        if i == 0:
            product.append(list[i] * list[-1])
        elif i > len(list) // 2:
            product.append(list[i] * list[i])
        else:
            product.append(list[i] * list[- i - 1])

print(product)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import *

# n = int(input('Введите длинну списка: '))
# list = []
# for i in range(n):
#     list.append(randint(10, 50) / 10)
# print(list)
list = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []
for i in range(len(list)):
    ld = list[i] - int(list[i])
    list2.append(ld)
print(max(list2) - min(list2))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число: '))

binum = ''
while num > 0:
    binum = str(num % 2) + binum
    num //= 2
print(binum)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    fib_list = [0,1]
    for i in range(n-1):
        fib_list.append(fib_list[-2]+fib_list[-1])
    return fib_list

def neg_fib(n):
    nfib_list = [0,1]
    for i in range(n-1):
        nfib_list.append(nfib_list[-2]-nfib_list[-1])
    return nfib_list

num = int(input('Введите число: '))

print(neg_fib(num)[::-1] + fib(num)[1:])
