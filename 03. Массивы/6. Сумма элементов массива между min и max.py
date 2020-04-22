# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
N = 10
lis = [random.randint(0, 30) for _ in range(N)]
print(lis)
imax = 0
imin = 0
for i in range(N):
    if lis[i] < lis[imin]:
        imin = i
    elif lis[i] > lis[imax]:
        imax = i
if imin > imax:
    imin, imax = imax, imin
summ = 0
for i in range(imin + 1, imax):
        summ += lis[i]

print(f'Максимальный элемент - {lis[imax]}, минимальный элемент - {lis[imin]}')
print(f'Сумма элементов без учета максимального и минимального - {summ}')