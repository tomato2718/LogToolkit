'''
Not for import, import Global instead.
'''

__all__ = ['Global']
from typing import Any

class Global:
    '''
    Class to store global variable for whole program.
    '''
    @classmethod
    def set_global(cls, container: str, content: Any) -> None:
        '''
        Store global variable.

        :param str container: Name of global variable.
        :param Any content: Value of global variable.
        '''
        setattr(cls, container, content)

    @classmethod
    def get_global(cls, container: str) -> Any:
        '''
        Get global variable.

        :param str container: Name of global variable.
        :return: Requested global variable.
        :rtype: `Any`
        '''
        return getattr(cls, container)