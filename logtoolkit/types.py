'''
Specific types used in logtoolkit module.
'''

__all__ = [
    'FormatStyle',
    'LogLevel',
    'FormattersModels',
    'StreamHandlersModels',
    'FileHandlersModels',
    'ColorName',
]

from typing import (
    Literal,
    TypeAlias,
)

FormatStyle: TypeAlias = Literal["%", "{", "$"]

LogLevel: TypeAlias = Literal[
    'DEBUG',
    'INFO',
    'WARNING',
    'ERROR',
    'CRITICAL',
]

FormattersModels: TypeAlias = Literal[
    'CLEAN',
    'XML',
    'COLOR',
]

StreamHandlersModels: TypeAlias = Literal[
    'stdout',
    'stderr',
]

FileHandlersModels: TypeAlias = Literal[
    'log_file',
    'error_log',
]

ColorName: TypeAlias = Literal[
    'BLACK',
    'RED',
    'GREEN',
    'YELLOW',
    'BLUE',
    'MAGENTA',
    'CYAN',
    'WHITE',
    'BRIGHT_BLACK',
    'BRIGHT_RED',
    'BRIGHT_GREEN',
    'BRIGHT_YELLOW',
    'BRIGHT_BLUE',
    'BRIGHT_MAGENTA',
    'BRIGHT_CYAN',
    'BRIGHT_WHITE',
]