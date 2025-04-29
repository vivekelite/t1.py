def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # Path compression
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot != yroot:
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

def kruskals(nodes, edges):
    parent = {}
    rank = {}
    for node in nodes:
        parent[node] = node
        rank[node] = 0

    mst = []
    total_cost = 0

    edges.sort(key=lambda x: x[2])  # Sort by weight

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, w))
            total_cost += w

    return total_cost, mst

# Example Graph (Edge List)
nodes = ['A', 'B', 'C', 'D']
edges = [ 
    ('A', 'B', 1),
    ('A', 'D', 3),
    ('B', 'C', 4),
    ('B', 'D', 2),
    ('C', 'D', 5)
]

cost, mst = kruskals(nodes, edges)
print("Kruskal's MST Cost:", cost)
print("Edges in MST:", mst)
