'''
Задание 1

Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
from tkinter import *
import time

tk = Tk()
tk.title('Задание 1. Светофор')
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=589)
canvas.pack()
bg = PhotoImage(file='svetofor.gif')
w = bg.width()
h = bg.height()
canvas.create_image(0, 0, image=bg, anchor='nw')
r = 150  # Радиус сектора светофора
l = 10  # расстояние между секторами
tk.update_idletasks()
tk.update()
time.sleep(0.01)


class VisualTrafficLight:
    __color = 'red'
    colors = ['red', 'yellow', 'green', 'black']
    r = 150  # Радиус сектора светофора
    l = 10  # расстояние между секторами
    # Координаты точек секторов
    x1 = 175
    y1 = 65
    x11 = x1 + r
    y11 = y1 + r

    x2 = x1
    y2 = y11 + l
    x22 = x2 + r
    y22 = y2 + r

    x3 = x1
    y3 = y22 + l
    x33 = x3 + r
    y33 = y3 + r

    def __init__(self):
        canvas.create_oval(
            self.x1, self.y1, self.x11, self.y11, outline="white",
            fill=self.colors[3], width=2
        )
        canvas.create_oval(
            self.x2, self.y2, self.x22, self.y22, outline="white",
            fill=self.colors[3], width=2
        )
        canvas.create_oval(
            self.x3, self.y3, self.x33, self.y33, outline="white",
            fill=self.colors[3], width=2
        )

    def picture(self, colors):
        # Добавление изображения светофора
        canvas.create_oval(
            self.x1, self.y1, self.x11, self.y11, outline="white",
            fill=self.colors[0], width=2
        )
        canvas.create_oval(
            self.x2, self.y2, self.x22, self.y22, outline="white",
            fill=self.colors[1], width=2
        )
        canvas.create_oval(
            self.x3, self.y3, self.x33, self.y33, outline="white",
            fill=self.colors[2], width=2
        )
        time.sleep(2)

    def timing(self):
        __color = 'red'
        print(__color)
        time.sleep(7)
        __color = 'yellow'
        print(__color)
        time.sleep(2)
        __color = 'green'
        print(__color)
        time.sleep(5)

    def working(self):
        __color = 'red'
        self.colors = ['red', 'black', 'black']
        self.picture(self.colors)
        print(self.__color)
        tk.update()
        time.sleep(7)

        self.colors = ['red', 'yellow', 'black']
        self.picture(self.colors)
        print(self.__color)
        tk.update()
        time.sleep(2)

        self.colors = ['black', 'black', 'green']
        self.picture(self.colors)
        __color = 'green'
        print(self.__color)
        tk.update()
        time.sleep(5)

        for i in range(0, 3):
            self.colors = ['black', 'black', 'black']
            self.picture(self.colors)
            __color = 'green'
            print(self.colors)
            tk.update()
            time.sleep(0.2)

            self.colors = ['black', 'black', 'green']
            self.picture(self.colors)
            __color = 'green'
            print(self.colors)
            tk.update()
            time.sleep(0.2)


v = VisualTrafficLight()
while True:
    v.working()

mainloop()
