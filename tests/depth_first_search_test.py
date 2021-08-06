from src.depth_first_search.depth_first_search import Node

def build_graph(start_node, nodes):
    # 1 find node whose id is start_node.id
    current_nodes_children = next(iter([node["children"] for node in nodes if node["id"] == start_node.id]))
    # 2 for each of its children
    for child in current_nodes_children:
    # 3 call add_child method on Node class
        updated_start_node = start_node.add_child(child)
    # 4 find added node in start_nodes children
        added_child = next((iter([node for node in updated_start_node.children if node.id == child])))
    # 5 call recursively build_graph on variable from step 4, pass nodes too
        build_graph(added_child, nodes)
            
def test_depth_first_search():
    graph = {
        "graph": {
            "nodes": [
            {"children": ["B", "C", "D"], "id": "A", "value": "A"},
            {"children": ["E", "F"], "id": "B", "value": "B"},
            {"children": [], "id": "C", "value": "C"},
            {"children": ["G", "H"], "id": "D", "value": "D"},
            {"children": [], "id": "E", "value": "E"},
            {"children": ["I", "J"], "id": "F", "value": "F"},
            {"children": ["K"], "id": "G", "value": "G"},
            {"children": [], "id": "H", "value": "H"},
            {"children": [], "id": "I", "value": "I"},
            {"children": [], "id": "J", "value": "J"},
            {"children": [], "id": "K", "value": "K"}
            ],
            "startNode": "A"
        }
    }

    start_node = graph["graph"]["startNode"]
    nodes = graph["graph"]["nodes"]

    complete_graph = Node(start_node)
    build_graph(complete_graph, nodes)

    assert complete_graph.depth_first_search([]) == ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]