"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, name, hours, hour_rate, premium = argv


def calculate_salary(name, hours, hour_rate, premium):
    try:
        payment = (int(hours) * int(hour_rate)) + int(premium)
        print(f'Сотрудник {name} заработал {payment}')
    except TypeError:
        print("Операция применена к объекту несоответствующего типа")
        exit()


calculate_salary(name, hours, hour_rate, premium)

""" Скрипт с параметрами можно запустить средствами PyCharm. Для этого необходимо:
1) открыть окно Run -> Edit Configurations
2) в поле parameters указать нужные параметры, 
например, "Иван Иванов" 100 10 1200 для нашего выбранного скрипта
3) запустить скрипт горячими клавишами Ctrl+Shift+F10
"""


