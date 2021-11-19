"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
«сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в
формате Unicode и вывести его содержимое
"""

import chardet


with open('test_file.txt', 'w', encoding='hz') as f:
    for item in ['сетевое программирование', 'сокет', 'декоратор']:
        f.write(item + '\n')

    print(f'Кодировка прямо так и называется, х.з.: {f.encoding}')

with open('test_file.txt', 'rb') as f:
    for line in f:
        res = chardet.detect(line)
        print(line.decode(res['encoding']), end='')
