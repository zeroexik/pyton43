# Задание 1
# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

import json

def display_menu():
    print("\n--- Сотрудники ---")
    print("1. Добавить сотрудника")
    print("2. Редактировать данные сотрудника")
    print("3. Удалить сотрудника")
    print("4. Найти сотрудника по фамилии")
    print("5. Показать сотрудников по возрасту")
    print("6. Показать сотрудников по первой букве фамилии")
    print("7. Показать всех сотрудников")
    print("8. Сохранить сотрудников в файл")
    print("9. Выход")

def load_employees(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_employees(employees, filename):
    with open(filename, 'w') as f:
        json.dump(employees, f, ensure_ascii=False, indent=4)

def add_employee(employees):
    name = input("Введите ФИО сотрудника: ")
    age = input("Введите возраст сотрудника: ")
    employees[name] = {'age': age}
    print(f"Сотрудник '{name}' добавлен.")

def edit_employee(employees):
    name = input("Введите ФИО сотрудника для редактирования: ")
    if name in employees:
        age = input("Введите новый возраст сотрудника: ")
        employees[name]['age'] = age
        print(f"Данные сотрудника '{name}' обновлены.")
    else:
        print("Сотрудник не найден.")

def remove_employee(employees):
    name = input("Введите ФИО сотрудника для удаления: ")
    if name in employees:
        del employees[name]
        print(f"Сотрудник '{name}' удалён.")
    else:
        print("Сотрудник не найден.")

def find_employee(employees):
    name = input("Введите фамилию сотрудника для поиска: ")
    for employee_name, info in employees.items():
        if employee_name.lower().startswith(name.lower()):
            print(f"{employee_name}: {info['age']} лет")

def show_employees_by_age(employees):
    age = input("Введите возраст для поиска сотрудников: ")
    for name, info in employees.items():
        if info['age'] == age:
            print(f"{name}: {info['age']} лет")

def show_employees_by_letter(employees):
    letter = input("Введите букву для поиска сотрудников: ")
    for name, info in employees.items():
        if name.lower().startswith(letter.lower()):
            print(f"{name}: {info['age']} лет")

def show_all_employees(employees):
    if employees:
        print("\n--- Все сотрудники ---")
        for name, info in employees.items():
            print(f"{name}: {info['age']} лет")
    else:
        print("Список сотрудников пуст.")

def main():
    filename = input("Введите имя файла для загрузки сотрудников: ")
    employees = load_employees(filename)

    while True:
        display_menu()
        choice = input("Выберите действие (1-9): ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            edit_employee(employees)
        elif choice == '3':
            remove_employee(employees)
        elif choice == '4':
            find_employee(employees)
        elif choice == '5':
            show_employees_by_age(employees)
        elif choice == '6':
            show_employees_by_letter(employees)
        elif choice == '7':
            show_all_employees(employees)
        elif choice == '8':
            save_employees(employees, filename)
            print("Список сотрудников сохранён.")
        elif choice == '9':
            save_employees(employees, filename)
            print("Список сотрудников сохранён. Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 9.")

if __name__ == "__main__":
    main()