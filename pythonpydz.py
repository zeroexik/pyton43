# Задание 1
# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# ■ Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius - value)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value
            return self
        return NotImplemented

    def __str__(self):
        return f"Circle with radius: {self.radius}"

circle1 = Circle(5)
circle2 = Circle(10)

print(circle1 == circle2)
print(circle1 < circle2)
print(circle1 <= circle2)
print(circle1 > circle2)
print(circle1 >= circle2)

circle3 = circle1 + 3
print(circle3)

circle1 -= 2
print(circle1)

# задание 2
# Создайте класс Complex (комплексное число).Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).

class Complex
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real**2 + other.imag**2
            if denominator == 0:
                raise ZeroDivisionError("Деление на ноль")
            real_part = (self.real * other.real + self.imag * other.imag) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag) / denominator
            return Complex(real_part, imag_part)
        return NotImplemented

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(2, 3)
c2 = Complex(1, 4)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

# Задание 3
# Вам необходимо создать класс Airplane (самолет). с помощью перегрузки операторов реализовать:■ Проверка на равенство типов самолетов (операция
# = =);
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
# < <= >=).

class Airplane:
    def __init__(self, model, max_passengers):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = 0

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.model == other.model
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            new_passengers = self.current_passengers + value
            if new_passengers <= self.max_passengers:
                self.current_passengers = new_passengers
                return self
            else:
                raise ValueError("Превышено максимальное количество пассажиров")
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, int):
            new_passengers = self.current_passengers - value
            if new_passengers >= 0:
                self.current_passengers = new_passengers
                return self
            else:
                raise ValueError("Количество пассажиров не может быть отрицательным")
        return NotImplemented

    def __iadd__(self, value):
        return self.__add__(value)

    def __isub__(self, value):
        return self.__sub__(value)

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented

    def __str__(self):
        return f"Самолет {self.model}: {self.current_passengers}/{self.max_passengers} пассажиров"

plane1 = Airplane("Boeing 737", 180)
plane2 = Airplane("Airbus A320", 150)

print(plane1 == plane2)
print(plane1 < plane2)
print(plane1 > plane2)

plane1 += 50
print(plane1)

plane1 += 130

# Задание 4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        return NotImplemented

    def __str__(self):
        return f"Квартира: площадь {self.area} м², цена {self.price} руб."

flat1 = Flat(50, 3000000)
flat2 = Flat(50, 3500000)
flat3 = Flat(70, 4000000)

print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 < flat2)
print(flat2 > flat3)

print(flat1)
print(flat3)

