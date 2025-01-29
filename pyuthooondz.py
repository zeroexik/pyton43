# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# Спомощью механизма наследования, реализуйте класс
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке). сделай простым кодом
# Каждый из классов должен содержать необходимые
# для работы методы

class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power
    def show_info(self):
        return f"Бренд: {self.brand}, Модель: {self.model}, Мощность: {self.power} Вт"

class Blender(Device):
    def __init__(self, brand, model, power, capacity):
        super().__init__(brand, model, power)
        self.capacity = capacity

    def blend(self):
        return f"Блендер {self.brand} {self.model} сейчас смешивает..."

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}, Вместимость: {self.capacity} Л"

class MeatGrinder(Device):
    def __init__(self, brand, model, power, grinding_speed):
        super().__init__(brand, model, power)
        self.grinding_speed = grinding_speed

    def grind(self):
        return f"Мясорубка {self.brand} {self.model} сейчас перемалывает мясо..."

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}, Скорость перемалывания: {self.grinding_speed} кг/мин"

if __name__ == "__main__":
    blender = Blender("BrandA", "ModelB", 500, 1.5)
    meat_grinder = MeatGrinder("BrandC", "ModelD", 800, 3)

    print(blender.show_info())
    print(blender.blend())

    print(meat_grinder.show_info())
    print(meat_grinder.grind())

# Задание 2
# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы сделай простым кодом

class Ship:
    def __init__(self, name, tonnage, speed):
        self.name = name
        self.tonnage = tonnage
        self.speed = speed

    def show_info(self):
        return f"Корабль: {self.name}, Водоизмещение: {self.tonnage} тонн, Скорость: {self.speed} узлов"

class Frigate(Ship):
    def __init__(self, name, tonnage, speed, weapon_system):
        super().__init__(name, tonnage, speed)
        self.weapon_system = weapon_system

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}, Оружейная система: {self.weapon_system}"

    def engage(self):
        return f"Фрегат {self.name} вступает в бой!"

class Destroyer(Ship):
    def __init__(self, name, tonnage, speed, missile_system):
        super().__init__(name, tonnage, speed)
        self.missile_system = missile_system

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}, Ракетная система: {self.missile_system}"

    def patrol(self):
        return f"Эсминец {self.name} патрулирует территорию."

class Cruiser(Ship):
    def __init__(self, name, tonnage, speed, armor):
        super().__init__(name, tonnage, speed)
        self.armor = armor

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}, Бронирование: {self.armor}"

    def escort(self):
        return f"Крейсер {self.name} сопровождает союзные силы."

if __name__ == "__main__":
    frigate = Frigate("Фрегат 1", 3000, 30, "Зенитные ракеты")
    destroyer = Destroyer("Эсминец 1", 8000, 28, "Корабельные ракеты")
    cruiser = Cruiser("Крейсер 1", 10000, 25, "Толстая броня")

    print(frigate.show_info())
    print(frigate.engage())

    print(destroyer.show_info())
    print(destroyer.patrol())

    print(cruiser.show_info())
    print(cruiser.escort())

#     Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки
# и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.

class Money:
    def __init__(self, dollars=0, cents=0):
        """Инициализация с целой и дробной частями"""
        self.dollars = dollars
        self.cents = cents
        self.normalize()

    def normalize(self):
        """Проверка и нормализация значений"""
        if self.cents < 0:
            raise ValueError("Cents cannot be negative.")
      
        if self.cents >= 100:
            additional_dollars = self.cents // 100
            self.dollars += additional_dollars
            self.cents = self.cents % 100

    def set_money(self, dollars, cents):
        """Установка значений для целой и дробной части"""
        self.dollars = dollars
        self.cents = cents
        self.normalize()

    def total_amount(self):
        """Возвращает общую сумму в виде строки"""
        return f"{self.dollars} dollars and {self.cents} cents"

    def __str__(self):
        """Строковое представление объекта"""
        return self.total_amount()

if __name__ == "__main__":
    money = Money(5, 150)
    print(money)

    money.set_money(3, 75)
    print(money)

    money.set_money(1, -10)