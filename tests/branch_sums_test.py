from src.branch_sums.branch_sums import branch_sums
from src.binary_tree.build_bt import build_binary_tree
from src.binary_tree.binary_tree import BT

def test_branch_sums_1():
    tree = {
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
            {"id": "10", "left": None, "right": None, "value": 10}
            ],
            "root": "1"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert branch_sums(binary_tree) == [15, 16, 18, 10, 11]
    
def test_branch_sums_2():
    tree = {
        "tree": {
            "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "2", "left": "4", "right": "5", "value": 2},
            {"id": "3", "left": "6", "right": "7", "value": 3},
            {"id": "4", "left": "8", "right": "9", "value": 4},
            {"id": "5", "left": "10", "right": "1-2", "value": 5},
            {"id": "6", "left": "1-3", "right": "1-4", "value": 6},
            {"id": "7", "left": None, "right": None, "value": 7},
            {"id": "8", "left": None, "right": None, "value": 8},
            {"id": "9", "left": None, "right": None, "value": 9},
            {"id": "10", "left": None, "right": None, "value": 10},
            {"id": "1-2", "left": None, "right": None, "value": 1},
            {"id": "1-3", "left": None, "right": None, "value": 1},
            {"id": "1-4", "left": None, "right": None, "value": 1}
            ],
            "root": "1"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert branch_sums(binary_tree) == [15, 16, 18, 9, 11, 11, 11]

def test_branch_sums_3():
    tree = {
        "tree": {
            "nodes": [
            {"id": "0", "left": "9", "right": "1", "value": 0},
            {"id": "9", "left": None, "right": None, "value": 9},
            {"id": "1", "left": "15", "right": "10", "value": 1},
            {"id": "15", "left": None, "right": None, "value": 15},
            {"id": "10", "left": "100", "right": "200", "value": 10},
            {"id": "100", "left": None, "right": None, "value": 100},
            {"id": "200", "left": None, "right": None, "value": 200}
            ],
            "root": "0"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert branch_sums(binary_tree) == [9, 16, 111, 211]
