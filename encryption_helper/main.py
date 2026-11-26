"""
Main module for the encryption_helper package.

This module contains the primary functionality for generating RSA key pairs and
post quantum key pairs. It handles the generation process, file I/O operations,
and logging.
"""

import os
from pathlib import Path
from typing import Tuple
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from .context import Context


def generate_rsa_key() -> Tuple[bytes, bytes]:
    """
    Generate a pair of RSA public and private keys and save them as PEM files.

    This function performs the following operations:
    1. Creates an RSA key pair (2048 bits)
    2. Saves both the public and private keys to PEM files
    3. Logs the keys for debugging purposes
    4. Prints the keys to the console

    The keys are saved in the 'keys/pem' directory relative to the current working directory.

    Returns:
        tuple: A tuple containing the generated public and private keys as bytes.
        The first element is the public key, and the second is the private key.

    Raises:
        OSError: If there's an error creating the directory or writing the key files.
        Exception: For any other unexpected errors during the key generation process.

    Example:
        >>> public_key, private_key = generate_rsa_key()
        >>> print(public_key[:20])  # Print first 20 bytes of public key
        b'-----BEGIN PUBLIC KEY'
    """
    # Get the logger instance from the Context
    logger = Context.get_instance().get_logger()

    try:
        # Generate the RSA key pair
        key_pair = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )

        # Export the private key
        private_key = key_pair.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),  # Use a passphrase if needed
        )

        # Export the public key
        public_key = key_pair.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        # Create the directory for storing keys
        keys_dir = Path("keys/pem")
        keys_dir.mkdir(parents=True, exist_ok=True)

        # Write the private key to a file
        with open(keys_dir / "private-key.pem", "wb") as file_out:
            file_out.write(private_key)

        # Write the public key to a file
        with open(keys_dir / "public-key.pem", "wb") as file_out:
            file_out.write(public_key)

        # Log the keys
        logger.debug(f"Public key:\n{public_key.decode()}\n")
        logger.debug(f"Private key:\n{private_key.decode()}\n")

        # Print the keys to console
        print("Public key:")
        print(public_key.decode())
        print("\nPrivate key:")
        print(private_key.decode())

        return public_key, private_key

    except OSError as e:
        logger.error(f"Error writing key files: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during key generation: {e}")
        raise


def generate_mldsa_key() -> Tuple[bytes, bytes]:
    """
    Generate a pair of ML-DSA public and private keys and save them as PEM files.

    ML-DSA is the module lattice digital signature algorithm standardised in FIPS
    204. This function uses the ML-DSA-65 parameter set which targets NIST
    security category 3 and fits settlement signing and document signing work.

    The private key is created with owner only file permissions and is never
    printed to the console or written to the debug log. Only the public key and
    the private key path are reported.

    Returns:
        tuple: A tuple containing the generated public and private keys as bytes.
        The first element is the public key and the second is the private key.

    Raises:
        RuntimeError: If the installed cryptography backend does not provide ML-DSA.
        OSError: If there is an error creating the directory or writing the key files.
        Exception: For any other unexpected error during the key generation process.

    Example:
        >>> public_key, private_key = generate_mldsa_key()
        >>> print(public_key[:21])  # Print first 21 bytes of public key
        b'-----BEGIN PUBLIC KEY'
    """
    # Get the logger instance from the Context
    logger = Context.get_instance().get_logger()

    try:
        from cryptography.hazmat.primitives.asymmetric import mldsa
    except ImportError as exc:
        raise RuntimeError(
            "ML-DSA requires cryptography 47 or newer built against OpenSSL 3.5 or newer"
        ) from exc

    try:
        # Generate the ML-DSA-65 key pair
        key_pair = mldsa.MLDSA65PrivateKey.generate()

        # Export the private key
        private_key = key_pair.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )

        # Export the public key
        public_key = key_pair.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        # Write the keys with the private key protected
        _, private_key_path = _write_key_pair("mldsa", public_key, private_key)

        # Log and report the public key only
        logger.debug(f"Public key:\n{public_key.decode()}\n")
        logger.info(f"Private key written to {private_key_path}")

        print("Public key:")
        print(public_key.decode())
        print(f"\nPrivate key written to {private_key_path}")

        return public_key, private_key

    except OSError as e:
        logger.error(f"Error writing key files: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during key generation: {e}")
        raise


def generate_mlkem_key() -> Tuple[bytes, bytes]:
    """
    Generate a pair of ML-KEM public and private keys and save them as PEM files.

    ML-KEM is the module lattice key encapsulation mechanism standardised in FIPS
    203. This function uses the ML-KEM-768 parameter set which targets NIST
    security category 3 and fits key establishment and data protection work.

    The private key is created with owner only file permissions and is never
    printed to the console or written to the debug log. Only the public key and
    the private key path are reported.

    Returns:
        tuple: A tuple containing the generated public and private keys as bytes.
        The first element is the public key and the second is the private key.

    Raises:
        RuntimeError: If the installed cryptography backend does not provide ML-KEM.
        OSError: If there is an error creating the directory or writing the key files.
        Exception: For any other unexpected error during the key generation process.

    Example:
        >>> public_key, private_key = generate_mlkem_key()
        >>> print(public_key[:21])  # Print first 21 bytes of public key
        b'-----BEGIN PUBLIC KEY'
    """
    # Get the logger instance from the Context
    logger = Context.get_instance().get_logger()

    try:
        from cryptography.hazmat.primitives.asymmetric import mlkem
    except ImportError as exc:
        raise RuntimeError(
            "ML-KEM requires cryptography 47 or newer built against OpenSSL 3.5 or newer"
        ) from exc

    try:
        # Generate the ML-KEM-768 key pair
        key_pair = mlkem.MLKEM768PrivateKey.generate()

        # Export the private key
        private_key = key_pair.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )

        # Export the public key
        public_key = key_pair.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        # Write the keys with the private key protected
        _, private_key_path = _write_key_pair("mlkem", public_key, private_key)

        # Log and report the public key only
        logger.debug(f"Public key:\n{public_key.decode()}\n")
        logger.info(f"Private key written to {private_key_path}")

        print("Public key:")
        print(public_key.decode())
        print(f"\nPrivate key written to {private_key_path}")

        return public_key, private_key

    except OSError as e:
        logger.error(f"Error writing key files: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during key generation: {e}")
        raise


def _write_key_pair(prefix: str, public_key: bytes, private_key: bytes) -> Tuple[Path, Path]:
    """
    Write a public and private key pair to the keys directory.

    The private key file is created with owner only permissions using os.open so
    there is no window where it is readable by group or other. The permissions
    are enforced again with os.chmod when the file already exists.

    Args:
        prefix (str): The file name prefix that identifies the algorithm.
        public_key (bytes): The public key bytes to write.
        private_key (bytes): The private key bytes to write.

    Returns:
        tuple: The public key path and the private key path.

    Raises:
        OSError: If there is an error creating the directory or writing the files.
    """
    keys_dir = Path("keys/pem")
    keys_dir.mkdir(parents=True, exist_ok=True)

    private_key_path = keys_dir / f"{prefix}-private-key.pem"
    descriptor = os.open(
        private_key_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600
    )
    with os.fdopen(descriptor, "wb") as file_out:
        file_out.write(private_key)
    os.chmod(private_key_path, 0o600)

    public_key_path = keys_dir / f"{prefix}-public-key.pem"
    with open(public_key_path, "wb") as file_out:
        file_out.write(public_key)

    return public_key_path, private_key_path


if __name__ == "__main__":
    generate_rsa_key()
