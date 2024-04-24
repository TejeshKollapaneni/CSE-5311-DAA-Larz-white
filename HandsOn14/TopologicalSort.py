from collections import defaultdict

class TopologicalGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def topological_sort(self):
        in_degree = {u: 0 for u in self.vertices}
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        queue = [u for u in self.vertices if in_degree[u] == 0]
        topological_order = []

        while queue:
            u = queue.pop(0)
            topological_order.append(u)
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if any(in_degree.values()):
            raise ValueError("Graph contains a cycle")

        return topological_order

# Testing the algorithm with the book example
g = TopologicalGraph()
g.add_edge('undershorts', 'socks')
g.add_edge('undershorts', 'pants')
g.add_edge('pants', 'belt')
g.add_edge('socks', 'belt')
g.add_edge('shirt', 'tie')
g.add_edge('tie', 'undershorts')
g.add_edge('belt', 'jacket')
g.add_edge('jacket', 'shoes')

print("Topological Ordering:")
print(g.topological_sort())
