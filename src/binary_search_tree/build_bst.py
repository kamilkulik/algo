from src.binary_search_tree.binary_search_tree import BST

def build_binary_search_tree(tree):
    binary_tree = BST(tree["root"])
    remaining_nodes = tree["nodes"]

    for node in remaining_nodes:
        binary_tree.insert(node)

    return binary_tree