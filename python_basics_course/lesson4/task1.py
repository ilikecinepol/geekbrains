"""
Задание 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""
from sys import argv


path, bid, production, prize = argv
print(argv)

wages = lambda bid, production, prize: int(bid) * int(production) + int(prize)
print(wages(bid, production, prize))


