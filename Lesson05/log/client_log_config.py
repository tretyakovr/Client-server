import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('client')

# Формат строки для вывода сообщений
strfmt = '%(asctime)s.%(msecs)03d %(levelname)-10s %(name)-10s %(message)s'

# Устанавливаем формат даты
datefmt = '%d-%m-%Y %H:%M:%S'
formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)
fh = logging.FileHandler('client.log', encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(TimedRotatingFileHandler('client.log', when='midnight'))
# logger.addHandler(TimedRotatingFileHandler('client.log', when='M', interval=10))
logger.setLevel(logging.INFO)
logger.propagate = False
