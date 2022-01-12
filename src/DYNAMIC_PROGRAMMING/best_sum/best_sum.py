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


def best_sum_tabularised(target, numbers):
    table = [None for _ in range(target + 1)]
    table[0] = []

    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                current_target = i + num
                if current_target <= target:
                    current_sum = table[i] + [sum]
                    table[current_target] = (
                        current_sum
                        if (
                            table[current_target] is None
                            or len(current_sum) < len(table[current_target])
                        )
                        else table[current_target]
                    )
    return table[target]
