"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ.

Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class NonNegative:
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if type(value) == dict:
            for val in value.values():
                if type(val) == int:
                    if val < 0:
                        raise ValueError("не может быть отрицательным!")
        else:
            if value < 0:
                raise ValueError("не может быть отрицательным!")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]


class Worker:
    _income = NonNegative()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def __str__(self):
        return f"Сотрудник {self.name} {self.surname}, работающий в должности {self.position}, " \
               f"имеет доход {self._income.get('wage') + self._income.get('bonus')}"


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


my_position1 = Position("Иван", "Иванов", "бухгалтер", 86000, 20000)
my_position2 = Position("Петр", "Петров", "директор", 120000, 40000)
print(my_position1)
print(my_position1.get_full_name())
print(my_position1.get_total_income())
print(my_position2)
print(my_position2.get_full_name())
print(my_position2.get_total_income())
