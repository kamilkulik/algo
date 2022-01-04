import pytest
from src.DYNAMIC_PROGRAMMING.can_sum.can_sum import can_sum

test_cases = [
    (7, [2, 4, 6], False),
    (7, [1, 5, 2], True),
    (3, [], False),
    (112, [1, 2, 3], True),
    (1874, [3, 7, 17], True),
    (17, [2, 4, 6], False),
]

ids = [f"Target: {case[0]}, Numbers: {case[1]}" for case in test_cases]


@pytest.mark.parametrize("target, numbers, sum_possible", test_cases, ids=ids)
def test_can_sum(target, numbers, sum_possible):
    assert can_sum(target, numbers) == sum_possible
