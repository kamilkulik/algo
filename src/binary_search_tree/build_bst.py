from src.binary_search_tree.binary_search_tree import BST

def build_binary_search_tree(remaining_nodes,root):
    binary_tree = BST(root)

    for node in remaining_nodes:
        binary_tree.insert(node)

    return binary_tree