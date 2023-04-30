import pytest

from src import utils


def test_load_operations(seven_operations):
    testing_path = 'tests/path_test.json'
    operations = utils.load_operations(testing_path)
    assert str(operations) == seven_operations


def test_get_last_five_operations(example_operations_list, five_operations):
    last_operations = utils.get_last_five_operations(example_operations_list)
    assert str(last_operations) == five_operations


def test_get_operation_data(operation_data, ex_operation):
    format_data = utils.get_operation_data(ex_operation)
    assert str(format_data) == operation_data


