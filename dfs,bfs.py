

def dfs(graph, start, visited=None):
    if visited is None:
        visited = {}
    visited[start]=1
    print(start)
    for i in graph[start]:
        if not visited.get(i, 0):
            dfs(graph, i, visited)
            
    return visited
def bfs(graph, start):
    queue = [start]
    visited = [start]
    while queue:
        node = queue.pop(0)
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                
                
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    start_node = 'A'
    print("DFS Traversal:", dfs(graph, start_node))
    print("BFS Traversal:", bfs(graph, start_node))
