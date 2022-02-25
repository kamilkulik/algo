import pytest
from src.GRAPHS.find_path.find_path import find_path

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
    )
]

ids = [
    f"Start {test_case[1]}, end {test_case[2]} expected path: {test_case[2]}"
    for test_case in test_cases
]


@pytest.mark.parametrize("graph, start, end, path", test_cases, ids=ids)
def test_find_path(graph, start, end, path):
    assert find_path(graph, start, end) == path
