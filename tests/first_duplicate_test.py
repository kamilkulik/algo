import pytest
from src.first_duplicate.first_duplicate import first_duplicate, first_duplicate_brute

test_cases = [
    ([2, 1, 5, 2, 3, 3, 4], 2),
    ([2, 1, 5, 3, 3, 2, 4], 3),
    ([1, 1, 2, 3, 3, 2, 2], 1),
    ([15, 3, 15, 6, 13, 3, 12, 10, 17, 8, 13, 1, 12, 9, 14, 7, 16], 15),
    ([11, 6, 8, 8, 8, 9, 10, 6, 4, 1, 10, 1, 6], 8),
    ([6, 15, 7, 10, 9, 14, 10, 1, 10, 1, 2, 11, 1, 6, 8], 10)
]

ids = ['input array: {}, expected result: {}'.format(case[0], case[1]) for case in test_cases]


@pytest.mark.parametrize('array, result', test_cases, ids=ids)
def test_first_duplicate(array, result):
    assert first_duplicate(array) == result


@pytest.mark.parametrize('array, result', test_cases, ids=ids)
def test_first_duplicate_brute(array, result):
    assert first_duplicate_brute(array) == result
