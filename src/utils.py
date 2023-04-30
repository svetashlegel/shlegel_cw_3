import json

from src import module


def load_operations(path):
    """Загружает операции из файла и создает список экземпляров класса Operations"""
    operations_list = []
    with open(path, encoding="utf-8") as file:
        content = json.load(file)
    for op in content:
        try:
            operation = module.Operations(op["id"], op["state"], op["date"], op["description"], op["from"], op["to"],
                                          op["operationAmount"]["amount"], op["operationAmount"]["currency"]["name"],
                                          op["to"].split()[-1], op["from"].split()[-1])
            operations_list.append(operation)
        except KeyError:
            operations_list.append(None)
    return operations_list


def get_last_five_operations(data):
    """Получает последние 5 операций из списка"""
    last_operations_list = []
    for operation in data:
        if operation.state == "EXECUTED":
            last_operations_list.append(operation)
        if len(last_operations_list) == 5:
            break
    return last_operations_list


def get_operation_data(operation):
    """Возвращает форматированные данные по операции"""
    hidden_card_num = operation.hide_card_num()
    hidden_account_num = operation.hide_account_num()
    return f"{operation.date.day}.{operation.date.month}.{operation.date.year} {operation.description}\n" \
           f"{hidden_card_num} -> {hidden_account_num}\n" \
           f"{operation.amount} {operation.currency}"

