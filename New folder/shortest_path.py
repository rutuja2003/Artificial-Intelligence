import heapq


def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    heap = [(0, source)]
    heapq.heapify(heap)

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


# Example usage:
graph = {
    'A': {'B': 6, 'C': 2},
    'B': {'D': 1},
    'C': {'B': 3, 'D': 5},
    'D': {'E': 1},
    'E': {}
}

source_node = 'A'
shortest_distances = dijkstra(graph, source_node)
print("Shortest distances from node", source_node)
for node, distance in shortest_distances.items():
    print(node, ":", distance)
