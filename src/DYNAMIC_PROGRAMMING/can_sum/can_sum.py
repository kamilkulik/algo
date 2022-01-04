def can_sum(target, numbers):
    if target < 0:
        return False
    if target == 0:
        return True

    for number in numbers:
        if can_sum(target - number, numbers):
            return True
    return False
