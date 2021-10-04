class BstTraversal:

    @staticmethod
    def in_order(tree, array):
        if tree is not None:
            BstTraversal.in_order(tree.left, array)
            array.append(tree.value)
            BstTraversal.in_order(tree.right, array)
        return array
