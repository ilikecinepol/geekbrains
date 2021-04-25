alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter1 = input('Введите первую букву латинского алфавита: ')
letter2 = input('Введите вторую букву латинского алфавита: ')


def get_number(letter, arr=alphabet):  # функция бинарного поиска буквы в алфавите
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        result = arr[mid]
        if result == letter:
            return mid + 1  # т.к. выводим порядковый номер буквы в алфавите, а не индекс в строке, который начинается с нуля
        elif result > letter:
            high = mid - 1
        else:
            low = mid + 1


num1 = get_number(letter1)
print(f'Номер буквы "{letter1}" в алфавите: {num1}')
num2 = get_number(letter2)
print(f'Номер буквы "{letter2}" в алфавите: {num2}')
print(f"Количество букв между '{letter2}' и '{letter1}': {num2 - num1}")
