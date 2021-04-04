import pytest
from src.parsers import Bank1


@pytest.mark.parametrize(
    "func, args, expect", [
        ('get_method_name', dict(field='some'), 'get_some'),
        ('get', dict(field='date', row={'timestamp': 'Oct 22 2019'}), '22-10-2019'),
        ('get', dict(field='date', row={'timestamp': 'Jan 3 2019'}), '03-01-2019'),
        ('get', dict(field='date', row={'timestamp': 'Jan 03 2019'}), '03-01-2019'),
        ('get', dict(field='type', row={'type': 'some'}), 'some'),
        ('get', dict(field='amount', row={'amount': '123'}), '123'),
        ('get', dict(field='from', row={'from': '123'}), '123'),
        ('get', dict(field='to', row={'to': '123'}), '123'),
    ]
)
def test_parser_success(func, args, expect):
    """
    Checks if parser correctly parses data
    """
    parser = Bank1()
    assert getattr(parser, func)(**args) == expect
