# def can_sum(target, numbers, memo={}):
#     if target in memo:
#         return memo[target]
#     if target < 0:
#         return False
#     if target == 0:
#         return True

#     for number in numbers:
#         if can_sum(target - number, numbers, memo) == True:
#             memo[target] = True
#             return True
#     memo[target] = False
#     return False


def cache(func):
    memo = {}

    def worker(*args):
        hashable_type = [arg for arg in args if type(arg) is int]
        for arg in hashable_type:
            if arg not in memo:
                memo[arg] = func(*args)
        return memo[hashable_type[0]]

    return worker


@cache
def can_sum(target, numbers):
    if target < 0:
        return False
    if target == 0:
        return True

    for number in numbers:
        if can_sum(target - number, numbers) == True:
            return True
    return False


#######################################


def cache(func):
    memo = {}

    def worker(*args):
        hashable_type = [arg for arg in args if type(arg) is int]
        for arg in hashable_type:
            if arg not in memo:
                memo[arg] = func(*args)
        return memo[hashable_type[0]]

    return worker


# def can_sum(target, numbers, memo={}):
#     if target in memo:
#         return memo[target]
#     if target < 0:
#         return False
#     if target == 0:
#         return True

#     for number in numbers:
#         if can_sum(target - number, numbers, memo) == True:
#             memo[target] = True
#             return True
#     memo[target] = False
#     return False


@cache
def can_sum(target, numbers):
    if target < 0:
        return False
    if target == 0:
        return True

    for number in numbers:
        if can_sum(target - number, numbers) == True:
            return True
    return False


test_cases = [
    [7, [2, 4, 6], False],
    [7, [1, 5, 2], True],
    [3, [], False],
    [112, [1, 2, 3], True],
    [1874, [3, 7, 17], True],
    [17, [2, 4, 6], False],
]

print(can_sum(test_cases[4][0], test_cases[4][1]))
