'''
Задание 8
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''
from random import randint

SIZE_M = 3
SIZE_N = 5
MAX_NUM = 100
MIN_NUM = 1

matrix = [[randint(MIN_NUM, MAX_NUM) for m in range(SIZE_M)] for n in range(SIZE_N)]
# print(f"Первоначальный массив: {matrix}")

sum_col = [0] * len(matrix[0])

for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += item
        sum_col[i] += item
        print(f'{item:>7}', end="")
    print(f'{sum_line:>10}')
