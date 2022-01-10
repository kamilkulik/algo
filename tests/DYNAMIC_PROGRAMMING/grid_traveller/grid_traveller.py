import pytest
from src.DYNAMIC_PROGRAMMING.grid_traveller.grid_traveller import (
    grid_traveller_tabularised,
)

test_cases = [
    (3, 3, 6),
    (3, 4, 10),
    (5, 5, 70),
    (2, 11, 11),
    (6, 7, 462),
    (5, 8, 330),
    (2, 2, 2),
]

ids = (
    "width: {}, height: {}, ways: {}".format(case[0], case[1], case[2])
    for case in test_cases
)


@pytest.mark.parametrize("width, height, ways", test_cases, ids=ids)
def test_grid_traveller(width, height, ways):
    assert grid_traveller_tabularised(width, height) == ways
