import pytest
from src.product_sum.product_sum import product_sum

test_cases = [
    ([5, 2, [7, -1], 3, [6, [-13, 8], 4]], 12),
    ([1, 2, 3, 4, 5], 15),
    ([
    [1, 2],
    3,
    [4, 5]
    ], 27),
    ([9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], [[[[3, 4, 1]]], 8], [1, 2, 3, 4, 5, [6, 7], -7], [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7], [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]], -3], 1351)
]

ids = ['Expected result: {}'.format(case[1]) for case in test_cases]

@pytest.mark.parametrize('array, sum', test_cases, ids = ids)
def test_product_sum(array, sum):
    assert product_sum(array) == sum