from src.node_depths.node_depths import node_depths_recursive
from src.node_depths.node_depths import node_depths_iterative
from src.binary_tree.build_bt import build_binary_tree

def test_node_depths_1():
    tree = {
        "tree": {
            "nodes": [
            {"id": "1", "left": "2", "right": "8", "value": 1},
            {"id": "2", "left": "3", "right": None, "value": 2},
            {"id": "3", "left": "4", "right": None, "value": 3},
            {"id": "4", "left": "5", "right": None, "value": 4},
            {"id": "5", "left": "6", "right": None, "value": 5},
            {"id": "6", "left": None, "right": "7", "value": 6},
            {"id": "7", "left": None, "right": None, "value": 7},
            {"id": "8", "left": None, "right": "9", "value": 8},
            {"id": "9", "left": None, "right": "10", "value": 9},
            {"id": "10", "left": None, "right": "11", "value": 10},
            {"id": "11", "left": None, "right": "12", "value": 11},
            {"id": "12", "left": "13", "right": None, "value": 12},
            {"id": "13", "left": None, "right": None, "value": 13}
            ],
            "root": "1"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert node_depths_recursive(binary_tree) == 42

def test_node_depths_2():
    tree = {
        "tree": {
            "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "2", "left": "4", "right": "5", "value": 2},
            {"id": "3", "left": "6", "right": "7", "value": 3},
            {"id": "4", "left": "8", "right": "9", "value": 4},
            {"id": "5", "left": None, "right": None, "value": 5},
            {"id": "6", "left": "10", "right": None, "value": 6},
            {"id": "7", "left": None, "right": None, "value": 7},
            {"id": "8", "left": None, "right": None, "value": 8},
            {"id": "9", "left": None, "right": None, "value": 9},
            {"id": "10", "left": None, "right": "11", "value": 10},
            {"id": "11", "left": "12", "right": "13", "value": 11},
            {"id": "12", "left": "14", "right": None, "value": 12},
            {"id": "13", "left": "15", "right": "16", "value": 13},
            {"id": "14", "left": None, "right": None, "value": 14},
            {"id": "15", "left": None, "right": None, "value": 15},
            {"id": "16", "left": None, "right": None, "value": 16}
            ],
            "root": "1"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert node_depths_recursive(binary_tree) == 51

def test_node_depths_3():
    tree = {
        "tree": {
            "nodes": [
            {"id": "1", "left": "2", "right": None, "value": 1},
            {"id": "2", "left": "3", "right": None, "value": 2},
            {"id": "3", "left": "4", "right": None, "value": 3},
            {"id": "4", "left": "5", "right": None, "value": 4},
            {"id": "5", "left": "6", "right": None, "value": 5},
            {"id": "6", "left": "7", "right": None, "value": 6},
            {"id": "7", "left": "8", "right": None, "value": 7},
            {"id": "8", "left": "9", "right": None, "value": 8},
            {"id": "9", "left": None, "right": None, "value": 9}
            ],
            "root": "1"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert node_depths_recursive(binary_tree) == 36

def test_node_depths_4():
    tree = {
        "tree": {
            "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "2", "left": None, "right": None, "value": 2},
            {"id": "3", "left": None, "right": None, "value": 3}
            ],
            "root": "1"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert node_depths_recursive(binary_tree) == 2

def test_node_depths_iterative_1():
    tree = {
        "tree": {
            "nodes": [
            {"id": "1", "left": "2", "right": "8", "value": 1},
            {"id": "2", "left": "3", "right": None, "value": 2},
            {"id": "3", "left": "4", "right": None, "value": 3},
            {"id": "4", "left": "5", "right": None, "value": 4},
            {"id": "5", "left": "6", "right": None, "value": 5},
            {"id": "6", "left": None, "right": "7", "value": 6},
            {"id": "7", "left": None, "right": None, "value": 7},
            {"id": "8", "left": None, "right": "9", "value": 8},
            {"id": "9", "left": None, "right": "10", "value": 9},
            {"id": "10", "left": None, "right": "11", "value": 10},
            {"id": "11", "left": None, "right": "12", "value": 11},
            {"id": "12", "left": "13", "right": None, "value": 12},
            {"id": "13", "left": None, "right": None, "value": 13}
            ],
            "root": "1"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert node_depths_iterative(binary_tree) == 42

def test_node_depths_iterative_2():
    tree = {
        "tree": {
            "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "2", "left": "4", "right": "5", "value": 2},
            {"id": "3", "left": "6", "right": "7", "value": 3},
            {"id": "4", "left": "8", "right": "9", "value": 4},
            {"id": "5", "left": None, "right": None, "value": 5},
            {"id": "6", "left": "10", "right": None, "value": 6},
            {"id": "7", "left": None, "right": None, "value": 7},
            {"id": "8", "left": None, "right": None, "value": 8},
            {"id": "9", "left": None, "right": None, "value": 9},
            {"id": "10", "left": None, "right": "11", "value": 10},
            {"id": "11", "left": "12", "right": "13", "value": 11},
            {"id": "12", "left": "14", "right": None, "value": 12},
            {"id": "13", "left": "15", "right": "16", "value": 13},
            {"id": "14", "left": None, "right": None, "value": 14},
            {"id": "15", "left": None, "right": None, "value": 15},
            {"id": "16", "left": None, "right": None, "value": 16}
            ],
            "root": "1"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert node_depths_iterative(binary_tree) == 51

def test_node_depths_iterative_3():
    tree = {
        "tree": {
            "nodes": [
            {"id": "1", "left": "2", "right": None, "value": 1},
            {"id": "2", "left": "3", "right": None, "value": 2},
            {"id": "3", "left": "4", "right": None, "value": 3},
            {"id": "4", "left": "5", "right": None, "value": 4},
            {"id": "5", "left": "6", "right": None, "value": 5},
            {"id": "6", "left": "7", "right": None, "value": 6},
            {"id": "7", "left": "8", "right": None, "value": 7},
            {"id": "8", "left": "9", "right": None, "value": 8},
            {"id": "9", "left": None, "right": None, "value": 9}
            ],
            "root": "1"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert node_depths_iterative(binary_tree) == 36

def test_node_depths_iterative_4():
    tree = {
        "tree": {
            "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "2", "left": None, "right": None, "value": 2},
            {"id": "3", "left": None, "right": None, "value": 3}
            ],
            "root": "1"
        }
    }

    binary_tree = build_binary_tree(tree)

    assert node_depths_iterative(binary_tree) == 2