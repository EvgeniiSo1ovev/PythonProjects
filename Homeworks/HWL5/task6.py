"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def gamechecknumber(num, countoftry=1):
    if countoftry > 10:
        print(f"Исчерпано 10 попыток. Загаданное число: {num}")
        return
    usernumber = int(input("Ваше число: "))
    if usernumber == num:
        print(f"Вы угадали. Это число {num}")
        return
    elif usernumber > num:
        print(f"Загаданное число меньше данного числа!")
        gamechecknumber(num, countoftry + 1)
    else:
        print(f"Загаданное число больше данного числа!")
        gamechecknumber(num, countoftry + 1)


number = random.randint(0, 100)
print("Загадано число от 0 до 100. Угадайте это число.")
gamechecknumber(number)
