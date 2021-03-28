from src.loaders import CSVFileLoader
from tests.conftest import BANK1_FILE_PATH


def test_loader_success(bank1_raw_result):
    """
    Checks if loader correctly loads data from csv file
    """
    loader = CSVFileLoader(path=BANK1_FILE_PATH)

    assert bank1_raw_result == list(loader.get_rows())
