'''
Задание 1

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''
import random

data = [[random.randint(10, 99) for x in range(10)], [random.randint(10, 99) for x in range(10)],
        [random.randint(10, 99) for x in range(10)], [random.randint(10, 99) for x in range(10)]]
data1 = [[random.randint(10, 99) for x in range(10)], [random.randint(10, 99) for x in range(10)],
         [random.randint(10, 99) for x in range(10)], [random.randint(10, 99) for x in range(10)]]

print(data)
print(data1)


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Объект с параметрами (\n |{self.data[0]}|, \n |{self.data[1]}|,\n |{self.data[2]}|, \n |{self.data[3]}|)"

    def __add__(self, other):
        result = []
        res = []
        for i in range(4):
            for j in range(10):
                result.append(self.data[i][j] + other.data[i][j])
        print(result)
        res1 = [result[0:9]]
        res2 = [result[10:19]]
        res3 = [result[20:29]]
        res4 = [result[30:39]]
        result = [res1, res2, res3, res4]
        print(result)
        return Matrix(result)


m = Matrix(data)
m1 = Matrix(data1)
print(m)
print(m + m1)
