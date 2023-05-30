class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


def kruskal_algorithm(graph):
    num_vertices = len(graph)
    disjoint_set = DisjointSet(num_vertices)
    edges = []

    # Create a list of all edges in the graph
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    # Sort the edges by weight in ascending order
    edges.sort(key=lambda x: x[2])

    minimum_spanning_tree = []
    total_weight = 0

    for edge in edges:
        u, v, weight = edge

        # Check if including this edge creates a cycle
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            minimum_spanning_tree.append(edge)
            total_weight += weight

    return minimum_spanning_tree, total_weight


# Example usage:
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

minimum_spanning_tree, total_weight = kruskal_algorithm(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
print("Total Weight:", total_weight)
