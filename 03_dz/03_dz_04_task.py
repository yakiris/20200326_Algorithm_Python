# 4. Определить, какое число в массиве встречается чаще всего.

import random
N = 20
lis = [random.randint(1, 10) for _ in range(N)]
print(lis)

num = lis[0]
max_frq = 1
for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if lis[i] == lis[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = lis[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
