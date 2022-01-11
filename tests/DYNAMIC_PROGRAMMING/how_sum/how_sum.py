import pytest
from src.DYNAMIC_PROGRAMMING.how_sum.how_sum import how_sum, how_sum_tabularised
from tests.conftest import reset_defaults

test_cases = [
    (7, [2, 4, 6], False),
    (7, [1, 5, 2], True),
    (3, [], False),
    (112, [1, 2, 3], True),
    (1874, [3, 7, 17], True),
    (17, [2, 4, 6], False),
    (300, [7, 14], False),
]

ids = [f"Target: {case[0]}, Numbers: {case[1]}" for case in test_cases]


@pytest.mark.parametrize("target, numbers, sum_possible", test_cases, ids=ids)
def test_how_sum(target, numbers, sum_possible):
    reset_defaults(how_sum)
    assert (type(how_sum(target, numbers)) is list) == sum_possible


@pytest.mark.parametrize("target, numbers, sum_possible", test_cases, ids=ids)
def test_how_sum_tabularised(target, numbers, sum_possible):
    assert (type(how_sum_tabularised(target, numbers)) is list) == sum_possible
