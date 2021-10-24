def binary_tree_diameter(tree):
    return calculate_bt_diameter(tree).diameter


def calculate_bt_diameter(tree):
    if tree is None:
        return TreeInfo(0, 0)

    left_subtree = calculate_bt_diameter(tree.left)
    right_subtree = calculate_bt_diameter(tree.right)

    diameter_through_the_root = left_subtree.height + right_subtree.height
    max_diameter_so_far = max(left_subtree.diameter, right_subtree.diameter)
    current_diameter = max(diameter_through_the_root, max_diameter_so_far)
    current_height = 1 + max(left_subtree.height, right_subtree.height)

    return TreeInfo(current_diameter, current_height)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
