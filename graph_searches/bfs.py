
def bfs(v_from, v_to, graph):

    visited = set()
    queue = [v_from]

    while len(queue) > 0:
        v = queue.pop(0)
        if v in visited:
            continue
        visited.add(v)
        neighbors = graph[v]
        queue.extend(neighbors)

    return v_to in visited


def bfs_distance(v_from, v_to, graph):

    visited = dict()
    queue = [(v_from, 0)]

    while len(queue) > 0:
        v, distance = queue.pop(0)
        if v in visited:
            continue
        visited[v] = distance
        neighbors = graph[v]
        queue.extend([(n, distance + 1) for n in neighbors])

    return visited.get(v_to, -1)
