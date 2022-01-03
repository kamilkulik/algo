def min_num_of_change(n, denoms):
    num_of_change = [float("inf") for _ in range(n + 1)]
    num_of_change[0] = 0
    for denom in denoms:
        for amount in range(len(num_of_change)):
            if denom <= amount:
                num_of_change[amount] = min(
                    num_of_change[amount], num_of_change[amount - denom] + 1
                )
    return num_of_change[n] if num_of_change[n] != float("inf") else -1
