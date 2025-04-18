# Задание 1
# При старте приложения запускаются три потока.
# Первый поток заполняет список случайными числами.
# Два других потока ожидают заполнения. Когда список
# заполнен оба потока запускаются. Первый поток находит
# сумму элементов списка, второй поток среднеарифметическое значение в списке. Полученный список, сумма и
# среднеарифметическое выводятся на экран. 

import threading
import random
import time

numbers = []
list_filled = threading.Event()

def fill_list():
    global numbers
    for _ in range(10):
        numbers.append(random.randint(1, 100))
        time.sleep(0.1)
    list_filled.set()

def calculate_sum():
    list_filled.wait() 
    total_sum = sum(numbers)
    print(f"Сумма элементов списка: {total_sum}")

def calculate_average():
    list_filled.wait()
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"Среднее арифметическое значение: {average}")

thread_fill = threading.Thread(target=fill_list)
thread_sum = threading.Thread(target=calculate_sum)
thread_average = threading.Thread(target=calculate_average)

thread_fill.start()
thread_sum.start()
thread_average.start()

thread_fill.join()
thread_sum.join()
thread_average.join()

print(f"Полученный список: {numbers}")

# Задание 2
# Пользователь с клавиатуры вводит путь к файлу.
# После чего запускаются три потока. Первый поток заполняет файл случайными числами. Два других потока
# ожидают заполнения. Когда файл заполнен оба потока
# стартуют. Первый поток находит все простые числа, второй поток факториал каждого числа в файле. Результаты
# поиска каждый поток должен записать в новый файл. На
# экран необходимо отобразить статистику выполненных
# операций.

import threading
import random
import os

file_path = ""
list_filled = threading.Event()

def fill_file():
    global file_path
    with open(file_path, 'w') as f:
        for _ in range(10):
            number = random.randint(1, 100)
            f.write(f"{number}\n")
    list_filled.set()

def find_primes():
    list_filled.wait()
    primes = []
    
    with open(file_path, 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    
    with open('primes.txt', 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")
    
    print(f"Найдено простых чисел: {len(primes)}")

def calculate_factorials():
    list_filled.wait()
    factorials = []
    
    with open(file_path, 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    
    for number in numbers:
        factorials.append((number, factorial(number)))
    
    with open('factorials.txt', 'w') as f:
        for number, fact in factorials:
            f.write(f"{number}! = {fact}\n")
    
    print(f"Вычислено факториалов: {len(factorials)}")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    file_path = input("Введите путь к файлу: ")

    thread_fill = threading.Thread(target=fill_file)
    thread_primes = threading.Thread(target=find_primes)

    thread_fill.start()
    thread_primes.start()
    thread_factorials.start()

    thread_fill.join()
    thread_primes.join()
    thread_factorials.join()


# Задание 3
# Пользователь с клавиатуры вводит путь к существующей директории и к новой директории. После чего
# запускается поток, который должен скопировать содержимое директории в новое место. Необходимо сохранить
# структуру директории. На экран необходимо отобразить
# статистику выполненных операций.

import os
import shutil
import threading

source_dir = ""
destination_dir = ""
copy_completed = threading.Event()

def copy_directory():
    global source_dir, destination_dir
    try:
        shutil.copytree(source_dir, destination_dir)
        copy_completed.set() 
    except Exception as e:
        print(f"Ошибка при копировании: {e}")

if __name__ == "__main__":
    source_dir = input("Введите путь к существующей директории: ")
    destination_dir = input("Введите путь к новой директории: ")

    if not os.path.exists(source_dir):
        print("Исходная директория не существует.")
    else:
        thread_copy = threading.Thread(target=copy_directory)

        thread_copy.start()

#         Задание 4
# Пользователь склавиатурывводитпутьксуществующей
# директории и слово для поиска. После чего запускаются
# два потока. Первый должен найти файлы, содержащие
# искомое слово и слить их содержимое в один файл. Второй поток ожидает завершения работы первого потока.
# После чего проводит вырезание всех запрещенных слов
# (список этих слов нужно считать из файла с запрещенными словами) из полученного файла. На экран необходимо
# отобразить статистику выполненных операций.

import os
import threading

search_dir = ""
search_word = ""
output_file = "merged_output.txt"
banned_words_file = "banned_words.txt"
banned_words = set()
merge_completed = threading.Event()

def find_and_merge_files():
    global search_dir, search_word, output_file
    try:
        with open(output_file, 'w') as outfile:
            for root, dirs, files in os.walk(search_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as infile:
                            content = infile.read()
                            if search_word in content:
                                outfile.write(content + "\n")
                                print(f"Содержимое файла '{file_path}' добавлено в '{output_file}'.")
                    except Exception as e:
                        print(f"Ошибка при чтении файла '{file_path}': {e}")
        merge_completed.set() 
    except Exception as e:
        print(f"Ошибка при записи в файл '{output_file}': {e}")

def remove_banned_words():
    global output_file, banned_words_file
    merge_completed.wait()

    try:

        with open(banned_words_file, 'r') as f:
            for line in f:
                banned_words.add(line.strip())

        with open(output_file, 'r') as infile:
            lines = infile.readlines()

        with open(output_file, 'w') as outfile:
            for line in lines:
                filtered_line = ' '.join(word for word in line.split() if word not in banned_words)
                outfile.write(filtered_line + "\n")

        print(f"Запрещенные слова удалены из '{output_file}'.")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

if __name__ == "__main__":
    search_dir = input("Введите путь к существующей директории: ")
    search_word = input("Введите слово для поиска: ")

    thread_merge = threading.Thread(target=find_and_merge_files)
    thread_remove_banned = threading.Thread(target=remove_banned_words)

    thread_merge.start()
    

    thread_remove_banned.start()

    thread_merge.join()
    thread_remove_banned.join()

    print("Операции завершены.")