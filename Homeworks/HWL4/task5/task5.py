"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""

indexes = {2: "\u00B2",
           3: "\u00B3",
           4: "\u2074",
           5: "\u2075",
           6: "\u2076",
           7: "\u2077",
           8: "\u2078",
           9: "\u2079"
           }

with open('file_1.txt', encoding='utf-8') as f_n:
    polynomial1 = f_n.read().split(' + ')
    print(polynomial1)
with open('file_2.txt', encoding='utf-8') as f_n:
    polynomial2 = f_n.read().split(' + ')
    print(polynomial2)
polynomial3 = str()
with open('file_3.txt', 'w', encoding='utf-8') as f_n:
    f_n.write(polynomial3)
