import pytest
from src.HEAPS.heap_construction.heap_construction import Heap, MIN_FUNCTION
from src.HEAPS.heap_construction.heap_property_checker import heap_property_checker

test_cases = [
    (
        [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8],
        [
            {
                "argument": -11,
                "method": "insert",
                "min_heap_property_satisfied": True,
                "output": None,
            },
            {
                "argument": None,
                "method": "peek",
                "min_heap_property_satisfied": True,
                "output": -11,
            },
            {
                "argument": None,
                "method": "remove",
                "min_heap_property_satisfied": True,
                "output": -11,
            },
            {
                "argument": None,
                "method": "remove",
                "min_heap_property_satisfied": True,
                "output": -10,
            },
            {
                "argument": None,
                "method": "remove",
                "min_heap_property_satisfied": True,
                "output": -7,
            },
            {
                "argument": None,
                "method": "remove",
                "min_heap_property_satisfied": True,
                "output": -7,
            },
        ],
    ),
    (
        [5],
        [
            {
                "argument": 4,
                "method": "insert",
                "min_heap_property_satisfied": True,
                "output": None,
            },
            {
                "argument": None,
                "method": "peek",
                "min_heap_property_satisfied": True,
                "output": 4,
            },
            {
                "argument": 15,
                "method": "insert",
                "min_heap_property_satisfied": True,
                "output": None,
            },
            {
                "argument": None,
                "method": "peek",
                "min_heap_property_satisfied": True,
                "output": 4,
            },
            {
                "argument": None,
                "method": "remove",
                "min_heap_property_satisfied": True,
                "output": 4,
            },
            {
                "argument": None,
                "method": "peek",
                "min_heap_property_satisfied": True,
                "output": 5,
            },
            {
                "argument": 7,
                "method": "insert",
                "min_heap_property_satisfied": True,
                "output": None,
            },
            {
                "argument": None,
                "method": "peek",
                "min_heap_property_satisfied": True,
                "output": 5,
            },
            {
                "argument": None,
                "method": "remove",
                "min_heap_property_satisfied": True,
                "output": 5,
            },
            {
                "argument": 7,
                "method": "insert",
                "min_heap_property_satisfied": True,
                "output": None,
            },
            {
                "argument": 10,
                "method": "insert",
                "min_heap_property_satisfied": True,
                "output": None,
            },
            {
                "argument": None,
                "method": "peek",
                "min_heap_property_satisfied": True,
                "output": 7,
            },
            {
                "argument": None,
                "method": "remove",
                "min_heap_property_satisfied": True,
                "output": 7,
            },
            {
                "argument": 20,
                "method": "insert",
                "min_heap_property_satisfied": True,
                "output": None,
            },
            {
                "argument": None,
                "method": "peek",
                "min_heap_property_satisfied": True,
                "output": 7,
            },
        ],
    ),
]


@pytest.mark.parametrize("array, operations", test_cases)
def test_heap_construction(array, operations):
    heap = Heap(MIN_FUNCTION, array)
    for i in range(len(operations)):
        argument = operations[i]["argument"]
        expected_output = operations[i]["output"]
        operation = getattr(heap, operations[i]["method"])

        if argument is not None:
            assert operation(argument) == expected_output
        else:
            assert operation() == expected_output

        assert (
            heap_property_checker(MIN_FUNCTION, heap)
            == operations[i]["min_heap_property_satisfied"]
        )
