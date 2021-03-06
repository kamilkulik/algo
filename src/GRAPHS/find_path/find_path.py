def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in path:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in path:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in path:
        return None
    shortest_path = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    return shortest_path
