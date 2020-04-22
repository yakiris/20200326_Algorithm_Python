# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

N = 21
lis = [random.randint(1, 100) for _ in range(N)]
print(lis)
imax = 0
imin = 0
for i in range(N):
    if lis[i] < lis[imin]:
        imin = i
    elif lis[i] > lis[imax]:
        imax = i
print(f'Минимальное число {lis[imin]} с индексом {imin}, максимальное число {lis[imax]} с индексом {imax}')
lis[imax], lis[imin] = lis[imin], lis[imax]
print(lis)

