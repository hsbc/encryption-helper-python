"""
Main entry point for the encryption_helper package when run as a module.

This module allows the package to be executed directly, demonstrating
the key generation functionality.
"""

import sys
from encryption_helper.main import generate_rsa_key


def main():
    """
    Execute the main function of the encryption_helper package.

    This function serves as the entry point when the package is run as a script.
    It generates an RSA key pair and prints a success message along with key information.

    Returns:
        None
    """
    print("Running encryption_helper...")
    try:
        public_key, private_key = generate_rsa_key()
        print("RSA key pair generated successfully.")
        print(f"Public key length: {len(public_key)} bytes")
        print(f"Private key length: {len(private_key)} bytes")
        print("The keys have been saved in the 'keys/pem' directory.")
    except OSError as e:
        print(f"An error occurred while writing the key files: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"An error occurred with the key generation parameters: {e}")
        sys.exit(1)
    except ImportError as e:
        print(f"An error occurred while importing required modules: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please report this issue to the maintainers.")
        sys.exit(1)


if __name__ == "__main__":
    main()
