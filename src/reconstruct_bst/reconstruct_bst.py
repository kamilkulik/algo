# [10, 4, 2, 1, 5, 17, 19, 18]


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstruct_bst(pre_order_traversal_values):
    # return None if there are no more nodes to be created
    if len(pre_order_traversal_values) == 0:
        return None
    root_value = pre_order_traversal_values[0]

    # look for the right subtree root
    # first the default value, in case current root has only a left substree
    right_idx = len(pre_order_traversal_values)
    for i in range(1, len(pre_order_traversal_values)):
        value = pre_order_traversal_values[i]
        if value >= root_value:
            right_idx = i

    left_subtree = reconstruct_bst(pre_order_traversal_values[1:right_idx])
    right_subtree = reconstruct_bst(pre_order_traversal_values[right_idx:])
    return BST(root_value, left_subtree, right_subtree)


def reconstruct_bst_optimum():
    pass
