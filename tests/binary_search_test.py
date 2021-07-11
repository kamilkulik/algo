from src.binary_search.binary_search import binarySearch

def test_binary_search_1():
    assert binarySearch([1, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 26) == 10

def test_binary_search_2():
    assert binarySearch([1, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 47) == -1

def test_binary_search_3():
    assert binarySearch([4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 4) == 0

def test_binary_search_4():
    assert binarySearch([4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 80) == 19

def test_binary_search_5():
    assert binarySearch([-8, -6, -5, 0, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 80) == 23

