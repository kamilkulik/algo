def can_sum(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    if target < 0:
        return False
    if target == 0:
        return True

    for number in numbers:
        if can_sum(target - number, numbers, memo) == True:
            memo[target] = True
            return True
    memo[target] = False
    return False
