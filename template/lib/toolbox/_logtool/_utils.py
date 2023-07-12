'''
Not for import.
'''

__all__ = ['read_config', 'set_abs_path']

from yaml import safe_load

from ..utils import get_abs_path

def read_config(path: str) -> dict:
    '''
    Read config from yaml file.

    :param str path: Path of config yml.
    :return: The result got after parsing yaml file.
    :rtype: `dict`
    '''
    with open(path, 'r') as file:
        config = safe_load(file)
    return config

def set_abs_path(dic: dict, target: str) -> dict:
    '''
    Convert all relative path in `dict` to absolute path.

    :param dict dic: Target dict.
    :param str target: Target key.
    :return: Converted dict.
    :rtype: `dict`
    '''
    for k, v in dic.items():
        if isinstance(v, dict):
            dic[k] = set_abs_path(v, target)
        elif k == target:
            dic[k] = get_abs_path(v)
    return dic