import pytest
from sys import argv

class MyPlugin:
    def pytest_sessionstart(self):
        pass
    def pytest_sessionfinish(self):
        pass


if __name__ == '__main__':
    arg = argv[1:] if argv[1:] else ['--cache-clear', '--verbose']
    pytest.main(arg, plugins=[])