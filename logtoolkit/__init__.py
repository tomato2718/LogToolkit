'''
A toolkit let you set up logging easier.
'''

__all__ = [
    'types',
    'models',
    'quickConfig',
    'getLogger',
    'yamlConfig',
    'ColorfulFormatter',
]

from . import types
from . import models
from ._logtoolkit import (
    getLogger,
    quickConfig,
    yamlConfig,
)
from ._formatters import (
    ColorfulFormatter
)