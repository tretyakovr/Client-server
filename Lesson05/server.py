from socket import *
import sys, logging, log.client_log_config, log.server_log_config
from service import encode_msg, decode_msg, create_socket, encode_reply, parse_server_params, get_logger


def make_connection(s, h, p):
    s.bind((h, p))
    s.listen(5)
    conn, address = s.accept()
    if conn:
        log.info(f'Установлено соединение с {conn} {address}')
    else:
        log.error(f'Ошибка установления соединения')
        sys.exit(1)

    return conn


def send_msg(c, m):
    m = encode_reply(m)
    c.send(m)


def exchange_msg(c):
    while True:
        msg = c.recv(1024)
        msg = decode_msg(msg)
        log.info(f'Получено сообщение от клиента: {msg["message"]}')
        send_msg(c, 'Уведомление об успешном получении сообщения')

        if msg['action'] == 'quit':
            break


def close_connection(c):
    log.info('Останавливаем сервер')
    c.close()
    log.info('Свервер остановлен')


def get_logger():
    l = None
    try:
        l = logging.getLogger('server')
    except Exception as e:
        print(f'Возникла ошибка при создании логгера {str(e)}')
        sys.exit(1)
    else:
        l.info(f'Логгер успешно создан: {l}')

    return l

"""
1. Стартуем логгирование
2. Проверяем параметры командной строки
3. Создаем сокет
4. Обмениваемся сообщениями с с сервером
    1. Принимаем сообщение от клиента
    2. Возвращаем клиенту статус 
5. При получении запроса на разрыв закрываем соединение
"""
if __name__ == '__main__':
    log = get_logger()
    if log:
        hosts, port = parse_server_params(sys.argv)
        log.info(f'Определены параметры командной строки: host = {hosts}, port = {port}')

        if hosts is None or port is None:
            log.critical(f'Некорректные параметры командной строки: {sys.argv}')
        else:
            socket = create_socket('server')
            client = make_connection(socket, hosts, port)
            exchange_msg(client)
            close_connection(client)
