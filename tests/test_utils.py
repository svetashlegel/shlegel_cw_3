import pytest

from src import utils


def test_load_operations(seven_operations):
    testing_path = 'tests/path_test.json'
    operations = utils.load_operations(testing_path)
    assert str(operations) == seven_operations, "Ошибка в составлении списка экземпляров класса Operations"


def test_load_operations__file_not_found():
    testing_path = ''
    content = utils.load_operations(testing_path)
    assert content == "Файл не найден", "Ошибка загрузки файла"


def test_get_last_five_operations(example_operations_list, five_operations):
    last_operations = utils.get_last_five_operations(example_operations_list)
    assert str(last_operations) == five_operations, "Неверно выделены 5 последних операций"


def test_get_operation_data(operation_data, ex_operation):
    format_data = utils.get_operation_data(ex_operation)
    assert format_data == operation_data, "Дата представлена в неверном формате"


