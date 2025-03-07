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
is_filled = threading.Event()

def fill_list(size):
    global numbers
    numbers = [random.randint(1, 100) for _ in range(size)]
    is_filled.set()
    print("Список заполнен:", numbers)

def calculate_sum():
    is_filled.wait()
    total = sum(numbers)
    print("Сумма элементов списка:", total)

def calculate_average():
    is_filled.wait()
    average = sum(numbers) / len(numbers)
    print("Среднее значение:", average)

size = 10
thread_fill = threading.Thread(target=fill_list, args=(size,))
thread_sum = threading.Thread(target=calculate_sum)
thread_average = threading.Thread(target=calculate_average)

thread_fill.start()
thread_sum.start()
thread_average.start()

thread_fill.join()
thread_sum.join()
thread_average.join()

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
import time
import math

numbers = []
is_filled = threading.Event()

def fill_file(file_path, size=10):
    global numbers
    numbers = [random.randint(1, 100) for _ in range(size)]
    
    with open(file_path, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")
    
    is_filled.set()
    print(f"Файл заполнен случайными числами: {numbers}")

def find_prime_numbers(file_path):
    is_filled.wait()
    primes = []
    
    with open(file_path, 'r') as file:
        for line in file:
            num = int(line.strip())
            if is_prime(num):
                primes.append(num)

    with open('prime_numbers.txt', 'w') as file:
        for prime in primes:
            file.write(f"{prime}\n")
    
    print(f"Найденные простые числа: {primes}")

def calculate_factorials(file_path):
    is_filled.wait()
    factorials = []
    
    with open(file_path, 'r') as file:
        for line in file:
            num = int(line.strip())
            factorials.append(math.factorial(num))

    with open('factorials.txt', 'w') as file:
        for fact in factorials:
            file.write(f"{fact}\n")
    
    print(f"Факториалы чисел: {factorials}")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

file_path = input("Введите путь к файлу для заполнения случайными числами: ")

thread_fill = threading.Thread(target=fill_file, args=(file_path,))
thread_primes = threading.Thread(target=find_prime_numbers, args=(file_path,))
thread_factorials = threading.Thread(target=calculate_factorials, args=(file_path,))

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

files_copied = 0
dirs_copied = 0
lock = threading.Lock()

def copy_directory(src, dst):
    global files_copied, dirs_copied
  
    if not os.path.exists(dst):
        os.makedirs(dst)
        with lock:
            dirs_copied += 1

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        
        if os.path.isdir(s):
            copy_directory(s, d)
        else:
            shutil.copy2(s, d)
            with lock:
                files_copied += 1

def main():

    src_directory = input("Введите путь к существующей директории: ")
    dst_directory = input("Введите путь к новой директории: ")

    copy_thread = threading.Thread(target=copy_directory, args=(src_directory, dst_directory))
    copy_thread.start()

    copy_thread.join()

    print(f"Копирование завершено. Копировано {files_copied} файлов и {dirs_copied} директорий.")

if __name__ == "__main__":
    main()



# Задание 4
# Пользователь склавиатурывводитпутьксуществующей
# директории и слово для поиска. После чего запускаются
# два потока. Первый должен найти файлы, содержащие
# искомое слово и слить их содержимое в один файл. Второй поток ожидает завершения работы первого потока.
# После чего проводит вырезание всех запрещенных слов
# (список этих слов нужно считать из файла с запрещенными словами) из полученного файла. На экран необходимо
# отобразить статистику выполненных операций.


import threading
import os

result_file = "merged_file.txt"
is_found = threading.Event()

def find_and_merge_files(directory, search_word):
    global result_file
    with open(result_file, 'w') as outfile:
        found_files = []
      
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        if search_word in content:
                            outfile.write(content)
                            found_files.append(file_path)
                except Exception as e:
                    print(f"Ошибка при чтении файла {file_path}: {e}")

    is_found.set()
    print(f"Найдены и объединены файлы: {found_files}")

def remove_prohibited_words(file_path, prohibited_words_file):
    is_found.wait()

    with open(prohibited_words_file, 'r', encoding='utf-8') as f:
        prohibited_words = [line.strip() for line in f]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        for word in prohibited_words:
            content = content.replace(word, "")

        with open(file_path, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        
        print(f"Запрещенные слова удалены из файла {file_path}.")
    
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")

directory = input("Введите путь к директории: ")
search_word = input("Введите слово для поиска: ")
prohibited_words_file = input("Введите путь к файлу с запрещенными словами: ")

thread_merge = threading.Thread(target=find_and_merge_files, args=(directory, search_word))
thread_remove = threading.Thread(target=remove_prohibited_words, args=(result_file, prohibited_words_file))

thread_merge.start()
thread_remove.start()

thread_merge.join()
thread_remove.join()