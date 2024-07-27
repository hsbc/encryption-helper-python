<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img src="https://www.hsbc.com/-/files/hsbc/header/hsbc-logo-200x25.svg" alt="HSBC Logo" width="200" title="HSBC Logo">
</p>

<h1 align="center">Encryption Helper Python</h1>

<p align="center">
  <img src="../../../assets/banner.jpg" alt="Encryption Helper Banner">
</p>

<h2 align="center">Checks Module</h2>

<p align="center">
  <strong>Checks module for the encryption_helper package.</strong>
</p>

<p align="center">
  <a href="#functions">Functions</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>
<!-- markdownlint-enable MD033 MD041 -->

## Functions

The `checks.py` module provides utility functions for input validation.

### str_none_or_empty

Check if one or more input strings are `None` or empty.

#### Args

- **argv (str)**: A variable number of string arguments to be checked.

#### Returns

- **bool**: `True` if any of the input strings is `None` or empty; otherwise `False`.

#### Examples

```python
from encryption_helper.utils.checks import str_none_or_empty

print(str_none_or_empty('test', 'hello', 'world'))  # Output: False
print(str_none_or_empty('test', None, 'world'))     # Output: True
print(str_none_or_empty('test', '', 'world'))       # Output: True
print(str_none_or_empty('test', '   ', 'world'))    # Output: True
print(str_none_or_empty())                          # Output: False
```

## License

This project is licensed under the MIT License. See the [LICENSE](../../../LICENSE) file for details.
