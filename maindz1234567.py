# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

def compare_files(file1, file2):
    lines1 = read_file(file1)
    lines2 = read_file(file2)

    max_length = max(len(lines1), len(lines2))

    for i in range(max_length):
        line1 = lines1[i].strip() if i < len(lines1) else None
        line2 = lines2[i].strip() if i < len(lines2) else None

        if line1 != line2:
            print(f"Несовпадающая строка:\nФайл 1: {line1}\nФайл 2: {line2}\n")

if __name__ == "__main__":
    file1 = input("Введите имя первого файла: ")
    file2 = input("Введите имя второго файла: ")

    compare_files(file1, file2)

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр

def analyze_file(input_file, output_file):
    vowels = "простонаборбуквАБВГ"
    consonants = "ВТОРОЙнаборбукв"

    total_chars = total_lines = total_vowels = total_consonants = total_digits = 0

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            total_lines += 1
            total_chars += len(line)
            for char in line:
                if char.isdigit():
                    total_digits += 1
                elif char in vowels:
                    total_vowels += 1
                elif char in consonants:
                    total_consonants += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Количество символов: {total_chars}\n")
        f.write(f"Количество строк: {total_lines}\n")
        f.write(f"Количество гласных букв: {total_vowels}\n")
        f.write(f"Количество согласных букв: {total_consonants}\n")
        f.write(f"Количество цифр: {total_digits}\n")

if __name__ == "__main__":
    input_file = input("Введите имя исходного файла: ")
    output_file = input("Введите имя файла для записи статистики: ")
    analyze_file(input_file, output_file)

# Задание 3
# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.

def remove_last_line(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if lines:
        lines = lines[:-1]

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    if __name__ == "__main__":
        input_file = input("Введите имя исходного файла: ")
        output_file = input("Введите имя файла для записи результата: ")
        remove_last_line(input_file, output_file)

# Задание 4
# Дан текстовый файл. Найти длину самой длинной
# строки.

def find_longest_line_length(input_file):
    longest_length = 0
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line_length = len(line.rstrip('\n'))
            if line_length > longest_length:
                longest_length = line_length
    return longest_length

if __name__ == "__main__":
    input_file = input("Введите имя исходного файла: ")
    longest_length = find_longest_line_length(input_file)
    print(f"Длина самой длинной строки: {longest_length}")

# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово.

def count_word_occurrences(input_file, word):
    count = 0
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            count += line.lower().count(word.lower())
    return count

if __name__ == "__main__":
    input_file = input("Введите имя исходного файла: ")
    word = input("Введите слово для поиска: ")
    occurrences = count_word_occurrences(input_file, word)
    print(f"Слово '{word}' встречается {occurrences} раз(а) в файле.")
    
# Задание 6
# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
# пользователем.

def replace_word_in_file(input_file, old_word, new_word):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace(old_word, new_word)

    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    input_file = input("Введите имя исходного файла: ")
    old_word = input("Введите слово для замены: ")
    new_word = input("Введите новое слово: ")
    replace_word_in_file(input_file, old_word, new_word)
    print(f"Слово '{old_word}' было заменено на '{new_word}' в файле '{input_file}'.")