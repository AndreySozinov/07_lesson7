# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import randint
__all__ = ['naming']


def naming(file_path: str, names_amount: int) -> None:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    vowel_letters= 'аеёиоуыэюя'
    with open(file_path, 'a+', encoding='utf-8') as f:
        for k in range(names_amount):
            test = False
            while not test:
                name = ''
                for i in range(randint(4, 8)):
                    name = f'{name}{alphabet[randint(0, 32)]}'
                for letter in vowel_letters:
                    if letter in name:
                        test = True
                        print(name.capitalize(), file=f)
                        break


if __name__ == '__main__':
    naming('pseudo_names.txt', 5)
