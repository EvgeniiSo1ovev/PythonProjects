"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

items:
- computer
- printer
- keyboard
- mouse
items_ptice:
  computer: 200€-1000€
  keyboard: 5€-50€
  mouse: 4€-7€
  printer: 100€-300€
items_quantity: 4

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

items = ['computer',
         'printer',
         'keyboard',
         'mouse']
items_price = {'computer': '200\u20AC-1000\u20AC',
               'keyboard': '5\u20AC-50\u20AC',
               'mouse': '4\u20AC-7\u20AC',
               'printer': '100\u20AC-300\u20AC'}
objs = {'items': items,
        'items_price': items_price,
        'items_quantity': 4}

with open('file.yaml', 'w') as f_n:
    yaml.dump(objs, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml') as f_n:
    print(f_n.read())
