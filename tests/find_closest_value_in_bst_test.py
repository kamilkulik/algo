from src.find_closest_value_in_bst.find_closest_value_in_bst import find_closest_value_in_bst
from src.binary_search_tree.binary_search_tree import BST

def build_binary_tree(tree):
    binary_tree = BST(tree["tree"]["nodes"][0]["value"])
    remaining_nodes = tree["tree"]["nodes"][1:]

    for node in remaining_nodes:
        binary_tree.insert(node["value"])

    return binary_tree

def test_find_closest_value_in_bst_1():
    tree = {
        "tree": {
            "nodes": [
            {"id": "10", "left": "5", "right": "15", "value": 10},
            {"id": "15", "left": "13", "right": "22", "value": 15},
            {"id": "22", "left": None, "right": None, "value": 22},
            {"id": "13", "left": None, "right": "14", "value": 13},
            {"id": "14", "left": None, "right": None, "value": 14},
            {"id": "5", "left": "2", "right": "5-2", "value": 5},
            {"id": "5-2", "left": None, "right": None, "value": 5},
            {"id": "2", "left": "1", "right": None, "value": 2},
            {"id": "1", "left": None, "right": None, "value": 1}
            ],
            "root": "10"
        },
        "target": 12
    }
    
    binary_tree = build_binary_tree(tree)

    assert find_closest_value_in_bst(binary_tree, 12) == 13