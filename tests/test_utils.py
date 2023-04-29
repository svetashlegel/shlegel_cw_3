from src import utils


def test_load_operations():
    testing_path = 'tests/path_test.json'
    operation = utils.load_operations(testing_path)
    assert operation == {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }}}


def test_get_last_5_operations(op_data):
    last_operations = utils.get_last_5_operations(op_data)
    assert last_operations == [{
        "id": 441945881,
        "state": "EXECUTED"},
    {
        "id": 441945882,
        "state": "EXECUTED"},
    {
        "id": 441945883,
        "state": "EXECUTED"},
    {
        "id": 441945885,
        "state": "EXECUTED"},
    {
        "id": 441945886,
        "state": "EXECUTED"}]