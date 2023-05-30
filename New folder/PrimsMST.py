import heapq

def greedy_prim_mst(graph):
    start_vertex = 0  # Start with vertex 0 as the initial vertex
    mst = []  # Minimum Spanning Tree
    visited = set()  # Set of visited vertices
    heap = []  # Priority queue of edges

    # Add the edges from the start vertex to the heap
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(heap, (weight, start_vertex, neighbor))

    visited.add(start_vertex)

    while heap:
        weight, u, v = heapq.heappop(heap)

        if v not in visited:
            # Add the edge to the MST
            mst.append((u, v, weight))

            # Add the neighbors of the new vertex to the heap
            for neighbor, weight in graph[v]:
                heapq.heappush(heap, (weight, v, neighbor))

            visited.add(v)

    return mst

# Example usage:
# Graph represented as an adjacency list
graph = [
    [(1, 4), (2, 1)],        # Vertex 0
    [(0, 4), (2, 2), (3, 3)],    # Vertex 1
    [(0, 1), (1, 2), (3, 5)],    # Vertex 2
    [(1, 3), (2, 5)]    # Vertex 3
]


mst = greedy_prim_mst(graph)
for u, v, weight in mst:
    print(f"Edge: {u} - {v}, Weight: {weight}")
