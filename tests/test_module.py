from src import module


def test_class_Operations():
    operation1 = module.Operations("2019-08-26T10:50:58.294041", "Перевод организации", "Maestro 1596837868705199",
                                   "Счет 64686473678894779589", "8221.37", "USD")
    assert operation1.date == "2019-08-26T10:50:58.294041"
    assert operation1.description == "Перевод организации"
    assert operation1.operation_from == "Maestro 1596837868705199"
    assert operation1.operation_to == "Счет 64686473678894779589"
    assert operation1.operation_sum == "8221.37"
    assert operation1.currency == "USD"

    dt = operation1.right_format_data()
    assert str(dt) == '26.8.2019 Перевод организации\n1596 83** **** 5199 -> **9589\n8221.37 USD'

    assert str(operation1.__repr__()) == "Operations (date=2019-08-26T10:50:58.294041, description=Перевод " \
                                         "организации, operation_from=Maestro 1596837868705199, operation_to=Счет " \
                                         "64686473678894779589, operation_sum=8221.37, currency=USD)"


