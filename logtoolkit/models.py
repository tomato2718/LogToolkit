'''
This module contains Configured models of Formatters and Handlers.
'''
__all__ = [
    'Formatters',
    'Handlers',
]

from sys import (
    stdout,
    stderr
)
from logging import (
    Formatter,
    StreamHandler,
)
from logging.handlers import TimedRotatingFileHandler

from ._formatters import ColorfulFormatter

class Formatters:
    '''
    Some configured instance of `logging.Formatter`.

    :var Formatter CLEAN: Format your log as follow: ``[INFO    1900-01-01 00:00:00]: foo``.
    :var Formatter XML: Format your log as follow: ``1900-01-01T00:00:00:INFO: foo``.
    :var ColorfulFormatter COLOR: Same as ``CLEAN``, but colored.
    '''

    CLEAN = Formatter(
        fmt='[%(levelname)-5s %(asctime)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    XML = Formatter(
        fmt='%(asctime)s:%(levelname)s: %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S',  
    )

    COLOR = ColorfulFormatter(
        colors={
            'DEBUG': 'CYAN',
            'WARNING': 'YELLOW',
            'ERROR': 'RED',
            'CRITICAL': 'BRIGHT_RED',
        },
        fmt='[%(levelname)-5s %(asctime)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

class Handlers:
    '''
    Class contains configured instance of `logging.handlers.*`.
    '''
    @staticmethod
    def log_file(path: str, formatter: Formatter) -> TimedRotatingFileHandler:
        '''
        Create a FileHandler for log file.

        :param str path: The path to output log file.
        :param Formatter formatter: The formatter to use for handler.
        :return: Configured instance of FileHandler.
        :rtype: `TimedRotatingFileHandler`
        '''
        handler = TimedRotatingFileHandler(
            filename=path,
            encoding='utf-8',
            when='D',
            interval=1,
            backupCount=30,
        )
        handler.setFormatter(formatter)
        handler.setLevel('INFO')
        return handler

    @staticmethod
    def error_log(path: str, formatter: Formatter) -> TimedRotatingFileHandler:
        '''
        Create a FileHandler for error log.

        :param str path: The path to output error log.
        :param Formatter formatter: The formatter to use for handler.
        :return: Configured instance of FileHandler.
        :rtype: `TimedRotatingFileHandler`
        '''
        handler = TimedRotatingFileHandler(
            filename=path,
            encoding='utf-8',
            when='D',
            interval=30,
            backupCount=12,
        )
        handler.setFormatter(formatter)
        handler.setLevel('ERROR')
        return handler

    @staticmethod
    def stdout(formatter: Formatter) -> StreamHandler:
        '''
        Create a StreamHandler for stdout.

        :param Formatter formatter: The formatter to use for handler.
        :return: Configured instance of StreamHandler.
        :rtype: ``StreamHandler``
        '''
        handler = StreamHandler(
            stream=stdout
        )
        handler.setFormatter(formatter)
        handler.setLevel('DEBUG')
        return handler
    
    @staticmethod
    def stderr(formatter: Formatter) -> StreamHandler:
        '''
        Create a StreamHandler for stderr.

        :param Formatter formatter: The formatter to use for handler.
        :return: Configured instance of StreamHandler.
        :rtype: ``StreamHandler``
        '''
        handler = StreamHandler(
            stream=stderr
        )
        handler.setFormatter(formatter)
        handler.setLevel('ERROR')
        return handler