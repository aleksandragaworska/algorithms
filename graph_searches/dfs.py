
def dfs(v_from, v_to, graph):

    visited = set()

    def recursive_search(v, graph, visited):
        if v in visited:
            return
        visited.add(v)
        for n in graph[v]:
            recursive_search(n, graph, visited)

    recursive_search(v_from, graph, visited)

    return v_to in visited


def dfs_while(v_from, v_to, graph):

    visited = set()
    stack = [v_from]

    while len(stack) > 0:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        neighbors = graph[v]
        stack.extend(neighbors)

    return v_to in visited
