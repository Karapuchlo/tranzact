import json
import logging
from logging_config import logger_utils
import os
import pandas as pd

def get_file_format(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.csv':
        return 'csv'
    elif file_extension.lower() == '.xlsx':
        return 'xlsx'
    else:
        return 'json'

def read_data(file_path):
    file_format = get_file_format(file_path)
    if file_format == 'csv':
        return pd.read_csv(file_path)
    elif file_format == 'xlsx':
        return pd.read_excel(file_path)
    else:
        return pd.read_json(file_path)

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
