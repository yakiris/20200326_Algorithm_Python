# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три разных числа.')
a = int(input('1-е число: '))
b = int(input('2-е число: '))
c = int(input('3-е число: '))

if b > a > c or c > a > b:
    print(f'Среднее число: {a}')
elif a > b > c or c > b > a:
    print(f'Среднее число: {b}')
else:
    print(f'Среднее число: {c}')
