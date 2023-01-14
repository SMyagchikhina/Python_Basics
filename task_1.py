"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""



from time import sleep

#вариант решения 1
class TrafficLight:
    __color = 'красный'

    def running(self):
        print('Светофор горит красным')
        sleep(7)
        print('Светофор горит желтым')
        sleep(2)
        print('Светофор горит зеленым')
        sleep(20)


traf_light = TrafficLight()
traf_light.running()


#вариант решения 2
print() #для вывода пустой строки между результатами вариантов решений
class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        print('На светофоре горит ', self.__color[0])
        sleep(7)
        print('На светофоре горит ', self.__color[1])
        sleep(2)
        print('На светофоре горит ', self.__color[2])
        sleep(20)


traf_light = TrafficLight()
traf_light.running()


#вариант решения 3
print()
class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 20}

    def running(self):
        for key, value in TrafficLight.__color.items():
            print(f'На светофоре горит {key}')
            sleep(value)


traf_light = TrafficLight()
traf_light.running()


