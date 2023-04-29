import pytest

OP_DATA = [
    {
        "id": 441945881,
        "state": "EXECUTED"},
    {
        "id": 441945882,
        "state": "EXECUTED"},
    {
        "id": 441945883,
        "state": "EXECUTED"},
    {
        "id": 441945884,
        "state": "CANCELED"},
    {
        "id": 441945885,
        "state": "EXECUTED"},
    {
        "id": 441945886,
        "state": "EXECUTED"},
    {
        "id": 441945887,
        "state": "EXECUTED"}]

EX_OPERATION = [{
    "id": 441945886,
    "state": "EXECUTED",
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }}}]


@pytest.fixture
def op_data():
    return OP_DATA


@pytest.fixture
def ex_operation():
    return EX_OPERATION
