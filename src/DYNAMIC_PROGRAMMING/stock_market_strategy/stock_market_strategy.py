def dp_td_recursive(trading_days):
    def optimal_profit(trading_day, stock_owned):
        if trading_day == len(trading_days):
            return 0
        if trading_day == 0:
            if stock_owned > 0:
                return -float("inf")
