"""
encryption_helper package.

This package provides utilities for generating RSA public and private key
pairs. It includes functions for key generation, file I/O operations, and context management.

Modules:
    main: Contains the primary function for RSA key generation.
    context: Provides context management for the application.
    utils: Contains utility functions for file operations and checks.

Functions:
    generate_rsa_key: Generates an RSA public/private key pair.

Version: 0.0.1
"""

from .main import generate_rsa_key

__version__ = "0.0.1"
__all__ = ["generate_rsa_key"]
