<p align="center">
  <img src="https://www.hsbc.com/-/files/hsbc/header/hsbc-logo-200x25.svg" alt="HSBC Logo" width="200" title="HSBC Logo">
</p>

<h1 align="center">Encryption Helper Python - Strings Module</h1>

<p align="center">
  <img src="../../assets/banner.jpg" alt="Encryption Helper Banner">
</p>

<p align="center">
  <strong>Strings module for the encryption_helper package.</strong>
</p>

<p align="center">
  <a href="#attributes">Attributes</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>

## Attributes

The `strings.py` module provides a collection of string constants used throughout the `encryption_helper` package. These constants include file suffixes for various key and encrypted file types.

- **private_key_suffix**: The file suffix for private key files.
- **public_key_suffix**: The file suffix for public key files.
- **encrypted_file_suffix**: The file suffix for encrypted files.

## Usage

This module defines string constants for use in the `encryption_helper` package. These constants help standardize file naming conventions across the package.

### Example

```python
from encryption_helper.common.strings import private_key_suffix, public_key_suffix, encrypted_file_suffix

print(private_key_suffix)  # Output: private-key.pem
print(public_key_suffix)   # Output: public_key.pem
print(encrypted_file_suffix)  # Output: .bin
```

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
