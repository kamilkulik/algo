from src.check_palindrome.check_palindrome import check_palindrome_string_concat

def test_check_palindrome_string_concat_1():
    assert check_palindrome_string_concat('kayak') == True
    
def test_check_palindrome_string_concat_2():
    assert check_palindrome_string_concat('kadyak') == False
