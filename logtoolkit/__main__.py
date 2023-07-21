from json import dumps

from ._argparser import arg_parser
from .lib._constants import Path
from .lib.toolbox import LogTool, Style
from .lib.toolbox.utils import parse_unknown_args

LOGGER_COLOR = {
    'debug': Style.FG.BRIGHT_CYAN,
    'info':'',
    'warning': Style.FG.YELLOW,
    'error': Style.FG.RED,
    'critical': Style(['BOLD'], 'RED'),
}
LogTool.set_logger(Path.LOGGING_CONFIG)
LogTool.colorful_logger(__name__, **LOGGER_COLOR)
logger = LogTool.get_logger(__name__)
if __debug__:
    logger.setLevel('DEBUG')
    logger.debug('Running under DEBUG mode.')

if __name__ == '__main__':
    args, unknown = arg_parser().parse_known_args()
    unknown = parse_unknown_args(unknown)
    logger.debug(dumps(vars(args), indent=4))
    logger.debug(dumps(unknown, indent=4))