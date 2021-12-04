class Linked_list:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __eq__(self, other):
        current_node = self
        current_other = other
        while current_node.next is not None:
            if current_node.value != current_other.value:
                return False
            current_node = current_node.next
            current_other = current_other.next
        return True

    def insert(self, value):
        next_node = Linked_list(value)
        current_node = self
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = next_node


def build_linked_list(input):
    nodes = input["nodes"]
    linked_list = None
    for node in nodes:
        if linked_list is None:
            linked_list = Linked_list(node["value"])
            continue
        linked_list.insert(node["value"])
    return linked_list
