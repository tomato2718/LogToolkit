'''
Module to create argument parser.
'''

__all__ = ['arg_parser']

import argparse

from . import __about__

def arg_parser() -> argparse.ArgumentParser:
    '''
    Create argument parser for the project.
    
    :return: The parser created.
    :rtype: `argparse.ArgumentParser`
    '''
    parser = argparse.ArgumentParser(
        prog=__about__.__project__,
        description=__about__.__doc__,
        epilog=__about__.__usage__,
        add_help=False,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Program informations
    information = parser.add_argument_group('Program Informations')
    information.add_argument(
        '--help', '-h',
        action='help',
        help='Show this help message and exit.'
    )
    
    return parser