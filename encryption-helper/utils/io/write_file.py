from rsa.utils.checks import checks
from rsa.context import context
import os


def write_text_in_binary_mode(directory, file_name, text):
    logger = context.Context.getinstance().get_logger()
    if checks.str_none_or_empty(directory, file_name, text):
        logger.exception('One or more arguments are empty')
        raise Exception('One or more arguments are empty')

    absolute_file_path = os.path.join(directory, file_name)
    return write_text_in_binary_mode_abs(absolute_file_path, text)


def write_text_in_binary_mode_abs(absolute_file_path, text):
    logger = context.Context.getinstance().get_logger()
    if checks.str_none_or_empty(absolute_file_path, text):
        logger.exception('One or more arguments are empty')
        raise Exception('One or more arguments are empty')

    logger.info('Writing to file : {0}'.format(absolute_file_path))
    with open(absolute_file_path, 'wb') as f:
        f.write(text)
    logger.info('Writing to file complete')

    return absolute_file_path
