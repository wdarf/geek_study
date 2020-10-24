"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

from time import sleep


class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]

    def running(self):
        c = 0
        for el in TrafficLight.__color:
            if c < 3:
                print(f"Загорается {TrafficLight.__color[c]} сигнал")
            if c == 0:
                sleep(2)
            elif c == 1:
                sleep(2)
            elif c == 2:
                sleep(2)
            c += 1


traff = TrafficLight()
traff.running()


"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число сантиметров толщины полотна. Проверить работу
метода. Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length = None
    _width = None
    massa = None
    thickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def asphalt_mass(self):
        self.massa = 25
        self.thickness = 0.05
        asphalt_mass = self.length * self.width * self.massa * self.thickness / 1000
        print(f'Для покрытия дорожного полотна необходимо {asphalt_mass} тонн')


a_m = Road(1000, 8)
a_m.asphalt_mass()


"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = None
    last_name = None
    position = None
    _income = None

    def __init__(self, name, last_name, position, wage, bonus):
        self.name = name
        self.last_name = last_name
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, last_name, position, wage, bonus):
        super().__init__(name, last_name, position, wage, bonus)

    def get_full_name(self):
        return self.name + self.last_name

    def get_full_profit(self):
        self._income = {"Оклад": self.wage, "Премия": self.bonus}
        return self._income


worker = Position("Дмитрий ", "Вавилов", "инженер 2 категории", 47000, 27000)
print(worker.get_full_name(), worker.get_full_profit())

"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f"Текущая скорость {self.name} составляет {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость городского автомобиля {self.name} составляет {self.speed} км/ч")

        if int(self.speed) > 40:
            return f"Текущая скорость {self.name} превышает разрешенную скорость передвижения"
        else:
            return f"Текущая скорость {self.name} не превышает допустимую скорость движения"

    def police(self):
        if self.is_police:
            return f"{self.name} яляется полицейской машиной"
        else:
            return f"{self.name} не яляется полицейской машиной"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} яляется полицейской машиной"
        else:
            return f"{self.name} не яляется полицейской машиной"


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость городского автомобиля {self.name} составляет {self.speed} км/ч")

        if int(self.speed) > 60:
            return f"Текущая скорость {self.name} превышает разрешенную скорость передвижения"
        else:
            return f"Текущая скорость {self.name} не превышает допустимую скорость движения"

    def police(self):
        if self.is_police:
            return f"{self.name} яляется полицейской машиной"
        else:
            return f"{self.name} не яляется полицейской машиной"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} яляется полицейской машиной"
        else:
            return f"{self.name} не яляется полицейской машиной"


lada_sedan = TownCar("80 ", "Баклажан ", "Лада", False)
porsche = SportCar("270 ", "Серебристый ", "911 Turbo", False)
gazel = WorkCar("39 ", "Жёлтая ", "Газель", False)
uazik = PoliceCar("60 ", "Болотный ", "УАЗ", True)

print(lada_sedan.name, lada_sedan.color, lada_sedan.speed, lada_sedan.is_police)
print(porsche.name, porsche.color, porsche.speed, porsche.is_police)
print(uazik.name, uazik.color, uazik.speed, uazik.is_police)
print(gazel.name, gazel.color, gazel.speed, gazel.is_police)
print(f"Является ли {uazik.name} полицейской машиной? {uazik.is_police}")
print(gazel.show_speed())
print(lada_sedan.show_speed())

"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""

class Stationery:
    atr_title = "Title"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандашом")


class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером")

stat = Stationery()
stat.draw()
my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()