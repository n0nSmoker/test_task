from abc import abstractmethod, ABC
from datetime import datetime

from .loaders import FileLoader


class Parser(ABC):
    date_format = '%d-%m-%Y'
    missing = ''

    def __init__(self, loader: FileLoader = None):
        self.loader = loader

    @staticmethod
    def get_method_name(field: str) -> str:
        """
        :param field: field name
        :return: method name
        """
        return f'get_{field}'

    @abstractmethod
    def get_date(self, row: dict) -> str:
        """
        :param row: dict
        :return: date in date_format
        """

    @abstractmethod
    def get_type(self, row: dict) -> str:
        """
        :param row: dict
        :return: type of transaction
        """

    @abstractmethod
    def get_amount(self, row: dict) -> str:
        """
        :param row: dict
        :return: amount in euro
        """

    @abstractmethod
    def get_from(self, row: dict) -> str:
        """
        :param row: dict
        :return: sender account id
        """

    @abstractmethod
    def get_to(self, row: dict) -> str:
        """
        :param row: dict
        :return: recipient account id
        """


class Bank1(Parser):
    def get_date(self, row: dict) -> str:
        dt = datetime.strptime(row['timestamp'], '%b %d %Y')
        return dt.strftime(self.date_format)

    def get_type(self, row: dict) -> str:
        return row['type']

    def get_amount(self, row: dict) -> str:
        return row['amount']

    def get_from(self, row: dict) -> str:
        return row['from']

    def get_to(self, row: dict) -> str:
        return row['to']


class Bank2(Parser):
    def get_date(self, row: dict) -> str:
        dt = datetime.strptime(row['date'], '%d-%m-%Y')
        return dt.strftime(self.date_format)

    def get_type(self, row: dict) -> str:
        return row['transaction']

    def get_amount(self, row: dict) -> str:
        return row['amounts']

    def get_from(self, row: dict) -> str:
        return row['from']

    def get_to(self, row: dict) -> str:
        return row['to']


class Bank3(Parser):
    def get_date(self, row: dict) -> str:
        dt = datetime.strptime(row['date_readable'], '%d %b %Y')
        return dt.strftime(self.date_format)

    def get_type(self, row: dict) -> str:
        return row['type']

    def get_amount(self, row: dict) -> str:
        return f"{row['euro']}.{row['cents']}"

    def get_from(self, row: dict) -> str:
        return row['from']

    def get_to(self, row: dict) -> str:
        return row['to']

