'''
Not for import.
'''

__all__ = ['Style']

from typing import Any

class StyleMeta(type):
    '''
    Meta class of Style.*.
    '''
    def __getattribute__(self, __name: str) -> Any:
        res = object.__getattribute__(self, __name)
        if isinstance(res, str):
            res = '\033[' + res + 'm'
        return res

    def _getvalue(self, __name: str) -> Any:
        '''
        Return requested value, '' if key not exist.
        '''
        if hasattr(self, __name):
            return object.__getattribute__(self, __name)
        else:
            return ''

class Style:
    '''
    A class store Select Graphic Rendition as constants to modify stdout.

    Usage::

        >>> print(Style.Font.BOLD + 'hello, world!' + Style.RESET_ALL)
        >>> print(Style(font=['ITALIC', 'STRIKE'], foreground='CYAN', background='RED') + 'hello, world' + Style.RESET_ALL)
    '''
    RESET_ALL = '\033[0m'
    RESET_FG   = '\033[39m'
    RESET_BG   = '\033[49m'
    
    def __new__(cls, font: list=[], fg: str=None, bg: str=None) -> str:
        res = []
        for style in font:
            res.append(cls.Font._getvalue(style))
        if fg:
            res.append(cls.FG._getvalue(fg))
        if bg:
            res.append(cls.BG._getvalue(bg))
        res = ';'.join(res)
        return '\033[' + res + 'm'
    

    def __init__(self, font: list=[], fg: str=None, bg: str=None) -> None:
        '''
        Contructor method.

        :param list font: List of font style name.
        :param str fg: Name of foreground color.
        :param str bg: Name of background color.
        :return: Code generated.
        :rtype: `str`
        '''
        pass
    
    class Font(metaclass = StyleMeta):
        '''
        Font style.

        Members:

            - BOLD
            - DIM
            - ITALIC
            - UNDERLINE
            - STRIKE
            - NORMAL
            - DOUBLE_UNDERLINE
        '''
        BOLD      = '1'
        DIM       = '2'
        ITALIC    = '3'
        UNDERLINE = '4'
        STRIKE    = '9'
        NORMAL    = '22'
        DOUBLE_UNDERLINE = '21'

    class FG(metaclass = StyleMeta):
        '''
        Foreground Colors.

        Members:

            - (BRIGHT_)BLACK
            - (BRIGHT_)RED
            - (BRIGHT_)GREEN
            - (BRIGHT_)YELLOW
            - (BRIGHT_)BLUE
            - (BRIGHT_)MAGENTA
            - (BRIGHT_)CYAN
            - (BRIGHT_)WHITE
        '''
        BLACK   = '30'
        RED     = '31'
        GREEN   = '32'
        YELLOW  = '33'
        BLUE    = '34'
        MAGENTA = '35'
        CYAN    = '36'
        WHITE   = '37'
        BRIGHT_BLACK   = '90'
        BRIGHT_RED     = '91'
        BRIGHT_GREEN   = '92'
        BRIGHT_YELLOW  = '93'
        BRIGHT_BLUE    = '94'
        BRIGHT_MAGENTA = '95'
        BRIGHT_CYAN    = '96'
        BRIGHT_WHITE   = '97'

    class BG(metaclass = StyleMeta):
        '''
        Background Colors.

        Members:
        
            - (BRIGHT_)BLACK
            - (BRIGHT_)RED
            - (BRIGHT_)GREEN
            - (BRIGHT_)YELLOW
            - (BRIGHT_)BLUE
            - (BRIGHT_)MAGENTA
            - (BRIGHT_)CYAN
            - (BRIGHT_)WHITE
        '''
        BLACK   = '40'
        RED     = '41'
        GREEN   = '42'
        YELLOW  = '43'
        BLUE    = '44'
        MAGENTA = '45'
        CYAN    = '46'
        WHITE   = '47'
        BRIGHT_BLACK   = '100'
        BRIGHT_RED     = '101'
        BRIGHT_GREEN   = '102'
        BRIGHT_YELLOW  = '103'
        BRIGHT_BLUE    = '104'
        BRIGHT_MAGENTA = '105'
        BRIGHT_CYAN    = '106'
        BRIGHT_WHITE   = '107'