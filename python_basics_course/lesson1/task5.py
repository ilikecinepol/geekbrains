'''
Задание 5

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''
gain = int(input('Введите показатели выручки фирмы: '))
costs = int(input('Введите показатели издержек фирмы: '))
if gain > costs:
    profit = gain - costs
    print(f'Поздравляю! Компания приносит прибыль в размере {profit}')
    print(f'Рентабельность составляет {profit/gain}')
elif gain < costs:
    profit = costs - gain
    print(f'К сожалению, пока компания приносит убыток в размере {profit}')

staff = int(input('Введите количество сотрудников: '))
print(f'Прибыль фирмы в расчёте на одного сотрудника составляет {profit/staff}')
