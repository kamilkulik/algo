from src.first_non_repeating_char.first_non_repeating_char import first_non_repeating_char

def test_first_non_repeating_char_1():
    assert first_non_repeating_char("abcdcaf") == 1
    
def test_first_non_repeating_char_2():
    assert first_non_repeating_char("a") == 0

def test_first_non_repeating_char_3():
    assert first_non_repeating_char("ababac") == 5

def test_first_non_repeating_char_4():
    assert first_non_repeating_char("lmnopqldsafmnopqsa") == 7

def test_first_non_repeating_char_5():
    assert first_non_repeating_char("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == -1
