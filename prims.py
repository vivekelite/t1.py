import heapq

def prims(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, to_node)
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        if weight != 0:
            mst_edges.append((weight, node))

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor))

    return total_cost, mst_edges

# Example Graph (Adjacency List)
graph = {
    'A': [('B', 1), ('D', 3)],
    'B': [('A', 1), ('C', 4), ('D', 2)],
    'C': [('B', 4), ('D', 5)],
    'D': [('A', 3), ('B', 2), ('C', 5)]
}

cost, edges = prims(graph, 'A')
print("Prim's MST Cost:", cost)
print("Edges in MST:", edges)
# Output:
