# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

def partition(array, pivot):
    smaller = []
    equally = []
    bigger = []
    for i in array:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            bigger.append(i)
        else:
            equally.append(i)
    return smaller, equally, bigger

def top_key(array, key):
    pivot = array[random.randrange(len(array))]
    left, middle, right = partition(array, pivot)
    if len(left) == key:
        return left
    if len(left) < key <= len(left) + len(middle):
        return middle
    if len(left) > key:
        return top_key(left, key)
    return top_key(right, key - len(left) - len(middle))

def median(array):
    result_list = top_key(array, len(array) // 2 + 1)
    return max(result_list)

size = 5
limit = 100
array = [random.randrange(0, limit) for _ in range(2 * size + 1)]
print(f'Не ранжированный массив: {array}')
print(f'Медиана = {median(array)}')
print(f'Ранжированный массив: {sorted(array)}')