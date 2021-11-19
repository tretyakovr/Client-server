"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и
длину соответствующих переменных.
"""

for item in ['class', 'function', 'method']:
    byte_str = bytes(item, 'utf-8')
    print(f'type = {type(byte_str)}, str = {byte_str}, lenght = {len(byte_str)}')

# result:
# type = <class 'bytes'>, str = b'class', lenght = 5
# type = <class 'bytes'>, str = b'function', lenght = 8
# type = <class 'bytes'>, str = b'method', lenght = 6
