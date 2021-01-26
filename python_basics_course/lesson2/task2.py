'''
Задание 2

Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
arr = []
num = int(input('Введите количество элементов списка: '))
for i in range(num):
    current = input(f'Введите элемент списка под номером {i}: ')
    arr.append(current)
print(f'Получился список: {arr}')
print('Идёт обработка списка...')
for i in arr:

    current_data = arr.index(i)
    last_data = arr.index(i) - 1
    if current_data % 2 == 1:
        arr[current_data], arr[last_data] = arr[last_data], arr[current_data]

print('_' * 50)
print(f'Получившийся список имеет вид: {arr}')
