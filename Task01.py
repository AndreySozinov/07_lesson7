# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
from random import randint, uniform
__all__ = ['fill_by_numbers']
MIN = -1000
MAX = 1000


def fill_by_numbers(strings_amount: int, filename: str) -> None:
    with open(filename, 'a+', encoding='utf-8') as f:
        for i in range(strings_amount):
            print(f'{str(randint(MIN, MAX))}|{str(uniform(MIN, MAX))}', file=f)


if __name__ == '__main__':
    fill_by_numbers(4, 'numbers.txt')
