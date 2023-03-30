# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
from pathlib import Path
__all__ = ['file_group_rename']


def file_group_rename(source_ext: str, destin_ext: str,
                      destin_filename: str = '', digits_amount: int = 4, scope_=None) -> None:
    if scope_ is None:
        scope_ = [0, 2]
    number = 0

    p = Path(Path().cwd())
    for obj in p.iterdir():
        if obj.is_file():
            old_name, old_ext = obj.name.split('.')
            if old_ext == source_ext:
                number += 1
                number_str = f'{number:0{digits_amount}}'
                new_name = f'{old_name[scope_[0]-1:scope_[1]-1]}{destin_filename}{number_str}.{destin_ext}'
                Path(obj.name).rename(new_name)


if __name__ == '__main__':
    file_group_rename('rtf', 'txt', destin_filename='test')
