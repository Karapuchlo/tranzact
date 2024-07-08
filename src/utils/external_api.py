import os
from venv import logger
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction):
    """
    Функция, которая принимает на вход словарь с данными о финансовой транзакции
    и возвращает сумму транзакции, конвертированную в рубли.
    """
    try:
        amount = float(transaction['operationAmount']['amount'])
        currency_code = transaction['operationAmount']['currency']['code']

        if currency_code != 'RUB':
            api_key = os.getenv('EXCHANGE_RATES_API_KEY')
            if api_key is None:
                raise ValueError('API key not found in environment variables')

            url = f'http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&base={currency_code}&symbols=RUB'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                rate = data['rates']['RUB']
                return float(amount) * rate
            else:
                return 0.0
            pass

        return amount
    except (KeyError, ValueError) as e:
        logger.error(f"Error converting transaction amount to RUB: {e}")
        return 0.0
