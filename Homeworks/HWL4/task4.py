"""
Задание 4
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
from random import randint

k = 2
a = list()
polynomial = str()
while k < 0:
    a.append = randint(0, 100)
    k -= 1
for el in a:
    if el > 0:
        polynomial += str(el) + '*x\u00B2'+