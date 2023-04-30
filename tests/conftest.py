import pytest

from src import module

SEVEN_OPERATIONS = "[Operations (id=441945886, state=EXECUTED, date=2019-08-26 10:50:58.294041, description=Перевод " \
          "организации, operation_from=Maestro 1596837868705199, operation_to=Счет 64686473678894779589, " \
          "amount=31957.58, currency=руб.account_num=64686473678894779589card=1596837868705199), Operations (" \
          "id=41428829, state=EXECUTED, date=2019-07-03 18:35:29.512364, description=Перевод организации, " \
          "operation_from=MasterCard 7158300734726758, operation_to=Счет 35383033474447895560, amount=8221.37, " \
          "currency=USDaccount_num=35383033474447895560card=7158300734726758), Operations (id=939719570, " \
          "state=EXECUTED, date=2018-06-30 02:08:58.425572, description=Перевод организации, operation_from=Счет " \
          "75106830613657916952, operation_to=Счет 11776614605963066702, amount=9824.07, " \
          "currency=USDaccount_num=11776614605963066702card=75106830613657916952), Operations (id=587085106, " \
          "state=EXECUTED, date=2018-03-23 10:45:06.972075, description=Открытие вклада, operation_from=Счет " \
          "44812258784861134719, operation_to=Счет 41421565395219882431, amount=48223.05, " \
          "currency=руб.account_num=41421565395219882431card=44812258784861134719), Operations (id=142264268, " \
          "state=EXECUTED, date=2019-04-04 23:20:05.206878, description=Перевод со счета на счет, operation_from=Счет " \
          "19708645243227258542, operation_to=Счет 75651667383060284188, amount=79114.93, " \
          "currency=USDaccount_num=75651667383060284188card=19708645243227258542), Operations (id=873106923, " \
          "state=EXECUTED, date=2019-03-23 01:09:46.296404, description=Перевод со счета на счет, operation_from=Счет " \
          "44812258784861134719, operation_to=Счет 74489636417521191160, amount=43318.34, " \
          "currency=руб.account_num=74489636417521191160card=44812258784861134719), Operations (id=214024827, " \
          "state=EXECUTED, date=2018-12-20 16:43:26.929246, description=Перевод организации, operation_from=Счет " \
          "10848359769870775355, operation_to=Счет 21969751544412966366, amount=70946.18, " \
          "currency=USDaccount_num=21969751544412966366card=10848359769870775355)]"


FIVE_OPERATIONS = "[Operations (id=1212, state=EXECUTED, date=2019-08-26 10:50:58.294041, description=Перевод " \
                  "организации, operation_from=Maestro 1596837868705199, operation_to=Счет 64686473678894779589, " \
                  "amount=31957.58, currency=руб.account_num=64686473678894779589card=1596837868705199), Operations (" \
                  "id=1213, state=EXECUTED, date=2019-08-26 10:50:58.294041, description=Перевод организации, " \
                  "operation_from=Maestro 1596837868705199, operation_to=Счет 64686473678894779589, amount=31957.58, " \
                  "currency=руб.account_num=64686473678894779589card=1596837868705199), Operations (id=1214, " \
                  "state=EXECUTED, date=2019-08-26 10:50:58.294041, description=Перевод организации, " \
                  "operation_from=Maestro 1596837868705199, operation_to=Счет 64686473678894779589, amount=31957.58, " \
                  "currency=руб.account_num=64686473678894779589card=1596837868705199), Operations (id=1215, " \
                  "state=EXECUTED, date=2019-08-26 10:50:58.294041, description=Перевод организации, " \
                  "operation_from=Maestro 1596837868705199, operation_to=Счет 64686473678894779589, amount=31957.58, " \
                  "currency=руб.account_num=64686473678894779589card=1596837868705199), Operations (id=1216, " \
                  "state=EXECUTED, date=2019-08-26 10:50:58.294041, description=Перевод организации, " \
                  "operation_from=Maestro 1596837868705199, operation_to=Счет 64686473678894779589, amount=31957.58, " \
                  "currency=руб.account_num=64686473678894779589card=1596837868705199)]"

OPERATION_DATA = "26.8.2019 Перевод организации\n" \
                 "1596 83** **** 5199 -> **9589\n" \
                 "31957.58 руб."


@pytest.fixture
def seven_operations():
    return SEVEN_OPERATIONS


@pytest.fixture
def five_operations():
    return FIVE_OPERATIONS


@pytest.fixture
def operation_data():
    return OPERATION_DATA


@pytest.fixture
def ex_operation():
    ex_operation = module.Operations (441945886, "EXECUTED", "2019-08-26T10:50:58.294041", "Перевод организации",
                                      "Maestro 1596837868705199", "Счет 64686473678894779589", "31957.58", "руб.",
                                      "64686473678894779589", "1596837868705199")
    return ex_operation


@pytest.fixture
def example_operations_list():
    op_list = []
    canc_operation = module.Operations (3456, "CANCALLED", "2019-08-26T10:50:58.294041", "Перевод организации",
                                      "Maestro 1596837868705199", "Счет 64686473678894779589", "31957.58", "руб.",
                                      "64686473678894779589", "1596837868705199")
    op_list.append(canc_operation)
    for i in range(1212, 1222):
        operation = module.Operations (i, "EXECUTED", "2019-08-26T10:50:58.294041", "Перевод организации",
                                      "Maestro 1596837868705199", "Счет 64686473678894779589", "31957.58", "руб.",
                                      "64686473678894779589", "1596837868705199")
        op_list.append(operation)
    return op_list