from sys import stdout

from queue import Queue

from logging import (
    getLogger,
    Formatter,
)
from logging.handlers import QueueHandler

import pytest

from logtoolkit._formatters import ColorfulFormatter

##### FIXTURES #####

@pytest.fixture(
    scope='module',
)
def colorfulformatter() -> ColorfulFormatter:
    res = ColorfulFormatter(
        colors={
            'DEBUG': 'CYAN',
            'WARNING': 'YELLOW',
            'ERROR': 'RED',
            'CRITICAL': 'BRIGHT_RED',
        },
        fmt='%(message)s',
    )
    return res

@pytest.fixture(
    scope='module',
)
def formatter() -> Formatter:
    res = Formatter(
        fmt='%(message)s',
    )
    return res

##### TESTS #####

def test_ColorfulFormatter(colorfulformatter: ColorfulFormatter, formatter: Formatter):
    queue = Queue()

    handler = QueueHandler(queue)
    handler.setFormatter(formatter)
    handler.setLevel('DEBUG')

    logger = getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel('DEBUG')

    # to catch the record
    logger.debug('debug')
    record = queue.get()
    assert colorfulformatter.format(record) == '\033[36m' + 'debug' + '\033[39m'

    logger.info('info')
    record = queue.get()
    assert colorfulformatter.format(record) == 'info'

    logger.warning('warning')
    record = queue.get()
    assert colorfulformatter.format(record) == '\033[33m' + 'warning' + '\033[39m'

    logger.error('error')
    record = queue.get()
    assert colorfulformatter.format(record) == '\033[31m' + 'error' + '\033[39m'

    logger.critical('critical')
    record = queue.get()
    assert colorfulformatter.format(record) == '\033[91m' + 'critical' + '\033[39m'

