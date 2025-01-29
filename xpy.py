# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла

def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_lines = max(len(lines1), len(lines2))

    mismatches1 = []
    mismatches2 = []

    for i in range(max_lines):
        line1 = lines1[i].strip() if i < len(lines1) else None
        line2 = lines2[i].strip() if i < len(lines2) else None

        if line1 != line2:
            if line1 is not None:
                mismatches1.append(line1)
            if line2 is not None:
                mismatches2.append(line2)

    if mismatches1:
        print("Несовпадающие строки из первого файла:")
        for line in mismatches1:
            print(line)

    if mismatches2:
        print("Несовпадающие строки из второго файла:")
        for line in mismatches2:
            print(line)

compare_files('file1.txt', 'file2.txt')

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.

def file_statistics(input_file, output_file):

    char_count = 0
    line_count = 0
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    
    vowels = 'aeiouAEIOU'

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
            char_count += len(line)

            for char in line:
                if char.isalpha():
                    if char in vowels:
                        vowel_count += 1
                    else:
                        consonant_count += 1
                elif char.isdigit():
                    digit_count += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Количество символов: {char_count}\n")
        f.write(f"Количество строк: {line_count}\n")
        f.write(f"Количество гласных: {vowel_count}\n")
        f.write(f"Количество согласных: {consonant_count}\n")
        f.write(f"Количество цифр: {digit_count}\n")

file_statistics('input.txt', 'output.txt')

# Задание 3
# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл. сделай простым кодом

def remove_last_line(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = lines[:-1]

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

remove_last_line('input.txt', 'output.txt')

# Задание 4
# Дан текстовый файл. Найти длину самой длинной
# строки.

def find_longest_line_length(input_file):
    max_length = 0

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line_length = len(line.rstrip('\n'))
            if line_length > max_length:
                max_length = line_length

    return max_length

longest_line_length = find_longest_line_length('input.txt')
print(f"Длина самой длинной строки: {longest_line_length}")

# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово.

def count_word_in_file(input_file, word):
    count = 0

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            count += line.lower().count(word.lower())

    return count

input_file = 'input.txt'
word_to_count = input('Введите слово для поиска: ')
word_count = count_word_in_file(input_file, word_to_count)
print(f"Слово '{word_to_count}' встречается {word_count} раз(а) в файле.")

# Задание 6
# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
# пользователем.

def replace_word_in_file(input_file, old_word, new_word):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    updated_content = content.replace(old_word, new_word)

    with open(input_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)

input_file = 'input.txt'
old_word = input('Введите слово для поиска: ')
new_word = input('Введите слово для замены: ')

replace_word_in_file(input_file, old_word, new_word)
print(f"Слово '{old_word}' было заменено на '{new_word}' в файле {input_file}.")