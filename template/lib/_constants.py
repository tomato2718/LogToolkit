'''
Constants module.
'''
from .toolbox.metaclasses import PathMeta

class Path(metaclass = PathMeta):
    CONFIG = 'conf/configs.yml'
    LOGGING_CONFIG = 'conf/logging_config.yml'