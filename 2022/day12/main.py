# read given input into python
import math
import string
from collections import defaultdict, deque

with open('input.txt') as input_text:
    heightmap = [line.strip() for line in input_text.readlines()]
    print(heightmap)


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


width, height = len(heightmap[0]), len(heightmap)
mountain, start, end = [], None, None
for row in heightmap:
    x = heightmap.index(row)
    for val in row:
        y = row.index(val)
        node = Node((x, y), val)
        mountain.append(node)
        if val == 'S':
            start = node
        elif val == 'E':
            end = node
        for r, c in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if r == -1 or c == -1:
                continue
            elif r >= height or c >= width:
                continue
            elif evaluate(node.value) > evaluate(heightmap[r][c]) + 1:
                continue
            else:
                node.children.append(Node((r, c), evaluate(heightmap[r][c])))

for m in mountain:
    print(m.__dict__)

# start = [k for k in mountain if mountain[k] == 'S']
# end = [k for k in mountain if mountain[k] == 'E']
seen = [start]
shortest_path = defaultdict(int)
shortest = math.inf
while seen:
    current = seen.pop()
    current.visited = True
    # next_step = steps + 1
    x, y = current.xy
    if current.dist < shortest: shortest = current.dist
    if (x, y) == end.xy:
        shortest = min(shortest, current.dist)
        break
    for n in current.children:
        if not n.visited:
            if n.dist + 1 < current.dist:
                current.dist = n.dist

print(shortest)

from collections import deque

def find_shortest_path(grid, start, goal):
    # Create a queue to store the paths being explored
    queue = deque([[start]])

    # Create a set to track the squares that have been visited
    visited = set()

    # While the queue is not empty
    while queue:
        # Remove the first path from the queue
        path = queue.popleft()
        # Get the last square on the path
        square = path[-1]
        # If the square is the goal, return the path
        if square == goal:
            return path
        # Otherwise, mark the square as visited
        visited.add(square)
        # Generate the next set of possible paths by exploring all the squares
        # that are reachable from the current square and have an elevation of a or one higher
        for next_square in get_reachable_squares(grid, square):
            if next_square not in visited:
                queue.append(path + [next_square])
    # If the queue becomes empty and no solution has been found, return "No solution found"
    return "No solution found"

def get_reachable_squares(grid, square):
    # Get the row and column indices of the current square
    row, col = square
    # Initialize a list to store the reachable squares
    reachable_squares = []
    # Check the squares to the left, right, top, and bottom of the current square
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        # Calculate the row and column indices of the next square
        next_row, next_col = row + dx, col + dy
        # If the next square is within the bounds of the grid, add it to the list of reachable squares
        if (0 <= next_row < len(grid)) and (0 <= next_col < len(grid[0])):
            reachable_squares.append((next_row, next_col))
    return reachable_squares

# Example usage
# grid = [
#     'Sabqponm',
#     'abcryxxl',
#     'accszExk',
#     'acctuvwj',
#     'abdefghi'
# ]
# # Find the indices of the start and goal squares
# for i, row in enumerate(heightmap):
#     for j, square in enumerate(row):
#         if square == 'S':
#             start = (i, j)
#         elif square == 'E':
#             goal = (i, j)
shortest_path = find_shortest_path(heightmap, start.xy, end.xy)
print(len(shortest_path))