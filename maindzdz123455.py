# Задание 1
# Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.

def main():
    basketball_players = {}
    
    while True:
        print("\nМеню:")
        print("1 Добавить баскетболиста")
        print("2 Удалить баскетболиста")
        print("3 Найти баскетболиста")
        print("4 Заменить данные баскетболиста")
        print("5 Показать всех баскетболистов")
        print("6 Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите ФИО баскетболиста:")
            height = input("Введите рост (см):")
            basketball_players[name] = height
            print(f"Баскетболист {name} добавлен")

        elif choice == "2":
            name = input("Введите ФИО баскетболиста для удаления:")
            if name in basketball_players:
                del basketball_players[name]
                print(f"Баскетболист {name} удален")
            else:
                print("Баскетболист не найден")

        elif choice == "3":
            name = input("Введите ФИО баскетболиста для поиска:")
            if name in basketball_players:
                print(f"{name}: рост {basketball_players[name]} см")
            else:
                print("Баскетболист не найден")

        elif choice == "4":
            name = input("Введите ФИО баскетболиста для замены данных:")
            if name in basketball_players:
                new_height = input("Введите новый рост (см):")
                basketball_players[name] = new_height
                print(f"Данные баскетболиста {name} обновлены")
            else:
                print("Баскетболист не найден")

        elif choice == "5":
            if not basketball_players:
                print("Нет данных о баскетболистах")
            else:
                print("Список баскетболистов:")
                for player, height in basketball_players.items():
                    print(f"{player}: рост {height} см")

        elif choice == "6":
            print("Выход из программы")
            break

        else:
            print("Неверный выбор. Попробуйте снова")

if __name__ == "__main__":
    main()

#     Задание 2
# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.

def display_menu():
    print("\n--- Англо-Французский Словарь ---")
    print("1. Добавить слово")
    print("2. Удалить слово")
    print("3. Найти перевод")
    print("4. Заменить перевод")
    print("5. Показать весь словарь")
    print("6. Выход")

def add_word(dictionary):
    english_word = input("Введите английское слово: ")
    french_word = input("Введите перевод на французский: ")
    dictionary[english_word] = french_word
    print(f"Слово '{english_word}' добавлено с переводом '{french_word}'.")

def remove_word(dictionary):
    english_word = input("Введите английское слово для удаления: ")
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"Слово '{english_word}' удалено.")
    else:
        print(f"Слово '{english_word}' не найдено в словаре.")

def find_translation(dictionary):
    english_word = input("Введите английское слово для поиска перевода: ")
    translation = dictionary.get(english_word)
    if translation:
        print(f"Перевод '{english_word}' на французский: '{translation}'.")
    else:
        print(f"Перевод для слова '{english_word}' не найден.")

def replace_translation(dictionary):
    english_word = input("Введите английское слово для замены перевода: ")
    if english_word in dictionary:
        new_translation = input("Введите новый перевод на французский: ")
        dictionary[english_word] = new_translation
        print(f"Перевод слова '{english_word}' изменён на '{new_translation}'.")
    else:
        print(f"Слово '{english_word}' не найдено в словаре.")

def show_dictionary(dictionary):
    if not dictionary:
        print("Словарь пуст.")
    else:
        print("\n--- Словарь ---")
        for english, french in dictionary.items():
            print(f"{english}: {french}")

def main():
    dictionary = {}
    while True:
        display_menu()
        choice = input("Выберите действие (1-6): ")
        
        if choice == '1':
            add_word(dictionary)
        elif choice == '2':
            remove_word(dictionary)
        elif choice == '3':
            find_translation(dictionary)
        elif choice == '4':
            replace_translation(dictionary)
        elif choice == '5':
            show_dictionary(dictionary)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()

#     Задание 3
# Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется
# реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения
# информации.

def display_menu():
    print("\n--- Фирма ---")
    print("1. Добавить сотрудника")
    print("2. Удалить сотрудника")
    print("3. Найти сотрудника")
    print("4. Заменить данные сотрудника")
    print("5. Показать всех сотрудников")
    print("6. Выход")

