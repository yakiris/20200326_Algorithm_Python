# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

# вариант с циклом for
for i in range(32, 128):
    print(f'{i}-{chr(i)}  ', end = '')
    if i % 10 == 1:
        print()
print()

# вариант с циклом while
number = 32
i = 0
while number <= 127:
    i +=1
    print(f'{number}-"{chr(number)}"  ', end='')
    number += 1
    if i % 10 == 0:
        print()
print()