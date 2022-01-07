def best_sum(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target < 0:
        return None
    if target == 0:
        return []

    shortest_combination = None
    for num in numbers:
        remainder_result = best_sum(target - num, numbers, memo)
        if remainder_result is not None:
            combination = remainder_result + [num]
            if shortest_combination is None or len(combination) < len(
                shortest_combination
            ):
                shortest_combination = combination

    memo[target] = shortest_combination
    return shortest_combination
