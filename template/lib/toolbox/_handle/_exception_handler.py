'''
Not for import.
'''

__all__ = ['Handle']

from functools import wraps
from typing import Any
from .._logtool import LogTool

class Handle:
    '''
    Error handling tools.
    '''
    class Ignore():
        '''
        To catch and ignore specific exceptions.

        :param Exception|tuple exceptions: Exceptions to catch. (Default = Exception)
        '''
        def __init__(self, exceptions: tuple = (Exception)) -> None:
            self.exceptions = exceptions

        def __call__(self, func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except self.exceptions:
                     pass
            return wrapper

    class Log():
        '''
        To catch and record specific exceptions by logging.Logger, logging level is error(40).
        
        exc_info will be recorded while running in debug mode.

        :param Exception | tuple exceptions: Exceptions to catch. (Default = Exception)
        :param str logger: Name of the logger to use.
        '''
        def __init__(self, exceptions: tuple = (Exception), logger: str = '') -> None:
            self.exceptions = exceptions
            self.logger = LogTool.get_logger(logger)

        def __call__(self, func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except self.exceptions as e:
                    self.logger.error(e.__class__.__name__ + ': ' + str(e), exc_info=__debug__)
            return wrapper
            
    class Raise():
        '''
        To catch and raise specific exceptions.

        :param Exception | tuple exceptions: Exceptions to catch. (Default = Exception)
        :param Exception | None raise_: Exception to raise. (Default = None)
        :param bool trace: To trace original exception or not, (Default = False)
        '''
        def __init__(self, exceptions: tuple = (Exception), raise_: Exception = None, trace: bool = False) -> None:
            self.exceptions = exceptions
            self.raise_ = raise_
            self.trace = trace
        
        def __call__(self, func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except self.exceptions as e:
                    if not self.trace:
                        e = None
                    if self.raise_:
                        raise self.raise_ from e
                    else:
                        raise
            return wrapper

    class Return():
        '''
        To catch specific exceptions and return something.
        
        :param Exception | tuple exceptions: Exceptions to catch. (Default = Exception)
        :param Any return_: Things to return while exceptions occurred.
        '''
        def __init__(self, exceptions: tuple = (Exception), return_: Any = None) -> None:
            self.exceptions = exceptions
            self.return_ = return_

        def __call__(self, func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except self.exceptions as e:
                    return self.return_
            return wrapper