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

    @staticmethod
    def pre_order(tree, array):
        if tree is not None:
            array.append(tree.value)
            BstTraversal.pre_order(tree.left, array)
            BstTraversal.pre_order(tree.right, array)
        return array
