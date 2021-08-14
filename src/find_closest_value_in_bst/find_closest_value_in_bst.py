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


def find_closest_value_in_bst_recursive(tree, target, closest):
    # base case is checking if the tree is none - we want that because we sum current node's value
    if tree is None: return closest
    # second we want to check if target minus the value of current node is less than target - closest
    # this is a check for smaller difference between the target and any of the nodes
    if abs(target - closest) > abs(target - tree.value): closest = tree.value
    # next we are checking if the target is less or greater than the value of the current node
    # since this is a BST, we can call the function recursively for both smaller and greater values
    if target > tree.value: return find_closest_value_in_bst_recursive(tree.right, target, closest)
    elif target < tree.value: return find_closest_value_in_bst_recursive(tree.left, target, closest)
    # when non of the above is hit, we've arrived to the right-most node of the BST
    # time to return
    else: return closest