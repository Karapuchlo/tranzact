import json
import logging
from logging_config import logger_utils
import os
import pandas as pd
import re


logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Получение логгера
logger_utils = logging.getLogger(__name__)

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
    """111
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

def search_in_transactions(transactions, search_string):
    """
    Функция, которая принимает список словарей с данными о банковских операциях
    и строку поиска, а возвращает список словарей, у которых в описании есть данная строка.
    """
    result = []
    for transaction in transactions:
        if re.search(search_string, transaction["description"], re.IGNORECASE):
            result.append(transaction)
    return result

def count_categories(transactions, categories):
    """
    Функция, которая принимает список словарей с данными о банковских операциях
    и список категорий операций, а возвращает словарь, в котором ключи — это
    названия категорий, а значения — это количество операций в каждой категории.
    """
    category_counts = {category: 0 for category in categories}
    for transaction in transactions:
        for category in categories:
            if re.search(category, transaction["description"], re.IGNORECASE):
                category_counts[category] += 1
                break
    return category_counts

