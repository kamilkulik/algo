import pytest
from src.bst_traversal.bst_traversal import BstTraversal
from src.binary_tree.build_bt import build_binary_tree

test_cases = [
    (
        {
            "tree": {
                "nodes": [
                    {"id": "5000", "left": "5", "right": "55000", "value": 5000},
                    {"id": "55000", "left": None, "right": None, "value": 55000},
                    {"id": "5", "left": "2", "right": "15", "value": 5},
                    {"id": "15", "left": "5-2", "right": "22", "value": 15},
                    {"id": "22", "left": None, "right": "502", "value": 22},
                    {"id": "502", "left": "204", "right": None, "value": 502},
                    {"id": "204", "left": "203", "right": "205", "value": 204},
                    {"id": "205", "left": None, "right": "207", "value": 205},
                    {"id": "207", "left": "206", "right": "208", "value": 207},
                    {"id": "208", "left": None, "right": None, "value": 208},
                    {"id": "206", "left": None, "right": None, "value": 206},
                    {"id": "203", "left": None, "right": None, "value": 203},
                    {"id": "5-2", "left": None, "right": None, "value": 5},
                    {"id": "2", "left": "1", "right": "3", "value": 2},
                    {"id": "3", "left": None, "right": None, "value": 3},
                    {"id": "1", "left": None, "right": "1-2", "value": 1},
                    {"id": "1-2", "left": None, "right": "1-3", "value": 1},
                    {"id": "1-3", "left": None, "right": "1-4", "value": 1},
                    {"id": "1-4", "left": None, "right": "1-5", "value": 1},
                    {"id": "1-5", "left": None, "right": None, "value": 1}
                ],
                "root": "5000"
            }
        },
        {
            "in_order_array": [1, 1, 1, 1, 1, 2, 3, 5, 5, 15, 22, 203, 204, 205, 206, 207, 208, 502, 5000, 55000],
            "post_order_array": [1, 1, 1, 1, 1, 3, 2, 5, 203, 206, 208, 207, 205, 204, 502, 22, 15, 5, 55000, 5000],
            "pre_order_array": [5000, 5, 2, 1, 1, 1, 1, 1, 3, 15, 5, 22, 502, 204, 203, 205, 207, 206, 208, 55000]
        }
    )
]


@pytest.mark.parametrize('tree, in_order_array', test_cases)
def test_in_order_bst_traversal(tree, in_order_array):
    built_tree = build_binary_tree(tree)
    assert BstTraversal.in_order(built_tree, []) == in_order_array["in_order_array"]
