import os
from rsa.utils.checks import checks
from rsa.context import context


def read_text_in_binary_mode(directory, file_name):
    logger = context.Context.getinstance().get_logger()
    if checks.str_none_or_empty(directory, file_name):
        logger.exception('One or more arguments are empty')
        raise Exception('One or more arguments are empty')

    absolute_file_path = os.path.join(directory, file_name)
    return read_text_in_binary_mode_abs(absolute_file_path)


def read_text_in_binary_mode_abs(absolute_file_path):
    logger = context.Context.getinstance().get_logger()
    if checks.str_none_or_empty(absolute_file_path):
        logger.exception('One or more arguments are empty')
        raise Exception('One or more arguments are empty')

    logger.info('Reading from file : {0}'.format(absolute_file_path))
    with open(absolute_file_path, "rb") as f:
        return f.read()
