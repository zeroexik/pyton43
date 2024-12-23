# задание 1
# Есть четыре списка целых. Необходимо их объединить
# в пятом списке. Полученный результат в зависимости от
# выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием линейного поиска.

list1 = [5, 2, 9, 1]
list2 = [3, 8, 6, 4]
list3 = [7, 0, 12, 10]
list4 = [15, 14, 13, 11]

combined_list = list1 + list2 + list3 + list4

def linear_search(arr, target):

    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def main():

    sort_order = input("Выберите порядок сортировки (1 - возрастание, 2 - убывание): ")
    
    if sort_order == '1':
        combined_list.sort()
        print("Список отсортирован по возрастанию:", combined_list)
    elif sort_order == '2':
        combined_list.sort(reverse = True)
        print("Список отсортирован по убыванию:", combined_list)
    else:
        print("Неверный выбор. Программа завершена.")
        return
    
    target = int(input("Введите значение для поиска: "))
    result = linear_search(combined_list, target)

    if result != -1:
        print(f"Значение {target} найдено на индексе {result}.")
    else:
        print(f"Значение {target} не найдено в списке.")

if __name__ == "__main__":
    main()

#     Задание 2
# Есть четыре списка целых. Необходимо объединить
# в пятом списке только те элементы, которые уникальны
# для каждого списка. Полученный результат в зависимости
# от выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием бинарного поиска.

list6 = [1, 3, 7, 2]
list7 = [3, 9, 3, 9]
list8 = [4, 6, 0, 4]
list9 = [9, 5, 3, 1]

def unique_elements(*lists):
    all_elements = list6 + list7 + list8 + list9
    unique = [item for item in all_elements if all_elements.count(item) == 1]
    return unique

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():

    unique_list = unique_elements(list6, list7, list8, list9)

    sort_order = input("Выберите порядок сортировки (1 - возрастание, 2 - убывание): ")
    
    if sort_order == '1':
        unique_list.sort()
        print("Список отсортирован по возрастанию:", unique_list)
    elif sort_order == '2':
        unique_list.sort(reverse = True)
        print("Список отсортирован по убыванию:", unique_list)
    else:
        print("Неверный выбор. Программа завершена.")
        return

    target = int(input("Введите значение для поиска: "))
    result = binary_search(unique_list, target)
    
    if result != -1:
        print(f"Значение {target} найдено на индексе {result}.")
    else:
        print(f"Значение {target} не найдено в списке.")

if __name__ == "__main__":
    main()