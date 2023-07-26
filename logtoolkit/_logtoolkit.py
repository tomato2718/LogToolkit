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

from ._models import (
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
                stream_handlers: set[StreamHandlersModels],
                file_handlers: dict[FileHandlersModels, str],
                )-> logging.Logger:
    '''
    Configure logger using templates. This function also return the logger with specified name.

    The formatter parameter MUST be one of the ``FormattersModels``, see ``logtoolkit.types.FormattersModels``.

    The handlers parameter MUST be a set of the ``HandlersModels``, see ``logtoolkit.types.HandlersModels``.

    :param str name: Name to use for the logger.
    :param FormattersModels formatter: Formatter to use for the logger.
    :param set[StreamHandlersModels] stream_handlers: Name of StreamHandlers to use for the logger.
    :param dict[FileHandlersModels, str] file_handlers: Name-Path pair of FileHandlers to use for the logger.
    :return: Configured logger.
    :rtype: `logging.Logger`
    '''
    logger = getLogger(name)
    logger.setLevel('INFO')
    
    fmt: logging.Formatter = getattr(Formatters, formatter)
    for name in stream_handlers:
        handler = getattr(Handlers, name)(formatter=fmt)
        logger.addHandler(handler)

    if formatter == 'COLOR':
        fmt = Formatters.CLEAN
    for name, path in file_handlers.items():
        handler = getattr(Handlers, name)(formatter=fmt, path = path)
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