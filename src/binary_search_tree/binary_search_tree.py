class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right
        return self

    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left
            else:
                return True
        return False
        pass
    
    def getSmallest(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def remove(self, value, parent_node = None):
        current_node = self
        # case: we're removing a node with two children nodes
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:	
                if current_node.left is not None and current_node.right is not None:
                    # set node to the smallest value in the subtree
                    current_node.value = current_node.right.getSmallest()
                    # remove the smallest value in the subtree (as it was reassigned above)
                    current_node.right.remove(current_node.value, current_node)
                # case for root node:
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        pass
                # case for a node with 1 child node at most
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break
        return self