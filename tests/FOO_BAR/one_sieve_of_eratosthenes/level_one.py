import pytest
from src.FOO_BAR.one_sieve_of_eratosthenes.sieve_of_eratosthenes import (
    seive_of_eratosthenes,
)

test_cases = [
    (0, "23571"),
    (3, "71113"),
    (10, "31374"),
]

ids = [
    f"number: {test_case[0]}, expected_id: {test_case[1]}" for test_case in test_cases
]


@pytest.mark.parametrize("number, expected_id", test_cases, ids=ids)
def test_foo_bar_one_eratosthenes(number, expected_id):
    assert seive_of_eratosthenes(number) == expected_id
