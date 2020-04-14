# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import sys
from collections import ChainMap
from collections import deque

dic1 = {}
dic2 = {}
dic3 = {}
for k, v in enumerate([str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']):
    dic1[k] = v
    dic2[v] = k
    dic3[str(k)] = v
dct = ChainMap(dic1, dic2, dic3)

fir = input('Первое число в 16-ричной системе: ')
sec = input('Второе число в 16-ричной системе: ')

# проверка корректности введенного числа
z = 0
for i in fir.upper():
    if i not in dct:
        z += 1
for j in sec.upper():
    if j not in dct:
        z += 2
if z != 0:
    if z == 1:
        print('Первое число введено не корректно.')
    elif z == 2:
        print('Второе число введено не корректно.')
    elif z == 3:
        print('Оба числа введены не корректно.')
    sys.exit()

first = list(fir.upper())[:: -1]
second = list(sec.upper())[:: -1]

# определение очередности для функции сложения
if len(second) > len(first):
    first, second = second, first

# функция возврата значения второго числа
def num_second(n):
    if n + 1 <= len(second):
        return dct[str(second[n])]
    else:
        return '0'

# функция сложения
def get_summ(first):
    summ = []
    k = 0
    for i in range(len(first)):
        num = num_second(i)
        res = int(dct[str(first[i])]) + int(num)
        summ.append(str((res + k) % 16))
        if res + k > 15:
            k = 1
        else:
            k = 0
    if k:
        summ.append(str(k))
    result = []
    for i in summ[:: -1]:
        result.append(str(dct[i]))
    return ''.join(result)

print(f'Сумма введенных чисел = {get_summ(first)}')

first_m = list(fir.upper())
second_m = list(sec.upper())

# функция умножения
def get_mult(first, second):
    result = deque()
    spam = deque([deque() for _ in range(len(second))])
    first, second = first.copy(), deque(second)
    for i in range(len(second)):
        m = int(dct[second.pop()])
        for j in range(len(first) - 1, -1, -1):
            spam[i].appendleft(m * int(dct[first[j]]))
        for _ in range(i):
            spam[i].append(0)
    k = 0
    for _ in range(len(spam[-1])):
        res = k
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()
        if res < 16:
            result.appendleft(dct[res])
        else:
            result.appendleft(dct[res % 16])
            k = res // 16
    if k:
        result.appendleft(dct[k])
    return ''.join(result)

print(f'Произведение введенных чисел = {get_mult(first_m, second_m)}')