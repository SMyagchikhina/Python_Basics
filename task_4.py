"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Новая машина: {self.name} полиция? {self.is_police}')

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'Машина {self.name} движется со скоростью {self.speed}'

class TownCar(Car):
    def show_speed(self):
        print(f'Городской автомобиль {self.name} движется со скоростью {self.speed}км/ч. '
              f'{"Превышение скорости!" if self.speed > 60 else "Скорость не превышена. "}')

class SportCar(Car):
    # pass
    '''Спортивный автомобиль'''

class WorkCar(Car):
    def show_speed(self):
        print(f'Рабочий автомобиль {self.name} движется со скоростью {self.speed}км/ч. '
              f'{"Превышение скорости!" if self.speed > 40 else "Скорость не превышена. "}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    # в этом классе прописываем __init__ и super() так как меняем унаследованный атрибут is_police,
    # выше у других классов ничего не меняли, поэтому не прописывала конструкторы

town_car = TownCar(50, 'white', 'Bus')
print(town_car.go())
print(town_car.turn('налево'))
print(town_car.show_speed())
print(town_car.stop())

print()
work_car = WorkCar(75, 'grey', 'KIA')
print(work_car.go())
print(work_car.show_speed())
print(work_car.stop())

print()
sport_car = SportCar(120, 'red', 'Audi')
print(f'{sport_car.go()} со скоростью {sport_car.speed}')
print(sport_car.stop())

print()
police_car = PoliceCar(90, 'white', 'Ford')
print(police_car.go())
print(police_car.show_speed())
print(police_car.stop())
print(police_car.is_police)



