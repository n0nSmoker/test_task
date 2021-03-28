import csv
from abc import ABC, abstractmethod


class FileLoader(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def get_rows(self):
        """
        :return: rows of the file
        """


class CSVFileLoader(FileLoader):
    newline = ''

    def get_rows(self):
        with open(self.path, newline=self.newline) as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row
