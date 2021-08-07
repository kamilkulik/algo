from src.binary_search.binary_search import binarySearch
import pytest

test_cases = [
    ([1, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 26, 10),
    ([1, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 47, -1),
    ([4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 4, 0),
    ([4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 80, 19),
    ([-8, -6, -5, 0, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 80, 23)
]

ids = ['Input: {}, Target: {}, Output: {}'.format(case[0], case[1], case[2]) for case in test_cases]

@pytest.mark.parametrize('array, target, index', test_cases, ids=ids)
def test_binary_search(array, target, index):
    assert binarySearch(array, target) == index