# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы
# обоих списков;
# ■ Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы
# общие для двух списков;
# ■ Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.
 
import random

list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]

print(f"Первый список: {list1}")
print(f"Второй список: {list2}")

combined = list1 + list2
print("\n1. Все элементы обоих списков:")
print(combined)

unique_combined = list(set(list1 + list2))
print("\n2. Элементы без повторений:")
print(unique_combined)

common_elements = list(set(list1) & set(list2))
print("\n3. Общие элементы:")
print(common_elements)

unique_list1 = [x for x in list1 if x not in list2]
unique_list2 = [x for x in list2 if x not in list1]
unique_for_each = unique_list1 + unique_list2
print("\n4. Уникальные элементы каждого списка:")
print(unique_for_each)

min_max_list1 = [min(list1), max(list1)]
min_max_list2 = [min(list2), max(list2)]
min_max_values = min_max_list1 + min_max_list2
print("\n5. Минимальные и максимальные значения:")
print(min_max_values)