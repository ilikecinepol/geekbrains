"""
Задание 4

Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
data = input('Напишите что-нибудь: ')
data = list(enumerate(data.split()))
for i in data:
    print(i[0] + 1, i[1])
