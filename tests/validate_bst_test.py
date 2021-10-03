import pytest
from src.validate_bst.validate_bst import validate_bst
from src.binary_tree.build_bt import build_binary_tree

test_cases = [
    (
        {
            "tree": {
                "nodes": [
                    {"id": "10", "left": "5", "right": "15", "value": 10},
                    {"id": "15", "left": None, "right": "22", "value": 15},
                    {"id": "22", "left": None, "right": None, "value": 22},
                    {"id": "5", "left": "2", "right": "5-2", "value": 5},
                    {"id": "5-2", "left": None, "right": "11", "value": 5},
                    {"id": "11", "left": None, "right": None, "value": 11},
                    {"id": "2", "left": "1", "right": None, "value": 2},
                    {"id": "1", "left": None, "right": None, "value": 1}
                  ],
                "root": "10"
            }
        }, False
    ),
    (
        {
            "tree": {
                "nodes": [
                    {"id": "10", "left": "5", "right": "15", "value": 10},
                    {"id": "15", "left": None, "right": "22", "value": 15},
                    {"id": "22", "left": None, "right": None, "value": 22},
                    {"id": "5", "left": "2", "right": "5-2", "value": 5},
                    {"id": "5-2", "left": None, "right": None, "value": 5},
                    {"id": "2", "left": "1", "right": None, "value": 2},
                    {"id": "1", "left": "-5", "right": None, "value": 1},
                    {"id": "-5", "left": "-15", "right": "-5-2", "value": -5},
                    {"id": "-5-2", "left": None, "right": "-2", "value": -5},
                    {"id": "-2", "left": None, "right": "-1", "value": -2},
                    {"id": "-1", "left": None, "right": None, "value": -1},
                    {"id": "-15", "left": "-22", "right": None, "value": -15},
                    {"id": "-22", "left": "11", "right": None, "value": -22},
                    {"id": "11", "left": None, "right": None, "value": 11}
                ],
                "root": "10"
            }
        }, False
    ),
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
        }, True
    )
]


@pytest.mark.parametrize('tree, valid', test_cases)
def test_validate_bst(tree, valid):
    binary_tree = build_binary_tree(tree)

    assert validate_bst(binary_tree) == valid
