'''
Задание 6
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
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


def amount(arr=arr, min=minimum(arr), max=maximum(arr)):
    min_ind = arr.index(min)
    max_ind = arr.index(max)
    amount = 0
    if max_ind >= min_ind:
        for i in range(min_ind + 1, max_ind):
            amount += arr[i]
    else:
        for i in range(max_ind + 1, min_ind):
            amount += arr[i]
    return amount


print(f'Максимальный элемент массива:{maximum(arr)}')
print(f'Минимальнй элемент массива:{minimum(arr)}')

print(f'Сумма промежуточных элементов: {amount()}')
