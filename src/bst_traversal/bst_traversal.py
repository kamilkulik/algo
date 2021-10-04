class BstTraversal:

    @staticmethod
    def in_order(tree, array):
        if tree is not None:
            BstTraversal.in_order(tree.left, array)
            array.append(tree.value)
            BstTraversal.in_order(tree.right, array)
        return array

    @staticmethod
    def post_order(tree, array):
        if tree is not None:
            BstTraversal.post_order(tree.left, array)
            BstTraversal.post_order(tree.right, array)
            array.append(tree.value)
        return array
