'''
Not for import.
'''

__all__ = ['ReadFile']

from typing import Any

import yaml

class ReadFile:
    '''
    File reader class.
    '''
    def __new__(cls):
        raise Exception("Don't use this as an instance")
    def __init__(self):
        '''
        Don't use this as an instance.
        '''
        pass

    @staticmethod
    def yml(path: str) -> Any:
        '''
        Read a yaml file.

        :param str path: yml file's path.
        :return: Data from yaml file.
        :rtype: `list | dict`
        '''
        with open(path, 'r') as file:
            res = yaml.safe_load(file)
        return res


