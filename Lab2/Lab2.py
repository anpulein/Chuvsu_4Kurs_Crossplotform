import os
import sys
import shutil

# Проверка наличия аргумента командной строки для целевого каталога
if len(sys.argv) > 1:
    target_dir = sys.argv[1]
else:
    target_dir = '/Users/anpulein/Documents/Projects/Chuvsu/Chuvsu_4Kurs_Crossplotform/Lab2/test_dir'  # Ввести путь к корневому каталогу самостоятельно


# Функция, которая перемещает файлы из подкаталога в корневой каталог
def move_dir(target_directory):
    for root, _, files in os.walk(target_directory):
        for file in files:
            if root != target_directory:
                new_filename = os.path.relpath(root, target_directory).replace(os.path.sep, '_') + '_' + file
                new_filepath = os.path.join(target_directory, new_filename)
                filepath = os.path.join(root, file)
                shutil.move(filepath, new_filepath)


# Функция, которая удаляет пустые каталоги
def del_empty_dir(target_directory):
    for root, dirs, _ in os.walk(target_directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)


move_dir(target_directory=target_dir)
del_empty_dir(target_directory=target_dir)
