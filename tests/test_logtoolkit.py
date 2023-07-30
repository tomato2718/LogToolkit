from logging import StreamHandler

import pytest

from logtoolkit._logtoolkit import (
    quickConfig,
)

##### FIXTURES #####

##### TESTS #####
def test_quickConfig():
    logger = quickConfig(
        name='test1',
        formatter='CLEAN',
        stream_handler='stdout'
    )
    assert isinstance(logger.handlers[0], StreamHandler)