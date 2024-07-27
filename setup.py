"""
Setup script for the encryption-helper package.
This script uses setuptools to define the package configuration,
including metadata, dependencies, and other installation details.
"""

from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="encryption-helper",
    version="0.0.1",
    author="Sebastien Rousseau",
    author_email="sebastien.rousseau-bedouch@hsbc.com",
    description="""
        A Python CLI application for generating RSA public and private
        key pairs
    """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hsbc/encryption-helper-python",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    install_requires=["pycryptodome==3.20.0"],
    extras_require={
        "dev": ["pytest>=7.0"],
    },
    keywords="rsa, keys, cryptography, encryption, decryption, python",
    python_requires=">=3.8",
    setup_requires=["build"],
    entry_points={
        "console_scripts": [
            "encryption-helper=encryption_helper.__main__:main",
        ],
    },
)
