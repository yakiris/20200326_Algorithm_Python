# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

import cProfile

# №1 с помощью алгоритма «Решето Эратосфена»
def eratosthenes(n):
    if n == 1:
        return 2
    n += 1
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result[len(result) - 1]

# python -m timeit -n 1000 -s "import dz_4_task_2" "dz_4_task_2.eratosthenes(10)"
# 1000 loops, best of 5: 3.67 usec per loop 10
# 1000 loops, best of 5: 132 usec per loop 100
# 1000 loops, best of 5: 393 usec per loop 1000

# cProfile.run('eratosthenes(10)')
# 1    0.000    0.000    0.000    0.000 dz_4_task_2.py:6(eratosthenes) 10
# 1    0.000    0.000    0.000    0.000 dz_4_task_2.py:6(eratosthenes) 100
# 1    0.001    0.001    0.001    0.001 dz_4_task_2.py:6(eratosthenes) 1000

# Итог: сложность данного алгоритма = О(N**2)

# --------------------------------------------------------------------------------------
# №2 без использования «Решета Эратосфена»

def myFunc(n):
    b = []
    for i in range(2, n):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            b.append(i)
    return b[len(b) - 1]

# python -m timeit -n 1000 -s "import dz_4_task_2" "dz_4_task_2.myFunc(10)"
# 1000 loops, best of 5: 22.8 usec per loop 10
# 1000 loops, best of 5: 365 usec per loop 100
# 1000 loops, best of 5: 66.3 msec per loop 1000

# cProfile.run('myFunc(10)')
# 1    0.000    0.000    0.000    0.000 dz_4_task_2.py:36(myFunc) 10
# 1    0.001    0.001    0.001    0.001 dz_4_task_2.py:36(myFunc) 100
# 1    0.069    0.069    0.069    0.069 dz_4_task_2.py:36(myFunc) 1000

# Итог: сложность данного алгоритма = О(N**2), при этом данный алгоритм медленнее чем алгоритм №1

# По итогу проведения оценки скорости работы алгоритмов можно сказать, что более оптимальным является алгоритм №1