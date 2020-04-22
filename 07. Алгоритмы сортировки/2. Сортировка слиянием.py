# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

def merge_sort(array):
    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    # разбиваем массив на две части
    left_list = merge_sort(array[:len(array) // 2])
    right_list = merge_sort(array[len(array) // 2:])
    i, j = 0, 0
    while len(left_list) > i and len(right_list) > j:
        if left_list[i] < right_list[j]:
            array[i + j] = left_list[i]
            i += 1
        else:
            array[i + j] = right_list[j]
            j += 1
    while len(left_list) > i:
        array[i + j] = left_list[i]
        i += 1
    while len(right_list) > j:
        array[i + j] = right_list[j]
        j += 1
    return array

size = 16
limit = 50
array = [round(random.uniform(0, limit), 3) for i in range(size)]
print(f'Не ранжированный массив: {array}')
merge_sort(array)
print(f'Ранжированный массив: {array}')