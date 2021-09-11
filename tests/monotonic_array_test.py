import pytest
from src.monotonic_array.monotonic_array import monotonic_array

test_cases = [
    ([-1, -5, -10, -1100, -1100, -1101, -1102, -9001], True),
    ([], True),
    ([1], True),
    ([1, 2], True),
    ([1, 5, 10, 1100, 1101, 1102, 9001], True),
    ([-1, -5, -10, -1100, -900, -1101, -1102, -9001], False),
    ([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11], False),
    ([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11], False)
]

ids = ["Array: {}, Monotonic: {}".format(case[0], case[1]) for case in test_cases]


@pytest.mark.parametrize('array, is_monotonic', test_cases, ids=ids)
def test_monotonic_array(array, is_monotonic):
    assert monotonic_array(array) == is_monotonic
