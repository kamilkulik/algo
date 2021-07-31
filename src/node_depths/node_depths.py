def node_depths_recursive(root, current_depth = 0):
    if root is None: return 0
    return current_depth + node_depths_recursive(root.left, current_depth + 1) + node_depths_recursive(root.right, current_depth + 1)
