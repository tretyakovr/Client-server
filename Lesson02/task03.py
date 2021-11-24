"""
Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в
файле YAML-формата. Для этого:

Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml


YAML_DICT = {'item1': ['value1', 'value2', 'value3', 'value4'],
             'item2': 123456.78,
             'item3': {'key1': '1₽',
                       'key2': '2₽',
                       'key3': '3₽'}}

with open('file.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml.dump(YAML_DICT, yaml_file, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r') as yaml_file:
    yaml_file_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(yaml_file_data)
