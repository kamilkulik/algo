from py import test
import pytest
from src.remove_kth_from_end.remove_kth_from_end import remove_kth_from_end
from src.linked_list.linked_list import build_linked_list

base_linked_list = {
    "linkedList": {
        "head": "0",
        "nodes": [
            {"id": "0", "next": "1", "value": 0},
            {"id": "1", "next": "2", "value": 1},
            {"id": "2", "next": "3", "value": 2},
            {"id": "3", "next": "4", "value": 3},
            {"id": "4", "next": "5", "value": 4},
            {"id": "5", "next": "6", "value": 5},
            {"id": "6", "next": "7", "value": 6},
            {"id": "7", "next": "8", "value": 7},
            {"id": "8", "next": "9", "value": 8},
            {"id": "9", "next": None, "value": 9},
        ],
    }
}

linked_list = build_linked_list(base_linked_list["linkedList"])

test_cases = [
    (
        4,
        {
            "head": "0",
            "nodes": [
                {"id": "0", "next": "1", "value": 0},
                {"id": "1", "next": "2", "value": 1},
                {"id": "2", "next": "3", "value": 2},
                {"id": "3", "next": "4", "value": 3},
                {"id": "4", "next": "5", "value": 4},
                {"id": "5", "next": "7", "value": 5},
                {"id": "7", "next": "8", "value": 7},
                {"id": "8", "next": "9", "value": 8},
                {"id": "9", "next": None, "value": 9},
            ],
        },
    )
]


@pytest.mark.parametrize("k, solution", test_cases)
def test_remove_kth_from_end(k, solution):
    output_list = build_linked_list(solution)
    assert remove_kth_from_end(linked_list, k) == output_list
