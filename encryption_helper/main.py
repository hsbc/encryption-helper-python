"""
Main module for the encryption_helper package.

This module contains the primary functionality for generating RSA key pairs.
It handles the generation process, file I/O operations, and logging.
"""

from pathlib import Path
from typing import Tuple
from Crypto.PublicKey import RSA
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
        key_pair = RSA.generate(2048)

        # Export the private key
        private_key = key_pair.export_key(
            format="PEM",
            # passphrase="1password",  # Uncomment if you want to use a passphrase
            # pkcs=1,
            # protection="scryptAndAES256-CBC",
        )

        # Export the public key
        public_key = key_pair.publickey().export_key(format="PEM")

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


if __name__ == "__main__":
    generate_rsa_key()
