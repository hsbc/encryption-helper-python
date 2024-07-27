<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img src="https://www.hsbc.com/-/files/hsbc/header/hsbc-logo-200x25.svg" alt="HSBC Logo" width="200" title="HSBC Logo">
</p>

<h1 align="center">Encryption Helper Python</h1>

<p align="center">
  <img src="../../../assets/banner.jpg" alt="Encryption Helper Banner">
</p>

<h2 align="center">I/O Modules</h2>

<p align="center">
  <strong>I/O modules for the encryption_helper package.</strong>
</p>

<p align="center">
  <a href="#read-file-functions">Read File Functions</a> •
  <a href="#write-file-functions">Write File Functions</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>
<!-- markdownlint-enable MD033 MD041 -->

## Read File Functions

The `read_file.py` module provides functions for reading text files in binary mode.

### read_text_in_binary_mode

Read text from a file in binary mode given a directory and file name.

#### Args

- **directory (str)**: The directory where the file is located.
- **file_name (str)**: The name of the file to be read.

#### Returns

- **bytes**: The content of the file read in binary mode.

#### Raises

- **Exception**: If one or more arguments are empty.
- **OSError**: If there is an error reading the file.

### read_text_in_binary_mode_abs

Read text from a file in binary mode given an absolute file path.

#### Args

- **absolute_file_path (str)**: The absolute path to the file to be read.

#### Returns

- **bytes**: The content of the file read in binary mode.

#### Raises

- **Exception**: If one or more arguments are empty.
- **OSError**: If there is an error reading the file.

## Write File Functions

The `write_file.py` module provides functions for writing text files in binary mode.

### write_text_in_binary_mode

Write text to a file in binary mode given a directory and file name.

#### Args

- **directory (str)**: The directory where the file will be written.
- **file_name (str)**: The name of the file to be written.
- **text (bytes)**: The text to be written to the file.

#### Returns

- **str**: The absolute file path of the written file.

#### Raises

- **Exception**: If one or more arguments are empty.
- **OSError**: If there is an error writing to the file.

### write_text_in_binary_mode_abs

Write text to a file in binary mode given an absolute file path.

#### Args

- **absolute_file_path (str)**: The absolute path to the file to be written.
- **text (bytes)**: The text to be written to the file.

#### Returns

- **str**: The absolute file path of the written file.

#### Raises

- **Exception**: If one or more arguments are empty.
- **OSError**: If there is an error writing to the file.

## Usage

```python
from encryption_helper.utils.io import read_file, write_file

# Read file example
content = read_file.read_text_in_binary_mode('/path/to/directory', 'file.txt')
print(content)

# Write file example
path = write_file.write_text_in_binary_mode('/path/to/directory', 'file.txt', b'test data')
print(path)
```

## License

This project is licensed under the MIT License. See the [LICENSE](../../../LICENSE) file for details.
