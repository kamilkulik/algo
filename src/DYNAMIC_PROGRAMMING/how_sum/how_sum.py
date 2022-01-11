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


def how_sum_tabularised(target, numbers):
    table = [None for _ in range(target + 1)]
    table[0] = []

    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = table[i] + [num]
    return table[target]
