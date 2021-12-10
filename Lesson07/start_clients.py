#! /usr/bin python3
# -*- coding: utf-8 -*-

from subprocess import Popen, call
import subprocess
import time
from os import path


# pathOfFile=path.dirname(__file__)
pathClient=path.join(path.dirname(__file__), '-client.py')
# pathToScriptClients = path.join(pathOfFile, "-client.py")
print(pathClient)
# print(path.dirname(__file__))
# print(f"open -n -a Terminal.app '{pathToScriptClients}'")

p_list = []  # Список клиентских процессов

while True:
    user = input("Запустить 10 клиентов (s) / Закрыть клиентов (x) / Выйти (q) ")

    if user == 'q':
        break
    elif user == 's':
        for i in range(1, 3):
            # Флаг CREATE_NEW_CONSOLE нужен для ОС Windows,
            # чтобы каждый процесс запускался в отдельном окне консоли

            # Это рабочий вариант, но с интерфейсом пока не понятно!
            p_list = Popen(
                f'osascript -e \'tell application "Terminal" to do'
                f' script "python3 {pathClient}"\'', shell=True)




            # p_list.append(Popen('python -client.py', creationflags=CREATE_NEW_CONSOLE))
            # p_list.append(Popen(['Terminal.app',  '-client.py'], shell=True))
            # p_list.append(Popen(f'script "/usr/bin/python3 {pathClient}"', shell=True))
            # p_list.append(Popen(f'script "/usr/bin/python3"', shell=True))

            # p_list.append(Popen(f'script "python3 {pathClient}"\'', shell=True))


            # retcode = call('Terminal.app ')
            # p_list.append(Popen(f'open -n -a Terminal.app {path.join(pathOfFile, "-client.py")}', shell=True))
            # p_list.append(Popen(f'open -n -a Terminal.app "/usr/bin/python -m {pathClient}"', shell=True))
            # p_list.append(subprocess.call(['open', '-n', '-a', 'Terminal.app', 'python3', '--args', f'{pathClient}'], shell=True))

            # p_list.append(Popen(f'open -n -a Terminal.app "{pathClient}"', shell=True))
            # p_list.append(Popen('open -n -a Terminal.app "-client.py"', shell=True))

            # p_list.append(Popen(f"open -n -a Terminal.app '{pathToScriptClients}'", shell=True))
            ## p_list.append(Popen(f"open -n -a Terminal.app 'python -client.py'", shell=True))
            # Задержка для того, что бы отправляющий процесс успел зарегистрироваться на сервере, и потом в словаре имен клиентов
            # остался только слушающий клиент
            # time.sleep(0.5)
            # p_list.append(Popen(f"open -n -a Terminal.app '{pathToScriptClients}'", shell=True))
            ## p_list.append(Popen(f"open -n -a Terminal.app 'python -client.py'", shell=True))

        print(' Запущено 10 клиентов')
    elif user == 'x':
        for p in p_list:
            p.kill()
        p_list.clear()
