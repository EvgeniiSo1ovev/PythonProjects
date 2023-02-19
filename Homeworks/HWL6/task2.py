"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

import random

leftvalue = int(input("Введите минимальное значение элемента массива: "))
rightvalue = int(input("Введите максимальное значение элемента массива: "))


def getlist(nlist, nn=10):
    if nn == 1:
        nlist.append(random.randint(0, 100))
        return nlist
    getlist(nlist, nn - 1)
    nlist.append(random.randint(0, 100))
    return nlist


def getindex(nlist, leftval, rightval):
    ilist = [i for i in range(0, len(nlist)) if (leftval <= nlist[i] <= rightval)]
    return ilist


my_list = list()
my_list = getlist(my_list)
index_list = getindex(my_list, leftvalue, rightvalue)

print(my_list)
print(index_list)
