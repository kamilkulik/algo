import pytest
from src.FOO_BAR.one_sieve_of_eratosthenes.sieve_of_eratosthenes import (
    seive_of_eratosthenes,
)

test_cases = [
    (2, []),
    (6, [2, 3, 5]),
    (70, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]),
]

ids = [f"number: {test_case[0]}, primes: {test_case[1]}" for test_case in test_cases]


@pytest.mark.parametrize("number, primes", test_cases, ids=ids)
def test_sieve_of_eratosthenes(number, primes):
    assert seive_of_eratosthenes(number) == primes
