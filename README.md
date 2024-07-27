<p align="center">
  <img src="https://www.hsbc.com/-/files/hsbc/header/hsbc-logo-200x25.svg" alt="HSBC Logo" width="200" title="HSBC Logo">
</p>

<h1 align="center">Encryption Helper Python</h1>

<p align="center">
  <img src="./assets/banner.jpg" alt="Encryption Helper Banner">
</p>

<p align="center">
  <strong>A Python CLI application for generating RSA public and private key pairs using PyCryptodome</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#development">Development</a> •
  <a href="#license">License</a>
</p>

## Features

Encryption Helper is a robust Python package designed to simplify the process of creating RSA key pairs. It leverages the PyCryptodome library to offer:

- Generation of 2048-bit RSA key pairs
- Automatic saving of keys in PEM format
- Logging of key generation for debugging purposes
- Simple CLI interface for ease of use

## Installation

This package requires Python 3.8 or later and uses PyCryptodome for cryptographic operations.

### Using Poetry (recommended)

Ensure you have Poetry installed, then follow these steps:

```bash
# Clone the repository
git clone https://github.com/hsbc/encryption-helper-python.git
cd encryption-helper-python

# Install dependencies (including PyCryptodome)
poetry install
```

### Using pip

If you prefer to use pip:

```bash
# Clone the repository
git clone https://github.com/hsbc/encryption-helper-python.git
cd encryption-helper-python

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the package and its dependencies (including PyCryptodome)
pip install .
```

## Usage

### With Poetry

To generate an RSA key pair using Poetry:

```bash
poetry run encryption-helper
```

### With standard Python

If you installed the package using pip:

```bash
# If you're using a virtual environment, make sure it's activated
encryption-helper
```

Or run the module directly:

```bash
python -m encryption_helper
```

These commands will:

- Use PyCryptodome to generate a 2048-bit RSA key pair
- Save the private key to `keys/pem/private-key.pem`
- Save the public key to `keys/pem/public-key.pem`
- Display both keys in the console
- Log the key generation process

## Configuration

The key generation process uses PyCryptodome with the following specifications:

- Standard: PKCS#1
- Type: RSA
- Size: 2048 bits

To modify these settings, you'll need to edit the `generate_rsa_key()` function in `encryption_helper/main.py`. Refer to the PyCryptodome documentation for more advanced configurations.

## Development

### With Poetry

To set up the development environment using Poetry:

```bash
# Create a virtual environment and install dependencies
poetry install

# Activate the virtual environment
poetry shell

# Run tests
pytest tests/

# Generate documentation
pydoc -w encryption_helper
```

### With standard Python

If you're not using Poetry:

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install development dependencies
pip install .[dev]

# Run tests
pytest tests/

# Generate documentation
pydoc -w encryption_helper
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
