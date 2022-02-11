from math import isqrt
from typing import List


def seive_of_eratosthenes(n: int) -> List[int]:
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    # we don't need to check to n, because
    # one of the facts needs to be smaller than square root of n
    for i in range(2, isqrt(n)):
        if is_prime[i]:
            # we can start at the square of i
            # if we have a factor less than square of i
            # it should've been marked by previous iteration of the loop
            for x in range(i * i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]


print(seive_of_eratosthenes(25))
