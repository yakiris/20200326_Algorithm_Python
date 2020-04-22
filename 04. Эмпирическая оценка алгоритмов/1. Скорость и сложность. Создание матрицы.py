# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.

# Создание матрицы
import random
import cProfile

# №1 создание матрицы двумя циклами
def m_create_2_for(size):
    matrix = [[random.randint(1, 100) for _ in range(1, size)] for _ in range(1, size)]

# python -m timeit -n 1000 -s "import dz_4_task_1" "dz_4_task_1.m_create_2_for(10)"
# 1000 loops, best of 5: 158 usec per loop 10
# 1000 loops, best of 5: 26 msec per loop 100

# cProfile.run('m_create_2_for(10)')
# 81    0.000    0.000    0.000    0.000 random.py:200(randrange) 10
# 9801    0.032    0.000    0.067    0.000 random.py:200(randrange) 100

# Итог: сложность данного алгоритма = О(N**2)

# --------------------------------------------------------------------------------------
# №2 Создание матрицы 1 циклом
def m_create_1_for(size_matrix):
    matrix = []
    temp_array = []
    for i in range(1, (size_matrix ** 2) + 1):
        val = random.randint(1, 100)
        if i % size_matrix == 0:
            temp_array.append(val)
            matrix.append(temp_array)
            temp_array = []
        else:
            temp_array.append(val)

# python -m timeit -n 1000 -s "import dz_4_task_1" "dz_4_task_1.m_create_1_for(10)"
# 1000 loops, best of 5: 199 usec per loop 10
# 1000 loops, best of 5: 28.1 msec per loop 100

# cProfile.run("m_create_1_for(10)")
# 100    0.000    0.000    0.000    0.000 random.py:200(randrange) 10
# 10000    0.011    0.000    0.024    0.000 random.py:200(randrange) 100

# Итог: сложность данного алгоритма = О(N**2), при этом данный алгоритм медленнее чем алгоритм №1

# ---------------------------------------------------------------------------------------------
# №3 Создание матрицы рекурсией

def m_create_recursion(range_raw, range_coll, coll_count=0, f_matrix = []):
    matrix = []
    if coll_count + 1 == range_coll:
        for _ in range(range_raw):
            matrix.append(random.randint(1, 100))
        f_matrix.append(matrix)
        return f_matrix
    else:
        for _ in range(range_raw):
            matrix.append(random.randint(1, 100))
        coll_count += 1
        f_matrix = m_create_recursion(range_raw, range_coll, coll_count)
        f_matrix.append(matrix)
        return f_matrix

# python -m timeit -n 1000 -s "import dz_4_task_1" "dz_4_task_1.m_create_recursion(10, 10)"
# 1000 loops, best of 5: 542 usec per loop 10, 10
# 1000 loops, best of 5: 33.3 msec per loop 100, 100

# cProfile.run('m_create_recursion(10, 10)')
# 100    0.000    0.000    0.000    0.000 random.py:200(randrange) 10, 10
# 10000    0.008    0.000    0.017    0.000 random.py:200(randrange) 100, 100

# Итог: сложность данного алгоритма так же О(N**2), при этом он медленнее алгоритмов №1 и №2.

# По итогу проведения оценки скорости работы алгоритмов можно сказать, что самым оптимальным является алгоритм №1