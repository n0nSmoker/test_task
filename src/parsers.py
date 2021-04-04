from datetime import datetime


class Parser:
    date_format = '%d-%m-%Y'
    missing = ''

    def __init__(self, loader=None):
        self.loader = loader

    def get(self, field: str, row: dict) -> str:
        """
        :param field: field_name
        :param row: dict
        :return: field value
        """
        method_name = self.get_method_name(field)
        method = getattr(self, method_name, None)
        if method:
            return method(row)
        else:
            return row.get(field) or self.missing

    @staticmethod
    def get_method_name(field: str) -> str:
        """
        :param field: field name
        :return: method name
        """
        return f'get_{field}'


class Bank1(Parser):
    def get_date(self, row: dict) -> str:
        dt = datetime.strptime(row['timestamp'], '%b %d %Y')
        return dt.strftime(self.date_format)


class Bank2(Parser):
    def get_date(self, row: dict) -> str:
        dt = datetime.strptime(row['date'], '%d-%m-%Y')
        return dt.strftime(self.date_format)

    def get_type(self, row: dict) -> str:
        return row['transaction']

    def get_amount(self, row: dict) -> str:
        return row['amounts']


class Bank3(Parser):
    def get_date(self, row: dict) -> str:
        dt = datetime.strptime(row['date_readable'], '%d %b %Y')
        return dt.strftime(self.date_format)

    def get_amount(self, row: dict) -> str:
        return f"{row['euro']}.{row['cents']}"


