# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random
N = 10
lis = [random.randint(0, 30) for _ in range(N)]
print(lis)
if lis[0] > lis[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, N):
    if lis[i] < lis[min1]:
        spam = min1
        min1 = i
        if lis[spam] < lis[min2]:
            min2 = spam
    elif lis[i] < lis[min2]:
        min2 = i

print(f"Первое минимальное {lis[min1]}, Второе минимальное {lis[min2]}")