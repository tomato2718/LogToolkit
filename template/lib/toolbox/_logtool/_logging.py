'''
Not for import.
'''

__all__ = ['LogTool']

import logging
import logging.config

from ._formatter import ColorfulFormatter
from ._utils import read_config, set_abs_path
from .._style import Style

class LogTool:
    '''
    Some tools about logging.
    '''
    @staticmethod
    def set_logger(path: str) -> None:
        '''
        Configure logging from yaml file.

        :param str path: Path of config yml.
        '''
        config_ = read_config(path)
        config_ = set_abs_path(config_, 'filename')
        logging.config.dictConfig(config_)

    @staticmethod
    def get_logger(target: str) -> logging.Logger:
        '''
        Wrapper of `logging.getLogger()`.

        :param str target: Name of the logger
        :return: Requested logger.
        :rtype: `logging.Logger`
        '''
        return logging.getLogger(target)

    @staticmethod
    def colorful_logger(target: str,
                    debug: str = '',
                    info: str = '',
                    warning: str = '',
                    error: str = '',
                    critical: str = '',
                    **kwargs) -> None:
        '''
        Color your logger, SHOULD be use with `toolbox.Style` together.

        Usage::

            >>> LOGGER_COLOR = {'debug': Style.FG.BRIGHT_CYAN,
            >>>                 'info':'',
            >>>                 'warning': Style.FG.YELLOW,
            >>>                 'error': Style.FG.RED,
            >>>                 'critical': Style(['BOLD'], 'RED'),
            >>>                 }
            >>> LogTool.colorful_logger(__name__, **LOGGER_COLOR)
            >>> logger = LogTool.get_logger(__name__)

        :param str target: The logger you want to color.
        :param str debug: Color of debug level.
        :param str info: Color of info level.
        :param str warning: Color of warning level.
        :param str error: Color of error level.
        :param str critical: Color of critical level.
        :param str ``**kwargs``: Color of your custom level.
        '''
        logger = logging.getLogger(target)
        end = Style.RESET_ALL
        for i, handler in enumerate(logger.handlers):
            if type(handler) != logging.StreamHandler:
                continue
            tmp = ColorfulFormatter(datefmt=logger.handlers[i].formatter.datefmt)
            fmt = logger.handlers[i].formatter._fmt
            format = {logging.DEBUG: debug + fmt + end,
                      logging.INFO: info + fmt + end,
                      logging.WARNING: warning + fmt + end,
                      logging.ERROR: error + fmt + end,
                      logging.CRITICAL: critical + fmt + end,
                     }
            for k, v in kwargs.items():
                format[k.upper] = v + fmt + end
            tmp.update(format)
            logger.handlers[i].formatter = tmp

