def node_depths_recursive(root, current_depth = 0):
    if root is None: return 0
    return current_depth + node_depths_recursive(root.left, current_depth + 1) + node_depths_recursive(root.right, current_depth + 1)

def node_depths_iterative(root):
    # we will store visited nodes in a stack - array
    # we will keep track of the running sum of depths by using a variable
    # we will traverse the tree until the stack is empty

    nodes_depth = 0
    nodes_stack = [{ "node": root, "depth": 0 }]

    while len(nodes_stack) > 0:
        node = nodes_stack.pop()
        node_instance, node_depth = node["node"], node["depth"]

        if node_instance is None:
            continue

        nodes_depth += node_depth

        nodes_stack.append({"node": node_instance.left, "depth": node_depth + 1})
        nodes_stack.append({"node": node_instance.right, "depth": node_depth + 1})
    
    return nodes_depth