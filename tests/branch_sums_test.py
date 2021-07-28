from src.branch_sums.branch_sums import branch_sums
from src.binary_search_tree.binary_search_tree import BST
from src.binary_search_tree.build_bst import build_binary_tree

def test_branch_sums_1():
    tree = {
        "root": 1,
        "nodes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }

    binary_tree = build_binary_tree(tree)

    assert branch_sums(binary_tree) == [15, 16, 18, 10, 11]
    
def test_branch_sums_2():
    tree = {
        "root": 1,
        "nodes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1]
    }

    binary_tree = build_binary_tree(tree)

    assert branch_sums(binary_tree) == [15, 16, 18, 9, 11, 11, 11]

def test_branch_sums_3():
    tree = {
        "root": 0,
        "nodes": [0, 9, 1, 15, 10, 100, 200]
    }

    binary_tree = build_binary_tree(tree)

    assert branch_sums(binary_tree) == [9, 16, 111, 211]
