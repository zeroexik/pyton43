# Создайте модуль "shopping_list.py", который будет реализовывать функционал списка покупок.
# Внутри должны быть функции add_item (для добавления в список, например «Хлеб, 2», где «Хлеб» 
#                                      - ключ, «2» - значение, которой по умолчанию в функции равно 0),
# remove_item для удаления покупки из списка, edit_quantity для редактирования количества 
# (то есть значения), view_list для отображения всего списка (то есть словаря). Создайте новый файл,
# куда вы импортируете созданный модуль и отобразите работу каждый из этих функций. Например,
# пользователь сначала добавил в список три покупки: Хлеб – 2, Молоко, Яйца – 10, далее посмотрел этот 
# список; потом он понял, что не хочет молоко, удалил его, посмотрел измененный список; потом решил, 
# что 10 яиц – это много, и поменял их количество на 7 и в конце решил посмотреть на итоговый список.

shopping_list = {}

def add_item(item, quantity=0):
    shopping_list[item] = quantity
    print(f"Добавлено: {item} - {quantity}")

def remove_item(item):
    if item in shopping_list:
        del shopping_list[item]
        print(f"Удалено: {item}")
    else:
        print(f"Товар '{item}' не найден в списке.")

def edit_quantity(item, quantity):
    if item in shopping_list:
        shopping_list[item] = quantity
        print(f"Изменено: {item} - {quantity}")
    else:
        print(f"Товар '{item}' не найден в списке.")

def view_list():
    print("Список покупок:")
    for item, quantity in shopping_list.items():
        print(f" - {item}: {quantity}")


from shopping_list import add_item, remove_item, edit_quantity, view_list

add_item("Хлеб", 2)
add_item("Молоко")
add_item("Яйца", 10)

view_list()

remove_item("Молоко")

view_list()

edit_quantity("Яйца", 7)

view_list()