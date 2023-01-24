"""
6. Продолжить работу над пятым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class MyOwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self):
        self._dict = {}
        self._div = {}

    def reception(self, equipment):
        """добавляем в словарь объект по его названию,
        в значении будет список экземпляров этого оборудования"""
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        """извлекаем из значения объект по названию группы"""
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class OfficeEquipment:
    def __init__(self, name, price, is_color, sheet_format, quantity):
        self.name = name
        self.price = price
        self.is_color = is_color
        self.sheet_format = sheet_format
        self.group = self.__class__.__name__
        try:
            if isinstance(quantity, int):
                self.quantity = quantity
            else:
                self.quantity = ''
                raise MyOwnExc("Вы ввели не число, количество будет пустым")

        except MyOwnExc as e:
            print(e.txt)

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name}, {self.price}, {self.is_color}, {self.sheet_format}, {self.quantity}'


class Printer(OfficeEquipment):
    def __init__(self, name, price, is_color, sheet_format, quantity, print_type):
        self.print_type = print_type
        super().__init__(name, price, is_color, sheet_format, quantity)

    def __repr__(self):
        return f'{self.name}, {self.price}, {self.is_color}, {self.sheet_format}, {self.quantity}, {self.print_type}'


class Scanner(OfficeEquipment):
    def __init__(self, name, price, is_color, sheet_format, quantity, scan_type):
        self.scan_type = scan_type
        super().__init__(name, price, is_color, sheet_format, quantity)

    def __repr__(self):
        return f'{self.name}, {self.price}, {self.is_color}, {self.sheet_format}, {self.quantity}, {self.scan_type}'


class Copier(OfficeEquipment):
    def __init__(self, name, price, is_color, sheet_format, quantity, copier_type):
        self.copier_type = copier_type
        super().__init__(name, price, is_color, sheet_format, quantity)

    def __repr__(self):
        return f'{self.name}, {self.price}, {self.is_color}, {self.sheet_format}, {self.quantity}, {self.copier_type}'


warehouse = Warehouse()
print(warehouse._dict)
# создаем объект и добавляем
printer = Printer('Xerox Phaser 3020', 9990, False, 'A4', 'ghgjh', 'laser')
warehouse.reception(printer)
printer = Printer('HP Deskjet 2320', 6781, True, 'A4', 1, 'laser')
warehouse.reception(printer)
scanner = Scanner('Canon CanoScan LiDe 400', 22795, True, 'A4', 10, 'flatbed')
warehouse.reception(scanner)
scanner = Scanner('Canon imageFormula DR-C240', 55940, True, 'A4', 1, 'broach')
warehouse.reception(scanner)
copier = Copier('Xerox WorkCentre 3335', 66490, False, 'A4', 2, 'laser')
warehouse.reception(copier)
copier = Copier('Xerox B1022', 81496, False, 'A3', 1, 'laser')
warehouse.reception(copier)

# выводим оборудование на складе
print(warehouse._dict)

# извлекаем со склада 1 принтер
warehouse.extract('Printer')
division = Warehouse()

# выводим обновленный список оборудования на складе
print(warehouse._dict)


