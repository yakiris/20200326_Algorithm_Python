# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

size = 5
N = 10
matrix = [[random.randint(1, N) for _ in range(size)] for _ in range(size)]

min1 = [0] * len(matrix[0])
M = [N] * len(matrix[0])
for line in matrix:
    for i, item in enumerate(line):
        if item < M[i]:
            M[i] = item
        min1[i] = M[i]
        print(f'{item:>5}', end='')
    print()
print(f'-' * (len(matrix) * 5))
mm = 0
for s in min1:
    if s > mm:
        mm = s
    print(f'{s:>5}', end='')
print(f'  | max = {mm}')