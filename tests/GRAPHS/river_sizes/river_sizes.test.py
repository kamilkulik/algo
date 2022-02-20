import pytest
from src.river_sizes.river_sizes import river_sizes

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
    )
]

ids = [f"river sizes: {river_sizes}" for river_sizes in test_cases]


@pytest.mark.parametrize("matrix, river_sizes", test_cases, ids=ids)
def river_sizes_test(matrix, river_sizes):
    assert river_sizes(matrix) == river_sizes
