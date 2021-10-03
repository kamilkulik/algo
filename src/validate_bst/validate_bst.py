def validate_bst(tree):
    return helper_validate_bst(tree, float('-inf'), float('inf'))


def helper_validate_bst(tree, min_value, max_value):
    if tree is None:
        return True

    if tree.value < min_value or tree.value >= max_value:
        return False

    left_validation = helper_validate_bst(tree.left, min_value, tree.value)
    right_validation = helper_validate_bst(tree.right, tree.value, max_value)

    return left_validation and right_validation
