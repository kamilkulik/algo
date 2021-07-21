def find_closest_value_in_bst(tree, target):
    # the idea is to keep a variable that will store the best match found so far while traversing the tree
    # best_match is node value that produces smallest difference between node value and target
    best_match = float("inf")
    current_node = tree

    while current_node is not None:
        if abs(target - best_match) > abs(target - current_node.value):
            best_match = current_node.value
        if current_node.value > target:
            current_node = current_node.left
        elif current_node.value < target:
            current_node = current_node.right
        else:
            break
    return best_match