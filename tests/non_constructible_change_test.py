import pytest
from src.non_constructible_change.non_constructible_change import non_constructible_change

test_cases = [
    ([109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4],87),
    ([1],2),
    ([5, 6, 1, 1, 2, 3, 4, 9],32),
    ([5, 6, 1, 1, 2, 3, 43],19),
    ([1, 1],3),
]

ids = ["Coins: {}".format(case[0]) for case in test_cases]

@pytest.mark.parametrize('coins, result', test_cases, ids = ids)
def test_non_constructible_change(coins, result):
    assert non_constructible_change(coins) == result