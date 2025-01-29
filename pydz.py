# Задание 1: Простое наследование
# Создайте базовый класс Vehicle со
# следующими атрибутами и методами:
# Атрибут brand (марка транспортного
# средства).
# Атрибут speed (скорость транспортного
# средства).
# Метод move(), который выводит на экран:
# "Vehicle is moving at [speed] km/h".
# Создайте подкласс Car, который наследует от
# класса Vehicle:
# Переопределите метод move() так, чтобы он
# выводил на экран: "Car is driving at [speed]
# km/h".
# Добавьте метод honk(), который выводит на
# экран: "Car honks!".
# Создайте подкласс Bicycle, который
# наследует от класса Vehicle:
# Переопределите метод move() так, чтобы он
# выводил на экран: "Bicycle is riding at
# [speed] km/h".
# Добавьте метод ring_bell(), который выводит
# на экран: "Bicycle bell rings!".
# Создайте объекты каждого класса и
# продемонстрируйте их работу:
# Создайте объект класса Vehicle с маркой
# "Generic" и скоростью 60.
# Создайте объект класса Car с маркой
# "Toyota" и скоростью 120.
# Создайте объект класса Bicycle с маркой
# "Trek" и скоростью 20.
# Вызовите методы move(), honk() (для Car) и
# ring_bell() (для Bicycle).

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Vehicle is moving at {self.speed} km/h")

class Car(Vehicle):
    def move(self):
        print(f"Car is driving at {self.speed} km/h")

    def honk(self):
        print("Car honks!")

class Bicycle(Vehicle):
    def move(self):
        print(f"Bicycle is riding at {self.speed} km/h")

    def ring_bell(self):
        print("Bicycle bell rings!")

vehicle = Vehicle("Generic", 60)
car = Car("Toyota", 120)
bicycle = Bicycle("Trek", 20)

vehicle.move()
car.move()
car.honk()
bicycle.move()
bicycle.ring_bell()

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Vehicle is moving at {self.speed} km/h")

class Car(Vehicle):
    def move(self):
        print(f"Car is driving at {self.speed} km/h")

    def honk(self):
        print("Car honks!")

class Bicycle(Vehicle):
    def move(self):
        print(f"Bicycle is riding at {self.speed} km/h")

    def ring_bell(self):
        print("Bicycle bell rings!")

vehicle = Vehicle("Generic", 60)
car = Car("Toyota", 120)
bicycle = Bicycle("Trek", 20)

vehicle.move()
car.move()
car.honk()
bicycle.move()
bicycle.ring_bell()

   
# Задание 2: Множественное наследование
# Создайте базовый класс Engine со
# следующими атрибутами и методами:
# Атрибут engine_type (тип двигателя,
# например,
# "Petrol"
# ,
# "Electric").
# Метод start_engine(), который выводит на
# экран: "Engine started: [engine_type]".
# Создайте базовый класс Seats со
# следующими атрибутами и методами:
# Атрибут seat_count (количество мест).
# Метод adjust_seats(), который выводит на
# экран: "Adjusting [seat_count] seats".
# Создайте подкласс ElectricCar, который
# наследует от классов Car и Engine:
# Убедитесь, что конструктор класса ElectricCar
# принимает параметры для всех атрибутов
# (brand, speed, engine_type, seat_count).
# Переопределите метод move() так, чтобы он
# выводил на экран: "Electric car is driving
# silently at [speed] km/h".
# Добавьте метод charge(), который выводит на
# экран: "Electric car is charging".
# Создайте объект класса ElectricCar и
# продемонстрируйте его работу:
# Создайте объект с маркой "Tesla"
# , скоростью
# 150, типом двигателя "Electric" и количеством
# мест 5.
# Вызовите методы move(), start_engine(),
# adjust_seats(), honk() и charge() сделай простым кодом


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start_engine(self):
        print(f"Engine started: {self.engine_type}")

class Seats:
    def __init__(self, seat_count):
        self.seat_count = seat_count

    def adjust_seats(self):
        print(f"Adjusting {self.seat_count} seats")


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Car is driving at {self.speed} km/h")

    def honk(self):
        print("Car honks!")


class ElectricCar(Car, Engine, Seats):
    def __init__(self, brand, speed, engine_type, seat_count):
        Car.__init__(self, brand, speed)
        Engine.__init__(self, engine_type)
        Seats.__init__(self, seat_count)

    def move(self):
        print(f"Electric car is driving silently at {self.speed} km/h")

    def charge(self):
        print("Electric car is charging")

electric_car = ElectricCar("Tesla", 150, "Electric", 5)

electric_car.move()
electric_car.start_engine()
electric_car.adjust_seats()
electric_car.honk()
electric_car.charge()

