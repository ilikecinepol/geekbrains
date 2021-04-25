'''
Задание 2

Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

'''
from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def calculation(self):
        pass

    def __add__(self, other):
        Clothes.result += self.calculation + other.calculation
        return Costume(0)

    def __str__(self):
        return f'Всего необходимо {Clothes.result} ткани'


class Coat(Clothes):
    @property
    def calculation(self):
        result = self.size / 6.5 * 0.5 / 100
        return round(result)


class Costume(Clothes):
    @property
    def calculation(self):
        result = self.size * 2 + 0.3 / 100
        return round(result)


cl_1 = Coat(45)
cl_2 = Costume(170)
print(cl_1 + cl_2)
