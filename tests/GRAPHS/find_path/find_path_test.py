import pytest
from src.GRAPHS.find_path.find_path import find_path, find_all_paths, find_shortest_path

test_cases = [
    (
        {
            "A": ["B", "C"],
            "B": ["C", "D"],
            "C": ["D"],
            "D": ["C"],
            "E": ["F"],
            "F": ["C"],
        },
        "A",
        "D",
        ["A", "B", "C", "D"],
        [["A", "B", "C", "D"], ["A", "B", "D"], ["A", "C", "D"]],
        ["A", "B", "D"],
    )
]

ids = [
    f"Start {test_case[1]}, end {test_case[2]} expected path: {test_case[3]}"
    for test_case in test_cases
]


@pytest.mark.parametrize(
    "graph, start, end, path, all_paths, shortest_path", test_cases, ids=ids
)
def test_find_path(graph, start, end, path, all_paths, shortest_path):
    assert find_path(graph, start, end) == path


@pytest.mark.parametrize(
    "graph, start, end, path, all_paths, shortest_path", test_cases
)
def test_find_all_paths(graph, start, end, path, all_paths, shortest_path):
    assert find_all_paths(graph, start, end) == all_paths


@pytest.mark.parametrize(
    "graph, start, end, path, all_paths, shortest_path", test_cases
)
def test_find_shortest_path(graph, start, end, path, all_paths, shortest_path):
    assert find_shortest_path(graph, start, end) == shortest_path
