# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных
# элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = []
for i in range(4):
    line = []
    summ = 0
    print(f'{i + 1}-я строка матрицы')
    for j in range(4):
        num = int(input(f'введите {j + 1}-е число: '))
        summ += num
        line.append(num)
    line.append(summ)
    matrix.append(line)

for i in matrix:
    for item in i:
        print(f'{item:>5}', end='')
    print()