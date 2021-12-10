import sys, logging, log.client_log_config, log.server_log_config
from service import encode_msg, decode_msg, create_socket, parse_client_params
from decos import log


@log
def make_connection(s, h, p):
    try:
        s.connect((h, p))
    except Exception as e:
        log.error(f'Возникла ошибка при установке соединения с сервером {str(e)}')
        sys.exit(1)


@log
def send_msg(s, m):
    log.info(f'Отправка сообщения {m} на сервер')
    m = encode_msg(m)

    if not s.send(m):
        log.error('Ошибка при отправке сообщения на сервер! Работа программы будет зваершена')
        sys.exit(1)


@log
def recieve_response(s):
    resp = s.recv(1024)
    if resp:
        resp = decode_msg(resp)
        status = resp['status']
        if status == 200:
            log.info('Status == OK!')
        elif status == 600:
            log.info('Получено подтверждение от сервера о разрыве соединения')
            s.close()

    else:
        log.error('Ошибка при получении ответа от сервера')
        sys.exit(1)


@log
def exchange_msg(s):
    send_msg(s, 'Hello!')
    recieve_response(s)

    while True:
        msg = input('Введите строку для отправки на сервер, либо пустую строку для разрыва соединения: ')
        if msg:
            send_msg(s, msg)
            recieve_response(s)
        else:
            break


@log
def close_connection(s):
    log.info('Инициируем разрыв соединения')
    send_msg(s, 'close_connection')
    log.info(f'Соединение закрыто')


@log
def get_logger():
    l = None
    try:
        l = logging.getLogger('client')
    except Exception as e:
        print(f'Возникла ошибка при создании логгера {str(e)}')
        sys.exit(1)
    else:
        l.info(f'Логгер успешно создан: {l}')

    return l


@log
def read_message(s):
    while True:
        resp = s.recv(1024)
        if resp:
            resp = decode_msg(resp)
            log.info(f'Получено сообщение: {resp["message"]}')
            print(resp['message'])


@log
def write_message(s):
    while True:
        msg = input('Введите строку для отправки на сервер, либо пустую строку для разрыва соединения: ')
        if msg:
            log.info(f'Отправка сообщения {msg} на сервер')
            msg = encode_msg(msg)

            if not s.send(msg):
                log.error('Ошибка при отправке сообщения на сервер! Работа программы будет зваершена')
                sys.exit(1)

        else:
            break


if __name__ == '__main__':
    log = get_logger()
    if log:
        host, port, mode = parse_client_params(sys.argv)
        log.info(f'Определены параметры командной строки: host = {host}, port = {port}, mode = {mode}')

        if host is None or port is None or mode is None:
            log.critical(f'Некорректные параметры командной строки: {sys.argv}')
            sys.exit(1)
        else:
            print('mode = ', mode)
            socket = create_socket('client')
            make_connection(socket, host, port)
            if mode == 'read':
                read_message(socket)
            else:
                write_message(socket)

            close_connection(socket)
