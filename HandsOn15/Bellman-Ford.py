def bellman_ford(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    for u in graph:
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                print("Graph contains negative weight cycle")
                return {}

    return dist

# Updated Example
graph_bellmanFord = {
    'S': {'T': 4, 'Y': 3},
    'T': {'X': 7, 'Y': -1, 'Z': 2},
    'X': {'T':2},
    'Y': {'X': 3, 'Z': 5},
    'Z': {'S': -2, 'X':6}
}

start_node_bf = 'S'
dist_bf = bellman_ford(graph_bellmanFord, start_node_bf)

for node, distance in dist_bf.items():
    print(f"Shortest path from {start_node_bf} to {node} is {distance}")



'''
Shortest path from S to S is 0
Shortest path from S to T is 4
Shortest path from S to X is 6
Shortest path from S to Y is 3
Shortest path from S to Z is 1
'''
