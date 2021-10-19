import pytest
from src.binary_tree.build_bt import build_binary_tree
from src.invert_bt.invert_bt import invert_bt_iterative, invert_bt_recursive

test_cases = [
    (
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "2", "left": "4", "right": "5", "value": 2},
                    {"id": "3", "left": "6", "right": "7", "value": 3},
                    {"id": "4", "left": "8", "right": "9", "value": 4},
                    {"id": "5", "left": None, "right": None, "value": 5},
                    {"id": "6", "left": None, "right": None, "value": 6},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "8", "left": None, "right": None, "value": 8},
                    {"id": "9", "left": None, "right": None, "value": 9},
                ],
                "root": "1",
            }
        },
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "3", "right": "2", "value": 1},
                    {"id": "2", "left": "5", "right": "4", "value": 2},
                    {"id": "4", "left": "9", "right": "8", "value": 4},
                    {"id": "8", "left": None, "right": None, "value": 8},
                    {"id": "9", "left": None, "right": None, "value": 9},
                    {"id": "5", "left": None, "right": None, "value": 5},
                    {"id": "3", "left": "7", "right": "6", "value": 3},
                    {"id": "6", "left": None, "right": None, "value": 6},
                    {"id": "7", "left": None, "right": None, "value": 7},
                ],
                "root": "1",
            }
        },
    ),
    (
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "2", "left": "4", "right": "5", "value": 2},
                    {"id": "3", "left": "6", "right": None, "value": 3},
                    {"id": "4", "left": None, "right": None, "value": 4},
                    {"id": "5", "left": None, "right": None, "value": 5},
                    {"id": "6", "left": None, "right": None, "value": 6},
                ],
                "root": "1",
            }
        },
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "3", "right": "2", "value": 1},
                    {"id": "2", "left": "5", "right": "4", "value": 2},
                    {"id": "4", "left": None, "right": None, "value": 4},
                    {"id": "5", "left": None, "right": None, "value": 5},
                    {"id": "3", "left": None, "right": "6", "value": 3},
                    {"id": "6", "left": None, "right": None, "value": 6},
                ],
                "root": "1",
            }
        },
    ),
    (
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "2", "left": "4", "right": "5", "value": 2},
                    {"id": "3", "left": "6", "right": "7", "value": 3},
                    {"id": "4", "left": "8", "right": "9", "value": 4},
                    {"id": "5", "left": "10", "right": None, "value": 5},
                    {"id": "6", "left": None, "right": None, "value": 6},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "8", "left": None, "right": None, "value": 8},
                    {"id": "9", "left": None, "right": None, "value": 9},
                    {"id": "10", "left": None, "right": None, "value": 10},
                ],
                "root": "1",
            }
        },
        {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "3", "right": "2", "value": 1},
                    {"id": "2", "left": "5", "right": "4", "value": 2},
                    {"id": "4", "left": "9", "right": "8", "value": 4},
                    {"id": "8", "left": None, "right": None, "value": 8},
                    {"id": "9", "left": None, "right": None, "value": 9},
                    {"id": "5", "left": None, "right": "10", "value": 5},
                    {"id": "10", "left": None, "right": None, "value": 10},
                    {"id": "3", "left": "7", "right": "6", "value": 3},
                    {"id": "6", "left": None, "right": None, "value": 6},
                    {"id": "7", "left": None, "right": None, "value": 7},
                ],
                "root": "1",
            }
        },
    ),
]


@pytest.mark.parametrize("binary_tree, inverted_binary_tree", test_cases)
def test_invert_binary_tree_iterative(binary_tree, inverted_binary_tree):
    input_tree = build_binary_tree(binary_tree)
    output_tree = invert_bt_iterative(input_tree)
    expected_tree = build_binary_tree(inverted_binary_tree)
    assert output_tree == expected_tree


@pytest.mark.parametrize("binary_tree, inverted_binary_tree", test_cases)
def test_invert_binary_tree_recursive(binary_tree, inverted_binary_tree):
    input_tree = build_binary_tree(binary_tree)
    output_tree = invert_bt_recursive(input_tree)
    expected_tree = build_binary_tree(inverted_binary_tree)
    assert output_tree == expected_tree
