def build_graph(start_node, nodes):
    # 1 find node whose id is start_node.id
    current_nodes_children = next(iter([node["children"] for node in nodes if node["id"] == start_node.id]))
    # 2 for each of its children
    for child in current_nodes_children:
    # 3 call add_child method on Node class
        updated_start_node = start_node.add_child(child)
    # 4 find added node in start_nodes children
        added_child = next(iter([node for node in updated_start_node.children if node.id == child]))
    # 5 call recursively build_graph on variable from step 4, pass nodes too
        build_graph(added_child, nodes)