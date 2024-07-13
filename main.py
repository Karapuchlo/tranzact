from pathlib import Path
from src.utils.utils import read_data
from src.utils.external_api import convert_to_rub
from src.utils.utils import search_in_transactions, count_categories

def main():
    """хелоу
    Функция, которая отвечает за основную логику проекта и связывает функциональности между собой.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_path = Path('data/operations.json')
    transactions = read_data(file_path)

    if transactions.empty:
        print("No transactions found.")
        return

    print(f"Number of transactions: {len(transactions)}")

    # Проверяем второй объект транзакции
    first_transaction = transactions.iloc[1]
    print("transaction:")
    print(first_transaction)

    amount_in_rub = convert_to_rub(first_transaction)
    print(f"Amount in rubles: {amount_in_rub:.2f}")

    total_amount = 0.0
    for _, transaction in transactions.iterrows():
        amount_in_rub = convert_to_rub(transaction)
        total_amount += amount_in_rub

    print(f"Total amount in rubles: {total_amount:.2f}")

if __name__ == "__main__":
    main()
