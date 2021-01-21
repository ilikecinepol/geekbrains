'''
Задание 4

Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
'''
num = int(input('Введите число: '))
const_num = num
last_max = num % 10
i = len(str(num))
while i > 0:
    current_max = num % 10
    if last_max < current_max:
        last_max = current_max
    else:
        pass
    num = num // 10
    i -= 1

print(last_max)