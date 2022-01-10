# get the n-th fibonacci number where fibonacci sequence is:
# 0 1 1 2 3 5 8
# formula: nth fib number = (n - 1)th number + (n - 2)th number

# Naive recursion:
# time: O(2^n), space O(n)


def nthFib_naive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nthFib_naive(n - 1) + nthFib_naive(n - 2)


# memoised recursion:
# time: O(n) time, space: O(n)
def nthFib_recursion_memoised(n, memoised={1: 0, 2: 1}):
    if n in memoised:
        return memoised[n]
    else:
        memoised[n] = nthFib_recursion_memoised(n - 1) + nthFib_recursion_memoised(
            n - 2
        )
        return memoised[n]


# iterative - by far the best
# time: O(n) time, space O(1)
def nthFib(n):
    if n == 1:
        return 0

    last_two_numbers = [0, 1]

    counter = 2
    while counter < n:
        next_no = last_two_numbers[0] + last_two_numbers[1]
        last_two_numbers[0] = last_two_numbers[1]
        last_two_numbers[1] = next_no
        counter += 1
    return last_two_numbers[1]


def fib_dp_tabularised(n):
    table = [0 for _ in range(n + 1)]
    table[1] = 1

    for i in range(n - 1):
        table[i + 1] += table[i]
        table[i + 2] += table[i]

    return table[n - 1]
