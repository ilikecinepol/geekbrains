'''
Задание 3
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
from random import randint

SIZE = 10
MAX_NUM = 100
MIN_NUM = 0

arr = [randint(MIN_NUM, MAX_NUM) for x in range(SIZE)]
print(f"Первоначальный массив: {arr}")


def maximum(arr):
    maximum = 0
    for n in arr:
        if n > maximum:
            maximum = n
    return maximum


def minimum(arr):
    minimum = MAX_NUM
    for n in range(len(arr) - 1, 0, -1):
        # print(arr[n])
        if arr[n] < minimum:
            minimum = arr[n]

    return minimum


print(f'Максимальный элемент массива:{maximum(arr)}')
print(f'Минимальнй элемент массива:{minimum(arr)}')
