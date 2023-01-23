"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, name, price, is_color, sheet_format, quantity, *args):
        self.name = name
        self.price = price
        self.is_color = is_color
        self.sheet_format = sheet_format
        self.quantity = quantity


class Printer(OfficeEquipment):
    def __init__(self, name, price, is_color, sheet_format, quantity, print_type):
        self.print_type = print_type
        super().__init__(name, price, is_color, sheet_format, quantity)


class Scanner(OfficeEquipment):
    def __init__(self, name, price, is_color, sheet_format, quantity, scan_type):
        self.scan_type = scan_type
        super().__init__(name, price, is_color, sheet_format, quantity)


class Copier(OfficeEquipment):
    def __init__(self, name, price, is_color, sheet_format, quantity, copier_type):
        self.copier_type = copier_type
        super().__init__(name, price, is_color, sheet_format, quantity)


