# Задание 1
# Написать программу «справочник».Создать два списка
# целых. Один список хранит идентификационные коды,
# второй — телефонные номера. Реализовать меню для
# пользователя:
# ■ Отсортировать по идентификационным кодам;
# ■ Отсортировать по номерам телефона;
# ■ Вывести список пользователей с кодами и телефонами;
# ■ Выход.

id_codes = [102, 101, 104, 103]
phone_numbers = ["+49 975 4859 940", "+1 987 647", "+375 095 594 544", "+7 988 163 70 76"]

def display_users():
    print("\nСписок пользователей:")
    for i in range(len(id_codes)):
        print(f"ID: {id_codes[i]}, Телефон: {phone_numbers[i]}")

def main():
    while True:
        print("\nМеню:")
        print("1. Вывести список пользователей с кодами и телефонами")
        print("2. Отсортировать по идентификационным кодам")
        print("3. Отсортировать по номерам телефона")
        print("4. Выход")

        choice = input("Выберите опцию (1-4): ")

        if choice == '1':
            display_users()
        elif choice == '2':
            id_codes.sort()
            print("Список отсортирован по идентификационным кодам.")
        elif choice == '3':
            phone_numbers.sort()
            print("Список отсортирован по номерам телефонов.")
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()

#    задание 2: Написать программу «книги». Создать два списка
# годы выпуска. Реализовать меню для пользователя:
# ■ Отсортировать по названию книг;
# ■ Отсортировать по годам выпуска;
# ■ Вывести список книг с названиями и годами выпуска;
# ■ Выход;

book_titles = ["Война и мир", "1984", "Гарри Поттер", "Мастер и Маргарита"]
release_years = [1869, 1949, 1997, 1967]

def display_books():
    print("\nСписок книг:")
    for i in range(len(book_titles)):
        print(f"Название: {book_titles[i]}, Год выпуска: {release_years[i]}")

def sort_by_title():
    global book_titles, release_years
    combined = list(zip(book_titles, release_years))
    combined.sort()
    book_titles, release_years = zip(*combined)
    print("Список отсортирован по названиям книг.")

def sort_by_year():
    global book_titles, release_years
    combined = list(zip(release_years, book_titles))
    combined.sort()
    release_years, book_titles = zip(*combined)
    print("Список отсортирован по годам выпуска.")

def main():
    while True:
        print("\nМеню:")
        print("1. Отсортировать по названиям книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список книг с названиями и годами выпуска")
        print("4. Выход")

        choice = input("Выберите опцию (1-4): ")

        if choice == '1':
            sort_by_title()
        elif choice == '2':
            sort_by_year()
        elif choice == '3':
            display_books()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
    