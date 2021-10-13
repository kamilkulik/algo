class TraversalInfo:
    def __init__(self, nodes_visited, kth_value):
        self.nodes_visited = nodes_visited
        self.kth_value = kth_value


# Complexity: O(h + k) time | O(h) space, where h is height of the tree and k is the number of nodes to traverse
def find_kth_largest_val_bst(bst, k):
    traversal_info = TraversalInfo(0, -1)
    reverse_in_order_traverse(bst, k, traversal_info)
    return traversal_info.kth_value


def reverse_in_order_traverse(node, k, info):
    if node is None or info.nodes_visited >= k:
        return
    reverse_in_order_traverse(node.right, k, info)
    if info.nodes_visited < k:
        info.nodes_visited += 1
        info.kth_value = node.value
        reverse_in_order_traverse(node.left, k, info)
