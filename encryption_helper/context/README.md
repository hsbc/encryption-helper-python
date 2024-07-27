<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img src="https://www.hsbc.com/-/files/hsbc/header/hsbc-logo-200x25.svg" alt="HSBC Logo" width="200" title="HSBC Logo">
</p>

<h1 align="center">Encryption Helper Python</h1>

<p align="center">
  <img src="../../assets/banner.jpg" alt="Encryption Helper Banner">
</p>

<h2 align="center">Context Module</h2>

<p align="center">
  <strong>Context module for the encryption_helper package.</strong>
</p>

<p align="center">
  <a href="#classes">Classes</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>
<!-- markdownlint-enable MD033 MD041 -->

## Classes

The `context.py` module provides a `Context` class for managing application-wide settings and logging. It implements the Singleton pattern to ensure only one instance of the context exists.

### Context

A singleton class for managing application context and logging.

#### Attributes

- **_instance** (Optional[Context]): The singleton instance of the Context class.
- **name** (str): The name of the application context, used for logging.
- **log_level** (int): The current logging level.
- **logger** (Optional[logging.Logger]): The logger instance for the context.

### Methods

- `__new__(cls) -> Context`: Creates and returns the singleton instance of the Context class.
- `get_instance(cls) -> Context`: Gets the singleton instance of the Context class.
- `set_name(self, name: str) -> None`: Sets the name of the context.
- `set_log_level(self, log_level: Optional[str]) -> None`: Sets the logging level for the context.
- `init_logging(self) -> None`: Initializes the logger for the context.
- `get_logger(self) -> logging.Logger`: Gets the logger for the context, initializing it if necessary.

## Usage

This module defines a `Context` class for managing application-wide settings and logging.

### Example

```python
from encryption_helper.context.context import Context

# Get the singleton instance of the Context class
context = Context.get_instance()

# Set the name and logging level of the context
context.set_name('my_app')
context.set_log_level('DEBUG')

# Get the logger instance and log a message
logger = context.get_logger()
logger.debug('This is a debug message')
```

## License

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.