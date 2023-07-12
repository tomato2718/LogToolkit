'''
Not for import.
'''
__all__ = ['PathMeta']
from typing import Any

from ..utils import get_abs_path

class PathMeta(type):
    '''
    Metaclass make class return abs path instead of relative path.

    Usage::
    
        class Path(metaclass = PathMeta):
            PATH = 'path/to/file/sth.txt'
    '''
    def __getattribute__(self, __name: str) -> Any:
        res = object.__getattribute__(self, __name)
        if isinstance(res, str):
            res = get_abs_path(res)
        return res