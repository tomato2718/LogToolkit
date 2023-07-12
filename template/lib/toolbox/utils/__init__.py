'''
Some useful tools.
'''
__all__ = ['ReadFile',
           'get_abs_path',
           'parse_unknown_args']

from ._reader import ReadFile
from ._parser import parse_unknown_args
from ._path_helper import get_abs_path