import sys
from service import get_msg, encode_msg, decode_msg, create_socket, make_connection, parse_client_params

host, port = parse_client_params(sys.argv)
if host is None or port is None:
    print(f'Некорректные параметры командной строки: {sys.argv}')
else:
    s = create_socket()
    if make_connection(s, host, port):
        while True:
            print('Отправляем hello-сообщение')
            msg = 'Hello!'
            msg = encode_msg(msg)
            s.send(msg)
            resp = s.recv(1024)
            resp = decode_msg(resp)
            status = resp['status']
            if status == 200:
                print('Status == OK!')

            print('Инициируем разрыв соединения')
            msg = ''
            msg = encode_msg(msg)
            s.send(msg)
            resp = s.recv(1024)
            status = decode_msg(resp)['status']
            if status == 600:
                print('Получено подтверждение от сервера о разрыве соединения')
                s.close()
                break

        print(f'Соединение закрыто')
