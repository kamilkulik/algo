from src.validate_subsequence.validate_subsequence import validate_subsequence
from src.validate_subsequence.validate_subsequence import validate_subquence_for_loop

def test_validate_subsequence_1():
    assert validate_subsequence([1, 2, 3, 4], [2, 3]) == True

def test_validate_subsequence_2():
    assert validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]) == True

def test_validate_subsequence_3():
    assert validate_subsequence([1, 1, 1, 1, 1], [1, 1, 1]) == True

def test_validate_subsequence_4():
    assert validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 12]) == False

def test_validate_subsequence_5():
    assert validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10, 11, 11, 11, 11]) == False

def test_validate_subquence_for_loop_1():
    assert validate_subquence_for_loop([1, 2, 3, 4], [2, 3]) == True

def test_validate_subquence_for_loop_2():
    assert validate_subquence_for_loop([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]) == True

def test_validate_subquence_for_loop_3():
    assert validate_subquence_for_loop([1, 1, 1, 1, 1], [1, 1, 1]) == True

def test_validate_subquence_for_loop_4():
    assert validate_subquence_for_loop([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 12]) == False

def test_validate_subquence_for_loop_5():
    assert validate_subquence_for_loop([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10, 11, 11, 11, 11]) == False

