"""
задание 1.

поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

пример:
ведите ваше имя: василий
ведите ваш пароль: vas
введите ваш возраст: 45
ваши данные для входа в аккаунт: имя - василий, пароль - vas, возраст - 45
"""

a = 123
b = "текст"
print(a)
print(b)

user_name = input("Введите ваше имя: ")
user_password = input("Введите ваш пароль: ")
user_age = input("Введите ваш возраст: ")
print(f"Ваши данные для входа в аккаунт: имя - {user_name}, пароль - {user_password}, возраст - {user_age}")