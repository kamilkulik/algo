import pytest
from src.DYNAMIC_PROGRAMMING.min_number_of_change.min_number_of_change import (
    min_num_of_change,
)
from src.DYNAMIC_PROGRAMMING.best_sum.best_sum import best_sum, best_sum_tabularised
from tests.conftest import reset_defaults

test_cases = [
    ([1, 5, 10], 7, 3),
    ([2, 4, 6], 5, -1),
    ([1, 2, 3], 0, 0),
    ([1, 5, 10], 4, 4),
    ([39, 45, 130, 40, 4, 1], 135, 3),
]

ids = [
    f"Change: {case[0]}, amount: {case[1]}, expected output: {case[2]}"
    for case in test_cases
]


@pytest.mark.parametrize("denoms, amount, min_num_of_coins", test_cases, ids=ids)
def test_num_number_of_change(denoms, amount, min_num_of_coins):
    assert min_num_of_change(amount, denoms) == min_num_of_coins


@pytest.mark.parametrize("denoms, amount, min_num_of_coins", test_cases, ids=ids)
def test_best_sum(denoms, amount, min_num_of_coins):
    reset_defaults(best_sum)
    result = best_sum(amount, denoms)
    assert (len(result) if result is not None else -1) == min_num_of_coins


@pytest.mark.parametrize("denoms, amount, min_num_of_coins", test_cases, ids=ids)
def test_best_sum_tabularised(denoms, amount, min_num_of_coins):
    result = best_sum_tabularised(amount, denoms)
    assert (len(result) if result is not None else -1) == min_num_of_coins
