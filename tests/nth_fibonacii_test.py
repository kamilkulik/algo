import pytest
from src.nth_fibonacci.nth_fibonacci import nthFib_naive, nthFib, nthFib_recursion_memoised

test_cases = [
    (1, 0),
    (10, 34),
    (8, 13),
    (2, 1),
    (3, 2),
    (4, 3)
]

@pytest.mark.parametrize('number, nth_fib', test_cases)
def test_nth_fib_naive(number, nth_fib):
    assert nthFib_naive(number) == nth_fib