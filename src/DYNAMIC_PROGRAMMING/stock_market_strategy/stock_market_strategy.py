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
