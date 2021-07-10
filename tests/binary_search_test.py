from src.binary_search.binary_search import binarySearch

def test_binary_search():
    assert binarySearch([1, 4, 5, 7, 8, 10, 13, 16, 19, 20, 26, 43, 48, 49, 50, 53, 55, 59, 64, 67, 80], 26) == 10

