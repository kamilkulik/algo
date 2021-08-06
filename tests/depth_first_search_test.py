from src.depth_first_search.depth_first_search import Node
from src.graph.graph import build_graph
            
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