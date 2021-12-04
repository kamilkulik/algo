class Linked_list:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, value):
        next_node = Linked_list(value)
        self.next = next_node


def build_linked_list(input):
    nodes = input["nodes"]
    linked_list = None
    for node in nodes:
        if linked_list is None:
            linked_list = Linked_list(node["value"])
            continue
        linked_list.insert(node["value"])
    return linked_list
