import os
import logging

LOG_DIR = 'logs'
LOG_FILENAME_MASKS = 'masks.log'
LOG_FILENAME_UTILS = 'utils.log'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure logger for masks module
logger_masks = logging.getLogger('masks')
logger_masks.setLevel(logging.DEBUG)

file_handler_masks = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILENAME_MASKS))
file_handler_masks.setFormatter(logging.Formatter(LOG_FORMAT))
logger_masks.addHandler(file_handler_masks)

# Configure logger for utils module
logger_utils = logging.getLogger('utils')
logger_utils.setLevel(logging.DEBUG)

file_handler_utils = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILENAME_UTILS))
file_handler_utils.setFormatter(logging.Formatter(LOG_FORMAT))
logger_utils.addHandler(file_handler_utils)
