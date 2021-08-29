graph_directed = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'D': ['E'],
    'C': ['E'],
    'E': ['B'],
    'F': [],
    'W': ['A'],
}

test_graph_cases = [
    ('A', 'B', True),
    ('E', 'B', True),
    ('A', 'W', False),
    ('A', 'E', True),
    ('C', 'B', True),
    ('F', 'D', False),
    ('D', 'A', False),
    ('D', 'C', True),
]

test_graph_distance_cases = [
    ('A', 'B', 1),
    ('E', 'B', 1),
    ('A', 'W', -1),
    ('A', 'E', 2),
    ('C', 'B', 2),
    ('F', 'D', -1),
    ('D', 'A', -1),
    ('D', 'C', 3),
]

graph_weighted_directed = {
    'A': [('B', 2), ('D', 1)],
    'B': [('C', 2), ('E', 5)],
    'D': [('E', 6)],
    'C': [('E', 2)],
    'E': [('B', 1)],
    'F': [],
    'W': [('A', 1)],
}

test_graph_weighted_distance_cases = [
    ('A', 'B', 2),
    ('E', 'B', 1),
    ('A', 'W', -1),
    ('A', 'E', 6),
    ('C', 'B', 3),
    ('F', 'D', -1),
    ('D', 'A', -1),
    ('D', 'C', 9),
]
