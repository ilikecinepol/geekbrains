'''
Задание 4

Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''


class Car:
    speed = 60
    color = 'white'
    name = 'Lada'
    is_place = True

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        if direction == 'right':
            print(f'Машина {self.name} повернула направо!')
        else:
            print(f'Машина {self.name} повернула налево!')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self.speed}')
        if self.speed > 60:
            print('Вы превышаете скорость!')


class SportCar(Car):
    # atributes
    speed = 140


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self.speed}')
        if self.speed > 40:
            print('Вы превышаете скорость!')


class PoliceCar(Car):
    # atributes
    def chase(self):
        print(f'Полицейская машина {self.name} преследует  нарушителя!')


car1 = Car()
car1.name = 'Niva'
car1.color = 'black'
car1.go()
car1.turn('right')
car1.stop()

sportcar = SportCar()
sportcar.show_speed()

workcar = WorkCar()
workcar.speed = 50
workcar.show_speed()

police = PoliceCar()
police.go()
police.chase()
