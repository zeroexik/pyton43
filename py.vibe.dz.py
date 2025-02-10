# Задание 1
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала
# или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все
# вхождения)
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.

def show_menu():
    print("\nменю")
    print("1. добавить число в список")
    print("2. удалить все вхождения числа")
    print("3. показать содержимое списка")
    print("4. проверить наличие числа в списке")
    print("5. заменить значение в списке")
    print("6. выйти")

def main():
    numbers = []
    while True:
        show_menu()
        choice = input("выберите пункт меню  (от 1 до 6)")
        
        if choice == '1':
            num = input("введите число для добавления ")
            if num in numbers:
                print("это число уже существует в списке")
            else:
                numbers.append(num)
                print(f"число {num} добавлено в список")
        
        elif choice == '2':
            num = input("введите число для удаления")
            count = numbers.count(num)
            if count > 0:
                numbers = [x for x in numbers if x != num]
                print(f"все вхождения числа {num} удалены из списка")
            else:
                print("это число не найдено в списке")

        elif choice == '3':
            view_choice = input("показать список с начала (1), или с конца (2)? ")
            if view_choice == '1':
                print("cписок", numbers)
            elif view_choice == '2':
                print("список (обратный порядок)", list(reversed(numbers)))
            else:
                print("неверный выбор")
        
        elif choice == '4':
            num = input("введите число для проверки")
            if num in numbers:
                print(f"число {num} присутствует в списке")
            else:
                print(f"число {num} отсутствует в списке")
        
        elif choice == '5':
            old_value = input("введите значение для замены")
            if old_value not in numbers:
                print(f"число {old_value} не найдено в списке")
                continue
            new_value = input("введите новое значение: ")
            replace_all = input("заменить все вхождения? (да/нет): ").lower()
            if replace_all == 'y':
                numbers = [new_value if x == old_value else x for x in numbers]
                print(f"все вхождения числа {old_value} заменены на {new_value}.")
            else:
                for i in range(len(numbers)):
                    if numbers[i] == old_value:
                        numbers[i] = new_value
                        print(f"Первое вхождение числа {old_value} заменено на {new_value}.")
                        break

        elif choice == '6':
            print("выход из программы")
            break
        
        else:
            print("Неверный выбор, пожалуйста выберите пункт от 1 до 6.")

if __name__ == "__main__":
    main()

# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необходимую операцию

    class StringStack:
        def __init__(self, size):
            self.size = size
            self.stack = []
        
    def push(self, string):
        if self.is_full():
            print("стек полный, нельзя добавить строку")
        else:
            self.stack.append(string)
            print(f"строка '{string}' добавлена в стек")
    
    def pop(self):
        if self.is_empty():
            print("стек пустой, неььзя удалить строку")
            return None
        else:
            return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.size
    
    def clear(self):
        self.stack.clear()
        print("стек очищен")
    
    def peek(self):
        if self.is_empty():
            print("стек пуст")
            return None
        else:
            return self.stack[-1]

def show_menu():
    print("\nменю:")
    print("1. моместить строку в стек")
    print("2. вытолкнуть строку из стека")
    print("3. подсчитать количество строк в стеке")
    print("4. проверить, пуст ли стек")
    print("5. проверить, полный ли стек")
    print("6. очистить стек")
    print("7. получить верхнюю строку из стека без выталкивания")
    print("8. выход")

def main():
    stack_size = int(input("введите размер стека"))
    stack = StringStack(stack_size)

    while True:
        show_menu()
        choice = input("выберите пункт меню (от 1 до 8)")
        
        if choice == '1':
            string = input("введите строку для добавления")
            stack.push(string)
        elif choice == '2':
            removed_string = stack.pop()
            if removed_string:
                print(f"убраная строка'{removed_string}'")
        elif choice == '3':
            print(f"количиство строк в стеке{stack.count()}")
        elif choice == '4':
            print("стек пустой" if stack.is_empty() else "стек не пуст.")
        elif choice == '5':
            print("стек полный" if stack.is_full() else "стек не полный.")
        elif choice == '6':
            stack.clear()
        elif choice == '7':
            top_string = stack.peek()
            if top_string:
                print(f"верхняя строка в стеке'{top_string}'")
        elif choice == '8':
            print("выход из программы")
            break
        else:
            print("неверный выбор, пожалуйста, выберите пункт от 1 до 8")

if __name__ == "__main__":
    main()

#     Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.

class StringStack:
    def __init__(self):
        self.stack = []

    def push(self, string):
        self.stack.append(string)
        print(f"строка '{string}' добавлена в стек.")

    def pop(self):
        if self.is_empty():
            print("стек пуст, невозможно удалить строку")
            return None
        else:
            return self.stack.pop()

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack.clear()
        print("cтек очищен")

    def peek(self):
        if self.is_empty():
            print("cтек пуст")
            return None
        else:
            return self.stack[-1]

def show_menu():
    print("\nменю:")
    print("1. поместить строку в стек")
    print("2. вытолкнуть строку из стека")
    print("3. подсчитать количество строк в стеке")
    print("4. проверить, пуст ли стек")
    print("5. очистить стек")
    print("6. получить верхнюю строку из стека без выталкивания")
    print("7. выход")

def main():
    stack = StringStack()

    while True:
        show_menu()
        choice = input("выбери те пункт(от 1 до 7): ")

        if choice == '1':
            string = input("введите строку для добавления")
            stack.push(string)
        elif choice == '2':
            removed_string = stack.pop()
            if removed_string:
                print(f"убрана строка'{removed_string}'")
        elif choice == '3':
            print(f"количиство строк св стеке{stack.count()}")
        elif choice == '4':
            print("cтек пуст" if stack.is_empty() else "cтек не пуст")
        elif choice == '5':
            stack.clear()
        elif choice == '6':
            top_string = stack.peek()
            if top_string:
                print(f"верхняя строка в стеке'{top_string}'")
        elif choice == '7':
            print("выход из программы")
            break
        else:
            print("неверный выбор, Пожалуйста, выберите пункт от 1 до 7")

if __name__ == "__main__":
    main()