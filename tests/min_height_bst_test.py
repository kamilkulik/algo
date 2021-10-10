import pytest
from src.bst_depth.bst_depth import get_bst_height
from src.min_height_bst.min_height_bst import min_height_bst, min_height_bst_optimised
from src.binary_tree.build_bt import build_binary_tree

test_cases = [
    (
        [1, 2, 5, 7, 10, 13, 14, 15, 22],
        {
            "tree": {
                "nodes": [
                    {"id": "10", "left": "2", "right": "14", "value": 10},
                    {"id": "14", "left": "13", "right": "15", "value": 14},
                    {"id": "15", "left": None, "right": "22", "value": 15},
                    {"id": "22", "left": None, "right": None, "value": 22},
                    {"id": "13", "left": None, "right": None, "value": 13},
                    {"id": "2", "left": "1", "right": "5", "value": 2},
                    {"id": "5", "left": None, "right": "7", "value": 5},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "1", "left": None, "right": None, "value": 1},
                ],
                "root": "10",
            }
        },
    ),
    (
        [1, 2],
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": None, "right": "2", "value": 1},
                    {"id": "2", "left": None, "right": None, "value": 2},
                ],
                "root": "1",
            }
        },
    ),
    (
        [1, 2, 5, 7],
        {
            "tree": {
                "nodes": [
                    {"id": "2", "left": "1", "right": "5", "value": 2},
                    {"id": "5", "left": None, "right": "7", "value": 5},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "1", "left": None, "right": None, "value": 1},
                ],
                "root": "2",
            }
        },
    ),
]


@pytest.mark.parametrize("array, tree", test_cases)
def test_min_height_bst(array, tree):
    bst = build_binary_tree(tree)
    min_height = get_bst_height(bst)
    min_height_algo_bst = min_height_bst(array)
    bst_height = get_bst_height(min_height_algo_bst)
    assert bst_height == min_height


@pytest.mark.parametrize("array, tree", test_cases)
def test_min_height_bst_optimised(array, tree):
    bst = build_binary_tree(tree)
    min_height = get_bst_height(bst)
    min_height_algo_bst = min_height_bst_optimised(array)
    bst_height = get_bst_height(min_height_algo_bst)
    assert bst_height == min_height
