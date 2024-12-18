class Car:

    default_color = "black"
    default_model = "sedan"

    def __init__(self, color=None, model=None):
        self.color = color
        self.model = model 
        self.color = color if color is not None else Car.default_color
        self.model = model if model is not None else Car.default_model

car1 = Car(color = "red", model = "SUV")
car2 = Car()

print(f"Car 1 = Color:{car1.color}, Model 1 = Model{car1.model}")
print(f"Car 2 = Color:{car2.color}, Model 2 = Model{car2.model}")


class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


sum_result = MathOperations.add(5, 3)
multiply_result = MathOperations.multiply(5, 3)

print(f"Сумма: {sum_result}")
print(f"Произведение: {multiply_result}")

math_ops = MathOperations()

sum_result_obj = math_ops.add(10, 4)
multiply_result_obj = math_ops.multiply(10, 4)

print(f"Сумма через объект: {sum_result_obj}")
print(f"Произведение через объект: {multiply_result_obj}")



class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):

        if isinstance(other, Vector):

            summed_values = [a + b for a, b in zip(self.values, other.values)]
            return Vector(summed_values)
        return NotImplemented

    def __mul__(self, other):

        if isinstance(other, Vector):

            dot_product = sum(a * b for a, b in zip(self.values, other.values))
            return dot_product
        return NotImplemented

vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])

result_add = vector1 + vector2
print(f"Сумма векторов: {result_add.values}")

result_mul = vector1 * vector2
print(f"Скалярное произведение: {result_mul}")




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __contains__(self, item):
        return item in ['name', 'age']

person = Person("Alice", 30)

has_name = 'name' in person
has_id = 'id' in person

print(f"Содержит 'name': {has_name}")
print(f"Содержит 'id': {has_id}")