import pytest
from src.binary_tree.build_bt import build_binary_tree
from src.binary_tree_diameter.binary_tree_diameter import binary_tree_diameter

test_cases = [
    (
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "3", "right": "2", "value": 1},
                    {"id": "3", "left": "7", "right": "4", "value": 3},
                    {"id": "7", "left": "8", "right": None, "value": 7},
                    {"id": "8", "left": "9", "right": None, "value": 8},
                    {"id": "9", "left": None, "right": None, "value": 9},
                    {"id": "4", "left": None, "right": "5", "value": 4},
                    {"id": "5", "left": None, "right": "6", "value": 5},
                    {"id": "6", "left": None, "right": None, "value": 6},
                    {"id": "2", "left": None, "right": None, "value": 2},
                ],
                "root": "1",
            }
        },
        6,
    ),
    (
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "3", "left": "6", "right": "7", "value": 3},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "6", "left": None, "right": None, "value": 6},
                    {"id": "2", "left": "4", "right": "5", "value": 2},
                    {"id": "5", "left": None, "right": None, "value": 5},
                    {"id": "4", "left": None, "right": None, "value": 4},
                ],
                "root": "1",
            }
        },
        4,
    ),
    (
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "3", "left": None, "right": None, "value": 3},
                    {"id": "2", "left": None, "right": None, "value": 2},
                ],
                "root": "1",
            }
        },
        2,
    ),
    (
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "3", "right": "9", "value": 1},
                    {"id": "3", "left": None, "right": None, "value": 3},
                    {"id": "9", "left": "14", "right": "10", "value": 9},
                    {"id": "10", "left": None, "right": "11", "value": 10},
                    {"id": "11", "left": None, "right": "12", "value": 11},
                    {"id": "12", "left": None, "right": "17", "value": 12},
                    {"id": "17", "left": None, "right": None, "value": 17},
                    {"id": "14", "left": None, "right": "19", "value": 14},
                    {"id": "19", "left": "25", "right": None, "value": 19},
                    {"id": "25", "left": None, "right": None, "value": 25},
                ],
                "root": "1",
            }
        },
        7,
    ),
    (
        {
            "tree": {
                "nodes": [
                    {"id": "4", "left": "2", "right": None, "value": 4},
                    {"id": "2", "left": None, "right": None, "value": 2},
                ],
                "root": "4",
            }
        },
        1,
    ),
]


@pytest.mark.parametrize("binary_tree, diameter", test_cases)
def test_binary_tree_diameter(binary_tree, diameter):
    bt = build_binary_tree(binary_tree)
    assert binary_tree_diameter(bt) == diameter
