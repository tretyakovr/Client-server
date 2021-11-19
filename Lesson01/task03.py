"""
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе
"""


for item in [b'attribute', b'класс', b'функция', b'type']:
    print(f'type = {type(item)}, str = {item}, lenght = {len(item)}')

# result:
#   File "/Users/rtretyakov/OneDrive/Geekbrains/Client-Server/Lesson01/task03.py", line 6
#     for item in [b'attribute', b'класс', b'функция', b'type']:
#                                             ^
# SyntaxError: bytes can only contain ASCII literal characters.
