"""Задание 1
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""
import math

# при $d = 0.001
print(float("{:.3f}".format(math.pi)))

# при $10^{-1} ≤ d ≤10^{-10}$
count_of_numbers = 1
while count_of_numbers <= 10:
    format_count_of_numbers = "{:." + str(count_of_numbers) + "f}"
    print(float(format_count_of_numbers.format(math.pi)))
    count_of_numbers += 1
