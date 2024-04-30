import heapq

def dijkstraAlgorithmImp(graph, start):
    # Initialize distances from start vertex to all other vertices
    initial_distances = {node: float('inf') for node in graph}
    initial_distances[start] = 0

    # Priority queue to store the vertices going to get visited next
    pq = [(0, start)]

    while pq:
        # Delet the vertex of the smallest distance from start
        current_distance, current_vertex = heapq.heappop(pq)

        # Visit each neighbor vertex from the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < initial_distances[neighbor]:
                initial_distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return initial_distances

# Updated Example
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3},
}

start_node = 'A'
shortest_distances = dijkstraAlgorithmImp(graph, start_node)
print("Shortest distances from the source node", start_node)
for node, distance in shortest_distances.items():
    print(f"Node {node}: Distance {distance}")


Shortest distances from the source node A
Node A: Distance 0
Node B: Distance 2
Node C: Distance 3
Node D: Distance 6

