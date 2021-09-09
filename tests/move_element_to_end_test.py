import pytest
from src.move_element_to_end.move_element_to_end import move_element_to_end

test_cases = [
    ([2, 1, 2, 2, 2, 3, 4, 2], 2, [4, 1, 3, 2, 2, 2, 2, 2]),
    ([], 3, []),
    ([1, 2, 4, 5, 6], 3, [1, 2, 4, 5, 6]),
    ([3, 3, 3, 3, 3], 3, [3, 3, 3, 3, 3]),
    ([3, 1, 2, 4, 5], 3, [5, 1, 2, 4, 3]),
    ([5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12], 5, [12, 1, 2, 11, 10, 3, 4, 6, 7, 9, 8, 5, 5, 5, 5, 5, 5])
]

ids = ["array: {}, to_move: {}".format(case[0], case[1]) for case in test_cases]

@pytest.mark.parametrize('input, to_move, result', test_cases, ids = ids)
def test_move_element_to_end(input, to_move, result):
    assert move_element_to_end(input, to_move) == result