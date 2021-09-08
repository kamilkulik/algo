import pytest
from src.smallest_difference.smallest_difference import smallest_difference

test_cases = [
    ([10, 0, 20, 25, 2000], [1005, 1006, 1014, 1032, 1031], [2000, 1032]),
    ([240, 124, 86, 111, 2, 84, 954, 27, 89], [1, 3, 954, 19, 8], [954, 954]),
    ([0, 20], [21, -2], [20, 21]),
    ([10, 1000], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530], [1000, 1014]),
    ([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17], [28, 26])
]

ids = ["first array: {}, second array: {}, result: {}".format(case[0], case[1], case[2]) for case in test_cases]

@pytest.mark.parametrize('first_array, second_array, result', test_cases, ids = ids)
def test_smallest_difference(first_array, second_array, result):
    assert smallest_difference(first_array, second_array) == result