import pytest
from src.sorted_squared_array.sorted_squared_array import sorted_squared_array_naive, sorted_squared_array, sorted_squared_array_no_reversal

test_cases = [
    ([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20],[0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]),
    ([0],[0]),
    ([1, 2, 3, 5, 6, 8, 9],[1, 4, 9, 25, 36, 64, 81]),
]

ids = ["array: {}".format(case[0]) for case in test_cases]

@pytest.mark.parametrize('array, sorted_squares', test_cases, ids = ids)
def test_sorted_squared_array_naive(array, sorted_squares):
    assert sorted_squared_array_naive(array) == sorted_squares

@pytest.mark.parametrize('array, sorted_squares', test_cases, ids = ids)
def test_sorted_squared_array(array, sorted_squares):
    assert sorted_squared_array(array) == sorted_squares

@pytest.mark.parametrize('array, sorted_squares', test_cases, ids = ids)
def test_sorted_squared_array_no_reversal(array, sorted_squares):
    assert sorted_squared_array_no_reversal(array) == sorted_squares