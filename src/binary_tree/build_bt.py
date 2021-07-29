from src.binary_tree.binary_tree import BT

def build_binary_tree(tree):
    binary_tree = BT(tree["tree"]["root"])
    remaining_nodes = tree["tree"]["nodes"]

    for node in remaining_nodes:
        binary_tree.insert(node["id"], node["left"], node["right"], node["value"])

    return binary_tree