"""
Задание 4
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
from random import randint


def get_list(k):
    my_list = list()
    while k >= 0:
        my_list.append(randint(0, 100))
        k -= 1
    return my_list


indexes = {2: "\u00B2",
           3: "\u00B3",
           4: "\u2074",
           5: "\u2075",
           6: "\u2076",
           7: "\u2077",
           8: "\u2078",
           9: "\u2079"
           }
k = 6
polynomial = str()
a = get_list(k)
for i in range(len(a)):
    if k > 1:
        if a[i] > 1:
            if polynomial == '':
                polynomial += str(a[i]) + '*x' + indexes.get(k)
            else:
                polynomial += ' + ' + str(a[i]) + '*x' + indexes.get(k)
        elif a[i] == 1:
            if polynomial == '':
                polynomial += 'x' + indexes.get(k)
            else:
                polynomial += ' + ' + 'x' + indexes.get(k)
    elif k == 1:
        if a[i] > 1:
            if polynomial == '':
                polynomial += str(a[i]) + '*x'
            else:
                polynomial += ' + ' + str(a[i]) + '*x'
        elif a[i] == 1:
            if polynomial == '':
                polynomial += 'x'
            else:
                polynomial += ' + ' + 'x'
    else:
        if a[i] > 0:
            if polynomial == '':
                polynomial += str(a[i])
            else:
                polynomial += ' + ' + str(a[i])
    k -= 1
polynomial += ' = 0'
print(polynomial)
with open('txt_task4.txt', 'w', encoding='utf-8') as f_n:
    f_n.write(polynomial)
