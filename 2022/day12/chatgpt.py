import string
from collections import deque
import math

with open('input.txt') as input_text:
    heightmap = [line.strip() for line in input_text.readlines()]


class Node:

    def __init__(self, xy: tuple, value: chr):
        self.xy = xy
        self.value = value
        self.children = []
        self.visited = False
        self.dist = math.inf


def evaluate(v: chr) -> int:
    elevation = string.ascii_lowercase
    if v == 'S':
        return elevation.index('a')
    elif v == 'E':
        return elevation.index('z')
    else:
        return elevation.index(v)


def get_reachable_squares(grid, square):
    # Get the coordinates of the current square
    x, y = square.xy
    # Initialize a list to store the reachable squares
    reachable_squares = []
    # Iterate over the possible movements
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        # Calculate the new coordinates
        x2, y2 = x + dx, y + dy
        # If the new coordinates are within the grid and the elevation difference is at most 1,
        # add the square at the new coordinates to the list of reachable squares
        if (0 <= x2 < len(grid)) and (0 <= y2 < len(grid[0])) and abs(
                evaluate(square.value) - evaluate(grid[x2][y2])) <= 1:
            reachable_squares.append(Node((x2, y2), grid[x2][y2]))
    # Return the list of reachable squares
    return reachable_squares


def find_shortest_path(grid, start, goal):
    # Initialize a queue to store the squares that still need to be visited
    queue = deque([start])
    # Initialize a dictionary to store the predecessor squares for each square
    predecessors = {}
    # Set the distance of the start square to 0
    start.dist = 0
    # While there are squares in the queue
    while queue:
        # Get the square at the front of the queue
        square = queue.popleft()
        # If the square is the goal square, return the path from the start to the goal
        if square == goal:
            return get_path(predecessors, start, goal)
        # Mark the square as visited
        square.visited = True
        # Get the reachable squares from the current square
        reachable_squares = get_reachable_squares(grid, square)
        # Iterate over the reachable squares
        for neighbor in reachable_squares:
            # If the neighbor has not been visited
            if not neighbor.visited:
                # Set the distance of the neighbor to the distance of the current square + 1
                neighbor.dist = square.dist + 1
                # Set the predecessor of the neighbor to the current square
                predecessors[neighbor] = square
                # Add the neighbor to the queue
                queue.append(neighbor)


def get_path(predecessors, start, goal):
    # Initialize a list to store the path
    path = []
    # Set the current square to the goal square
    current_square = goal
    # While the current square is not the start square
    while current_square != start:
        # Add the current square to the front of the path
        path.insert(0, current_square)
        # Set the current square to its predecessor
        current_square = predecessors[current_square]
    # Add the start square to the front of the path
    path.insert(0, start)
    # Return the path
    return path


# Find the start and goal squares
start = None
goal = None
for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        if heightmap[i][j] == 'S':
            start = Node((i, j), 'S')
        elif heightmap[i][j] == 'E':
            goal = Node((i, j), 'E')
# Find the shortest path from the start to the goal
shortest_path = find_shortest_path(heightmap, start, goal)
# Print the length of the shortest path
print(len(shortest_path) - 1)
# Initialize a variable to store the minimum distance from any square at elevation a to the goal
min_distance = math.inf
# Iterate over the squares in the grid
for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        # If the square has elevation a
        if heightmap[i][j] == 'a':
            # Find the shortest path from the square to the goal
            path = find_shortest_path(heightmap, Node((i, j), 'a'), goal)
            # If the distance from the square to the goal is shorter than the current minimum distance,
            # update the minimum distance
            min_distance = min(min_distance, len(path) - 1)
# Print the minimum distance
print(min_distance)
