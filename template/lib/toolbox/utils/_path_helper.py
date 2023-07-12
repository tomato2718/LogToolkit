'''
Not for import.
'''

__all__ = ['get_abs_path']

import os
from sys import argv

def get_abs_path(path: str) -> str:
    '''
    Get absolute path of relative path.

    :param str path_: Relative path.
    :return: Absolute path of input.
    :rtype: `str`
    '''
    return os.path.join(os.path.dirname(argv[0]), path)