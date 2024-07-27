"""
Write File module for the encryption_helper package.

This module provides functions to write text files in binary mode. It includes 
functions to write files given a directory and file name or an absolute file path.

Functions:
    write_text_in_binary_mode: Writes text to a file in binary mode given a directory and file name.
    write_text_in_binary_mode_abs: Writes text to a file in binary mode given an absolute file path.
"""

import os
from encryption_helper.utils.checks import checks
from encryption_helper.context import context


def write_text_in_binary_mode(directory, file_name, text):
    """
    Write text to a file in binary mode given a directory and file name.

    This function constructs the absolute file path from the given directory and file name,
    checks if the inputs are valid, and writes the text to the file in binary mode.

    Args:
        directory (str): The directory containing the file.
        file_name (str): The name of the file to be written.
        text (bytes): The text to be written to the file.

    Returns:
        str: The absolute file path of the written file.

    Raises:
        Exception: If one or more arguments are empty.
        OSError: If there is an error writing to the file.

    Examples:
        >>> path = write_text_in_binary_mode('path/to/dir', 'file.txt', b'test data')
        >>> print(path)

    """
    logger = context.Context.get_instance().get_logger()
    if checks.str_none_or_empty(directory, file_name, text):
        logger.exception("One or more arguments are empty")
        raise Exception("One or more arguments are empty")

    absolute_file_path = os.path.join(directory, file_name)
    return write_text_in_binary_mode_abs(absolute_file_path, text)


def write_text_in_binary_mode_abs(absolute_file_path, text):
    """
    Write text to a file in binary mode given an absolute file path.

    This function checks if the inputs are valid and writes the text to the file in binary mode.

    Args:
        absolute_file_path (str): The absolute path to the file to be written.
        text (bytes): The text to be written to the file.

    Returns:
        str: The absolute file path of the written file.

    Raises:
        Exception: If one or more arguments are empty.
        OSError: If there is an error writing to the file.

    Examples:
        >>> path = write_text_in_binary_mode_abs('/path/to/dir/file.txt', b'test data')
        >>> print(path)

    """
    logger = context.Context.get_instance().get_logger()
    if checks.str_none_or_empty(absolute_file_path, text):
        logger.exception("One or more arguments are empty")
        raise Exception("One or more arguments are empty")

    logger.info("Writing to file : {0}".format(absolute_file_path))
    with open(absolute_file_path, "wb") as f:
        f.write(text)
    logger.info("Writing to file complete")

    return absolute_file_path
