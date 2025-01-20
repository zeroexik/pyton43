# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# Спомощью механизма наследования, реализуйте класс CoffeeMachine(содержит информацию о кофемашине)
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые
# для работы методы

class Device:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def __str__(self):
        return f"{self.brand} (Мощность: {self.power} Вт)"


class CoffeeMachine(Device):
    def __init__(self, brand, power, water_capacity):
        super().__init__(brand, power)
        self.water_capacity = water_capacity

    def brew_coffee(self):
        return f"{self.brand} кофемашина готовит кофе."

    def __str__(self):
        return f"{super().__str__()}, Вместимость: {self.water_capacity} л"


class Blender(Device):
    def __init__(self, brand, power, capacity):
        super().__init__(brand, power)
        self.capacity = capacity

    def blend(self):
        return f"{self.brand} блендер смешивает ингредиенты."

    def __str__(self):
        return f"{super().__str__()}, Вместимость: {self.capacity} л"


class MeatGrinder(Device):
    def __init__(self, brand, power, grinding_speed):
        super().__init__(brand, power)
        self.grinding_speed = grinding_speed

    def grind(self):
        return f"{self.brand} мясорубка измельчает мясо."

    def __str__(self):
        return f"{super().__str__()}, Скорость измельчения: {self.grinding_speed} кг/мин"

coffee_machine = CoffeeMachine("DeLonghi", 1500, 1.2)
blender = Blender("Philips", 600, 1.5)
meat_grinder = MeatGrinder("Bosch", 800, 2.5)

print(coffee_machine)
print(coffee_machine.brew_coffee())

print(blender)
print(blender.blend())

print(meat_grinder)
print(meat_grinder.grind())

# Задание 2
# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы.

class Ship:
    def __init__(self, name, length, width, displacement):
        self.name = name
        self.length = length
        self.width = width
        self.displacement = displacement

    def __str__(self):
        return f"{self.name} (Длина: {self.length} м, Ширина: {self.width} м, Водоизмещение: {self.displacement} т)"

class Frigate(Ship):
    def __init__(self, name, length, width, displacement, armament):
        super().__init__(name, length, width, displacement)
        self.armament = armament

    def fire(self):
        return f"{self.name} стреляет с помощью {self.armament}."

    def __str__(self):
        return f"{super().__str__()}, Оружие: {self.armament}"

class Destroyer(Ship):
    def __init__(self, name, length, width, displacement, speed):
        super().__init__(name, length, width, displacement)
        self.speed = speed

    def engage(self):
        return f"{self.name} вступает в бой со скоростью {self.speed} узлов."

    def __str__(self):
        return f"{super().__str__()}, Скорость: {self.speed} узлов"

class Cruiser(Ship):
    def __init__(self, name, length, width, displacement, missile_system):
        super().__init__(name, length, width, displacement)
        self.missile_system = missile_system

    def launch_missile(self):
        return f"{self.name} запускает ракету с помощью {self.missile_system}."

    def __str__(self):
        return f"{super().__str__()}, Ракетная система: {self.missile_system}"

frigate = Frigate("Фрегат 'Адмирал Касатонов'", 130, 16, 4000, "пушка 76 мм")
destroyer = Destroyer("Эсминец 'Совершенны'", 150, 20, 8000, 30)
cruiser = Cruiser("Крейсер 'Москва'", 200, 22, 12000, "С-300")

print(frigate)
print(frigate.fire())

print(destroyer)
print(destroyer.engage())

print(cruiser) 
print(cruiser.launch_missile())

# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки
# и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей. 
 
class Money:
    def __init__(self, whole_part=0, fractional_part=0):
        self.whole_part = whole_part
        self.fractional_part = fractional_part

    def __str__(self):
        return f"{self.whole_part}.$ {self.fractional_part}¢"

    def set_whole_part(self, whole_part):
        self.whole_part = whole_part

    def set_fractional_part(self, fractional_part):
        if 0 <= fractional_part < 100:
            self.fractional_part = fractional_part
        else:
            raise ValueError("Дробная часть должна быть в диапазоне от 0 до 99.")

    def total_amount(self):
        return self.whole_part + self.fractional_part / 100

    def add(self, other):
        total_whole = self.whole_part + other.whole_part
        total_fractional = self.fractional_part + other.fractional_part
        if total_fractional >= 100:
            total_whole += total_fractional // 100
            total_fractional = total_fractional % 100
        return Money(total_whole, total_fractional)

money1 = Money(10, 50)
money2 = Money(5, 75)

print(money1)
print(money2)

total_money = money1.add(money2)
print(total_money)
print(f"Общая сумма: {total_money.total_amount()}$")