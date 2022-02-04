class Heap:
    def __init__(self, HEAP_FUNCTION, array):
        self.HEAP_FUNCTION = HEAP_FUNCTION
        self.heap = self.build_heap(array)
        self.length = len(self.heap)

    def __build_heap(self, array):
        pass

    def __sift_down(self, node_idx, end_idx, heap):
        pass

    def __sift_up(self, node_idx, heap):
        pass

    def __swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def insert(self, value):
        # IDEA: append the new value to the end of heap and sift it up into position
        self.heap.append(value)
        self.sift_up(self.length - 1, self.heap)

    def peek(self):
        return self.heap[0]

    def remove(self):
        # IDEA: move head node to the end of the heap and pop it from there
        self.__swap(0, self.length - 1, self.heap)
        removed_node = self.heap.pop(-1)
        return removed_node
