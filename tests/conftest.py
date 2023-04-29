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


@pytest.fixture
def op_data():
    return OP_DATA
