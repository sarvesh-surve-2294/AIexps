from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]
        
    def addEdge(self, v, w):
        self.adj_list[v].append(w)
        
    def bfs(self, start):
        visited = [False] * self.vertices  # Keeps track of visited nodes
        queue = deque([start])  # Initialize queue with the start node
        visited[start] = True  # Mark the start node as visited
        
        while queue:  # Continue until the queue is empty
            current_node = queue.popleft()  # Get the first node from the queue
            print(current_node, end=" ")  # Print the current node
            
            # Visit all adjacent nodes (neighbors)
            for neighbor in self.adj_list[current_node]:
                if not visited[neighbor]:  # If the neighbor hasn't been visited
                    queue.append(neighbor)  # Add it to the queue
                    visited[neighbor] = True  # Mark the neighbor as visited

# Create a graph with 7 vertices
graph = Graph(7)

# Add edges
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 5)
graph.addEdge(2, 6)

# Perform BFS starting from node 0
graph.bfs(0)
