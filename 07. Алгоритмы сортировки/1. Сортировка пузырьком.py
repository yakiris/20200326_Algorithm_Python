# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

def bubble_sort(array, reverse=False):
    sing = int(reverse) * 2 - 1
    n = 1
    while n < len(array):
        # для улучшения алгоритма добавляем проверку на перестановку
        m = True
        for i in range(len(array) - n):
            if array[i] * sing > array[i + 1] * sing:
                array[i], array[i + 1] = array[i + 1], array[i]
                m = False
        if m:
            break
        n += 1

size = 32
limit = 100
array = [random.randrange(-limit, limit) for i in range(size)]
print(f'Не ранжированный массив: {array}')
bubble_sort(array, reverse=True)
print(f'Ранжированный массив: {array}')