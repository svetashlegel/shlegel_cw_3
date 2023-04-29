import datetime


class Operations:
    def __init__(self, date, description, operation_from, operation_to, operation_sum, currency):
        self.date = date
        self.description = description
        self.operation_from = operation_from
        self.operation_to = operation_to
        self.operation_sum = operation_sum
        self.currency = currency

    def __repr__(self):
        return f"{self.__class__.__name__} (" \
               f"date={self.date}, " \
               f"description={self.description}, " \
               f"operation_from={self.operation_from}, " \
               f"operation_to={self.operation_to}, " \
               f"operation_sum={self.operation_sum}, " \
               f"currency={self.currency})"

    def right_format_data(self):
        """Возвращает форматированные данные"""
        thedate = self.date
        date_formated = datetime.datetime.strptime(thedate, '%Y-%m-%dT%H:%M:%S.%f')

        card_num = self.operation_from.split()[-1]
        formated_from = card_num[:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]

        account_num = self.operation_to.split()[-1]
        formated_to = "**" + account_num[-4:]

        return f"{date_formated.day}.{date_formated.month}.{date_formated.year} {self.description}\n" \
               f"{formated_from} -> {formated_to}\n" \
               f"{self.operation_sum} {self.currency}"
