from src.sorted_squared_array.sorted_squared_array import sorted_squared_array_naive
from src.sorted_squared_array.sorted_squared_array import sorted_squared_array

test_cases = [
    {
        "inputs": [[-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]],
        "expected_result": [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]
    },
    {
        "inputs": [[0]],
        "expected_result": [0]
    },
    {
        "inputs": [[1, 2, 3, 5, 6, 8, 9]],
        "expected_result": [1, 4, 9, 25, 36, 64, 81]
    },
]

def test_sorted_squared_array_naive():
    for test_case in test_cases:
        inputs = test_case["inputs"]
        result = test_case["expected_result"]
        assert sorted_squared_array_naive(*inputs) == result

def test_sorted_squared_array():
    for test_case in test_cases:
        inputs = test_case["inputs"]
        result = test_case["expected_result"]
        assert sorted_squared_array(*inputs) == result

# def test_sorted_squared_array_test_1(array):
#     assert sorted_squared_array([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]) == [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]

# def test_sorted_squared_array_test_2(array):
#     assert sorted_squared_array([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]) == [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]

# def test_sorted_squared_array_test_3(array):
#     assert sorted_squared_array([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]) == [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]

# def test_sorted_squared_array_test_4(array):
#     assert sorted_squared_array([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]) == [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]

# def test_sorted_squared_array_test_5(array):
#     assert sorted_squared_array([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]) == [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]

