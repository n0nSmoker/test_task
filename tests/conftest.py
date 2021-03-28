import pytest


FIELDNAMES = ('date', 'type', 'amount', 'from', 'to')

BANK1_FILE_PATH = 'tests/data/bank1.csv'
BANK2_FILE_PATH = 'tests/data/bank2.csv'
BANK3_FILE_PATH = 'tests/data/bank3.csv'
RESULT_FILE_PATH = 'tests/data/result.csv'


@pytest.fixture
def bank1_correct_result():
    return [{
        'date': '01-10-2019',
        'type': 'remove',
        'amount': '99.20',
        'from': '198',
        'to': '182',
    }, {
        'date': '02-10-2019',
        'type': 'add',
        'amount': '2000.10',
        'from': '188',
        'to': '198'
    }]


@pytest.fixture
def bank1_raw_result():
    return [{
        'timestamp': 'Oct 1 2019',
        'type': 'remove',
        'amount': '99.20',
        'from': '198',
        'to': '182',
    }, {
        'timestamp': 'Oct 2 2019',
        'type': 'add',
        'amount': '2000.10',
        'from': '188',
        'to': '198'
    }]

