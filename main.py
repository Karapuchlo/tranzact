from pathlib import Path
from src.utils.utils import read_data
from src.utils.external_api import convert_to_rub
from src.utils.utils import search_in_transactions, count_categories
from data.loader import load_transactions_from_json, load_transactions_from_csv, load_transactions_from_xlsx

def main():
    """
    Функция, которая отвечает за основную логику проекта и связывает функциональности между собой.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    file_path = Path('data/operations.json')

    while True:
        user_input = input("Введите номер пункта меню: ")
        if user_input == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = load_transactions_from_json(file_path)
            break
        elif user_input == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = load_transactions_from_csv("transactions.csv")
            break
        elif user_input == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = load_transactions_from_xlsx("transactions.xlsx")
            break
        else:
            print("Неверный ввод. Выберите пункт меню от 1 до 3.")

            while True:
                status = input("Введите статус, по которому необходимо выполнить фильтрацию. "
                               "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper()
                if status in ["EXECUTED", "CANCELED", "PENDING"]:
                    print(f"Операции отфильтрованы по статусу \"{status}\"")
                    filtered_transactions = [tx for tx in transactions if tx["state"].upper() == status]
                    break
                else:
                    print("Статус операции недоступен.")

            search_string = input("Введите строку для поиска в описании транзакций: ")
            print("Список транзакций, содержащих введенную строку:")
            for transaction in search_in_transactions(filtered_transactions, search_string):
                print(transaction)

            categories = ["Перевод", "Зарплата", "Покупка"]
            category_counts = count_categories(filtered_transactions, categories)
            print("Количество транзакций по категориям:")
            for category, count in category_counts.items():
                print(f"{category}: {count}")

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