def add_employee(employees):
    fio = input("Введите ФИО сотрудника: ")
    phone = input("Введите телефон сотрудника: ")
    email = input("Введите рабочий email сотрудника: ")
    position = input("Введите должность сотрудника: ")
    office = input("Введите номер кабинета: ")
    skype = input("Введите skype сотрудника: ")
    employees[fio] = {
        'phone': phone,
        'email': email,
        'position': position,
        'office': office,
        'skype': skype
    }
    print(f"Сотрудник '{fio}' добавлен.")

def remove_employee(employees):
    fio = input("Введите ФИО сотрудника для удаления: ")
    if fio in employees:
        del employees[fio]
        print(f"Сотрудник '{fio}' удалён.")
    else:
        print("Сотрудник не найден.")

def find_employee(employees):
    fio = input("Введите ФИО сотрудника для поиска: ")
    employee = employees.get(fio)
    if employee:
        print(f"Информация о '{fio}': {employee}")
    else:
        print("Сотрудник не найден.")

def replace_employee_data(employees):
    fio = input("Введите ФИО сотрудника для замены данных: ")
    if fio in employees:
        print("Введите новые данные (оставьте пустым, чтобы не менять):")
        for field in employees[fio].keys():
            new_value = input(f"{field.capitalize()}: ")
            if new_value:
                employees[fio][field] = new_value
        print("Данные обновлены.")
    else:
        print("Сотрудник не найден.")

def show_all_employees(employees):
    if employees:
        print("\n--- Список сотрудников ---")
        for fio, info in employees.items():
            print(f"\nФИО: {fio}")
            for key, value in info.items():
                print(f"{key.capitalize()}: {value}")
    else:
        print("Список сотрудников пуст.")

def main():
    employees = {}
    while True:
        display_menu()
        choice = input("Выберите действие (1-6): ")
        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            remove_employee(employees)
        elif choice == '3':
            find_employee(employees)
        elif choice == '4':
            replace_employee_data(employees)
        elif choice == '5':
            show_all_employees(employees)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()

#     Задание 4
# Создайте программу «Книжная коллекция». Нужно
# хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для
# хранения информации.

def display_menu():
    print("\n--- Книжная коллекция ---")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу")
    print("4. Заменить данные о книге")
    print("5. Показать все книги")
    print("6. Выход")

def add_book(books):
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    genre = input("Введите жанр книги: ")
    year = input("Введите год выпуска: ")
    pages = input("Введите количество страниц: ")
    publisher = input("Введите издательство: ")

    books[title] = {
        'author': author,
        'genre': genre,
        'year': year,
        'pages': pages,
        'publisher': publisher
    }
    print(f"Книга '{title}' добавлена.")

def remove_book(books):
    title = input("Введите название книги для удаления: ")
    if title in books:
        del books[title]
        print(f"Книга '{title}' удалена.")
    else:
        print("Книга не найдена.")

def find_book(books):
    title = input("Введите название книги для поиска: ")
    book_info = books.get(title)
    if book_info:
        print(f"Информация о книге '{title}': {book_info}")
    else:
        print("Книга не найдена.")

def replace_book_data(books):
    title = input("Введите название книги для замены данных: ")
    if title in books:
        print("Введите новые данные (оставьте пустым, чтобы не менять):")
        for field in books[title].keys():
            new_value = input(f"{field.capitalize()}: ")
            if new_value:
                books[title][field] = new_value
        print("Данные книги обновлены.")
    else:
        print("Книга не найдена.")

def show_all_books(books):
    if books:
        print("\n--- Список книг ---")
        for title, info in books.items():
            print(f"\nНазвание: {title}")
            for key, value in info.items():
                print(f"{key.capitalize()}: {value}")
    else:
        print("Список книг пуст.")

def main():
    books = {}
    while True:
        display_menu()
        choice = input("Выберите действие (1-6): ")
        if choice == '1':
            add_book(books)
        elif choice == '2':
            remove_book(books)
        elif choice == '3':
            find_book(books)
        elif choice == '4':
            replace_book_data(books)
        elif choice == '5':
            show_all_books(books)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()