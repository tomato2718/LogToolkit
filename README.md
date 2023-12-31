# LogToolkit
## Summary
A toolkit let you set up logging easier.

![example]

## Requirements
### System
- `python >= 3.10.10`

### Python
- `PyYAML >= 6.0`


## Setup
### Installation
- Install with Python pip
```sh
>>> pip install logtoolkit-1.0.2-py3-none-any.whl
```

## Usage
### Start Up
- Import this Project as a module.

```py
from logtoolkit import (
    types,
    models,
    quickConfig,
    getLogger,
    yamlConfig,
    ColorfulFormatter,
)

logger = quickConfig(
    name = __name__,
    formatter='COLOR',
    stream_handler='stdout',
    file_handlers={
        'log_file': './logtoolkit.log',
        'error_log': './logtoolkit.error.log'
    }
)

logger.info('Hello, World!')
```

## Features
### Configure your logger faster
```py
from logtoolkit import (
    quickConfig,
    getLogger,
    yamlConfig,
)

# Configure by template
logger = quickConfig(
    name = __name__,
    formatter='COLOR',
    stream_handler='stdout',
    file_handlers={
        'log_file': './logtoolkit.log',
        'error_log': './logtoolkit.error.log'
    }
)

# Configure by YAML file
# See docs/logging_config.yml for the example
yamlConfig(
    path='/path/to/config/file.yml'
)
logger = getLogger(__name__)
```

### Modify from models
```py
# The Colorful formatter use for quickConfig
from logtoolkit import (
    ColorfulFormatter,
)

class MyFormatter(ColorfulFormatter):
    pass


# Get the models use for quickConfig
from logtoolkit.models import (
    Formatters,
    Handlers,
)

fmt = Formatters.CLEAN

handler = Handlers.stdout(fmt)
handler.do_something()
```

## Run the tests
- Unit tests
```sh
>>> python -m tests
```

## Support
### Author
- `yveschen2718@gmail.com`
### Maintainer
- `yveschen2718@gmail.com`

<!--links-->

[example]: ./docs/source/example.png