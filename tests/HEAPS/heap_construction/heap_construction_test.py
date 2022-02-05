import pytest
from src.HEAPS.heap_construction.heap_construction import Heap, MIN_FUNCTION

# from src.HEAPS.heap_construction.heap_property_checker import heap_property_checker

test_cases = [
    (
        [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8],
        [
            {
                "argument": [-11],
                "method": "insert",
                "min_heap_property_satisfied": True,
                "output": None,
            },
            {
                "argument": [],
                "method": "peek",
                "min_heap_property_satisfied": True,
                "output": -11,
            },
        ],
    )
]


@pytest.mark.parametrize("array, operations", test_cases)
def test_heap_construction(array, operations):
    heap = Heap(MIN_FUNCTION, array)
    for i in range(len(operations) - 1):
        argument = operations[i]["argument"][0]
        expected_output = operations[i]["output"]
        operation = getattr(heap, operations[i]["method"])

        assert operation(argument) == expected_output
        # assert (
        #     heap_property_checker(MIN_FUNCTION, heap)
        #     == operations[i]["min_heap_property_satisfied"]
        # )
