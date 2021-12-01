from socket import *
import sys
import json
import logging, log.client_log_config, log.server_log_config


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


def encode_msg(msg):
    if msg == 'close_connection':
        msg = {'action': 'quit',
               'message': msg}
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


def create_socket(logger):
    s = None
    try:
        s = socket(AF_INET,SOCK_STREAM)  # Создать сокет TCP
    except Exception as e:
        logging.getLogger(logger).error(f'Ошибка при создании сокета {str(e)}')
        sys.exit(1)
    else:
        logging.getLogger(logger).info(f'Сокет успешно создан: {s}')

    return s


def get_logger(name_logger):
    l = None
    try:
        l = logging.getLogger(name_logger)
    except Exception as e:
        print(f'Возникла ошибка при создании логгера {name_logger} {str(e)}')
        sys.exit(1)
    else:
        l.info(f'Логгер успешно создан: {l}')

    return l
