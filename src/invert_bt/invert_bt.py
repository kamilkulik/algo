def swap_left_and_right(tree):
    tree.left, tree.right = tree.right, tree.left


def invert_bt_iterative(tree):
    queue = [tree]
    while len(queue):
        current_node = queue.pop(0)
        if current_node is None:
            continue
        swap_left_and_right(current_node)
        queue.append(current_node.left)
        queue.append(current_node.right)
    return tree


def invert_bt_recursive(tree):
    if tree is None:
        return

    swap_left_and_right(tree)
    invert_bt_recursive(tree.left)
    invert_bt_recursive(tree.right)
