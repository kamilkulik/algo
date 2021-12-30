import pytest
from src.DYNAMIC_PROGRAMMING.stock_market_strategy.stock_market_strategy import dp_td_recursive

test_cases = [([2, 5, 1], 3), ([2, 5, 1, 3], 5)]

ids = ["Trading days: {}, Profit: {}".format(test_case[0], test_case[1]) for test_case in test_cases]


@pytest.mark.parametrize("trading_days, profit", test_cases, ids=ids)
def test_stock_market_strategy_dp_td(trading_days, profit):
    assert dp_td_recursive(trading_days) == profit
