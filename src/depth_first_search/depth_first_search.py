class Node():
    def __init__ (self, id):
        self.children = []
        self.id = id

    def add_child(self, id):
        self.children.append(Node(id))
        return self

    def depth_first_search(self, array):
        array.append(self.id)
        for child in self.children:
            child.depth_first_search(array)
        return array