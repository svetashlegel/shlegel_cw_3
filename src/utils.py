import json

from src import module


def load_operations(path):
    """Загружает список операций из файла"""
    with open(path, encoding="utf-8") as file:
        content = json.load(file)
        return content


def get_last_5_operations(data):
    """Получает последние 5 операций из списка"""
    last_operations_list = []
    for operation in data:
        if operation["state"] == "EXECUTED":
            last_operations_list.append(operation)
        if len(last_operations_list) == 5:
            break
    return last_operations_list


def get_right_format(raw_list):
    """Создает список экземпляров класса Operations"""
    right_format_list = []
    for op in raw_list:
        operation = module.Operations(op["date"], op["description"], op["from"], op["to"],
                                      op["operationAmount"]["amount"], op["operationAmount"]["currency"]["name"])
        right_format_list.append(operation)
    return right_format_list
