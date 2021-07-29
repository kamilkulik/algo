class BT:
    def __init__(self, id, value = None):
        self.id = id
        self.value = value
        self.left = None
        self.right = None

    def insert(self, id, left, right, value):
        # need to traverse the tree to find the right node
        current_node = self
        while True:
            if id == current_node.id:
                current_node.value = value
                current_node.left = BT(left)
                current_node.right = BT(right)
                break
            else:
                found_node = []
                self.find_next_node(current_node, id, found_node)
                if found_node[0] is not None:
                    current_node = found_node[0]
                    continue
                else:
                    break

        return self

    def find_next_node(self, node, id, found_node):
        if node is None: return None
        if node.id == id:
            found_node.append(node)
        self.find_next_node(node.left, id, found_node)
        self.find_next_node(node.right, id, found_node)