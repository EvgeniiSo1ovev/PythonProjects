"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

# первый вариант решения задания
my_list = [b'class', b'function', b'method']

for el in my_list:
    print(type(el))
    print(el)
    print(len(el))

# второй вариант решения задания
my_list = ['class', 'function', 'method']

for el in my_list:
    el_bytes = bytes(el, encoding='ascii')
    print(type(el_bytes))
    print(el_bytes)
    print(len(el_bytes))
