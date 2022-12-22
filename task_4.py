"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


# способ первый с **
def my_func(x, y):
    try:
        if y < 0:
            res = 1 / (x ** (-y))
            return res
        else:
            return 'Число y должно быть строго отрицательным'
    except TypeError:
        return 'Вы ввели не число!'


print(my_func(2, -3))
print(my_func(2, 3))
print(my_func('строка', -3))


# способ второй без **
def my_func(x, y):
    try:
        y = int(num2)
        if y < 0:
            x = float(x)
            res = 1
            for i in range(abs(y)):
                res /= x
            return round(res, 7)
        else:
            return 'Число y должно быть строго отрицательным'
    except ValueError:
        return 'Вы ввели не число!'

num1 = input('Введите число x: ')
num2 = input('Введите число y: ')


print(my_func(num1, num2))


# способ третий, без **
def get_exp(x, y):
    """
    Возведение числа x в степень y. Более сложная реализация без оператора **,
    предусматривающая использование цикла.
    :param x: целое число. Не равно нулю
    :param y: целое отрицательное число
    :return: результат возведения в степень y числа x
    """
    try:
        y = int(num2)
        if y < 0:
            x = float(x)
            res = 1
            for i in range(y, 0):
                res = res * x
            res = 1 / res
            return f'Для значений x = {num1}, y = {num2} результат: {res}'
        else:
            return "Число y должно быть строго отрицательным"
    except TypeError:
        return "Пожалуйста, вводите только числа"
    except ZeroDivisionError:
        return "На ноль делить нельзя"


num1 = input('Введите число x: ')
num2 = input('Введите число y: ')


print(get_exp(num1, num2))
