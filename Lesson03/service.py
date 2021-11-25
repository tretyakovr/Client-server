from socket import *
import json


def parse_client_params(params):
    host, port = None, None

    if len(params) == 1:
        host = 'localhost'
        port = 7777

    elif len(params) == 3:
        if params[1] == 'addr':
            host = params[2]
            port = 7777
        elif params[1] == 'port':
            host = 'localhost'
            port = params[2]

    elif len(params) == 5:
        if params[1] == 'addr':
            host = params[2]
        elif params[1] == 'port':
            port = params[2]

        if params[3] == 'addr':
            host = params[4]
        elif params[3] == 'port':
            port = params[4]

    return host, port


def parse_server_params(params):
    hosts, port = None, None

    if len(params) == 1:
        hosts = ''
        port = 7777

    elif len(params) == 3:
        if params[1] == '-a':
            hosts = params[2]
            port = 7777
        elif params[1] == '-p':
            hosts = ''
            port = params[2]

    elif len(params) == 5:
        if params[1] == '-a':
            hosts = params[2]
        elif params[1] == '-p':
            port = params[2]

        if params[3] == '-a':
            hosts = params[4]
        elif params[3] == '-p':
            port = params[4]

    return hosts, port


def get_msg():
    return input('Введите строку для отправки сообщения на сервер или пустую строку для остановки соединения: ')


def encode_msg(msg):
    if msg == '':
        msg = {'action': 'quit'}
    else:
        msg = {'action': 'msg',
               'message': msg}

    return json.dumps(msg).encode('utf-8')


def encode_reply(reply):
    if reply == 'quit':
        reply = {'action': 'quit',
                 'status': 600}
    else:
        reply = {'action': 'reply',
                 'status': 200,
                 'message': reply}

    return json.dumps(reply).encode('utf-8')


def decode_msg(msg):
    return json.loads(msg.decode('utf-8'))


def create_socket():
    s = socket(AF_INET,SOCK_STREAM)  # Создать сокет TCP
    return s


def make_connection(s, host, port):
    s.connect((host, port))   # Соединиться с сервером
    return True
