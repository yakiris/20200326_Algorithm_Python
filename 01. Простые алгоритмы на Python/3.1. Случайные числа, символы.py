# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

print('Введите диапазон чисел в порядке возрастания')
x1 = int(input('1-е число: '))
x2 = int(input('2-е число: '))

print('Введите диапазон буквенных символов в порядке возрастания')
y1 = input('1-я буква: ')
y2 = input('2-я буква: ')

import random

n = random.randint(x1, x2)
m = random.uniform(x1, x2)
l = random.randint(ord(y1), ord(y2))

print(f'Случайное целое число в диапазоне от {x1} до {x2} = {n}')
print(f'Случайное вещестенное число в диапазоне от {x1} до {x2} = {m}')
print(f'Случайная буква в диапазоне от {y1} до {y2} = {chr(l)}')