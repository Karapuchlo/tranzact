import json
from pathlib import Path
from unittest.mock import patch
from utils.utils import load_transactions
from utils.external_api import convert_to_rub

def test_load_transactions_from_valid_file():
    file_path = Path('data/operations.json')
    transactions = load_transactions(file_path)
    assert isinstance(transactions, list)
    assert len(transactions) > 0

def test_load_transactions_from_empty_file():
    file_path = Path('data/empty.json')
    transactions = load_transactions(file_path)
    assert isinstance(transactions, list)
    assert len(transactions) == 0

def test_load_transactions_from_non_existent_file():
    file_path = Path('data/non_existent.json')
    transactions = load_transactions(file_path)
    assert isinstance(transactions, list)
    assert len(transactions) == 0

@patch('utils.external_api.requests.get')
def test_convert_to_rub_with_rub_currency(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'rates': {'RUB': 1.0}}
    transaction = {'amount': '100', 'currency': 'RUB'}
    assert convert_to_rub(transaction) == 100.0

@patch('utils.external_api.requests.get')
def test_convert_to_rub_with_usd_currency(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'rates': {'RUB': 75.0}}

    transaction = {'amount': '100', 'currency': 'USD'}
    assert convert_to_rub(transaction) == 7500.0

@patch('utils.external_api.requests.get')
def test_convert_to_rub_with_error_response(mock_get):
    mock_get.return_value.status_code = 404
    transaction = {'amount': '100', 'currency': 'USD'}
    assert convert_to_rub(transaction) == 0.0
