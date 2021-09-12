import pytest
from src.spiral_traverse.spiral_traverse import spiral_traverse

test_cases = [
    ([
         [1, 2, 3, 4],
         [10, 11, 12, 5],
         [9, 8, 7, 6]
     ], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    ([
         [1, 2, 3],
         [12, 13, 4],
         [11, 14, 5],
         [10, 15, 6],
         [9, 8, 7]
     ], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    ([
         [1, 11],
         [2, 12],
         [3, 13],
         [4, 14],
         [5, 15],
         [6, 16],
         [7, 17],
         [8, 18],
         [9, 19],
         [10, 20]
     ], [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2]),
    ([
         [1, 3, 2, 5, 4, 7, 6]
     ], [1, 3, 2, 5, 4, 7, 6]),
    ([[1]], [1])
]

ids = ['{} by {} array'.format(len(case[0]), len(case[0][0])) for case in test_cases]

#len(case[0]), len(case[0])

@pytest.mark.parametrize('input_array, result', test_cases, ids=ids)
def test_spiral_traverse(input_array, result):
    assert spiral_traverse(input_array) == result
