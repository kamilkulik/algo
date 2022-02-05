from random import paretovariate


class Heap:
    def __init__(self, HEAP_FUNCTION, array):
        self.HEAP_FUNCTION = HEAP_FUNCTION
        self.heap = self.__build_heap(array)
        self.length = len(self.heap)

    def __build_heap(self, array):
        last_parent_node = (len(array) - 2) // 2
        for i in reversed(range(last_parent_node + 1)):
            self.__sift_down(i, len(array) - 1, array)
        return array

    def __sift_down(self, node_idx, end_idx, heap):
        child_node_idx = node_idx * 2 + 1
        while child_node_idx < end_idx:
            second_child_node_idx = (
                child_node_idx + 1 if child_node_idx <= end_idx else -1
            )
            # CASE 1: two children
            if second_child_node_idx != -1:
                if self.HEAP_FUNCTION(
                    heap[child_node_idx], heap[second_child_node_idx]
                ):
                    idx_to_swap = child_node_idx
                else:
                    idx_to_swap = second_child_node_idx
            # CASE 2: one child
            else:
                idx_to_swap = child_node_idx
            if self.HEAP_FUNCTION(heap[idx_to_swap], heap[node_idx]):
                self.__swap(node_idx, idx_to_swap, heap)
                node_idx = idx_to_swap
                child_node_idx = node_idx * 2 + 1
            else:
                return

    def __sift_up(self, node_idx, heap):
        parent_node_idx = (node_idx - 1) // 2
        while node_idx > 0:
            if self.HEAP_FUNCTION(heap[node_idx], heap[parent_node_idx]):
                self.__swap(node_idx, parent_node_idx, heap)
                node_idx = parent_node_idx
                parent_node_idx = (node_idx - 1) // 2
            else:
                return

    def __swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def insert(self, value):
        # IDEA: append the new value to the end of heap and sift it up into position
        self.heap.append(value)
        self.length += 1
        self.__sift_up(self.length - 1, self.heap)

    def peek(self):
        return self.heap[0]

    def remove(self):
        # IDEA: move head node to the end of the heap and pop it from there
        self.__swap(0, self.length - 1, self.heap)
        removed_node = self.heap.pop()
        self.length -= 1
        self.__sift_down(0, self.length - 1, self.heap)
        return removed_node


def MAX_FUNCTION(a, b):
    return a > b


def MIN_FUNCTION(a, b):
    return a < b
