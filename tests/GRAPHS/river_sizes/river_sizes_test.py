import pytest
from src.GRAPHS.river_sizes.river_sizes import river_sizes

test_cases = [
    (
        [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
        ],
        [2, 1, 5, 2, 2],
    ),
    ([[0]], []),
    ([[1]], [1]),
    ([[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]], [3, 2, 1]),
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],
        [],
    ),
]

ids = [f"river sizes: {river_sizes}" for _, river_sizes in test_cases]


@pytest.mark.parametrize("matrix, river_sizes_list", test_cases, ids=ids)
def test_river_sizes(matrix, river_sizes_list):
    assert river_sizes(matrix) == river_sizes_list
