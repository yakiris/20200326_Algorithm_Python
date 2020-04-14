# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from _collections import defaultdict

org = int(input('Введите количество предприятий: '))
summ = []
# прибыль за год по каждому предприятию
summ_org = defaultdict(int)
for i in range(org):
    name = input('Наименование предприятия: ')
    for j in range(4):
        profit = int(input(f'Прибыль за {j + 1} квартал предприятия {name}: '))
        summ_org[name] += profit
summ += summ_org.values()
mean = round(sum(summ) / org, 2)
print(f'Средняя прибыль за год по всем предприятиям: {mean}')
for k in summ_org:
    if summ_org[k] > mean:
        print(f'Прибыль предприятия {k} равна {summ_org[k]} - это выше среднего')
    elif summ_org[k] < mean:
        print(f'Прибыль предприятия {k} равна {summ_org[k]} - это ниже среднего')