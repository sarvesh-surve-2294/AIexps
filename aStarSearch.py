import heapq

# A* search function
def a_star_search(graph, start, goal, heuristic):
    # Priority queue for frontier nodes to explore, initialized with the start node
    frontier = []
    heapq.heappush(frontier, (0, start))

    # Dictionaries to store the cost of reaching each node and the path taken
    came_from = {start: None}
    g_cost = {start: 0}

    while frontier:
        # Get the node with the lowest f(n) value (g(n) + h(n))
        current_cost, current_node = heapq.heappop(frontier)

        # If the goal is reached, reconstruct the path
        if current_node == goal:
            return reconstruct_path(came_from, start, goal)

        # Explore neighbors
        for neighbor, move_cost in graph[current_node]:
            new_g_cost = g_cost[current_node] + move_cost

            # If a better path to the neighbor is found
            if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_g_cost
                priority = new_g_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    return None  # If there's no path to the goal


# Function to reconstruct the path
def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


# Example usage
if __name__ == "__main__":
    # Graph representation: each node points to a list of tuples (neighbor, move_cost)
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('D', 1), ('E', 5)],
        'C': [('A', 3), ('F', 2)],
        'D': [('B', 1), ('G', 3)],
        'E': [('B', 5), ('G', 1)],
        'F': [('C', 2), ('G', 2)],
        'G': [('D', 3), ('E', 1), ('F', 2)]
    }

    # Heuristic (h(n)) - Estimated cost from each node to the goal 'G'
    heuristic = {
        'A': 6,
        'B': 4,
        'C': 4,
        'D': 2,
        'E': 1,
        'F': 2,
        'G': 0
    }

    start = 'A'
    goal = 'G'

    # Perform A* search
    path = a_star_search(graph, start, goal, heuristic)

    if path:
        print("Path found:", path)
    else:
        print("No path found")
