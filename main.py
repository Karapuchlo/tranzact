from pathlib import Path
from src.utils.utils import load_transactions
from src.utils.external_api import convert_to_rub

def main():
    file_path = Path('data/operations.json')
    transactions = load_transactions(file_path)

    if not transactions:
        print("No transactions found.")
        return

    print(f"Number of transactions: {len(transactions)}")

    # Проверяем второй объект транзакции
    first_transaction = transactions[1]
    print("transaction:")
    print(first_transaction)

    amount_in_rub = convert_to_rub(first_transaction)
    print(f"Amount in rubles: {amount_in_rub:.2f}")

    total_amount = 0.0
    for transaction in transactions:
        amount_in_rub = convert_to_rub(transaction)
        total_amount += amount_in_rub

    print(f"Total amount in rubles: {total_amount:.2f}")

if __name__ == "__main__":
    main()

