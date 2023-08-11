"""
    Breadth-First Search (BFS) is a graph traversal algorithm that explores a graph layer by layer, starting from a specified source node.
"""

from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Queue for BFS traversal

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=" ")  # Process the visited node
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
