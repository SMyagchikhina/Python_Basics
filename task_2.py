"""
Задание 2.
Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt

divisible = input('Введите делимое: ')
divider = input('Введите делитель: ')

try:
    divider = int(divider)
    divisible = int(divisible)
    if divider == 0:
        raise DivisionByZero('Делить на ноль нельзя!')
    print(divisible/divider)
except ValueError:
    print('Вы ввели не число!')
except DivisionByZero as err:
    print(err)


