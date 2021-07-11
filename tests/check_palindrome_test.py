from src.check_palindrome.check_palindrome import check_palindrome_reversed_string_concat, check_palindrome_reversed_string_array, check_palindrome_reservsed_string_recursive

def test_check_palindrome_reversed_string_concat_1():
    assert check_palindrome_reversed_string_concat('kayak') == True
    
def test_check_palindrome_reversed_string_concat_2():
    assert check_palindrome_reversed_string_concat('kadyak') == False

def test_check_palindrome_reversed_string_array_1():
    assert check_palindrome_reversed_string_array('kayak') == True
    
def test_check_palindrome_reversed_string_array_2():
    assert check_palindrome_reversed_string_array('kadyak') == False

def test_check_palindrome_reservsed_string_recursive_1():
    assert check_palindrome_reservsed_string_recursive('kayak') == True
    
def test_check_palindrome_reservsed_string_recursive_2():
    assert check_palindrome_reservsed_string_recursive('kadyak') == False

