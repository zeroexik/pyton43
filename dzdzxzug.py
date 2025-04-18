# Задание 1
# Создайте класс, содержащий набор целых чисел.
# -
# ональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

class IntegerSet:
    def __init__(self):
        self.numbers = set()

    def add(self, number):
        if isinstance(number, int):
            self.numbers.add(number)
        else:
            raise ValueError("Only integers can be added.")

    def sum(self):
        return sum(self.numbers)

    def average(self):
        if not self.numbers:
            return 0
        return self.sum() / len(self.numbers)

    def maximum(self):
        if not self.numbers:
            return None
        return max(self.numbers)

    def minimum(self):
        if not self.numbers:
            return None
        return min(self.numbers)

    def __str__(self):
        return f"IntegerSet({self.numbers})"

        import unittest

class TestIntegerSet(unittest.TestCase):

    def setUp(self):
        """Создаем экземпляр IntegerSet для тестов."""
        self.integer_set = IntegerSet()
    
    def test_add_integer(self):
        """Тестируем добавление целого числа."""
        self.integer_set.add(5)
        self.assertIn(5, self.integer_set.numbers)

    def test_add_non_integer(self):
        """Тестируем добавление нецелого числа."""
        with self.assertRaises(ValueError):
            self.integer_set.add(3.14)

    def test_sum(self):
        """Тестируем сумму элементов набора."""
        self.integer_set.add(1)
        self.integer_set.add(2)
        self.integer_set.add(3)
        self.assertEqual(self.integer_set.sum(), 6)

    def test_average(self):
        """Тестируем среднее арифметическое элементов набора."""
        self.integer_set.add(1)
        self.integer_set.add(2)
        self.integer_set.add(3)
        self.assertEqual(self.integer_set.average(), 2.0)

    def test_maximum(self):
        """Тестируем нахождение максимума."""
        self.integer_set.add(1)
        self.integer_set.add(2)
        self.integer_set.add(3)
        self.assertEqual(self.integer_set.maximum(), 3)

    def test_minimum(self):
        """Тестируем нахождение минимума."""
        self.integer_set.add(1)
        self.integer_set.add(2)
        self.integer_set.add(3)
        self.assertEqual(self.integer_set.minimum(), 1)

    def test_empty_average(self):
        """Тестируем среднее арифметическое для пустого набора."""
        self.assertEqual(self.integer_set.average(), 0)

    def test_empty_maximum_and_minimum(self):
        """Тестируем максимум и минимум для пустого набора."""
        self.assertIsNone(self.integer_set.maximum())
        self.assertIsNone(self.integer_set.minimum())

if __name__ == '__main__':
    unittest.main()

#     Задание 2
# Создайте класс для числа. В классе должна быть реализована следующая функциональность:
# ■ Запись и чтение значения.
# ■ Перевод числа в восьмеричную систему исчисления.
# ■ Перевод числа в шестнадцатеричную систему исчисления.
# ■ Перевод числа в двоичную систему исчисления.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest)

class Number:
    def __init__(self, value=0):
        self.value = value

    def set_value(self, value):
        if isinstance(value, (int, float)):
            self.value = value
        else:
            raise ValueError("Value must be an integer or float.")

    def get_value(self):
        return self.value

    def to_octal(self):
        return oct(int(self.value))

    def to_hexadecimal(self):
        return hex(int(self.value))

    def to_binary(self):
        return bin(int(self.value))

    def __str__(self):
        return str(self.value)

        import unittest

class TestNumber(unittest.TestCase):

    def setUp(self):
        """Создаем экземпляр Number для тестов."""
        self.number = Number(10)

    def test_set_value(self):
        """Тестируем установку значения."""
        self.number.set_value(20)
        self.assertEqual(self.number.get_value(), 20)

    def test_get_value(self):
        """Тестируем получение значения."""
        self.assertEqual(self.number.get_value(), 10)

    def test_set_invalid_value(self):
        """Тестируем установку недопустимого значения."""
        with self.assertRaises(ValueError):
            self.number.set_value("string")

    def test_to_octal(self):
        """Тестируем перевод в восьмеричную систему."""
        self.assertEqual(self.number.to_octal(), '0o12')

    def test_to_hexadecimal(self):
        """Тестируем перевод в шестнадцатеричную систему."""
        self.assertEqual(self.number.to_hexadecimal(), '0xa')

    def test_to_binary(self):
        """Тестируем перевод в двоичную систему."""
        self.assertEqual(self.number.to_binary(), '0b1010')

if __name__ == '__main__':
    unittest.main()