'''
Задание 7
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
'''
n = int(input('Введите число: '))

part1 = n * (n + 1) / 2


def funk(n):
    if n == 1:
        return 1
    result = n + funk(n - 1)
    return result


print(f'Для числа {n} правая часть n(n+1)/2 = {part1}, а левая: 1+2+...+n = {funk(n)}')
print('ЧТД')
