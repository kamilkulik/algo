def how_sum(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in numbers:
        remainder = target - num
        remainder_result = how_sum(remainder, numbers)

        if remainder_result is not None:
            remainder_result.append(num)
            memo[target] = remainder_result
            return memo[target]

    memo[target] = None
    return None
