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
        parent_node = node_idx
        child_node_idx = parent_node * 2 + 1
        while child_node_idx < end_idx:
            second_child_node_idx = child_node_idx + 1
            children_nodes = [child_node_idx, second_child_node_idx]
            smaller_child_idx = (
                children_nodes.pop(0)
                if heap[child_node_idx] < heap[second_child_node_idx]
                else children_nodes.pop(1)
            )
            greater_child_idx = children_nodes[0]
            if self.HEAP_FUNCTION(heap[smaller_child_idx], heap[greater_child_idx]):
                # MIN heap
                if heap[parent_node] < heap[smaller_child_idx]:
                    self.__swap(parent_node, smaller_child_idx, heap)
                    parent_node = smaller_child_idx
                    child_node_idx = parent_node * 2 + 1
                else:
                    break
            else:
                # MAX heap
                if heap[parent_node] < heap[greater_child_idx]:
                    self.__swap(parent_node, greater_child_idx, heap)
                    parent_node = greater_child_idx
                    child_node_idx = parent_node * 2 + 1
                else:
                    break

    def __sift_up(self, node_idx, heap):
        child_node = node_idx
        parent_node = (node_idx - 1) // 2
        while child_node > 0 and self.HEAP_FUNCTION(
            heap[child_node], heap[parent_node]
        ):
            self.__swap(child_node, parent_node, heap)
            child_node = parent_node
            parent_node = (child_node - 1) // 2

    def __swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def insert(self, value):
        # IDEA: append the new value to the end of heap and sift it up into position
        self.heap.append(value)
        self.__sift_up(self.length - 1, self.heap)

    def peek(self):
        return self.heap[0]

    def remove(self):
        # IDEA: move head node to the end of the heap and pop it from there
        self.__swap(0, self.length - 1, self.heap)
        removed_node = self.heap.pop(-1)
        return removed_node


def MIN_FUNCTION(a, b):
    return a < b


def MAX_FUNCTION(a, b):
    return a > b
