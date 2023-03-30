# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните # имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
__all__ = ['strange_func']


def strange_func(file_path1: str, file_path2: str, result_file: str) -> None:
    with(
        open(file_path1, 'r', encoding='utf-8') as file1,
        open(file_path2, 'r', encoding='utf-8') as file2,
        open(result_file, 'w', encoding='utf-8') as result
    ):
        len_file1 = sum(1 for _ in file1)
        len_file2 = sum(1 for _ in file2)
        for i in range(max(len_file1, len_file2)):
            number = read_line(file1)
            name = read_line(file2)
            mult = int(number.split('|')[0]) * float(number.split('|')[1])
            if mult < 0:
                print(f'{name.lower()} {abs(mult)}', file=result)
            elif mult > 0:
                print(f'{name.upper()} {round(mult)}', file=result)


def read_line(fd) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


if __name__ == '__main__':
    strange_func('numbers.txt', 'pseudo_names.txt', 'newest.txt')
