'''
Not for import.
'''

__all__ = ['ColorfulFormatter']

from logging import Formatter

class ColorfulFormatter(Formatter):
    '''
    Custom formatter to color your logger.
    '''

    def update(self, color):
        self.__format = color

    def format(self, record):
        log_fmt = self.__format.get(record.levelno)
        formatter = Formatter(log_fmt, datefmt=self.datefmt)
        return formatter.format(record)