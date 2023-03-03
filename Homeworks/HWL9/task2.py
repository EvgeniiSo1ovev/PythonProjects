"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ.

Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class NonNegative:
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("не может быть отрицательным!")
        instance.__dict__[self.my_attr] = value


class Road:
    mass_square = 25
    heigth = 0.05
    _length = NonNegative()
    _width = NonNegative()

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self):
        return self._length * self._width * self.mass_square * self.heigth


my_road_length = int(input("Введите длину дороги: "))
my_road_width = int(input("Введите ширину дороги: "))
my_road = Road(my_road_length, my_road_width)
print(f"Масса асфальта, необходимого для покрытия всего дорожного полотна длиной "
      f"{my_road_length} м., шириной {my_road_width} м., составляет {my_road.get_mass()} кг.")
