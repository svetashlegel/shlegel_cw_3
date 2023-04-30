import datetime


class Operations:
    def __init__(self, id, state, date, description, operation_from, operation_to,
                 amount, currency, account_num, card):
        self.id = id
        self.state = state
        self.date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
        self.description = description
        self.operation_from = operation_from
        self.operation_to = operation_to
        self.amount = amount
        self.currency = currency
        self.account_num = account_num
        self.card = card

    def __repr__(self):
        return f"{self.__class__.__name__} (" \
               f"id={self.id}, " \
               f"state={self.state}, " \
               f"date={self.date}, " \
               f"description={self.description}, " \
               f"operation_from={self.operation_from}, " \
               f"operation_to={self.operation_to}, " \
               f"amount={self.amount}, " \
               f"currency={self.currency}" \
               f"account_num={self.account_num}" \
               f"card={self.card})"

    def hide_card_num(self):
        """Скрывает номер карты"""
        hidden_card_num = self.card[:4] + " " + self.card[4:6] + "** **** " + self.card[-4:]
        return hidden_card_num

    def hide_account_num(self):
        """Скрывает номер счета"""
        hidden_account_num = "**" + self.account_num[-4:]
        return hidden_account_num
