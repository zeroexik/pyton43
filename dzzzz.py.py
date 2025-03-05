# Задание 1
# Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса.

class House:
    def __init__(self):
        self.walls = None
        self.roof = None

    def __str__(self):
        return f"House with {self.walls} walls and a {self.roof} roof."
    
class HouseBuilder:
    def build_walls(self):
        raise NotImplementedError

    def build_roof(self):
        raise NotImplementedError

    def get_house(self):
        raise NotImplementedError

class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "brick"

    def build_roof(self):
        self.house.roof = "tile"

    def get_house(self):
        return self.house

class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_roof()

if __name__ == "__main__":
    builder = ConcreteHouseBuilder()
    director = Director(builder)
    director.construct_house()
    house = builder.get_house()
    print(house)

# Задание 2
# Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты. Классы различной пасты должны иметь следующие
# методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

from abc import ABC, abstractmethod

class Pasta(ABC):
    @abstractmethod
    def type(self):
    pass

    @abstractmethod
    def sauce(self):
    pass

    @abstractmethod
    def filling(self):
    pass

    @abstractmethod
    def additives(self):
    pass

class Spaghetti(Pasta):
    def type(self):
        return "Spaghetti"

    def sauce(self):
        return "Marinara"

    def filling(self):
        return "None"

    def additives(self):
        return "Parmesan cheese"

class Penne(Pasta):
    def type(self):
        return "Penne"

    def sauce(self):
        return "Alfredo"

    def filling(self):
        return "Chicken"

    def additives(self):
        return "Basil"

class Fettuccine(Pasta):
    def type(self):
        return "Fettuccine"

    def sauce(self):
        return "Carbonara"

    def filling(self):
        return "Pancetta"

    def additives(self):
        return "Black pepper"

if __name__ == "__main__":
    pastas = [Spaghetti(), Penne(), Fettuccine()]
    for pasta in pastas:
        print(f"Type: {pasta.type()}, Sauce: {pasta.sauce()}, Filling: {pasta.filling()}, Additives: {pasta.additives()}")

#         Задание 3
# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.

import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototypeA(Prototype):
    def __init__(self, attribute):
        self.attribute = attribute
    
    def __str__(self):
        return f"ConcretePrototypeA with attribute '{self.attribute}'"

class ConcretePrototypeB(Prototype):
    def __init__(self, attribute):
        self.attribute = attribute
    
    def __str__(self):
        return f"ConcretePrototypeB with attribute '{self.attribute}'"

if __name__ == "__main__":

    prototype_a = ConcretePrototypeA("A1")
    prototype_b = ConcretePrototypeB("B1")

    clone_a = prototype_a.clone()
    clone_b = prototype_b.clone()

    clone_a.attribute = "A2"
    clone_b.attribute = "B2"

    print(prototype_a)
    print(clone_a)
    print(prototype_b)
    print(clone_b)