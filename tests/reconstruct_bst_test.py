import pytest
from src.binary_tree.build_bt import build_binary_tree
from src.reconstruct_bst.reconstruct_bst import reconstruct_bst, reconstruct_bst_optimum
from src.bst_traversal.bst_traversal import BstTraversal

test_cases = [
    (
        [10, 4, 2, 1, 5, 17, 19, 18],
        {
            "tree": {
                "nodes": [
                    {"id": "10", "left": "4", "right": "17", "value": 10},
                    {"id": "17", "left": None, "right": "19", "value": 17},
                    {"id": "19", "left": "18", "right": None, "value": 19},
                    {"id": "18", "left": None, "right": None, "value": 18},
                    {"id": "4", "left": "2", "right": "5", "value": 4},
                    {"id": "5", "left": None, "right": None, "value": 5},
                    {"id": "2", "left": "1", "right": None, "value": 2},
                    {"id": "1", "left": None, "right": None, "value": 1},
                ],
                "root": "10",
            }
        },
    ),
    (
        [2, 0, 1, 4, 3, 3],
        {
            "tree": {
                "nodes": [
                    {"id": "2", "left": "0", "right": "4", "value": 2},
                    {"id": "4", "left": "3", "right": None, "value": 4},
                    {"id": "3", "left": None, "right": "3-2", "value": 3},
                    {"id": "3-2", "left": None, "right": None, "value": 3},
                    {"id": "0", "left": None, "right": "1", "value": 0},
                    {"id": "1", "left": None, "right": None, "value": 1},
                ],
                "root": "2",
            }
        },
    ),
    (
        [10, 4, 2, 1, 3, 5, 5, 6, 5, 5, 9, 7, 17, 19, 18, 18, 19],
        {
            "tree": {
                "nodes": [
                    {"id": "10", "left": "4", "right": "17", "value": 10},
                    {"id": "17", "left": None, "right": "19", "value": 17},
                    {"id": "19", "left": "18", "right": "19-2", "value": 19},
                    {"id": "19-2", "left": None, "right": None, "value": 19},
                    {"id": "18", "left": None, "right": "18-2", "value": 18},
                    {"id": "18-2", "left": None, "right": None, "value": 18},
                    {"id": "4", "left": "2", "right": "5", "value": 4},
                    {"id": "5", "left": None, "right": "5-2", "value": 5},
                    {"id": "5-2", "left": None, "right": "6", "value": 5},
                    {"id": "6", "left": "5-3", "right": "9", "value": 6},
                    {"id": "9", "left": "7", "right": None, "value": 9},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "5-3", "left": None, "right": "5-4", "value": 5},
                    {"id": "5-4", "left": None, "right": None, "value": 5},
                    {"id": "2", "left": "1", "right": "3", "value": 2},
                    {"id": "3", "left": None, "right": None, "value": 3},
                    {"id": "1", "left": None, "right": None, "value": 1},
                ],
                "root": "10",
            }
        },
    ),
]


@pytest.mark.parametrize("pre_order_traversal_values, expected_bst", test_cases)
def test_reconstruct_bst(pre_order_traversal_values, expected_bst):
    expected_binary_tree = build_binary_tree(expected_bst)
    expected_bst_pre_order_array = BstTraversal.pre_order(expected_binary_tree, [])
    test_bst_pre_order_array = BstTraversal.pre_order(
        reconstruct_bst(pre_order_traversal_values), []
    )
    assert expected_bst_pre_order_array == test_bst_pre_order_array


@pytest.mark.parametrize("pre_order_traversal_values, expected_bst", test_cases)
def test_reconstruct_bst_optimum(pre_order_traversal_values, expected_bst):
    expected_binary_tree = build_binary_tree(expected_bst)
    expected_bst_pre_order_array = BstTraversal.pre_order(expected_binary_tree, [])
    test_bst_pre_order_array = BstTraversal.pre_order(
        reconstruct_bst_optimum(pre_order_traversal_values), []
    )
    assert expected_bst_pre_order_array == test_bst_pre_order_array
