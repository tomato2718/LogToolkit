'''
Customize exceptions module.
'''

__all__ = ['SomeException']

from typing import Any

class MyException(Exception):
    def __init__(self, message: Any):
        '''
        Base class for exceptions
        '''
        if isinstance(message, Exception):
            self._message = str(message)
        else:
            self._message = message

    def __str__(self):
        return self.__class__.__name__ + ': ' + self._message

class SomeException(MyException):
    def __init__(self, message: Any):
        '''
        Custom exception
        '''
        super().__init__(message)