import pytest
from src.find_kth_largest_val_bst.find_kth_largest_val_bst import (
    find_kth_largest_val_bst,
)
from src.binary_tree.build_bt import build_binary_tree

test_cases = [
    (
        {
            "tree": {
                "nodes": [
                    {"id": "20", "left": "15", "right": "25", "value": 20},
                    {"id": "15", "left": "10", "right": "19", "value": 15},
                    {"id": "25", "left": "21", "right": "30", "value": 25},
                    {"id": "10", "left": None, "right": None, "value": 10},
                    {"id": "19", "left": None, "right": None, "value": 19},
                    {"id": "21", "left": None, "right": "22", "value": 21},
                    {"id": "30", "left": None, "right": None, "value": 30},
                    {"id": "22", "left": None, "right": None, "value": 22},
                ],
                "root": "20",
            }
        },
        3,
        22,
    ),
    (
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": None, "right": "2", "value": 1},
                    {"id": "2", "left": None, "right": "3", "value": 2},
                    {"id": "3", "left": None, "right": "4", "value": 3},
                    {"id": "4", "left": None, "right": "5", "value": 4},
                    {"id": "5", "left": None, "right": None, "value": 5},
                ],
                "root": "1",
            }
        },
        5,
        1,
    ),
    (
        {
            "tree": {
                "nodes": [
                    {"id": "15", "left": "5", "right": "20", "value": 15},
                    {"id": "20", "left": "17", "right": "22", "value": 20},
                    {"id": "22", "left": None, "right": "24", "value": 22},
                    {"id": "24", "left": "23", "right": "25", "value": 24},
                    {"id": "23", "left": None, "right": None, "value": 23},
                    {"id": "25", "left": None, "right": None, "value": 25},
                    {"id": "17", "left": None, "right": None, "value": 17},
                    {"id": "5", "left": "2", "right": "5-2", "value": 5},
                    {"id": "5-2", "left": None, "right": None, "value": 5},
                    {"id": "2", "left": "1", "right": "3", "value": 2},
                    {"id": "3", "left": None, "right": None, "value": 3},
                    {"id": "1", "left": None, "right": None, "value": 1},
                ],
                "root": "15",
            }
        },
        7,
        15,
    ),
]

ids = [f"{case[1]}th value should be: {case[2]}" for case in test_cases]


@pytest.mark.parametrize("tree, k, kth_max", test_cases, ids=ids)
def test_kth_largest_val_in_bst(tree, k, kth_max):
    bst = build_binary_tree(tree)
    assert find_kth_largest_val_bst(bst, k) == kth_max
