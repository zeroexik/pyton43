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

def main():
    numbers = [] 

    while True:
        print("\nМеню:")
        print("1. Добавить новое число в список")
        print("2. Удалить все вхождения числа из списка")
        print("3. Показать содержимое списка")
        print("4. Проверить, есть ли значение в списке")
        print("5. Заменить значение в списке")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            num = float(input("Введите число для добавления: "))
            if num in numbers:
                print("Такое число уже существует в списке.")
            else:
                numbers.append(num)
                print(f"Число {num} добавлено в список.")

        elif choice == '2':
            num = float(input("Введите число для удаления: "))
            while num in numbers:
                numbers.remove(num)
            print(f"Все вхождения числа {num} удалены из списка.")

        elif choice == '3': 
            show_from_end = input("Показать список с конца? (да/нет): ").strip().lower()
            if show_from_end == 'да':
                print("Содержимое списка с конца:", numbers[::-1])
            else:
                print("Содержимое списка с начала:", numbers)

        elif choice == '4': 
            num = float(input("Введите число для проверки: "))
            if num in numbers:
                print("Число есть в списке.")
            else:
                print("Числа нет в списке.")

        elif choice == '5': 
            old_value = float(input("Введите число, которое хотите заменить: "))
            if old_value not in numbers:
                print("Число не найдено в списке.")
                continue
            
            new_value = float(input("Введите новое значение: "))
            replace_all = input("Заменить все вхождения? (да/нет): ").strip().lower()
            
            if replace_all == 'да':
                numbers = [new_value if x == old_value else x for x in numbers]
                print(f"Все вхождения {old_value} заменены на {new_value}.")
            else:
                for i in range(len(numbers)):
                    if numbers[i] == old_value:
                        numbers[i] = new_value
                        print(f"Первое вхождение {old_value} заменено на {new_value}.")
                        break

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

#     Задание 2
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
# помощью, которого пользователь может выбрать необходимую операцию. сделай код попроще

class StringStack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, string):
        if self.is_full():
            print("Стек полон. Нельзя добавить новую строку.")
        else:
            self.stack.append(string)
            print(f"Строка '{string}' добавлена в стек.")

    def pop(self):
        if self.is_empty():
            print("Стек пуст. Нельзя удалить строку.")
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def clear(self):
        self.stack.clear()
        print("Стек очищен.")

    def peek(self):
        if self.is_empty():
            print("Стек пуст. Нельзя получить значение.")
            return None
        return self.stack[-1]


def main():
    size = int(input("Введите размер стека: "))
    string_stack = StringStack(size)

    while True:
        print("\nМеню:")
        print("1. Поместить строку в стек")
        print("2. Вытолкнуть строку из стека")
        print("3. Подсчитать количество строк в стеке")
        print("4. Проверить пустой ли стек")
        print("5. Проверить полный ли стек")
        print("6. Очистить стек")
        print("7. Получить значение без выталкивания верхней строки")
        print("8. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            string = input("Введите строку: ")
            string_stack.push(string)
        elif choice == '2':
            removed_string = string_stack.pop()
            if removed_string is not None:
                print(f"Удалена строка: '{removed_string}'")
        elif choice == '3':
            print(f"Количество строк в стеке: {string_stack.count()}")
        elif choice == '4':
            print("Стек пуст." if string_stack.is_empty() else "Стек не пуст.")
        elif choice == '5':
            print("Стек полон." if string_stack.is_full() else "Стек не полон.")
        elif choice == '6':
            string_stack.clear()
        elif choice == '7':
            peeked_string = string_stack.peek()
            if peeked_string is not None:
                print(f"Верхняя строка в стеке: '{peeked_string}'")
        elif choice == '8':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()