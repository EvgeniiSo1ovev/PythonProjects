"""
задание 2.

пользователь вводит время в секундах.
переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
используйте форматирование строк.

пример:
введите время в секундах: 3600
время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

user_time = int(input("Введите время в секундах: "))
print(f"Время в формате ч:м:с - {user_time / 3600} : {user_time / 60} : {user_time}")