import setuptools
from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="encryption-helper",
    version="0.0.1",
    author="Sebastien Rousseau",
    author_email="sebastien.rousseau-bedouch@hsbc.com",
    description="A Python CLI application for generating RSA public and private key pairs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hsbc/encryption-helper-python",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=["cryptography"],
    keywords="rsa, keys, cryptography, encryption, decryption, python",
    python_requires=">=3.6",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
