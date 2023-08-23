'''
Informations about the project.
'''

__all__ = [
    '__project__',
    '__version__',
    '__author__',
    '__maintainer__',
    '__release__',
    '__summary__',
    '__usage__'
]

__project__ = 'LogToolkit'
__version__ = '1.0.1'
__author__ = 'yveschen2718@gmail.com'
__maintainer__ = 'yveschen2718@gmail.com'
__release__ = '2023/07/30'
__summary__ = 'A toolkit let you set up logging easier.'
__usage__ = '''
Usage:
    >>> from logtoolkit import quickConfig 
    >>> logger = quickConfig(
            name = __name__,
            formatter='COLOR',
            stream_handler='stdout',
            file_handlers={
                'log_file': './logtoolkit.log',
                'error_log': './logtoolkit.error.log'
            }
        )
    >>> logger.info('Hello, World!')
'''