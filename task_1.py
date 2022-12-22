"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!
Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0
Process finished with exit code 0
"""


def division(numb1, numb2):
    try:
        numb1, numb2 = int(numb1), int(numb2)
        res = numb1 / numb2
    except ValueError:
        return "Вы ввели не число. Пожалуйста, вводите только числа"
    except ZeroDivisionError:
        return "Вы что? Пытаетесь делить на 0!"
    return res


a = input('Введите первое число: ')
b = input('Введите второе число: ')
print(division(a, b))


