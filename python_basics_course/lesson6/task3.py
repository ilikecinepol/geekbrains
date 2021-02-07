'''
Задание 3

Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    # atributes
    name = 'unnamed'
    surname = 'unnamed'
    position = 'unnamed'
    _income = {"wage": 50000, "bonus": 10000}


class Position(Worker):
    full_name = 'unnamed'
    full_income = 0

    def get_full_name(self):
        self.full_name = self.name + ' ' + self.surname
        print(f'Полное имя работника: {self.full_name}')

    def get_full_income(self):
        self.full_income = self._income['wage'] + self._income['bonus']
        print(f'Оклад работника {self.full_name} с учётом премии: {self.full_income}')


worker1 = Position()
worker1.name = "John"
worker1.surname = 'Brown'
worker1.get_full_name()

worker1.get_full_income()
worker1._income['wage'] = 70000
worker1._income['bonus'] = 130000
worker1.get_full_income()
