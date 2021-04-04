import csv
from abc import abstractmethod, ABC


class FileSaver(ABC):
    def __init__(self, fields: tuple, sources: tuple):
        self.fields = fields
        self.sources = sources

    @abstractmethod
    def save(self, path):
        """
        :param path: path to file to save results
        """

    def fetch(self):
        for source in self.sources:
            for row in source.loader.get_rows():
                result = {}
                for field in self.fields:
                    result[field] = source.get(field=field, row=row)
                yield result


class CSVFilerSaver(FileSaver):
    newline = ''

    def save(self, path: str):
        with open(path, 'w', newline=self.newline) as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writeheader()
            for row in self.fetch():
                writer.writerow(row)
