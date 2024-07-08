import logging
from logging_config import logger_masks

def some_function():
    logger_masks.debug('This is a debug message from masks module')
    logger_masks.info('This is an info message from masks module')
    logger_masks.warning('This is a warning message from masks module')
    logger_masks.error('This is an error message from masks module')
    logger_masks.critical('This is a critical message from masks module')
