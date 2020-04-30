# 1. Определение количества различных подстрок с использованием хеш-функции.
# Дана строка S длиной N. Например, состоящая только из строчных латинских букв.
# Требуется найти количество подстрок в этой строке.

import hashlib

def count_substring(input_string: str):

    input_string = str(input_string).lower()
    set_hash = set()
    length = len(input_string)

    for i in range(length - 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest()
            set_hash.add(h)

    return len(set_hash) - 1

some_string = input('Введите строку для проверки: ')
count = count_substring(some_string)
print(f'В строке "{some_string}" есть {count} различных подстрок')