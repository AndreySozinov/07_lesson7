# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байтов, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байтов, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
from random import randint
__all__ = ['ext_file_gen', 'file_generator']


def file_generator(path_dir: str, extension: str, name_len_min: int = 6, name_len_max: int = 30,
                   byte_min: int = 256, byte_max: int = 4096, files: int = 42) -> None:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(files):
        filename = ''
        for j in range(randint(name_len_min, name_len_max)):
            filename = f'{filename}{alphabet[randint(0, 25)]}'
        if path_dir != '':
            filename = f'{path_dir}/{filename}.{extension}'
        else:
            filename = f'{filename}.{extension}'

        with open(filename, 'ab') as file_:
            print(bytes(randint(byte_min, byte_max)), file=file_)


def ext_file_gen(directory: str = '', **extension) -> None:
    for extension, files_amount in extension.items():
        file_generator(directory, extension, files=files_amount)


if __name__ == '__main__':
    ext_file_gen(txt=2, doc=3, rtf=5)
