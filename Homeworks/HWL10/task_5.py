"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def ping_web(domain_name):
    args = ['ping', domain_name]
    ya_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in ya_ping.stdout:
        res = chardet.detect(line)
        print(line.decode(res['encoding']))


ping_web('yandex.ru')
ping_web('youtube.com')
