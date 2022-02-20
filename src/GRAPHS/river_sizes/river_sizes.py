from typing import List


def river_sizes(matrix: List[List[int]]) -> List[List[int]]:
    river_sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverse_node(i, j, matrix, visited, river_sizes)
    return river_sizes


def traverse_node(
    i: int,
    j: int,
    matrix: List[List[int]],
    visited: List[List[bool]],
    river_sizes: List[int],
) -> None:
    nodes_to_explore = [[i, j]]
    current_river_size = 0
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_river_size += 1
        neighbouring_nodes = get_neighbouring_nodes(i, j, visited, matrix)
        for node in neighbouring_nodes:
            nodes_to_explore.append(node)
    if current_river_size > 0:
        river_sizes.append(current_river_size)


def get_neighbouring_nodes(
    i: int, j: int, visited: List[List[bool]], matrix: List[List[int]]
) -> List[List[int]]:
    neighbouring_nodes = []
    if i > 0 and not visited[i - 1][j]:
        neighbouring_nodes.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        neighbouring_nodes.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        neighbouring_nodes.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        neighbouring_nodes.append([i, j + 1])
    return neighbouring_nodes
