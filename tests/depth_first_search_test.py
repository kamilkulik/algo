from src.depth_first_search.depth_first_search import Node

def build_graph(start_node, nodes):
    
            
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

    first_node = Node(start_node)
    built_graph = build_graph(first_node, nodes)

    assert built_graph.children is [nodes[0]["children"]]