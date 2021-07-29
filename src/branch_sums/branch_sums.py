def branch_sums(root):
    sums = []
    new_branch_sums(root, sums)
    return sums

def new_branch_sums(node, sums, running_sum = 0):
    if node is None: return
    new_running_sum = running_sum + node.value
    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return
    new_branch_sums(node.left, sums, new_running_sum)
    new_branch_sums(node.right, sums, new_running_sum)