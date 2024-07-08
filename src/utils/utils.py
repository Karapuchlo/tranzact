import json
import logging
from logging_config import logger_utils

def load_transactions(file_path):
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error loading transactions from {file_path}: {e}")
        return []



def another_function():
    logger_utils.debug('This is a debug message from utils module')
    logger_utils.info('This is an info message from utils module')
    logger_utils.warning('This is a warning message from utils module')
    logger_utils.error('This is an error message from utils module')
    logger_utils.critical('This is a critical message from utils module')
