from typing import Callable
from src.HEAPS.heap_construction.heap_construction import Heap


def heap_property_checker(
    HEAP_FUNCTION: Callable[[int, int], bool], heap: Heap
) -> bool:
    if not heap.length:
        return False
    for i in range(heap.length):
        parent_node = i
        child_node = parent_node * 2 + 1
        if child_node < (heap.length - 1) and (
            not HEAP_FUNCTION(parent_node, child_node)
            or not HEAP_FUNCTION(parent_node, child_node + 1)
        ):
            return False
    return True
