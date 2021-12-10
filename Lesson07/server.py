from socket import *
import select
import sys, logging, log.client_log_config, log.server_log_config
from service import decode_msg, create_socket, encode_reply, parse_server_params, encode_msg
from decos import log


@log
def send_msg(c, m):
    m = encode_reply(m)
    c.send(m)


@log
def exchange_msg(c):
    while True:
        msg = c.recv(1024)
        msg = decode_msg(msg)
        log.info(f'Получено сообщение от клиента: {msg["message"]}')
        send_msg(c, 'Уведомление об успешном получении сообщения')

        if msg['action'] == 'quit':
            break


@log
def close_connection(c):
    log.info('Останавливаем сервер')
    c.close()
    log.info('Свервер остановлен')


@log
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


def read_messages(w_clients, all_clients):
    responses = []  # Список полученных сообщений

    for client in w_clients:
        try:
            data = client.recv(1024)  # Получили сообщениеот клиента

        except OSError as e:
            pass # отвалились по таймауту

        except:
            pass # не получили сообщение от клиента

        else:
            if data:
                msg = decode_msg(data) # Декодировали сообщение от клиента
                print('На сервер прилетело сообщение: ', msg['message'])
                responses.append(msg['message']) # Записали сообщение в список на отправку

    return responses


def write_responses(responses, r_clients, all_clients):
    for client in r_clients:
        for response in responses:
            response = encode_msg(response.upper())
            try:
                client.send(response)

            except OSError as e:
                pass

            except:
                # Сокет недоступен, клиент отвалился
                log.error('Клиент {} {} отключился'.format(client.fileno(), client.getpeername()))
                client.close()
                all_clients.remove(client)

    # Отправили все сообщения из списка, список очистили
    responses.clear()


if __name__ == '__main__':
    log = get_logger()
    if log:
        hosts, port = parse_server_params(sys.argv)
        log.info(f'Определены параметры командной строки: host = {hosts}, port = {port}')

        if hosts is None or port is None:
            log.critical(f'Некорректные параметры командной строки: {sys.argv}')
        else:
            socket = create_socket('server')
            socket.bind((hosts, port))
            socket.listen(5)
            socket.settimeout(1)

            clients = []

            while True:
                try:
                    conn, address = socket.accept()
                except OSError as e:
                    pass
                else:
                    log.info(f'Установлено соединение с {conn} {address}')
                    clients.append(conn)
                finally:
                    # Проверить наличие событий ввода-вывода
                    wait = 5
                    r = [] # Список клиентов, читающих сообщения
                    w = [] # Список клиентов, отправляющих сообщения
                    try:
                        r, w, e = select.select(clients, clients, [], wait)
                    except Exception as e:
                        pass  # Ничего не делать, если какой-то клиент отключился

                    responses = read_messages(r, clients)  # Получаем сообщения от клиентов
                    if responses:
                        write_responses(responses, w, clients)  # Отправляем полученные сообщения читателям
