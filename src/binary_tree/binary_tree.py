class BT:
    def __init__(self, id, value = None):
        self.id = id
        self.value = value
        self.left = None
        self.right = None

    def insert(self, id, left, right, value):
        if self.id == id:
            self.value = value
            if left is not None:
                self.left = BT(left)
            else:
                self.left = None
            if right is not None:
                self.right = BT(right)
            else:
                self.right = None
        else:
            if self.left is not None:
                self.left.insert(id, left, right, value)
            if self.right is not None:
                self.right.insert(id, left, right, value)
        return self

    # def insert(self, id, left, right, value):
    #     # need to traverse the tree to find the right node
    #     current_node = self
    #     while True:
    #         if id == current_node.id:
    #             current_node.value = value
    #             if left is not None:
    #                 current_node.left = BT(left)
    #             else:
    #                 current_node.left = None
    #             if right is not None:
    #                 current_node.right = BT(right)
    #             else: 
    #                 current_node.right = None
    #             break
    #         else:
    #             found_node = []
    #             self.find_next_node(current_node, id, found_node)
    #             if found_node[0] is not None:
    #                 current_node = found_node[0]
    #                 continue
    #             else:
    #                 break
    #     return self

    # def find_next_node(self, node, id, found_node):
    #     if node is None: return None
    #     if node.id == id:
    #         found_node.append(node)
    #     self.find_next_node(node.left, id, found_node)
    #     self.find_next_node(node.right, id, found_node)

tree = {
    "tree": {
        "nodes": [
        {"id": "1", "left": "2", "right": "3", "value": 1},
        {"id": "2", "left": "4", "right": "5", "value": 2},
        {"id": "3", "left": "6", "right": "7", "value": 3},
        {"id": "4", "left": "8", "right": "9", "value": 4},
        {"id": "5", "left": "10", "right": None, "value": 5},
        {"id": "6", "left": None, "right": None, "value": 6},
        {"id": "7", "left": None, "right": None, "value": 7},
        {"id": "8", "left": None, "right": None, "value": 8},
        {"id": "9", "left": None, "right": None, "value": 9},
        {"id": "10", "left": None, "right": None, "value": 10}
        ],
        "root": "1"
    }
}

def build_binary_tree(tree):
    binary_tree = BT(tree["tree"]["root"])
    remaining_nodes = tree["tree"]["nodes"]

    for node in remaining_nodes:
        binary_tree.insert(node["id"], node["left"], node["right"], node["value"])

    return binary_tree

print(build_binary_tree(tree))