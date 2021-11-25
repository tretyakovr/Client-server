"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
«Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import csv
import re
import chardet

FILES_LIST = ['info_1.txt', 'info_2.txt', 'info_3.txt']
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
MAIN_DATA = ['Изготовитель системы',
             'Название ОС',
             'Код продукта',
             'Тип системы']


def get_file_encoding(file_name):
    # Невозможно определить кодировку файла по одной только первой строке, так как в ней
    # русские и латинские буквы. Необходимо использовать UniversalDetector
    detector = chardet.UniversalDetector()
    with open(file_name, 'rb') as input_file:
        for row in input_file:
            detector.feed(row)
            if detector.done:
                break
    detector.close()

    return detector.result['encoding']


def get_data(input_file):
    for row in input_file:
        re_row_list = re.split(r': ', row)
        if len(re_row_list) == 2:
            # Есть строки, в которых отсутствует разделитель
            # Поэтому проверяем, что строка распознана корректно
            param_name = re_row_list[0]
            param_value = re_row_list[1].strip()

            if param_name == MAIN_DATA[0]:
                os_prod_list.append(param_value)

            elif param_name == MAIN_DATA[1]:
                os_name_list.append(param_value)

            elif param_name == MAIN_DATA[2]:
                os_code_list.append(param_value)

            elif param_name == MAIN_DATA[3]:
                os_type_list.append(param_value)


def write_to_csv(file):
    file_encoding = get_file_encoding(file)
    with open(file, 'r', encoding=file_encoding) as input_file:
        get_data(input_file)

    res_data = [MAIN_DATA, os_prod_list, os_name_list, os_code_list, os_type_list]

    with open('main_data.csv', 'w') as output_file:
        output_file_writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
        for row in res_data:
            output_file_writer.writerow(row)


for file in FILES_LIST:
    write_to_csv(file)
