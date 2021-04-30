'''
Задание 4
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
'''
n = int(input('Введите количество элементов: '))
current = 1
result = 1
for i in range(n):
    if i % 2 == 0:
        k = 1
    k = -1
    current = current * k / 2
    result += current
    print(current)

print(result)
