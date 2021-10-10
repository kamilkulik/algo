# naive implementation using the given BST class and insert method
# it is naive because we are traversing the tree each time to make an insertion
# which means each insertion is nlong(n) time
# Complexity: O(log(n)) time | O(n) space
def min_height_bst(array):
    return construct_min_height_bst(array, None, 0, len(array) - 1)


def construct_min_height_bst(array, bst, start_idx, end_idx):
    if end_idx < start_idx:
        return
    mid_idx = (start_idx + end_idx) // 2  # round down for numbers not devisible by 2
    value_to_add = array[mid_idx]
    if bst is None:
        bst = BST(value_to_add)  # root node
    else:
        bst.insert(value_to_add)
    construct_min_height_bst(array, bst, start_idx, mid_idx - 1)
    construct_min_height_bst(array, bst, mid_idx + 1, end_idx)
    return bst


# given BST class and insert method
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
