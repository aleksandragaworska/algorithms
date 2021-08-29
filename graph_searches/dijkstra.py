from heapq import heappush, heappop

def dijkstra(v_from, v_to, graph):

    visited = dict()
    priority_queue = [(0, v_from)]

    while len(priority_queue) > 0:
        distance, v = heappop(priority_queue)
        if v in visited:
            continue
        visited[v] = distance
        neighbors = graph[v]
        for n, d in neighbors:
            heappush(priority_queue, (d + distance, n))

    return visited.get(v_to, -1)
