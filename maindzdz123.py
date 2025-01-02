# Задание 1
# Есть четыре списка целых. Необходимо их объединить
# в пятом списке. Полученный результат в зависимости от
# выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием линейного поиска.

def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

list1 = list(map(int, input("Введите элементы первого списка через пробел: ").split()))
list2 = list(map(int, input("Введите элементы второго списка через пробел: ").split()))
list3 = list(map(int, input("Введите элементы третьего списка через пробел: ").split()))
list4 = list(map(int, input("Введите элементы четвертого списка через пробел: ").split()))

combined_list = list1 + list2 + list3 + list4

sort_order = input("Введите 'asc' для сортировки по возрастанию или 'desc' для сортировки по убыванию: ")
if sort_order == 'asc':
    combined_list.sort()
elif sort_order == 'desc':
    combined_list.sort(reverse=True)
else:
    print("Некорректный ввод, сортировка не будет выполнена.")

print("Отсортированный список:", combined_list)

target_value = int(input("Введите значение для поиска: "))

index = linear_search(combined_list, target_value)

if index != -1:
    print(f"Значение {target_value} найдено на индексе {index}.")
else:
    print(f"Значение {target_value} не найдено.")

# Задание 2
# Есть четыре списка целых. Необходимо объединить
# в пятом списке только те элементы, которые уникальны
# для каждого списка. Полученный результат в зависимости
# от выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием бинарного поиска.


def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid 
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

list1 = list(map(int, input("Введите элементы первого списка через пробел: ").split()))
list2 = list(map(int, input("Введите элементы второго списка через пробел: ").split()))
list3 = list(map(int, input("Введите элементы третьего списка через пробел: ").split()))
list4 = list(map(int, input("Введите элементы четвертого списка через пробел: ").split()))

unique_elements = set(list1) | set(list2) | set(list3) | set(list4)

unique_list = list(unique_elements)

sort_order = input("Введите 'asc' для сортировки по возрастанию или 'desc' для сортировки по убыванию: ")
if sort_order == 'asc':
    unique_list.sort()
elif sort_order == 'desc':
    unique_list.sort(reverse=True)
else:
    print("Некорректный ввод, сортировка не будет выполнена.")

print("Отсортированный список уникальных элементов:", unique_list)

target_value = int(input("Введите значение для поиска: "))

index = binary_search(unique_list, target_value)

if index != -1:
    print(f"Значение {target_value} найдено на индексе {index}.")
else:
    print(f"Значение {target_value} не найдено.")