# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num = int(input('Количество чисел: '))
max_num = 0
max_sum = 0
for i in range(num):
    m = int(input('Введите число: '))
    temp_num = m
    temp_sum = 0
    while m > 0:
        temp_sum = temp_sum + m % 10
        m = m // 10
        if temp_sum > max_sum:
            max_sum = temp_sum
            max_num = temp_num

print(f'Наибольшая сумма цифр {max_sum} числа {max_num}')