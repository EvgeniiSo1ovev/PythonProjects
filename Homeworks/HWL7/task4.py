"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, matrix):
        self.__matrix = matrix

    def __str__(self):
        result = ""
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                if j < len(self.__matrix[i]) - 1:
                    result += str(self.__matrix[i][j]) + "\t"
                else:
                    result += str(self.__matrix[i][j])
            if i < len(self.__matrix) - 1:
                result += "\n"
        return result

    def __add__(self, other):
        matrix_result = []
        for i in range(len(self.__matrix)):
            matrix_pre_result = []
            for j in range(len(self.__matrix[i])):
                matrix_pre_result.append(self.__matrix[i][j] + other.__matrix[i][j])
            matrix_result.append(matrix_pre_result)
        return Matrix(matrix_result)


my_matrix_1 = Matrix([[3, 5, 32],
                      [2, 4, 6],
                      [-1, 64, -8]])
my_matrix_2 = Matrix([[-3, -5, -32],
                      [-2, -4, -6],
                      [1, -64, 8]])
my_matrix_3 = my_matrix_1 + my_matrix_2
print(my_matrix_1)
print()
print(my_matrix_2)
print()
print(my_matrix_3)
