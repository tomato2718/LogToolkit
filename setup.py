from importlib import import_module

from setuptools import setup, find_namespace_packages

PROJECT = 'logtoolkit'

__about__ = import_module(
    name=f'{PROJECT}.__about__',
)

metadata: dict[str, str] = {
    'name': getattr(__about__, '__project__'),
    'version': getattr(__about__, '__version__'),
    'author': getattr(__about__, '__author__'),
    'maintainer': getattr(__about__, '__maintainer__'),
    'description': getattr(__about__, '__summary__'),
}
    
with open(f'./{PROJECT}/requirements.txt', 'r') as file:
    req = file.readlines()

setup(
    **metadata,
    packages = find_namespace_packages(include=[f'{PROJECT}*']),
    include_package_data = True,
    install_requires=req,
)