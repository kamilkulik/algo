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
        # 1. add idea of the root node to the array
        array.append(self.id)
        # 2. loop over node's children
        for child in self.children:
            # 3. call child's depth_first_search method because
            # if we called it on self then it would get into an infinite loop
            # since we'd be always iterating over the same children
            child.depth_first_search(array)
            # 4. return the array
        return array