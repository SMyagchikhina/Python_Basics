"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NumbersOnly(Exception):
    def __init__(self, txt):
        self.txt = txt


my_lst = []
while True:
    try:
        el = input("Введите число или stop для завершения: ")
        if el.lower() == 'stop':
            break
        elif el.isdigit():
            my_lst.append(int(el))
        else:
            raise NumbersOnly("Вы ввели не число")
    except NumbersOnly as err:
        print(err.txt)

print(my_lst)


