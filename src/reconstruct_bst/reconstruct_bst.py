class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(nlog(n)) time | O(n) space
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


class TreeInfo:
    def __init__(self, root_idx):
        self.root_idx = root_idx


# O(n) time | O(n) space
def reconstruct_bst_optimum(pre_order_traversal_values):
    tree_info = TreeInfo(0)
    return reconstruct_bst_from_root_node(pre_order_traversal_values, float("-inf"), float("inf"), tree_info)


def reconstruct_bst_from_root_node(pre_order_traversal_values, min_bound, max_bound, current_subtree_info):
    if len(pre_order_traversal_values) == current_subtree_info.root_idx:
        return None

    root_value = pre_order_traversal_values[current_subtree_info.root_idx]
    # [10, 4, 2, 1, 5, 17, 19, 18]
    if root_value < min_bound or root_value >= max_bound:
        return None

    current_subtree_info.root_idx += 1
    left_subtree = reconstruct_bst_from_root_node(
        pre_order_traversal_values, min_bound, root_value, current_subtree_info
    )
    right_subtree = reconstruct_bst_from_root_node(
        pre_order_traversal_values, root_value, max_bound, current_subtree_info
    )

    return BST(root_value, left_subtree, right_subtree)
