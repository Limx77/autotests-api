import logging

def get_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # создали логгер и указали что он будет логгировать, какой уровень - в даном случае дебаг и выше

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)  # указывает начиная от какого уровня пишутся логи, если указать инфо, то логи дебаг не будет видно
    # Создали обработчик, который будет обрабатывать логги с уровнем дебаг

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s)')
    handler.setFormatter(formatter)
    # Создали формат, после чего дали этот формат обработчику, созданному выше

    logger.addHandler(handler)
    # В логгер добавили обработчик, который был создан выше

    return logger

logger = get_logger("INPUT")