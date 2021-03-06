import pytest
from src.DYNAMIC_PROGRAMMING.fibonacci.fibonacci import (
    nthFib_naive,
    nthFib,
    nthFib_recursion_memoised,
    fib_dp_tabularised,
)

test_cases = [(1, 0), (10, 34), (8, 13), (2, 1), (3, 1), (4, 2)]


@pytest.mark.parametrize("number, nth_fib", test_cases)
def test_nth_fib_naive(number, nth_fib):
    assert nthFib_naive(number) == nth_fib


@pytest.mark.parametrize("number, nth_fib", test_cases)
def test_nth_fib(number, nth_fib):
    assert nthFib(number) == nth_fib


@pytest.mark.parametrize("number, nth_fib", test_cases)
def test_nthFib_recursion_memoised(number, nth_fib):
    assert nthFib_recursion_memoised(number) == nth_fib


@pytest.mark.parametrize("number, nth_fib", test_cases)
def test_fib_dp_tabularised(number, nth_fib):
    assert fib_dp_tabularised(number) == nth_fib
