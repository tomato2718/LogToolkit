from setuptools import setup, find_namespace_packages

from template import __about__

with open('./template/requirements.txt', 'r') as file:
    req = file.readlines()

setup(
    name = __about__.__project__,
    version = __about__.__version__,
    author = __about__.__author__,
    maintainer = __about__.__maintainer__,
    description = __about__.__summary__,
    packages = find_namespace_packages(include=['template*']),
    include_package_data = True,
    install_requires=req,
)