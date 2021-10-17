import pytest
from src.depth_first_search.depth_first_search import Node
from src.graph.graph import build_graph

test_cases = [
    (
        {
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
                    {"children": [], "id": "K", "value": "K"},
                ],
                "startNode": "A",
            }
        },
        ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"],
    ),
    (
        {
            "graph": {
                "nodes": [
                    {"children": ["B", "C", "D", "E", "F"], "id": "A", "value": "A"},
                    {"children": ["G", "H", "I"], "id": "B", "value": "B"},
                    {"children": ["J"], "id": "C", "value": "C"},
                    {"children": ["K", "L"], "id": "D", "value": "D"},
                    {"children": [], "id": "E", "value": "E"},
                    {"children": ["M", "N"], "id": "F", "value": "F"},
                    {"children": [], "id": "G", "value": "G"},
                    {"children": ["O", "P", "Q", "R"], "id": "H", "value": "H"},
                    {"children": [], "id": "I", "value": "I"},
                    {"children": [], "id": "J", "value": "J"},
                    {"children": ["S"], "id": "K", "value": "K"},
                    {"children": [], "id": "L", "value": "L"},
                    {"children": [], "id": "M", "value": "M"},
                    {"children": [], "id": "N", "value": "N"},
                    {"children": [], "id": "O", "value": "O"},
                    {"children": ["T", "U"], "id": "P", "value": "P"},
                    {"children": [], "id": "Q", "value": "Q"},
                    {"children": ["V"], "id": "R", "value": "R"},
                    {"children": [], "id": "S", "value": "S"},
                    {"children": [], "id": "T", "value": "T"},
                    {"children": [], "id": "U", "value": "U"},
                    {"children": ["W", "X", "Y"], "id": "V", "value": "V"},
                    {"children": [], "id": "W", "value": "W"},
                    {"children": ["Z"], "id": "X", "value": "X"},
                    {"children": [], "id": "Y", "value": "Y"},
                    {"children": [], "id": "Z", "value": "Z"},
                ],
                "startNode": "A",
            }
        },
        [
            "A",
            "B",
            "G",
            "H",
            "O",
            "P",
            "T",
            "U",
            "Q",
            "R",
            "V",
            "W",
            "X",
            "Z",
            "Y",
            "I",
            "C",
            "J",
            "D",
            "K",
            "S",
            "L",
            "E",
            "F",
            "M",
            "N",
        ],
    ),
    (
        {
            "graph": {
                "nodes": [
                    {"children": ["B", "C"], "id": "A", "value": "A"},
                    {"children": ["D"], "id": "B", "value": "B"},
                    {"children": [], "id": "C", "value": "C"},
                    {"children": [], "id": "D", "value": "D"},
                ],
                "startNode": "A",
            }
        },
        ["A", "B", "D", "C"],
    ),
]

ids = [f"Results: {case[1]}" for case in test_cases]


@pytest.mark.parametrize("graph, expected_result", test_cases, ids=ids)
def test_depth_first_search(graph, expected_result):
    start_node = graph["graph"]["startNode"]
    nodes = graph["graph"]["nodes"]

    complete_graph = Node(start_node)
    build_graph(complete_graph, nodes)

    assert complete_graph.depth_first_search([]) == expected_result
