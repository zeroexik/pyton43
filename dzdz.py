# Задание 1: Декораторы
# Создайте декоратор timer, который измеряет время выполнения функции.
# Декоратор должен выводить время, затраченное на выполнение функции.
# Пример использования:

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции: {end_time - start_time:.6f} секунд")
        return result
    return wrapper

@timer
def example_function(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

print(example_function(1000000))

# 2) Создайте декоратор retry, который повторяет выполнение функции
# в случае возникновения исключения.
# Декоратор должен принимать параметр max_retries, который указывает
# максимальное количество попыток.
# Если после max_retries попыток функция не выполнится успешно,
# декоратор должен выбросить исключение.
# Пример использования:

def retry(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Попытка {attempt + 1} не удалась: {e}")
                    if attempt == max_retries - 1:
                        raise
        return wrapper
    return decorator

@retry(max_retries=3)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Ошибка выполнения функции")
    return "Успех!"

try:
    result = unreliable_function()
    print(result)
except Exception as e:
    print(f"Функция завершилась с ошибкой: {e}")

# 3) Задание : Замыкания
# Создайте функцию counter, которая возвращает функцию,
# подсчитывающую количество вызовов.
# Пример использования

def counter_func():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

my_counter = counter_func()

print(my_counter())
print(my_counter())
print(my_counter())

# 4) Создайте функцию make_multiplier, которая принимает число и
# возвращает функцию, умножающую на это число.

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))