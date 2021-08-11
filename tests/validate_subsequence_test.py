import pytest
from src.validate_subsequence.validate_subsequence import validate_subsequence, validate_subsequence_for_loop

test_cases = [
    ([1, 2, 3, 4], [2, 3], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6], True),
    ([1, 1, 1, 1, 1], [1, 1, 1], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 12], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10, 11, 11, 11, 11], False)
]

ids = ["array: {}, subarray: {}".format(case[0], case [1]) for case in test_cases]

@pytest.mark.parametrize('array, subarray, result', test_cases, ids = ids)
def test_validate_subsequence(array, subarray, result):
    assert validate_subsequence(array, subarray) == result

@pytest.mark.parametrize('array, subarray, result', test_cases, ids = ids)
def test_validate_subsequence_for_loop(array, subarray, result):
    assert validate_subsequence_for_loop(array, subarray) == result
