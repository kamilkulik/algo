def node_depths_recursive(root, current_depth = 0):
    if root is None: return 0
    return current_depth + node_depths_recursive(root.left, current_depth + 1) + node_depths_recursive(root.right, current_depth + 1)

def node_depths_iterative(root):
    # we will store visited nodes in a stack - array
    # we will keep track of the running sum of depths by using a variable
    # we will traverse the tree until the stack is empty

    # 1. initiate a variable to hold all depths
    nodes_depth = 0
    # 2. we'll use an array of dictionaries to hold all the nodes we'll be looking at
    # we need to store the node + it's depth to increase it when adding a new node
    nodes_stack = [{ "node": root, "depth": 0 }]
    # 3. loop over the nodes array as long as it is non-empty
    while len(nodes_stack) > 0:
        # 4. get the latest node & pop it from the nodes array
        node = nodes_stack.pop()
        # 5. desctructure the node we're working with
        node_instance, node_depth = node["node"], node["depth"]
        # 6. check if the node_instance is None and continue is that's the case
        if node_instance is None:
            continue
        # 7. Now we know our node is not None. We can add it's depth to the depths variable
        nodes_depth += node_depth

        # 8. append to the nodes array left and right nodes of the current node
        nodes_stack.append({"node": node_instance.left, "depth": node_depth + 1})
        nodes_stack.append({"node": node_instance.right, "depth": node_depth + 1})
    
    return nodes_depth