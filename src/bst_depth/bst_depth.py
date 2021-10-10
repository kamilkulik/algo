def get_bst_height(tree, height=1):
    if tree is None:
        return height - 1
    return max(
        get_bst_height(tree.left, height + 1), get_bst_height(tree.right, height + 1)
    )
