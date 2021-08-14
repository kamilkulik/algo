import pytest
from src.find_closest_value_in_bst.find_closest_value_in_bst import find_closest_value_in_bst, find_closest_value_in_bst_recursive
from src.binary_search_tree.build_bst import build_binary_search_tree

test_cases = [
    ([15, 22, 13, 14, 5, 5, 2, 1], 10, 12, 13),
    ([502, 55000, 1001, 4500, 204, 205, 207, 208, 206, 203, 5, 15, 22, 57, 60, 5, 2, 3, 1, 1, 1, 1, 1, -51, -403], 100, 100, 100),
    ([502, 55000, 1001, 4500, 204, 205, 207, 208, 206, 203, 5, 15, 22, 57, 60, 5, 2, 3, 1, 1, 1, 1, 1, -51, -403], 100, -70, -51),
]

ids = ['target: {}, closest: {}'.format(case[2], case[3]) for case in test_cases]

@pytest.mark.parametrize('tree, root, target, closest', test_cases, ids = ids)
def test_find_closest_value_in_bst(tree, root, target, closest):
    
    binary_tree = build_binary_search_tree(tree, root)

    assert find_closest_value_in_bst(binary_tree, target) == closest

@pytest.mark.parametrize('tree, root, target, closest', test_cases, ids = ids)
def test_find_closest_value_in_bst_recursive(tree, root, target, closest):
    
    binary_tree = build_binary_search_tree(tree, root)

    assert find_closest_value_in_bst_recursive(binary_tree, target, root) == closest
