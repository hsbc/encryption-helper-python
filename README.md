<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <img src="https://www.hsbc.com/-/files/hsbc/header/hsbc-logo-200x25.svg" alt="HSBC Logo" width="200" title="HSBC Logo">
</p>

<h1 align="center">Encryption Helper Python</h1>

<p align="center">
  <img src="./assets/banner.jpg" alt="Encryption Helper Banner">
</p>

<p align="center">
  <strong>A Python CLI application for generating RSA public and private key pairs using the cryptography library</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#post-quantum-keys">Post quantum keys</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#development">Development</a> •
  <a href="#license">License</a>
</p>
<!-- markdownlint-enable MD033 MD041 -->

## Features

Encryption Helper is a robust Python package designed to simplify the process of creating RSA key pairs. It leverages the [cryptography][0] library to offer:

- Generation of 2048-bit RSA key pairs
- Generation of ML-DSA and ML-KEM post quantum key pairs that follow the NIST standards
- Automatic saving of keys in PEM format
- Logging of key generation for debugging purposes
- Simple CLI interface for ease of use

## Installation

This package requires Python 3.8 or later and uses cryptography for cryptographic operations.

### Using Poetry (recommended)

Ensure you have Poetry installed, then follow these steps:

```bash
# Clone the repository
git clone https://github.com/hsbc/encryption-helper-python.git
cd encryption-helper-python

# Install dependencies (including cryptography)
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

# Install the package and its dependencies (including cryptography)
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

- Use cryptography to generate a 2048-bit RSA key pair
- Save the private key to `keys/pem/private-key.pem`
- Save the public key to `keys/pem/public-key.pem`
- Display both keys in the console
- Log the key generation process

## Post quantum keys

Encryption Helper can also generate post quantum key pairs for teams that are preparing for the quantum migration. The algorithms follow the NIST post quantum standards.

- ML-DSA-65 is the module lattice digital signature scheme from FIPS 204 and it fits settlement signing and document signing
- ML-KEM-768 is the module lattice key encapsulation mechanism from FIPS 203 and it fits key establishment and data protection

To generate an ML-DSA key pair run the command with the algorithm flag.

```bash
encryption-helper --algorithm ml-dsa
```

To generate an ML-KEM key pair use the same flag with the other value.

```bash
encryption-helper --algorithm ml-kem
```

The private key is written with owner only permissions and it is never printed to the console or written to the debug log. Only the public key and the private key path are shown. The keys are saved under `keys/pem` with a name that identifies the algorithm.

Post quantum generation needs cryptography 47 or newer built against OpenSSL 3.5 or newer. On an older build the tool reports that the algorithm is not available and the RSA path keeps working as before.

## Configuration

The key generation process uses cryptography with the following specifications:

- Standard: PKCS#1
- Type: RSA
- Size: 2048 bits

To modify these settings, you'll need to edit the `generate_rsa_key()` function in `encryption_helper/main.py`. Refer to the cryptography documentation for more advanced configurations.

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


[0]: https://github.com/pyca/cryptography