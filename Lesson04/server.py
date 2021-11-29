from socket import *
import sys
from service import get_msg, encode_msg, decode_msg, create_socket, encode_reply, parse_server_params

hosts, port = parse_server_params(sys.argv)
if hosts is None or port is None:
    print(f'Некорректные параметры командной строки: {sys.argv}')
else:
    s = create_socket()
    s.bind((hosts, port))
    s.listen(5)

    client, addr = s.accept()
    print(f'Установлено соединение с {addr}')

    while True:
        msg = client.recv(1024)
        msg = decode_msg(msg)
        if msg['action'] == 'msg':
            print(f'Получено сообщение от клиента: {msg["message"]}')
            reply_str = 'Уведомление об успешном получении сообщения'
            reply_str = encode_reply(reply_str)
            client.send(reply_str)

        elif msg['action'] == 'quit':
            print(f'Получен запрос от клиента на разрыв соединения')
            reply_str = 'quit'
            reply_str = encode_reply(reply_str)
            client.send(reply_str)
            print('Остановка сервера')
            client.close()
            break

    client.close()
    print('Сервер остановлен')
