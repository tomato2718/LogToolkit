'''
Not for import.
'''

__all__ = [
    'ColorfulFormatter',
]

from collections import defaultdict
from typing import Any, Mapping
from logging import (
    Formatter,
    LogRecord,
)

from ._constants import (
    Color,
)
from .types import (
    LogLevel,
    FormatStyle,
    ColorName,
)

class ColorfulFormatter(Formatter):
    '''
    Custom formatter to color your logger.

    Usage::

        >>> cfmt = ColorfulFormatter(
                colors={
                    'DEBUG': 'CYAN',
                    'WARNING': 'YELLOW',
                    'ERROR': 'RED',
                    'CRITICAL': 'BRIGHT_RED'
                },
                fmt='[%(levelname)-5s %(asctime)s]: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
            )
        >>> handler = StreamHandler()
        >>> handler.setFormatter(cfmt)
    '''
    _format: defaultdict[str, str] = defaultdict(lambda: '{record}')
    def __init__(self,
                 colors: dict[LogLevel, ColorName],
                 fmt: str | None = None,
                 datefmt: str | None = None,
                 style: FormatStyle = "%",
                 validate: bool = True,
                 *,
                 defaults: Mapping[str, Any] | None = None
                 ) -> None:
        '''
        Constructor method.

        The colors parameter SHOULD be as follow::

            {
                'DEBUG': 'CYAN',
                'WARNING': 'YELLOW',
                'ERROR': 'RED',
                'CRITICAL': 'BRIGHT_RED'
            }

        The key of colors MUST be log level in capitalize string, basically:
            ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, ``CRITICAL``

        The value of colors MUST be one of the color, see `logtoolkit.types.ColorName`. 

        About other parameters:
            See `logging.Formatter` documentation for more information.

        :param dict[LogLevel, ColorName] colors: Key-value pair of the color to use for each level.
        :param str|None fmt: The format to use in formatter.
        :param str|None datefmt: The date format to use in formatter.
        :param FormatStyle style: The style parameter use for formatting.
        :param bool validate: Valid the input format or not.
        :param Mapping[str, Any] defaults: Assign extra parameter to `fmt`.
        '''
        for level, color in colors.items():
            if hasattr(Color, color):
                self._format[level] = getattr(Color, color) + '{record}' + Color.RESET
        super().__init__(fmt, datefmt, style, validate, defaults=defaults)

    def format(self, record: LogRecord) -> str:
        return self._format[record.levelname].format(record=super().format(record))