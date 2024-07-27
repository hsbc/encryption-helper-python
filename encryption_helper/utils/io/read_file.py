"""
Read File module for the encryption_helper package.

This module provides functions to read text files in binary mode. It includes 
functions to read files given a directory and file name or an absolute file path.

Functions:
    read_text_in_binary_mode: Reads a file in binary mode given a directory and file name.
    read_text_in_binary_mode_abs: Reads a file in binary mode given an absolute file path.
"""

import os
from encryption_helper.utils.checks import checks
from encryption_helper.context import context


def read_text_in_binary_mode(directory, file_name):
    """
    Read a file in binary mode given a directory and file name.

    This function constructs the absolute file path from the given directory and file name,
    checks if the inputs are valid, and reads the file in binary mode.

    Args:
        directory (str): The directory containing the file.
        file_name (str): The name of the file to be read.

    Returns:
        bytes: The contents of the file in binary mode.

    Raises:
        Exception: If one or more arguments are empty.
        OSError: If there is an error reading the file.

    Examples:
        >>> data = read_text_in_binary_mode('path/to/dir', 'file.txt')
        >>> print(data)

    """
    logger = context.Context.get_instance().get_logger()
    if checks.str_none_or_empty(directory, file_name):
        logger.exception("One or more arguments are empty")
        raise Exception("One or more arguments are empty")

    absolute_file_path = os.path.join(directory, file_name)
    return read_text_in_binary_mode_abs(absolute_file_path)


def read_text_in_binary_mode_abs(absolute_file_path):
    """
    Read a file in binary mode given an absolute file path.

    This function checks if the input is valid and reads the file in binary mode.

    Args:
        absolute_file_path (str): The absolute path to the file to be read.

    Returns:
        bytes: The contents of the file in binary mode.

    Raises:
        Exception: If the argument is empty.
        OSError: If there is an error reading the file.

    Examples:
        >>> data = read_text_in_binary_mode_abs('/path/to/dir/file.txt')
        >>> print(data)

    """
    logger = context.Context.get_instance().get_logger()
    if checks.str_none_or_empty(absolute_file_path):
        logger.exception("One or more arguments are empty")
        raise Exception("One or more arguments are empty")

    logger.info("Reading from file : {0}".format(absolute_file_path))
    with open(absolute_file_path, "rb") as f:
        return f.read()
