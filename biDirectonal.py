from collections import deque

# Function to perform Bidirectional Search
def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # Initialize the forward and backward queues
    forward_queue = deque([start])
    backward_queue = deque([goal])

    # Initialize the visited nodes sets for both directions
    forward_visited = {start: None}
    backward_visited = {goal: None}

    # Function to reconstruct the path from the intersection point
    def reconstruct_path(forward_visited, backward_visited, meeting_node):
        # From start to meeting point
        path_forward = []
        node = meeting_node
        while node:
            path_forward.append(node)
            node = forward_visited[node]
        path_forward.reverse()

        # From meeting point to goal
        path_backward = []
        node = backward_visited[meeting_node]
        while node:
            path_backward.append(node)
            node = backward_visited[node]

        return path_forward + path_backward

    # Perform the search
    while forward_queue and backward_queue:
        # Forward search
        current_node_f = forward_queue.popleft()
        for neighbor in graph[current_node_f]:
            if neighbor not in forward_visited:
                forward_visited[neighbor] = current_node_f
                forward_queue.append(neighbor)
                
                # Check if the two searches meet
                if neighbor in backward_visited:
                    return reconstruct_path(forward_visited, backward_visited, neighbor)

        # Backward search
        current_node_b = backward_queue.popleft()
        for neighbor in graph[current_node_b]:
            if neighbor not in backward_visited:
                backward_visited[neighbor] = current_node_b
                backward_queue.append(neighbor)
                
                # Check if the two searches meet
                if neighbor in forward_visited:
                    return reconstruct_path(forward_visited, backward_visited, neighbor)

    # If no path is found
    return None


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

# Test bidirectional search
start = 'A'
goal = 'G'
path = bidirectional_search(graph, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found")
