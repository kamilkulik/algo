from functools import lru_cache


def dp_td_recursive(daily_price):
    @lru_cache(maxsize=None)
    def optimal_profit(trading_day, have_stock):
        if trading_day == len(daily_price):
            return 0
        if trading_day < 0:
            if not have_stock:
                return 0
            else:
                return -float("inf")
        price = daily_price[trading_day]
        if have_stock:
            hold_strategy = optimal_profit(trading_day - 1, True)
            buy_strategy = optimal_profit(trading_day - 1, False) - price
            return max(hold_strategy, buy_strategy)
        else:
            sell_strategy = optimal_profit(trading_day - 1, True) + price
            avoid_strategy = optimal_profit(trading_day - 1, False)
            return max(sell_strategy, avoid_strategy)

    last_day = len(daily_price) - 1
    no_stock = False
    return optimal_profit(last_day, no_stock)


def dp_bu_iterative(daily_price):
    cash_not_owning_share = 0
    cash_owning_share = -float("inf")

    for price in daily_price:
        strategy_buy = cash_not_owning_share - price
        strategy_hold = cash_owning_share
        strategy_sell = cash_owning_share + price
        strategy_avoid = cash_not_owning_share
        # current states
        cash_owning_share = max(strategy_buy, strategy_hold)
        cash_not_owning_share = max(strategy_sell, strategy_avoid)
    return cash_not_owning_share
