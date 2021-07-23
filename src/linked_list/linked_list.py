class Linked_list:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def insert(self, value):
        next_node = Linked_list(value)
        self.next = next_node