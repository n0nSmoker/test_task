import pytest
from src.parsers import Bank1


@pytest.mark.parametrize(
    "func, arg, expect", [
        ('get_method_name', 'some', 'get_some'),
        ('get_date', {'timestamp': 'Oct 22 2019'}, '22-10-2019'),
        ('get_date', {'timestamp': 'Jan 3 2019'}, '03-01-2019'),
        ('get_date', {'timestamp': 'Jan 03 2019'}, '03-01-2019'),
        ('get_type', {'type': 'some'}, 'some'),
        ('get_amount', {'amount': '123'}, '123'),
        ('get_from', {'from': '123'}, '123'),
        ('get_to', {'to': '123'}, '123'),
    ]
)
def test_parser_success(func, arg, expect):
    """
    Checks if parser correctly parses data
    """
    parser = Bank1()
    assert getattr(parser, func)(arg) == expect
