import pytest
from src.longest_peak.longest_peak import longest_peak

test_cases = [
    ([1, 2, 3, 3, 2, 1], 0),
    ([1, 1, 3, 2, 1], 4),
    ([1, 2, 3, 2, 1, 1], 5),
    ([1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1], 9),
    ([1, 2, 3, 3, 4, 0, 10], 3),
    ([5, 4, 3, 2, 1, 2, 1], 3)
]

ids = ["longest peak: {}".format(case[1]) for case in test_cases]


@pytest.mark.parametrize("array, longest_peak_length", test_cases, ids=ids)
def test_longest_peak(array, longest_peak_length):
    assert longest_peak(array) == longest_peak_length