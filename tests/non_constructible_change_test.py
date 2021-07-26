from src.non_constructible_change.non_constructible_change import non_constructible_change

test_cases = [
    {
        "coins": [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4],
        "result": 87,
    },
    {
        "coins": [1],
        "result": 2,
    },
    {
        "coins": [5, 6, 1, 1, 2, 3, 4, 9],
        "result": 32,
    },
    {
        "coins": [5, 6, 1, 1, 2, 3, 43],
        "result": 19,
    },
    {
        "coins": [1, 1],
        "result": 3,
    }
]

def test_non_constructible_change():
    for test_case in test_cases:
        coins = test_case["coins"]
        result = test_case["result"]
        assert non_constructible_change(coins) == result