# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random
N = 10
lis = [random.randint(-10, 10) for _ in range(N)]
print(lis)
mm = - N
index = 0
for i, num in enumerate(lis):
    if lis[i - 1] > mm and lis[i - 1] < 0:
        mm = lis[i - 1]
        index = i - 1
print(f'Максимально отрицательный элемент {mm}, позиция в массиве {index + 1}.')