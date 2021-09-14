import pytest
from src.three_number_sum.three_number_sum import three_number_sum

test_cases = [
    ([1, 2, 3], 7, []),
    ([8, 10, -2, 49, 14], 57, [
        [-2, 10, 49]
    ]),
    ([12, 3, 1, 2, -6, 5, 0, -8, -1], 0, [
        [-8, 3, 5],
        [-6, 1, 5],
        [-1, 0, 1]
    ]),
    ([12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0, [
        [-8, 2, 6],
        [-8, 3, 5],
        [-6, 0, 6],
        [-6, 1, 5],
        [-1, 0, 1]
    ]),
    ([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0, [
        [-8, 2, 6],
        [-8, 3, 5],
        [-6, 0, 6],
        [-6, 1, 5],
        [-5, -1, 6],
        [-5, 0, 5],
        [-5, 2, 3],
        [-1, 0, 1]
    ])
]

ids = ['array: {}, target_sum: {}'.format(case[0], case[1]) for case in test_cases]


@pytest.mark.parametrize('array,target, triplets', test_cases, ids=ids)
def test_three_number_sum(array, target, triplets):
    assert three_number_sum(array, target) == triplets
