'''
Задание 5,

Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    title = 'paper'

    def draw(self):
        print('Запуск отрисовки.')


class Pen:
    title = 'Pen'

    def draw(self):
        print('Берём ручку в руки и до ночи пишем')


class Pencil:
    title = 'Pencil'

    def draw(self):
        print('Берём карандаш в руки и стараемся не грызть')


class Handle:
    title = 'Handle'

    def draw(self):
        print('Берём маркер в руки и всё')


Stationery = Stationery()
Pen = Pen()
Pencil = Pencil()
Handle = Handle()
Stationery.draw()
Pen.draw()
Handle.draw()
Pencil.draw()
