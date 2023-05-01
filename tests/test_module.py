from src import module


def test_class_Operations():
    operation1 = module.Operations(176798279, "EXECUTED", "2019-08-26T10:50:58.294041", "Перевод организации",
                                   "Maestro 1596837868705199", "Счет 64686473678894779589", "8221.37", "USD",
                                   "90417871337969064865", "9454780748494532")
    assert operation1.id == 176798279, "Неверный номер id"
    assert operation1.state == "EXECUTED", "Неверный статус"
    assert str(operation1.date) == '2019-08-26 10:50:58.294041', "Неверная дата"
    assert operation1.description == "Перевод организации", "Неверное описание"
    assert operation1.operation_from == "Maestro 1596837868705199", "Ошибка в графе перевода: откуда"
    assert operation1.operation_to == "Счет 64686473678894779589", "Ошибка в графе перевода: куда"
    assert operation1.amount == "8221.37", "Неверно указана сумма"
    assert operation1.currency == "USD", "Неверно указана валюта"
    assert operation1.account_num == "90417871337969064865", "Неверный номер счета"
    assert operation1.card == "9454780748494532", "Неверный номер карты"

    assert operation1.__repr__() == "Operations (id=176798279, state=EXECUTED, date=2019-08-26 10:50:58.294041, " \
                                         "description=Перевод организации, operation_from=Maestro 1596837868705199, " \
                                         "operation_to=Счет 64686473678894779589, amount=8221.37, " \
                                         "currency=USDaccount_num=90417871337969064865card=9454780748494532)", \
                                         "Ошибка в представлении класса"

    assert operation1.hide_card_num() == "9454 78** **** 4532", "Неверное сокрытие номера карты"

    assert operation1.hide_account_num() == "**4865", "Неверное сокрытие номера счета"

