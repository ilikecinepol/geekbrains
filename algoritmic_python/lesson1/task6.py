'''
Задание 6
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

num = int(input('Введите номер буквы (1-26): '))


def get_letter(num, arr=alphabet):  # функция бинарного поиска буквы в алфавите
    low = 0
    high = 25

    while low <= high:
        mid = int((low + high) / 2)
        result = arr[mid - 1]  # т.к. выводим порядковый номер буквы в алфавите, а не индекс в строке, который начинается с нуля
        if mid == num:
            return result
        elif mid > num:
            high = mid - 1
        else:
            low = mid + 1


print(get_letter(num))
