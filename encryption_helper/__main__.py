"""
Main entry point for the encryption_helper package when run as a module.

This module allows the package to be executed directly, demonstrating
the key generation functionality for RSA and for post quantum algorithms.
"""

import sys
import argparse
from encryption_helper.main import (
    generate_rsa_key,
    generate_mldsa_key,
    generate_mlkem_key,
)


def main(argv=None):
    """
    Execute the main function of the encryption_helper package.

    This function serves as the entry point when the package is run as a script.
    It generates a key pair for the chosen algorithm and prints a success message
    along with key information. The default algorithm is RSA so the behaviour
    without arguments is unchanged.

    Args:
        argv (list): Optional list of command line arguments. When it is None the
            arguments are read from the process command line.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        prog="encryption-helper",
        description="Generate a public and private key pair.",
    )
    parser.add_argument(
        "--algorithm",
        choices=["rsa", "ml-dsa", "ml-kem"],
        default="rsa",
        help="the key algorithm to generate",
    )
    args, _ = parser.parse_known_args(argv)

    generators = {
        "rsa": (generate_rsa_key, "RSA"),
        "ml-dsa": (generate_mldsa_key, "ML-DSA-65"),
        "ml-kem": (generate_mlkem_key, "ML-KEM-768"),
    }
    generate, label = generators[args.algorithm]

    print("Running encryption_helper...")
    try:
        public_key, private_key = generate()
        print(f"{label} key pair generated successfully.")
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
