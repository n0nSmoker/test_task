import os

import pytest

from src.loaders import CSVFileLoader
from src.parsers import Bank1, Bank2, Bank3
from src.savers import CSVFilerSaver, NoMethodException
from tests.conftest import (
    BANK1_FILE_PATH,
    BANK2_FILE_PATH,
    BANK3_FILE_PATH,
    RESULT_FILE_PATH,
    FIELDNAMES,
)


def test_csv_saver_success(tmpdir):
    """
    Check that all files are successfully parsed and
    all rows have been saved correctly
    """
    dest = tmpdir.mkdir("test").join('dest.csv')
    with open(RESULT_FILE_PATH) as f:
        correct_result = f.read()

    saver = CSVFilerSaver(
        fields=FIELDNAMES,
        sources=(
            Bank1(loader=CSVFileLoader(path=BANK1_FILE_PATH)),
            Bank2(loader=CSVFileLoader(path=BANK2_FILE_PATH)),
            Bank3(loader=CSVFileLoader(path=BANK3_FILE_PATH)),
        )
    )
    saver.save(path=dest)

    assert os.path.exists(dest)
    with open(dest) as f:
        assert correct_result == f.read()


def test_csv_saver_failure(tmpdir):
    """
    Check that saver raises exception if finds
    unknown field if silent is False
    """
    dest = tmpdir.mkdir("test").join('dest.csv')

    saver = CSVFilerSaver(
        fields=FIELDNAMES + ('unknown',),
        sources=(
            Bank1(loader=CSVFileLoader(path=BANK1_FILE_PATH)),
        )
    )

    assert not saver.silent
    with pytest.raises(NoMethodException):
        saver.save(path=dest)

    saver.silent = True
    saver.save(path=dest)
