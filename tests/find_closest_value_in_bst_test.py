from src.find_closest_value_in_bst.find_closest_value_in_bst import find_closest_value_in_bst
from src.binary_search_tree.binary_search_tree import BST

def build_binary_tree(tree):
    binary_tree = BST(tree["root"])
    remaining_nodes = tree["nodes"]

    for node in remaining_nodes:
        binary_tree.insert(node)

    return binary_tree

def test_find_closest_value_in_bst_1():
    
    tree = {
        "root": 10,
        "nodes": [15, 22, 13, 14, 5, 5, 2, 1]
    }
    
    binary_tree = build_binary_tree(tree)

    assert find_closest_value_in_bst(binary_tree, 12) == 13

def test_find_closest_value_in_bst_2():
    
    tree = {
        "root": 100,
        "nodes": [502, 55000, 1001, 4500, 204, 205, 207, 208, 206, 203, 5, 15, 22, 57, 60, 5, 2, 3, 1, 1, 1, 1, 1, -51, -403]
    }
    
    binary_tree = build_binary_tree(tree)

    assert find_closest_value_in_bst(binary_tree, 100) == 100
    
def test_find_closest_value_in_bst_3():
    
    tree = {
        "root": 100,
        "nodes": [502, 55000, 1001, 4500, 204, 205, 207, 208, 206, 203, 5, 15, 22, 57, 60, 5, 2, 3, 1, 1, 1, 1, 1, -51, -403]
    }
    
    binary_tree = build_binary_tree(tree)

    assert find_closest_value_in_bst(binary_tree, -70) == -51
