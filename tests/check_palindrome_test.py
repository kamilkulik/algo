import pytest
from src.check_palindrome.check_palindrome import check_palindrome_reversed_string_concat
from src.check_palindrome.check_palindrome import check_palindrome_reversed_string_array
from src.check_palindrome.check_palindrome import check_palindrome_reservsed_string_recursive
from src.check_palindrome.check_palindrome import check_palindrome_reservsed_string_recursive_verbose

test_cases = [
    ('kayak', True),
    ('kaydak', False),
    ('u$a5%%5a$u', True),
    ('u$a5%%!5a$u', False),
]

ids = ['string: {}, palindrome: {}'.format(case[0], case[1]) for case in test_cases]

@pytest.mark.parametrize('string, palindrome', test_cases, ids = ids)
def test_check_palindrome_reversed_string_concat(string, palindrome):
    assert check_palindrome_reversed_string_concat(string) == palindrome

@pytest.mark.parametrize('string, palindrome', test_cases, ids = ids)
def test_check_palindrome_reversed_string_array(string, palindrome):
    assert check_palindrome_reversed_string_array(string) == palindrome

@pytest.mark.parametrize('string, palindrome', test_cases, ids = ids)
def test_check_palindrome_reservsed_string_recursive(string, palindrome):
    assert check_palindrome_reservsed_string_recursive(string) == palindrome

@pytest.mark.parametrize('string, palindrome', test_cases, ids = ids)
def test_check_palindrome_reservsed_string_recursive_verbose(string, palindrome):
    assert check_palindrome_reservsed_string_recursive_verbose(string) == palindrome

