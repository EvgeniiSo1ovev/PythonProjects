"""
4. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

count_of_product = int(input("Введите количество товаров: "))
number = 1
my_list = list()
while number <= count_of_product:
    name = input("Введите название товара: ")
    cost = int(input("Введите цену товара: "))
    count = int(input("Введите количество товара: "))
    unit = input("Введите единицу измерения количества товара: ")
    my_dict = {"название": name, "цена": cost, "количество": count, "eд": unit}
    my_tuple = (number, my_dict)
    my_list.append(my_tuple)
    number += 1
print(my_list)

names = list()
costs = list()
counts = list()
units = list()
for element in my_list:
    names.append(element[1].setdefault("название"))
    costs.append(element[1].setdefault("цена"))
    counts.append(element[1].setdefault("количество"))
    units.append(element[1].setdefault("eд"))
analized_dict = {"названия": names, "цены": costs, "количества": counts, "eд": units}
print(analized_dict)
