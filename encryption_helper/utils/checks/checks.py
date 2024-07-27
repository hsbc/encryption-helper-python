"""
Checks module for the encryption_helper package.

This module provides utility functions to validate input strings. It includes 
functions to check if strings are `None` or empty.

Functions:
    str_none_or_empty: Checks if one or more input strings are `None` or empty.
"""


def str_none_or_empty(*argv):
    """
    Check if one or more input strings are `None` or empty.

    This function takes a variable number of string arguments and checks each
    one to determine if it is either `None` or an empty string (including strings
    that are only whitespace).

    Args:
        *argv: A variable number of string arguments to be checked.

    Returns:
        bool: `True` if any of the input strings is `None` or empty; otherwise `False`.

    Examples:
        >>> str_none_or_empty('test', 'hello', 'world')
        False
        >>> str_none_or_empty('test', None, 'world')
        True
        >>> str_none_or_empty('test', '', 'world')
        True
        >>> str_none_or_empty('test', '   ', 'world')
        True
        >>> str_none_or_empty()
        False
    """
    for arg in argv:
        if arg is None or not isinstance(arg, str) or len(arg.strip()) == 0:
            return True
    return False
