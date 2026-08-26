import logging

logger = logging.getLogger('AUTOTEST')
logger.setLevel(logging.DEBUG)
#создали логгер и указали что он будет логгировать, какой уровень - в даном случае дебаг

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG) #указывает начиная от какого уровня пишутся логи, если указать инфо, то логи дебаг не будет видно
#Создали обработчик, который будет обрабатывать логги с уровнем дебаг

formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s)')
handler.setFormatter(formatter)
#Создали формат, после чего дали этот формат обработчику, созданному выше

logger.addHandler(handler)
# В логгер добавили обработчик, который был создан выше

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


def make_api_request():
    logger.info('making API request')
    client = ...
    client.get(...)