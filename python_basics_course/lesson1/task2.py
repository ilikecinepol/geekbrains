'''
Задание 2

Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''
time = int(input('Введите время в секундах: '))

hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60

print(f'Вы ввели время, равное {hours} часов {minutes} минут {seconds} секунд')
