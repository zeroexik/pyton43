# Задание 1
# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицыв качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).

import pickle

class CountryCapitalManager:
    def __init__(self):
        self.data = {}

    def add_country(self, country, capital):
        self.data[country] = capital
        print(f"Добавлена страна: {country} с капиталом: {capital}")

    def remove_country(self, country):
        if country in self.data:
            del self.data[country]
            print(f"Удалена страна: {country}")
        else:
            print(f"Страна {country} не найдена!")

    def find_capital(self, country):
        return self.data.get(country, "Страна не найдена!")

    def edit_capital(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
            print(f"Столица страны {country} обновлена на: {new_capital}")
        else:
            print(f"Страна {country} не найдена!")

    def save_data(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)
            print("Данные сохранены.")

    def load_data(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
                print("Данные загружены.")
        except FileNotFoundError:
            print("Файл не найден!")

manager = CountryCapitalManager()
manager.add_country("Россия", "Москва")
manager.add_country("Франция", "Париж")

print(manager.find_capital("Россия"))
manager.edit_capital("Франция", "Лион")
print(manager.find_capital("Франция"))
manager.remove_country("Россия")
manager.save_data("countries.pkl")

new_manager = CountryCapitalManager()
new_manager.load_data("countries.pkl")
print(new_manager.find_capital("Франция"))

# Задание 2
# Есть некоторый словарь, который хранит названия
# музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
# альбомов в качестве значения. Необходимо реализовать:
# добавление данных, удаление данных, поиск данных,
# редактирование данных, сохранение и загрузку данных
# (используя упаковку и распаковку).

import pickle

class MusicGroupManager:
    def __init__(self):
        """Инициализация словаря для хранения групп и их альбомов."""
        self.data = {}

    def add_group(self, group, albums):
        """Добавление новой группы с альбомами."""
        self.data[group] = albums
        print(f"Добавлена группа: {group} с альбомами: {albums}")

    def remove_group(self, group):
        """Удаление группы и её альбомов."""
        if group in self.data:
            del self.data[group]
            print(f"Удалена группа: {group}")
        else:
            print(f"Группа {group} не найдена!")

    def find_albums(self, group):
        """Поиск альбомов по названию группы."""
        return self.data.get(group, "Группа не найдена!")

    def edit_albums(self, group, new_albums):
        """Редактирование альбомов у существующей группы."""
        if group in self.data:
            self.data[group] = new_albums
            print(f"Альбомы группы {group} обновлены на: {new_albums}")
        else:
            print(f"Группа {group} не найдена!")

    def save_data(self, filename):
        """Сохранение данных в файл с использованием упаковки (serialization)."""
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)
        print("Данные сохранены.")

    def load_data(self, filename):
        """Загрузка данных из файла с использованием распаковки (deserialization)."""
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
            print("Данные загружены.")
        except FileNotFoundError:
            print("Файл не найден!")

manager = MusicGroupManager()
manager.add_group("The Beatles", ["Abbey Road", "Sgt. Pepper's Lonely Hearts Club Band"])
manager.add_group("Nirvana", ["Nevermind", "In Utero"])

print(manager.find_albums("The Beatles"))
manager.edit_albums("Nirvana", ["Nevermind", "MTV Unplugged in New York"])
print(manager.find_albums("Nirvana"))
manager.remove_group("The Beatles")
manager.save_data("music_groups.pkl")

new_manager = MusicGroupManager()
new_manager.load_data("music_groups.pkl")
print(new_manager.find_albums("Nirvana"))