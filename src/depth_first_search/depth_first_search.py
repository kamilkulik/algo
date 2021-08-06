class Node():
    def __init__ (self, id):
        self.children = []
        self.id = id

    def add_child(self, id):
        self.children.append(Node(id))
        return self

    # Complexity
    # Time: O(V + E) where: V are vertexes of the graph and E are its edges
    # Space: O(V) meaning the array of results will have length equal to number of vertexes
    def depth_first_search(self, array):
        array.append(self.id)
        for child in self.children:
            child.depth_first_search(array)
        return array