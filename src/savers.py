import csv
from abc import abstractmethod, ABC


class NoMethodException(Exception):
    pass


class FileSaver(ABC):
    def __init__(self, fields: tuple, sources: tuple, silent: bool = False):
        self.fields = fields
        self.sources = sources
        self.silent = silent

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
                    method_name = source.get_method_name(field)
                    method = getattr(source, method_name, None)
                    if method:
                        result[field] = method(row)
                    elif self.silent:
                        result[field] = source.missing
                    else:
                        raise NoMethodException(f'Can not get {field} form {source} {method_name} is missing')
                yield result


class CSVFilerSaver(FileSaver):
    newline = ''

    def save(self, path: str):
        with open(path, 'w', newline=self.newline) as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writeheader()
            for row in self.fetch():
                writer.writerow(row)
