import pytest
from src.two_number_sum.two_number_sum import two_num_sum, two_num_sum_pointer

test_cases = [
    ([15], 15, []),
    ([14], 15, []),
    ([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164, []),
    ([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163, [210, -47]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18, [3, 15])
]

ids = ["array: {}, target: {}".format(case[0], case[1]) for case in test_cases]

@pytest.mark.parametrize('array, target, result', test_cases, ids = ids)
def test_two_number_sum(array, target, result):
    assert two_num_sum(array, target) == result

@pytest.mark.parametrize('array, target, result', test_cases, ids = ids)
def test_two_number_sum_pointer(array, target, result):
    assert two_num_sum(array, target) == result