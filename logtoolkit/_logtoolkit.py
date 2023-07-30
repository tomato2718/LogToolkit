'''
Not for import.
'''

__all__ = [
    'getLogger',
    'quickConfig',
    'yamlConfig',
]

import logging
from logging.config import dictConfig

from yaml import safe_load

from .models import (
    Formatters,
    Handlers,
)
from .types import (
    FormattersModels,
    StreamHandlersModels,
    FileHandlersModels
)

def getLogger(name: str|None = None) -> logging.Logger:
    '''
    Wrapper of `logging.getLogger()`.

    :param Optional[str] target: Name of the logger
    :return: Requested logger.
    :rtype: `logging.Logger`
    '''
    return logging.getLogger(name)

def quickConfig(name: str, 
                formatter: FormattersModels,
                stream_handler: StreamHandlersModels|None = None,
                file_handlers: dict[FileHandlersModels, str] = {},
                )-> logging.Logger:
    '''
    Configure logger using templates. This function also return the logger with specified name.

    About formatters:
    
    The `formatter` parameter MUST be one of the ``FormattersModels``, see follows:

    ``CLEAN``:
        Format your log as ``[INFO    1900-01-01 00:00:00]: foo``.
    ``XML``:
        Format your log as ``1900-01-01T00:00:00:INFO: foo``.
    ``COLOR``:
        Same as ``CLEAN``, but colored. Only use for console output.

        Will switch to ``CLEAN`` formatter automatically when using FileHandlers.

    About handlers:

    The `stream_handler` parameter SHOULD be one of the StreamHandlersModels, Will not create any if not specified.

    ``stdout``:
        Create a StreamHandler with stdout, Loglevel will be set to DEBUG.
    ``stderr``:
        Create a StreamHandler with stderr, Loglevel will be set to ERROR.

    The `file_handlers` parameter SHOULD be one of the ``FileHandlersModels``, Also won't create any if not specified.

    ``log_file``:
        Create a FileHandler for log file, Loglevel will be set to INFO, Create a new log file everyday and keep for 1*30 days.
    ``error_log``:
        Create a FileHandler for error log, Loglevel will be set to INFO, Create a new error log file every 30 days and keep for 30*12 days.

    :param str name: Name to use for the logger.
    :param FormattersModels formatter: Formatter to use for the logger.
    :param StreamHandlersModels|None stream_handlers: Name of StreamHandler to use for the logger.
    :param dict[FileHandlersModels, str] file_handlers: Name-Path pair of FileHandlers to use for the logger.
    :return: Configured logger.
    :rtype: `logging.Logger`
    '''
    logger = getLogger(name)
    logger.setLevel('INFO')
    
    fmt: logging.Formatter = getattr(Formatters, formatter)
    if stream_handler:
        handler = getattr(Handlers, stream_handler)(formatter=fmt)
        logger.addHandler(handler)

    if formatter == 'COLOR':
        fmt = Formatters.CLEAN
    for key, path in file_handlers.items():
        handler = getattr(Handlers, key)(formatter=fmt, path = path)
        logger.addHandler(handler)
    
    return logger
    
def yamlConfig(path: str) -> None:
    '''
    Read and configure logging from a YAML file.

    :param str path: Path of the YAML file.
    '''
    with open(path, 'r') as stream:
        config = safe_load(stream)
    dictConfig(config=config)