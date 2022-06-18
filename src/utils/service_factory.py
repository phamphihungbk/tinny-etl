from logging import Logger, getLogger, INFO, basicConfig

LOG_FILE_NAME = 'log'
LOG_FORMAT = '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s'
DATE_FORMAT = '%H:%M:%S'


class ServiceFactory:

    @staticmethod
    def get_logger(name: str) -> Logger:
        basicConfig(
            filename=LOG_FILE_NAME,
            filemode='a',
            format=LOG_FORMAT,
            datefmt=DATE_FORMAT,
            level=INFO
        )
        logger = getLogger(name)

        return logger
